"""Simüle edilmiş sensör ölçümleri.

Her sensör, hedeflerin gerçek konumuna gürültü ekleyerek konum ölçümü üretir.
Ölçümler sensörün kendi zaman çizelgesinde alınır ve kendi gecikmesiyle
füzyon merkezine ulaşır. Her ölçüm, sensörün beyan ettiği nominal gürültü
kovaryansını (R) taşır; sis veya karıştırma gibi bozulmalar bu beyana
yansımaz, füzyon merkezi bunu kendisi fark etmek zorundadır.
"""

from dataclasses import dataclass
from math import erfc, log, sqrt

import numpy as np

from .saha import SAHA_BOYUTU, SURE

# Senaryolar: olayların geçerli olduğu zaman pencereleri (s)
SENARYOLAR = {
    "normal": {},
    "sis": {"sis": (60.0, SURE)},
    "karistirma": {"karistirma": (80.0, 220.0)},
    "sensor_kaybi": {"kayip": {"radar": (100.0, 170.0),
                               "kamera": (150.0, 230.0),
                               "konum": (200.0, 260.0)}},
}

KARISTIRICI_KONUM = np.array([7000.0, 6500.0])  # karıştırma kaynağının yeri

# Kamera tespit modeli (Johnson kriterleri). Bir hedefin %50 olasılıkla tespiti
# için kritik boyutu boyunca 1 çizgi çifti (~2 piksel) gerekir. Kamera çözünürlüğü
# ve görüş açısı varsayımdır (1280 piksel, 10° yatay görüş açısı).
KAMERA_PIKSEL = 1280
KAMERA_GORUS_ACISI = np.deg2rad(10.0)
JOHNSON_N50_TESPIT = 1.0    # çizgi çifti

# Radar karıştırma modeli: hedeflerden ayrı, sabit noktadaki gürültü karıştırıcısı
# (stand-off). Karıştırma/gürültü oranı radarın karıştırıcıya bakan anten kazancına
# bağlıdır; ana lob için Gauss yaklaşımı, yan loblar için sabit seviye kullanılır.
RADAR_HUZME_GENISLIGI = np.deg2rad(2.0)   # 3 dB hüzme genişliği
YAN_LOB_SEVIYESI_DB = -30.0                # ana loba göre (NAWCWD el kitabı: tipik >30 dB)
JNR_ANA_LOB_DB = 42.0                      # karıştırıcı ana lobdayken karıştırma/gürültü oranı
RADAR_SNR_MAKS_MENZIL_DB = 13.0            # karıştırmasız, en uzak menzildeki hedefin SNR'ı
RADAR_PFA = 1e-6                           # yanlış alarm olasılığı (tespit eşiği)
SERIT_YANLIS_ALARM = 6.0                   # karıştırıcı yönündeki şeritte tarama başına yanlış tespit


@dataclass
class SensorTanimi:
    ad: str
    konum: np.ndarray      # sensörün sahadaki yeri (konum bildirimi için anlamsız)
    menzil: float          # m
    frekans: float         # Hz
    faz: float             # ilk ölçüm anı (s); sensörler aynı anda ölçmez
    gecikme: float         # ortalama iletim gecikmesi (s)
    titreme: float         # gecikmedeki rastgele oynama (s)
    sigma_sabit: float     # gürültü: sigma = sigma_sabit + sigma_oran * mesafe
    sigma_oran: float
    tespit_olasiligi: float
    yanlis_alarm: float    # tarama başına ortalama yanlış alarm sayısı
    sadece_dost: bool = False
    bias: tuple = (0.0, 0.0)


SENSORLER = {
    "radar": SensorTanimi("radar", np.array([4000.0, 4000.0]), 8_000.0, 1.0, 0.37,
                          0.6, 0.1, 12.0, 0.002, 0.9, 0.5),
    "kamera": SensorTanimi("kamera", np.array([5500.0, 5000.0]), 3_500.0, 5.0, 0.05,
                           0.3, 0.05, 3.0, 0.004, 0.95, 0.0),
    "konum": SensorTanimi("konum", np.array([np.nan, np.nan]), np.inf, 0.5, 0.8,
                          1.5, 0.2, 3.0, 0.0, 0.98, 0.0, sadece_dost=True,
                          bias=(35.0, -20.0)),
}

FUZYON_GECIKMESI = 2.0  # füzyonun beklediği sabit gecikme penceresi (s); en büyük gecikmeden büyük


@dataclass
class Olcum:
    sensor: str
    t_olcum: float         # ölçümün alındığı an
    t_varis: float         # füzyon merkezine ulaştığı an
    z: np.ndarray          # ölçülen konum (2,)
    R: np.ndarray          # sensörün beyan ettiği gürültü kovaryansı (2x2)
    etiket: int = None     # konum bildiriminde dost birliğin kimliği
    kaynak: int = None     # sadece hata ayıklama için: ölçümü üreten gerçek hedef


def _icinde(t, pencere):
    return pencere is not None and pencere[0] <= t < pencere[1]


def sensor_durumu(senaryo, ad, t):
    """Senaryoya göre sensörün t anındaki etkin parametrelerini döndürür."""
    s = SENSORLER[ad]
    olay = SENARYOLAR[senaryo]
    durum = dict(aktif=True, menzil=s.menzil, gurultu_carpani=1.0,
                 pd=s.tespit_olasiligi, yanlis_alarm=s.yanlis_alarm, karistirma=False)
    if _icinde(t, olay.get("kayip", {}).get(ad)):
        durum["aktif"] = False
    if ad == "kamera" and _icinde(t, olay.get("sis")):
        # Sis: görüş mesafesi kısalır, gürültü artar, hedefler kaçırılır
        durum.update(menzil=s.menzil * 0.65, gurultu_carpani=3.0, pd=0.5)
    if ad == "radar" and _icinde(t, olay.get("karistirma")):
        # Karıştırma: etkisi hedefin yönüne ve menziline bağlıdır (karistirma_etkisi)
        durum["karistirma"] = True
    return durum


def _sigma(s, mesafe):
    return s.sigma_sabit + s.sigma_oran * mesafe


def johnson_tespit_olasiligi(kritik_boyut, mesafe):
    """Hedef aktarım olasılık fonksiyonu: P = x^E / (1 + x^E), E = 2.7 + 0.7x.

    x, hedefin kritik boyutu boyunca düşen çizgi çifti sayısının tespit için
    gereken sayıya (N50) oranıdır.
    """
    if mesafe <= 0:
        return 1.0
    piksel_acisi = KAMERA_GORUS_ACISI / KAMERA_PIKSEL
    cizgi_cifti = kritik_boyut / (mesafe * piksel_acisi) / 2.0
    x = cizgi_cifti / JOHNSON_N50_TESPIT
    e = 2.7 + 0.7 * x
    return x ** e / (1.0 + x ** e)


def _north_pd(snr_db):
    """Sabit genlikli hedef için North yaklaşımı: Pd = 0.5 erfc(√(-ln Pfa) - √(SNR + 0.5))."""
    snr = 10 ** (snr_db / 10)
    return 0.5 * erfc(sqrt(-log(RADAR_PFA)) - sqrt(snr + 0.5))


def _aci_farki(a, b):
    return abs((a - b + np.pi) % (2 * np.pi) - np.pi)


def _jnr(s, aci):
    """Radar aci yönüne bakarken karıştırıcıdan aldığı karıştırma/gürültü oranı (doğrusal)."""
    fark = _aci_farki(aci, _yon(s.konum, KARISTIRICI_KONUM))
    kazanc_db = max(-12.0 * (fark / RADAR_HUZME_GENISLIGI) ** 2, YAN_LOB_SEVIYESI_DB)
    return 10 ** ((JNR_ANA_LOB_DB + kazanc_db) / 10)


def _yon(a, b):
    d = b - a
    return np.arctan2(d[1], d[0])


def karistirma_etkisi(s, p):
    """p konumundaki hedef için (tespit olasılığı çarpanı, gürültü çarpanı).

    Karıştırma gürültü tabanını (1 + JNR) kat yükseltir; hedefin SINR'ı o kadar
    düşer. Hedefin SNR'ı radar denklemine göre menzilin 4. kuvvetiyle azaldığından
    radara yakın hedefler karıştırmaya rağmen görülür (burn-through). Ölçüm
    hatası SNR'ın kareköküyle ters orantılı büyür.
    """
    mesafe = max(np.linalg.norm(p - s.konum), 1.0)
    jnr = _jnr(s, _yon(s.konum, p))
    snr_db = RADAR_SNR_MAKS_MENZIL_DB + 40 * np.log10(s.menzil / mesafe)
    sinr_db = snr_db - 10 * np.log10(1 + jnr)
    return _north_pd(sinr_db) / _north_pd(snr_db), sqrt(1 + jnr)


def _serit_yanlis_alarmi(s, rng):
    """Karıştırıcı yönünde, rastgele menzilde bir yanlış tespit (gürültü şeridi)."""
    aci = _yon(s.konum, KARISTIRICI_KONUM) + rng.normal(0, RADAR_HUZME_GENISLIGI / 2)
    menzil = rng.uniform(0, s.menzil)
    return s.konum + menzil * np.array([np.cos(aci), np.sin(aci)])


def olcumleri_uret(hedefler, senaryo, rng):
    """Tüm sensörlerin senaryo boyunca ürettiği ölçümleri döndürür (sözlük: sensör -> liste)."""
    sonuc = {}
    for ad, s in SENSORLER.items():
        liste = []
        for t in np.arange(s.faz, SURE, 1.0 / s.frekans):
            d = sensor_durumu(senaryo, ad, t)
            if not d["aktif"]:
                continue
            gecikme = s.gecikme + rng.uniform(0, s.titreme)

            # Gerçek hedeflerden gelen tespitler
            for h in hedefler:
                if s.sadece_dost and not h.dost:
                    continue
                p = h.konum_at(t)
                mesafe = 0.0 if s.sadece_dost else np.linalg.norm(p - s.konum)
                pd, gurultu = d["pd"], d["gurultu_carpani"]
                if ad == "kamera":
                    pd *= johnson_tespit_olasiligi(h.kritik_boyut, mesafe)
                if d["karistirma"]:
                    pd_carpani, gurultu = karistirma_etkisi(s, p)
                    pd *= pd_carpani
                if mesafe > d["menzil"] or rng.random() > pd:
                    continue
                sigma_nom = _sigma(s, mesafe)
                z = p + np.array(s.bias) + rng.normal(0, sigma_nom * gurultu, 2)
                liste.append(Olcum(ad, t, t + gecikme, z, np.eye(2) * sigma_nom ** 2,
                                   etiket=h.hid if s.sadece_dost else None, kaynak=h.hid))

            # Yanlış alarmlar: sahaya rastgele dağılan arka plan ve karıştırma şeridi
            yanlislar = [rng.uniform(0, SAHA_BOYUTU, 2) for _ in range(rng.poisson(d["yanlis_alarm"]))]
            if d["karistirma"]:
                yanlislar += [_serit_yanlis_alarmi(s, rng) for _ in range(rng.poisson(SERIT_YANLIS_ALARM))]
            for z in yanlislar:
                mesafe = np.linalg.norm(z - s.konum)
                if mesafe > d["menzil"] or not np.all((0 <= z) & (z <= SAHA_BOYUTU)):
                    continue
                liste.append(Olcum(ad, t, t + gecikme, z, np.eye(2) * _sigma(s, mesafe) ** 2))
        sonuc[ad] = liste
    return sonuc
