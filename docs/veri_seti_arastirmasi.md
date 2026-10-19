# Veri Seti Araştırması: Final Rapor

*13 Ekim 2026 (güncelleme: 18 Ekim 2026). Çok Sensörlü Veri Füzyonu
projesinin simülasyonunu gerçek ölçümlere dayandırmak ve yöntemini gerçek sensör
verisinde sınamak için yapılan veri seti araştırmasının sonuçları. İki ayrı
araştırmanın (ekip arkadaşının iki belgesi ve bu oturumdaki tarama)
birleştirilmiş ve kaynakları tek tek doğrulanmış hâlidir. Veri ihtiyaçlarının
tablo hâli: `docs/veri_ihtiyac_tablosu.xlsx`.*

**18 Ekim güncellemesinde eklenenler:**
- Üç simülasyon parametresi için literatür kaynakları: yaya grubu hızı
  (Moussaïd 2010), kamera menzili (Johnson kriterleri) ve karıştırma modeli
  (NAWCWD EW el kitabı). Bkz. 5.3.
- Autoferry makalesinden yer gerçeği ayrıntıları.
- COSMOS'un hangi kaydında hangi senaryonun olduğu. Repository A açık
  erişimli çıktı.
- MAPFusion'ın içeriği.
- Yazarlara gönderilen mailler. Bkz. 12.

## İçindekiler

1. [Kısaca](#1-kısaca)
2. [Proje](#2-proje)
3. [Veriyi ne için arıyoruz](#3-veriyi-ne-için-arıyoruz)
4. [Projenin veri ihtiyaçları](#4-projenin-veri-ihtiyaçları)
5. [Bulunan veri setleri](#5-bulunan-veri-setleri)
6. [İhtiyaç → veri eşlemesi](#6-ihtiyaç--veri-eşlemesi)
7. [Eksik veriler](#7-eksik-veriler)
8. [Kullanım planı](#8-kullanım-planı)
9. [Değerlendirme kuralları](#9-değerlendirme-kuralları)
10. [Yapılmayacaklar](#10-yapılmayacaklar)
11. [Doğrulama notları](#11-doğrulama-notları)
12. [Açık sorular](#12-açık-sorular)
13. [Kaynaklar](#13-kaynaklar)

---

## 1. Kısaca

- Projenin bütün senaryosunu tek başına karşılayan açık bir veri seti **yok**.
  Aranan veri şu özellikleri bir arada taşımalıydı:
  - km ölçeğinde bir kara/hava sahası,
  - radar, kamera ve konum bildirimi sensörleri,
  - aynı anda birden çok hedef ve dost/diğer ayrımı,
  - hedeften bağımsız bir yer gerçeği,
  - sis ve karıştırma koşulları.

  Bu tür veri genelde askerî tatbikatlarda üretilir ve paylaşılmaz.
- Bu yüzden **bileşen doğrulaması** yapılır: Projenin her iddiası, kendisine en
  uygun veriyle ayrı ayrı sınanır ve ayrı satırda raporlanır. Farklı veri
  setleri tek bir sahnede birleştirilmez.
- Veriler iki iş için kullanılır:
  1. **Kalibrasyon:** Simülasyondaki elle seçilmiş parametrelerin gerçek
     ölçümlere dayandırılması.
  2. **Doğrulama:** Füzyon hattının gerçek sensör verisinde, bağımsız yer
     gerçeğine göre sınanması.
- **Ana gerçek veri** Autoferry'dir (radar, lidar, EO ve IR kamera, hedeflerde
  GNSS). Hava hedefi için AERPAW AADM (gerçek İHA, radar, RF sensörleri, RTK
  GNSS) eklenir.
- **En büyük eksik:** Konum bildirimi ve dost/diğer etiketi, bağımsız yer
  gerçeğiyle birlikte gerçek veride sınanamıyor. Kasıtlı radar karıştırması
  altında da açık bir iz verisi yok.

| Rol | Veri seti | Cevap verdiği soru |
|---|---|---|
| **Ana veri** | Autoferry | Füzyon hattı gerçek, çok sensörlü, çok hedefli veride çalışıyor mu? |
| Doğrulama | AERPAW AADM | Gerçek bir İHA, gerçek bir İHA karşıtı radar ve RF sensörleriyle izlenebiliyor mu? |
| Doğrulama (isteğe bağlı) | DRaT | Çok sayıda kara hedefinde ilişkilendirme ve kimlik tutma nasıl? |
| Doğrulama (isteğe bağlı) | LocaRDS | km ölçeğinde konum bildirimi (ADS-B) ile bağımsız bir konum kaynağı nasıl birleşiyor? |
| Kalibrasyon | CUAS | Hedef hareketleri, sahte izler ve iz yönetimi gerçekte nasıl? |
| Kalibrasyon | CEREMA sis ölçümleri | Sis modeli ölçümlere dayanıyor mu? |
| Kalibrasyon | JKU Linz radar girişimi, COSMOS | Karıştırma modeli ölçümlere dayanıyor mu? |
| Literatür modeli | Moussaïd 2010, Johnson kriterleri, NAWCWD EW el kitabı | İnsan grubu hızı, kamera menzili ve karıştırma etkisi neye dayanıyor? |
| Kaynak | RADIATE, AIS/ADS-B standartları | Sis ve konum bildirimi varsayımlarının gerekçesi |

---

## 2. Proje

### Amaç

Radar, EO/termal kamera ve konum bildirimi sensörlerinden gelen ölçümleri
birleştirip tek bir **ortak durum resmi** ("kim nerede") oluşturmak ve
füzyonun tek sensöre göre kazancını ölçmek. Proje şu an bir **simülasyon
demosudur**; gerçek sensör verisi kullanmaz.

### Saha ve hedefler

10 km × 10 km'lik bir sahada 5 hedef ([`src/saha.py`](../src/saha.py)):

| Hedef | Tür | Rota |
|---|---|---|
| Araç-1 | diğer | Düz, sabit 10 m/s |
| İHA-1 | diğer | 22 m/s, uzun sola dönüş ve ardından sağa kırılma |
| İnsan Grubu | diğer | 1.5 m/s, hafif kıvrımlı |
| Dost Araç | **dost** | Düz, hız değiştiren (8 → 16 → 5 m/s) |
| Dost İHA | **dost** | 18 m/s, 60° dönüş, ardından yavaşlama |

### Sensörler

[`src/sensorler.py`](../src/sensorler.py):

| Sensör | Menzil | Gürültü (1σ) | Hız | Gecikme | Tespit | Özel durum |
|---|---|---|---|---|---|---|
| Radar | 8 km | 12 m + 2 m/km | 1 Hz | 0.6 s | %90 | Taramada ~0.5 yanlış alarm |
| EO/termal kamera | 3.5 km | 3 m + 4 m/km | 5 Hz | 0.3 s | %95 | — |
| Konum bildirimi | sadece dostlar | 3 m | 0.5 Hz | 1.5 s | %98 | Sabit bias (35, -20) m, kimlik taşır |

### Senaryolar

| Senaryo | Ne oluyor | Simülasyondaki parametreler |
|---|---|---|
| Normal | Bozulma yok | — |
| Sis (60 s'den itibaren) | Kamera bozulur | Menzil ×0.65, gürültü ×3, tespit %50 |
| Karıştırma (80-220 s) | Radara sahte ölçüm yağar | Gürültü ×4, tespit %70, taramada 8 yanlış alarm (%70'i karıştırıcı çevresinde) |
| Sensör kaybı | Sensörler bir süre kapanır | Radar 100-170 s, kamera 150-230 s, konum bildirimi 200-260 s |

### Yöntem

1. **Zaman senkronizasyonu:** Füzyon 2 s geriden çalışır. Gecikmeli ve sırası
   bozuk ölçümler alınış anına göre işlenir.
2. **Bias düzeltme:** Konum bildirimindeki sabit sapma, radar ve kamera
   izlerine göre kestirilir.
3. **İz ilişkilendirme:** Mahalanobis kapılama (χ², %99.9) ve optimal atama.
   İz onayı 3 vuruş, silme 2.5 s (aday) ve 6 s (onaylı).
4. **IMM filtresi:** Sabit hız (CV) ve EKF koordineli dönüş (CT) modelleri.
   Geçiş matrisi 0.90/0.10, ivme gürültüsü σ = 1 m/s², dönüş hızı
   belirsizliği σ_ω = 0.3 rad/s ([`src/kalman.py`](../src/kalman.py)).
5. **Sensör güveni (NIS):** Tutarsızlaşan sensörün ölçüm kovaryansı büyütülür
   (tolerans 4).
6. **İz güven skoru ve kimlik:** Her iz, destekleyen sensörleri ve dost/diğer
   etiketini taşır.

### Değerlendirme ve mevcut sonuç

Ana ölçüt **GOSPA** (konum hatası, kaçırılan hedefler ve sahte izler bir
arada). Yanında RMSE, kaçırma oranı, sahte iz, ID switch ve etiket doğruluğu
hesaplanır. Füzyon dört senaryonun hepsinde, 30 koşunun 30'unda en iyi tek
sensörden daha düşük GOSPA veriyor. Sonuç, ayarlamada kullanılmamış ikinci bir
30'luk tekrar setinde de doğrulandı.

### Mevcut sınırlamalar

- Sonuçlar sadece simülasyondan geliyor.
- Yukarıdaki parametrelerin neredeyse hepsi deneme yanılmayla, elle seçildi.

Bu araştırmanın amacı bu iki sınırlamayı gidermek.

---

## 3. Veriyi ne için arıyoruz

### İki ayrı iş

| İş | Ne yapılır | Sonuç |
|---|---|---|
| **Kalibrasyon** | Simülasyon parametreleri (hızlar, gürültüler, sis/karıştırma etkileri, iz yönetimi eşikleri) gerçek ölçümlerden alınır. | Simülasyon yine simülasyondur, ama parametreleri uydurulmuş değil ölçülmüştür. 30 tekrarlı istatistiğin gücü korunur. |
| **Doğrulama** | Füzyon hattı gerçek sensör ölçümleriyle çalıştırılır, bağımsız yer gerçeğine göre değerlendirilir. | Yöntemin gerçek gürültü, kaçırma ve yanlış alarmla çalıştığı gösterilir. |

### Bileşen doğrulaması

Her iddia kendisine en uygun veriyle ayrı ayrı sınanır. Farklı yer, zaman ve
sensörlerden gelen veriler üst üste konmaz; bu, gerçekte yaşanmamış yapay bir
sahne üretir.

Gerçek veri projenin **füzyon mimarisini** sınar. Projenin **senaryosunu**
(10 × 10 km'lik kara/hava sahası, sis ve karıştırma bir arada) bütün olarak
sınamaz. Gerçek veri sonuçlarının simülasyondan farklı çıkması beklenir; bu
başarısızlık değil, bulgu olarak raporlanır.

### Kanıt düzeyleri

Her sonuç şu düzeylerden biriyle etiketlenir:

1. **Gerçek veri:** Gerçek sensör ölçümü, bağımsız yer gerçeği.
2. **Gerçek veri, yaklaşık referans:** Gerçek ölçüm, ama referans bağımsız
   değil (ör. hedefin kendi ADS-B ya da AIS bildirimi).
3. **Ölçüme dayalı simülasyon:** Sentetik veri, parametreleri yayımlanmış
   ölçümlerden.
4. **Saf simülasyon:** Sentetik veri, parametreler varsayım.

Projenin bugünkü bütün sonuçları **4. düzeydedir**.

---

## 4. Projenin veri ihtiyaçları

### A. Kalibrasyon için

| # | İhtiyaç | Projede nerede | Şu anki değer |
|---|---|---|---|
| K1 | Hedeflerin gerçek hızları (İHA, araç, insan) | `src/saha.py` | 22 / 18 / 10 / 1.5 m/s, elle |
| K2 | Hedeflerin ivmesi ve dönüş hızı | `src/kalman.py` (ivme σ, ω σ), IMM geçiş matrisi | 1 m/s², 0.3 rad/s, 0.90/0.10, elle |
| K3 | Radarın tespit olasılığı ve ölçüm hatası | `src/sensorler.py` | %90, 12 m + 2 m/km |
| K4 | Kameranın tespit olasılığı ve ölçüm hatası | `src/sensorler.py` | %95, 3 m + 4 m/km |
| K5 | Radarın yanlış alarmları ve sahte iz ömrü | `src/sensorler.py`, `src/fuzyon.py` (onay ve silme eşikleri) | 0.5 / tarama; 3 vuruş; 2.5 s / 6 s |
| K6 | Sisin kameraya etkisi | Sis senaryosu | Menzil ×0.65, gürültü ×3, tespit %50 |
| K7 | Karıştırmanın radara etkisi | Karıştırma senaryosu | Gürültü ×4, tespit %70, 8 yanlış alarm |
| K8 | Konum bildiriminin mesaj aralığı, gecikmesi ve kaybı | `src/sensorler.py` | 0.5 Hz, 1.5 s, %98 |
| K9 | Konum bildirimindeki sabit sapma | `src/sensorler.py` | (35, -20) m |
| K10 | Sensör kesintilerinin süresi ve sıklığı | Sensör kaybı senaryosu | 70-80 s'lik pencereler |
| K11 | Sensör güveni eşiği | `src/fuzyon.py` | NIS toleransı 4 |

### B. Doğrulama için

| # | İhtiyaç | Neden |
|---|---|---|
| D1 | Aynı hedefleri aynı anda gören birden çok farklı türde gerçek sensör | Füzyonun gerçek ölçümlerle çalıştığını göstermek |
| D2 | Hedeften bağımsız yer gerçeği | RMSE ve GOSPA hesaplamak |
| D3 | Aynı anda birden çok hedef | İlişkilendirme ve ID switch ölçütü |
| D4 | Manevra yapan gerçek hedef | IMM |
| D5 | Gerçek zaman damgalı, asenkron sensörler | Zaman senkronizasyonu |
| D6 | Gerçekten bozulmuş bir sensör | NIS tabanlı güven |
| D7 | Gerçek sensör kesintisi | Sensör kaybı |
| D8 | Gerçek konum bildirimi ile aynı hedefleri gören bağımsız bir sensör | Bias düzeltme |
| D9 | Dost/diğer etiketi | Kimlik ve etiket doğruluğu |
| D10 | Kara hedefleri (araç, insan grubu) | Sahadaki kara hedefleri |
| D11 | km ölçeği | Sahanın ölçeği |
| D12 | Kötü hava ve karıştırma altında gerçek izleme verisi | Senaryoların gerçek karşılığı |

---

## 5. Bulunan veri setleri

Her veri seti için: ne verisi, yer gerçeği, erişim, projede nerede, dikkat
edilecekler.

### 5.1 Doğrulama verileri

#### Autoferry: ana veri

[github.com/Autoferry/sensor_fusion_dataset](https://github.com/Autoferry/sensor_fusion_dataset)
· Helgesen ve ark., *Ocean Engineering* 252 (2022)

- **Ne verisi:** Bir otonom feribotun sensörlerinden gerçek **tespitler** (ham
  veri değil).
  - Radar (0.8 Hz) ve lidar (~10 Hz): feribot çerçevesinde (x, y).
  - EO kamera (5 Hz) ve IR kamera (9 Hz): yalnızca açı.
- **Hedefler:** Havfruen (7.3 m), Gunnerus (31.3 m), Jetboat (7.4 m). Ayrıca
  tespitlerde yer gerçeği olmayan başka tekneler var.
- **Senaryolar:** 1. ortam açık liman (2-6), 2. ortam kent içi kanal (13, 16,
  17, 22). Mayıs 2021.
- **Yer gerçeği:** Hedef teknelerdeki GNSS. Sensörlerden bağımsız. Makalenin
  söyledikleri:
  - **Alıcılar:** Gunnerus ve Jetboat'ta u-blox ZED-F9P, sonradan RTKLIB ile
    PPK işlenmiş. Havfruen'de SBG Ellipse-D; PPK'dan söz edilmiyor.
  - **Doğrulama yok:** Yazarlar kayıt sırasında alıcıları izleyecek personel
    olmadığını ve yer gerçeğinin doğrulanmadığını açıkça yazıyor.
  - **Zaman eşlemesinin** nasıl yapıldığı makalede ve repoda yok.
  - **Antenin teknedeki yeri** yazmıyor. Repodaki konumların antene mi yoksa
    tekne merkezine mi ait olduğu da belli değil.
  - **Çalışan antenler** (makale, Tablo 2-3):

    | Senaryo | Havfruen | Gunnerus | Jetboat |
    |---|---|---|---|
    | 2-6 (1. ortam) | Sadece arka | Sadece arka | — |
    | 13 | Sadece arka | — | Ön + arka |
    | 16, 17, 22 | Sadece arka | — | Sadece ön |

  - Yer gerçeğini toplayan ve işleyen yazar Kjetil Vasstein. Açık sorular
    18 Ekim'de ona soruldu (bkz. 12).
- **Erişim:** Açık, CC0, ~6 MB, JSON ve .mat.
- **Projede nerede:** Bütün füzyon hattı (D1, D2, D3, D5).
  - Kameralar için açı ölçüm modeli (EKF) gerekiyor.
  - 2. ortamda kameralar kıyıdaki bağlı teknelerden ötürü sonucu bozuyor
    (makalede Jetboat hatası 75 m). Bu, güven mekanizması için en değerli
    gerçek test (D6).
  - Gerçek ölçümler silinerek sensör kaybı denenebilir (D7).
- **Makalenin ek tabloları:** Tablo 10'da menzile göre tespit olasılıkları,
  Tablo 11'de izleyici ayarları var (ör. ivme gürültüsü σ = 1.5; bizde 1.0).
  Simülasyonla kıyas için kullanılabilir.
- **Kıyas noktası (makale):** GOSPA 1. ortamda 16.8-20.4 m, 2. ortamda
  16.0-32.1 m. Makalenin izleyicisinin ANEES değerleri de tutarsız; bu değerler
  ulaşılması gereken bir "doğru" değil, aynı veri üzerindeki bir kıyas
  noktasıdır.
- **Dikkat:**
  - Projede lidar yok. Radar + lidar füzyonu projenin sensör setini değil,
    füzyon mimarisini sınar.
  - GOSPA kesme değeri ve eşleşme eşiği makaleyle aynı alınır (1. ortam 20 m,
    2. ortam 10 m). Projedeki 250 m bu ölçekte anlamsız.
  - Deniz ortamı; hedefler bizim sahamızdaki hedefler değil.

#### AERPAW AADM: hava hedefi

[Dryad, doi:10.5061/dryad.7d7wm3898](https://datadryad.org/dataset/doi:10.5061/dryad.7d7wm3898)
· [Veri makalesi, arXiv 2602.16163](https://arxiv.org/abs/2602.16163)
· NC State, 2025 kaydı, Mart 2026 yayımı

- **Ne verisi:** Kablosuz haberleşme yarışması için yapılan İHA uçuşları.
  Radar ve RF sensörleri İHA'yı yan ölçüm olarak izliyor.
  - **Fortem R20 İHA karşıtı radar:** menzil, açı, yükseklik açısı, radyal
    hız, RCS, iz konumu (enlem-boylam-yükseklik), iz kimliği.
  - **Keysight RF sensörleri:** TDOA ile İHA konum kestirimi, ayrıca **CEP**
    (sensörün beyan ettiği hata).
- **Uçuşlar:**
  - 33 yarışma uçuşu tüm sensörlerle (11 takım × 3).
  - 3 ek uçuş (Opt1-3) sadece radar ve RF ile, konum bulma için.
  - Tek İHA, 25 m irtifa, ~500 s'lik görevler.
- **Yer gerçeği:** İHA'nın kendi GNSS kaydı (~1 Hz). Veri makalesine göre
  **RTK destekli**.
- **Erişim:** Açık, 7.7 GB tek zip, CSV/JSON/TXT. Lisans sayfada belirtilmemiş.
- **Projede nerede:**
  - Hava hedefinin gerçek veride izlenmesi (D1, D2, D4, D5).
  - Kutupsal (menzil-açı) radar ölçüm modeli. Bu, README'deki "Gelecek
    çalışmalar" maddelerinden biri.
  - CEP'ten ölçüm kovaryansı üretme.
  - **Gerçek sensör bozulması (D6):** Opt1'in ilk koşusunda İHA yanlış bant
    genişliğiyle yayın yapmış, RF konum doğruluğu düşmüş. Düzeltilmiş tekrar
    (`rerun`) dosyaları da var. Güven mekanizmasının gerçek bir bozulmayı fark
    edip etmediği burada sınanır.
- **Dikkat:**
  - Radar çıktısı ham tespit değil, **radarın kendi izi**. Ölçümler birbirinden
    bağımsız değil; NIS olduğundan düşük çıkabilir. Bu, ölçüm füzyonundan çok
    iz-iz füzyonu problemidir.
  - Tek hedef olduğu için ilişkilendirme sınanamaz.
  - Yer gerçeği 1 Hz; ölçüm anlarına ara değerleme gerekir. Hızlar gövde
    çerçevesinde verilmiş, dünya çerçevesine döndürülmesi gerekir.
  - Betikler MATLAB için. Biz JSON ve CSV'yi Python'da doğrudan okuruz.

#### DRaT: kara hedefleri (isteğe bağlı)

[zenodo.org/records/20171110](https://zenodo.org/records/20171110) · Purdue
Üniversitesi, Mayıs 2026

- **Ne verisi:** Bir otoyol kesitinde (~140 m) direğe takılı ticari K-bant
  trafik radarının nesne seviyesinde çıktısı: konum, hız, boyut, yön, 8 Hz.
  Radarın konumu RTK GPS ile ölçülmüş.
- **Hedefler:** 5.278 araç izi. 43 dakika serbest akış, 37 dakika sıkışık
  trafik.
- **Yer gerçeği:** 122 m'de duran bir drone'un 4K videosundan YOLO + BoT-SORT
  ile çıkarılıp yer kontrol noktalarıyla haritaya oturtulmuş izler, radar
  zamanlarına ara değerlenmiş.
- **Erişim:** Açık, CC BY 4.0, 91 MB, CSV.
- **Projede nerede:**
  - Çok hedefte ilişkilendirme ve kimlik tutma (D3, D10).
  - Kara aracı hız ve ivme istatistikleri (K1, K2). CUAS'ta yalnızca 14 araç
    izi var; bu açığı kapatır.
  - Sabit konumlu bir radar, bizim sahamıza benziyor.
- **Dikkat:**
  - Tek sensör: füzyon değil, radar izleme sınanır.
  - Radar çıktısı büyük olasılıkla radarın kendi izi.
  - Yer gerçeği de bir tespit edici ve izleyiciden geliyor.
  - Menzil 140 m.

#### LocaRDS: km ölçeği, konum bildirimi (isteğe bağlı)

[zenodo.org/records/4302249](https://zenodo.org/records/4302249) · Schäfer,
Strohmeier, Leonardi, Lenders · OpenSky Network, Kasım 2020

- **Ne verisi:** Avrupa'daki 323 yer alıcısının kaydettiği uçak yayınları.
  50 milyondan fazla yayın için 222 milyondan fazla alıcı ölçümü.
- **Ne için hazırlanmış:** Uçak konum bulma yarışması. Aynı yayını birden çok
  alıcı farklı zamanlarda duyduğu için, varış zamanı farklarından (MLAT)
  uçağın kendi bildiriminden bağımsız bir konum hesaplanabilir.
- **Referans:** Uçağın kendi ADS-B bildirimi.
- **Erişim:** Açık, CC BY-SA 4.0, 3.6 GB (8 parça).
- **Projede nerede:**
  - km ölçeği (D11) ve aynı anda çok hedef (D3).
  - **ADS-B, projedeki konum bildirimi sensörünün gerçek karşılığı.** MLAT
    konumu ikinci bir konum kaynağı olarak kullanılırsa, konum bildirimi ile
    bağımsız bir sensörün birleştirilmesi ve bias kestirimi gerçek veride
    sınanabilir (D8, K9).
  - Mesaj aralığı ve kaybı (K8).
- **Dikkat:**
  - Referans bağımsız değil; sonuçlar "ADS-B'ye göre" sunulur. ADS-B sensör
    olarak kullanılırsa kendi referansı olamaz (kanıt düzeyi 2).
  - Radar ve kamera yok.
  - MLAT çözümü ayrı bir iş. Yarışmanın açık kodları başlangıç olabilir.
  - Zaman damgalarının çözünürlüğü kayıt sayfasında yazmıyor; belgelerden
    kontrol edilmeli.

### 5.2 Kalibrasyon verileri

#### CUAS: hedef hareketleri ve sahte izler

[github.com/nrc-cnrc/CUAS-sensing-dataset](https://github.com/nrc-cnrc/CUAS-sensing-dataset)
· NRC Kanada ve Ottawa Üniversitesi, 2019-2021 kayıtları

- **Ne verisi:** Echodyne EchoGuard (K-bant) radarının izleri, 10 Hz. Her
  güncellemede 3B konum, 3B hız, menzil-açı ve RCS var. 8 saha denemesi.
  - **Etiketli Excel'ler:** 1.117 iz. Sınıflar: kuş 492, karışık 376, İHA 167,
    insan 65, araç 14. **Zaman sütunu yok.**
  - **Ham CSV'ler:** ~40 sütun, ISO 8601 UTC zaman damgalı. İçinde:
    - 31 seçilmiş İHA/kamyon izi (Demo-1, 4, 7),
    - Demo-4'te ~8.000 izlik 3 tam kayıt (çoğu yansıma ya da bilinmeyen),
    - radarın kendi ilişkilendirme ki-kare değerleri, iz ömrü, durum ve güven
      bilgisi.
- **Yer gerçeği:** Yalnızca sınıf etiketi (PTZ kamerayla gözle doğrulanmış).
  Konum yer gerçeği yok.
- **Erişim:** Açık, CC BY 4.0.
- **Projede nerede:**

  | Ne çıkarılır | Kaynak | Proje parametresi |
  |---|---|---|
  | Hız dağılımları (İHA, insan, araç) | Excel'ler (`veloX/Y`) | K1, `src/saha.py` |
  | İvme ve dönüş hızı | Zaman damgalı İHA/kamyon CSV'leri | K2, ivme σ, ω σ, IMM geçiş matrisi |
  | Sahte iz ömrü ve yoğunluğu | Demo-4 tam kayıtlar (`LifeTime`, `state`) | K5, onay ve silme eşikleri |
  | Ki-kare dağılımı | `associatedMeasurementChiStatistic1..3` | K11, NIS toleransı |

- **Dikkat:**
  - Ölçüm ilişkilendirilmemiş satırlar (`rcs` boş ya da `measurments = 0`)
    radarın tahminidir; hız ve ivme hesabından çıkarılmalı.
  - Konumlar radarın filtresinden geçmiş; ivme ve dönüş hızı tepe değerleri
    biraz düşük çıkar.
  - Yanlış alarm bilgisi iz seviyesinde, tespit seviyesinde değil.
  - İnsan izleri için zaman damgası yok; sadece hız dağılımı çıkar.
  - Demo-0'daki iki radar (R1/R2) zaman damgası olmadığı için birlikte
    kullanılamaz.
  - Menzil 100-1.200 m; menzile bağlı gürültü değerleri bize taşınamaz.

#### CEREMA sis ölçümleri: sis modeli

[Bijelic, Gruber, Ritter, "Benchmarking Image Sensors Under Adverse Weather Conditions for Autonomous Driving", IEEE IV 2018](https://arxiv.org/abs/1912.03238)

- **Ne verisi:** Clermont-Ferrand'daki CEREMA sis odasında (30 m) kontrollü
  sis. Görüş mesafesi aralıkları 10-20, 20-30, 30-40 ve 50-60 m. Bilinen
  hedeflerle kamera, kapılı NIR kamera ve lidar ölçümleri.
- **Model:** Saçılma modeli,
  I(d) = I₀/d² · e^(−βd) + I∞(1 − e^(−βd)). Görüş mesafesi Koschmieder
  yasasıyla β ≈ 3/V.
- **Projede nerede (K6):** Simülasyondaki sabit sis çarpanları (menzil ×0.65,
  gürültü ×3, tespit %50), görüş mesafesine bağlı bu modelle değiştirilir.
  Böylece sisin yoğunluğu bir parametre olur.
- **Dikkat:** Ölçümler 60 m görüşe kadar ve otomotiv kamerası için. km
  ölçeğine taşımak ekstrapolasyondur ve öyle yazılmalıdır.

#### JKU Linz radar girişimi: karıştırma modeli

[zenodo.org/records/21933926](https://zenodo.org/records/21933926) · Rienessl,
Feger, Johannes Kepler Üniversitesi Linz, Ağustos 2026

- **Ne verisi:** İki istasyonlu, zaman senkronize 77 GHz FMCW radar ağının
  **ham ADC verisi**. Bir otoparkta durağan sahne.
  - Ağa senkronize olmayan bir girişim kaynağı dört farklı ayarla (int_A-D)
    çalıştırılmış.
  - Girişimsiz referans ölçümleri de var. Bir ölçümde yürüyen bir yaya bulunuyor.
- **Erişim:** Açık, CC BY 4.0, 2.6 GB. MATLAB, Octave ve Python işleme
  betikleri var. Aynısı IEEE DataPort'ta da yayımlanmış.
- **Projede nerede (K7):** Temiz ve girişimli ölçümler karşılaştırılarak üç
  şey ölçülür:
  - gürültü tabanındaki artış,
  - tespit olasılığındaki düşüş,
  - yanlış alarm sayısındaki artış.

  Karıştırma senaryosundaki "gürültü ×4, tespit %70, 8 yanlış alarm" değerleri
  bunlara dayandırılır.
- **Dikkat:**
  - Bu kasıtlı karıştırma değil, girişim.
  - Ham veri; tespit için sinyal işleme (FFT, CFAR) gerekir.
  - İz yer gerçeği yok, sahne büyük ölçüde durağan.
  - 77 GHz otomotiv radarı; gözetleme radarına oranlar olarak taşınabilir,
    mutlak değerler olarak taşınamaz.

#### COSMOS: radar girişimi + GPS yer gerçeği

Birmingham Üniversitesi ve Jaguar Land Rover, Kasım 2021, Horiba MIRA test
pisti · [Repository A (777)](https://edata.bham.ac.uk/777/) ·
[B (785)](https://edata.bham.ac.uk/785/) ·
[E (788)](https://edata.bham.ac.uk/788/)

- **Ne verisi:** Araç radarlarının birbirini bozmasının (karşılıklı girişim)
  ölçümleri. Ham veri; kayıtlar 10-30 saniye.
  - Kurban araç: 2 radar (77 GHz, ham ADC), ZED stereo kamera, Velodyne
    lidar, GPS/IMU.
  - Girişim yapan araç: TI ve NXP radarları, GoPro, GPS/IMU.
  - Her senaryoda girişim kapalı (referans) ve açık iki kayıt var.
- **Hangi kayıtta ne var** (veri raporu Rev B ve Rev C):

  | Kayıt | Senaryo | Erişim | Boyut |
  |---|---|---|---|
  | A (777) | 1b (kalibrasyon), 2g, **3d girişimli koşu** (kavşak; kurban radar sabit, girişim yapan araç hareketli) | **Açık** | 9 GB |
  | B (785) | **2d** (kurban radar sabit, girişim yapan araç ona doğru sürüyor) | Talep formu | 6 GB |
  | E (788) | **3d** (referans koşusu dahil) | Talep formu | 7 GB |

  777'deki Readme.pdf, A'da 3d yerine 2d olduğunu söylüyor. İki rapor sürümü
  de 3d dediği için bu büyük olasılıkla Readme'deki bir yazım hatası. Kesin
  sonuç zip'in içine bakınca belli olacak.
- **Yer gerçeği:** İki araçta GPS/IMU; doğruluğu belirtilmemiş. Video da yer
  gerçeği olarak sunuluyor. Zaman damgaları verinin dizüstü bilgisayara varış
  anı; gecikme içeriyor.
- **Erişim:** CC BY 4.0. A açık; B ve E "Request a copy" formuyla.
- **Projede nerede (K7, D6, D12):** Girişimli ve girişimsiz kayıtlar
  karşılaştırılarak tespit olasılığındaki düşüş ve sahte tespitler ölçülür.
  2d ve 3d'de sensör sabit, hedef hareketli; bizim sahamıza benziyor. JKU
  Linz'den farkı, hareketli bir hedef ve GPS yer gerçeği olması.
- **Dikkat:**
  - Kasıtlı karıştırma değil, girişim; hedefin kendisi girişim kaynağı.
  - Ham ADC verisi; tespit için radar sinyal işleme gerekir.
  - Tek hedef, kısa kayıtlar, kısa menzil (50-300 m).

### 5.3 Kaynak olarak kullanılanlar (veri işlenmez)

| Kaynak | Ne destekliyor |
|---|---|
| [RADIATE](https://arxiv.org/abs/2010.09076) (Heriot-Watt, 2020) | "Sis kamerayı ve lidarı bozar, radarı bozmaz" varsayımı. Radarın tespit başarımı siste genel ortalamanın altına düşmüyor (AP %47-51 ve %45-47); yağmurda %26-33'e, karda %5-13'e düşüyor. Yazarlar senaryo farklarının havadan çok sahne türünden geldiğini belirtiyor; sayılar yön gösterir, doğrudan kullanılmaz. |
| ITU-R M.1371 (AIS) | Konum bildirimi mesaj aralıkları: A sınıfı gemide hıza göre 2-10 s, B sınıfında 30 s. *Değerler standardın kendisinden kontrol edilmeli.* |
| RTCA DO-260B (ADS-B) | Havadaki konum mesajı saniyede ~2 kez. *Standardın kendisinden kontrol edilmeli.* |
| Autoferry makalesi, Tablo 4-5 | Gerçek sensörlerin tespit olasılıkları (radar 0.70-0.76, lidar 0.75-0.92, EO 0.51-0.78, IR 0.32-0.55) ve ölçüm hataları. **Sadece kıyas için;** farklı sensör ve ölçek olduğu için simülasyon değerleri bunlara çekilmez. |
| [Moussaïd ve ark. (2010)](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0010047), PLoS ONE 5(4): e10047 | Yaya gruplarının yürüme hızı (K1, K2). Bkz. aşağıda. |
| [ETH/UCY](https://service.tib.eu/ldmservice/dataset/eth-and-ucy-datasets) yaya yörüngeleri | 5 sahne, 1.536 yaya, metre cinsinden konumlar, 2.5 kare/s; yalnızca araştırma amaçlı. Grupların dönüş davranışı için (K2). |
| [Johnson kriterleri](https://en.wikipedia.org/wiki/Johnson%27s_criteria) (NATO STANAG 4347'nin temeli) | Kamera tespit/tanıma/teşhis menzili ve mesafeye bağlı tespit olasılığı (K4). Bkz. aşağıda. |
| NAWCWD *Electronic Warfare and Radar Systems Engineering Handbook* (ABD Donanması, 1999; 2013 güncellemesi; açık erişim) · [HTML](https://rfcafe.com/references/electrical/ew-radar-handbook/support-jamming.htm) | Karıştırma/sinyal oranı denklemleri (K7). Bkz. aşağıda. |
| Fukuda, Tamaru, Kubo, Shoji (2024), *The Journal of Navigation* 77(5-6), 677-694 | AIS konum hatası ve yayın sıklığı (K8, K9). NavEYE makalesinin kaynakçasında bulundu; henüz okunmadı. |

#### Simülasyon parametreleri için literatür modelleri

Bu üç model veri indirmeyi gerektirmez. Simülasyondaki elle seçilmiş
parametreleri yayımlanmış ölçümlere ve fiziksel denklemlere bağlar. 18 Ekim 2026
itibarıyla koda işlendi (`src/saha.py`, `src/sensorler.py`; bkz. README).

**1. Yaya grubu hızı (Moussaïd ve ark. 2010).**
- **Veri:** Toulouse'da kamerayla kaydedilmiş, elle takip edilmiş 1.353 yaya
  grubu (2-4 kişilik).
- **Bulgular:**
  - Kalabalıktakilerin %55-70'i gruplar hâlinde yürüyor.
  - Yürüme hızı grup büyüdükçe doğrusal düşüyor. Düşük yoğunlukta makaledeki
    doğru denklemi: hız ≈ 1.26 − 0.04 × (grup büyüklüğü). Buradan yaklaşık 1
    kişi 1.22, 2 kişi 1.18, 3 kişi 1.14, 4 kişi 1.10 m/s. Bu değerler
    makaledeki denklemden hesaplandı; makale onları yalnızca grafikte veriyor.
- **Sonuç:** `src/saha.py`'deki insan grubu hızı (1.5 m/s) gerçekçi değerin
  üstünde; 1.1-1.2 m/s olmalı.

**2. Kamera menzili (Johnson kriterleri).**
- **Kural:** %50 olasılık için hedefin kritik boyutu boyunca gereken çizgi
  çifti sayısı (1 çizgi çifti ≈ 2 piksel): tespit 1.0 ± 0.25, tanıma
  4.0 ± 0.8, teşhis 6.4 ± 1.5.
- **Menzil:** hedef boyutu / (piksel sayısı × bir pikselin gördüğü açı).
  Örnek: 640 piksel, 2° görüş açılı bir kamera ve 2 m'lik bir araç için tespit
  ~18 km, tanıma ~4.6 km, teşhis ~2.9 km.
- **Mesafeye bağlı olasılık:** Johnson'ın hedef aktarım olasılık fonksiyonu
  P = (N/N50)^E / (1 + (N/N50)^E), E = 2.7 + 0.7·(N/N50). Formül kullanılmadan
  önce asıl kaynağından doğrulanmalı.
- **Sonuç:** Kameranın 3.5 km menzili ve sabit %95 tespiti yerine, seçilen
  bir kamera modelinden hesaplanan menzil ve mesafeyle yumuşak düşen tespit
  olasılığı kullanılır.
- **Sınır:** İdeal koşul; sis ve atmosfer ayrıca eklenir (CEREMA modeli).

**3. Karıştırma (NAWCWD el kitabı, stand-off karıştırıcı).**
- **Denklem:** Bizim karıştırıcımız hedeflerden ayrı, sabit bir noktada
  duruyor. Karıştırma/sinyal oranı, dB cinsinden:

  J/S = Pj − BF + Gja − Pt − Gt − σ + 10.99 + 40·log R_hedef − 20·log R_karıştırıcı

  - Pj, Gja: karıştırıcı gücü ve anten kazancı
  - Pt, Gt: radar gücü ve anten kazancı
  - σ: hedefin radar kesit alanı
  - BF: karıştırıcı ve radar bant genişliği farkı
- **Sonuçları:**
  - **Etki hedefin uzaklığına bağlı.** Hedef radara yaklaştıkça J/S 40 dB/dekad
    düşer ve hedef belli bir mesafede karıştırmaya rağmen görünür olur
    (burn-through).
  - **Etki yöne bağlı.** Karıştırıcı radarın yan loblarındayken etkisi
    genellikle 30 dB'den fazla zayıflar.
  - Bugünkü model (gürültü ×4, tespit %70, taramada 8 yanlış alarm) bütün
    hedefleri aynı ölçüde etkiliyor.
- **Modeldeki tutarsızlık:** Simülasyonda sahte ölçümlerin %70'i
  karıştırıcının *konumunda* yoğunlaşıyor. Gürültü karıştırıcısı sahte hedef
  üretmez; karıştırıcı *yönünde*, bütün menzil boyunca gürültü yükseltir. Belli
  bir yerde sahte hedef üreten aldatıcı karıştırıcıdır. Hangisinin
  modellendiği seçilip açıkça yazılmalı.
- **Sınır:** Güç ve kazanç değerleri yine varsayım. El kitabının burn-through
  sayfası HTML sürümde yok; menzil yukarıdaki denklemden türetilir.

### 5.4 Değerlendirilip seçilmeyenler

| Veri seti | Ne verisi | Neden seçilmedi |
|---|---|---|
| [HAXR](https://zenodo.org/records/19824555) (DLR, 2026) | 13 istasyonun ham X-bant radar görüntüsü + AIS, Hamburg limanı, CC BY 4.0, 5.4 GB | Yer gerçeği yalnızca AIS; ham radar işlenmeli. İleride bias ve çok radarlı tutarlılık için kullanılabilir. |
| [DLR radar + AIS (2. veri seti)](https://www.dlr.de/en/kn/about-us/departments/nautical-systems/real-world-marine-radar-datasets-for-target-tracking) | Radar tespitleri + AIS yer gerçeği | Talep formu, ihracat kontrolü, kullanım amacı beyanı gerekiyor. |
| [7V-Scanario](https://github.com/UniBwTAS/7V-Scanario) (UniBw Münih) | 6 radar, 4 kamera, lidar; 7 hedef araçta RTK-GNSS/INS | Sensörler hareketli araçta, menzil kısa, ROS bag, lisans talep üzerine. Kara aracı için en iyi yer gerçeği. |
| [Lille GNSS aldatma](https://doi.org/10.57745/3C63J0) (2024) | Araç filosu, GNSS aldatma | **Sayfa bot korumasıyla erişilemedi; hiçbir bilgisi doğrulanamadı.** Ekip arkadaşının notuna göre konum bildirimine saldırı için aday; tarayıcıdan elle kontrol edilmeli. |
| [RADIATE](https://arxiv.org/abs/2010.09076), [K-Radar](https://arxiv.org/abs/2206.08171) | Sis/kar altında radar, kamera, lidar görüntüleri | Yer gerçeği elle çizilmiş kutular, ham veri. Yalnızca kaynak olarak kullanılıyor (5.3). |
| [Pohang Canal](https://registry.opendata.aws/pohang-canal-dataset/) / [PoLaRIS](https://arxiv.org/html/2412.06192v2) | Deniz; radar, lidar, RGB ve termal kamera | Yer gerçeği elle çizilmiş 3B kutular, ham veri, CC BY-NC. |
| [MAPFusion / NavEYE](https://arxiv.org/abs/2607.03915) (Wuhan Teknoloji Üniversitesi, 2026) | Gemide AIS, ARPA radar izleri (elle hedef seçme modu), video, GNSS, cayro pusula; 135 dk, 1 s'de bir senkronize. Elle yapılmış AIS-radar (75.781 çift) ve görüntü-AIS-radar (5.541 çift) eşleştirme etiketleri. Bağımsız yer gerçeği tek bir gemide (Zhoudou 16, GoPro GPS, 3-5 m). | Makalede veri paylaşımına dair ifade yok. **18 Ekim'de Prof. Liu'dan istendi** (bkz. 12). Gelirse E1 ve E2 kısmen kapanır. |
| [WHUT-MSFVessel](https://github.com/yixiiii/Multi-Source-Fusion-for-Vessels) | Radar + kamera + AIS | Yer gerçeği görüntü kutuları; Baidu Pan'dan kısmen paylaşılmış, lisans yok. |
| [FVessel](https://github.com/gy65896/FVessel) | Kamera + AIS | Yer gerçeği görüntü kutuları; radar yok. |
| MUT (NTNU) | Kamera + lidar, GNSS + PPK yer gerçeği | Radar yok, ham veri. |
| [MMAUD](https://github.com/ntu-aris/MMAUD) | Lidar, kamera, radar, ses; İHA | Ham ve çok büyük (~72 GB+), 30-100 m, ticari olmayan lisans. |
| TSMS-Drone | Çok radarlı drone verisi | Ekip arkadaşının değerlendirmesine göre 2-30 m menzil, tek hedef. Sayfası bu oturumda okunamadı. |
| [OpenSky 2020 uçuş listesi](https://zenodo.org/record/4419079) | Uçuş başına ilk ve son konum | Mesaj seviyesinde veri yok; LocaRDS bunun yerini alıyor. |
| FFI Odin USV ([arXiv 2603.15137](https://arxiv.org/abs/2603.15137)) | Radar + lidar, RTK-GNSS | Bağlantı bir Stone Soup makalesi; veri yayımlanmamış. |
| FGI Jammertest | GNSS karıştırma, ham I/Q | Yazılım alıcı gerekir. Gelecek çalışma. |
| nuScenes | Otomotiv radar, kamera, lidar | Elle çizilmiş kutular, alan uymuyor. |

---

## 6. İhtiyaç → veri eşlemesi

✅ karşılanıyor · ⚠️ kısmen · ❌ açık kaynak yok

### Kalibrasyon

| # | İhtiyaç | Veri | Durum | Kanıt düzeyi |
|---|---|---|---|---|
| K1 | Hedef hızları | CUAS (İHA, insan), DRaT (araç), Moussaïd 2010 (yaya grupları) | ✅ | 3 |
| K2 | İvme, dönüş hızı | CUAS (İHA), DRaT (araç), ETH/UCY (yaya) | ✅ | 3 |
| K3 | Radar tespit ve hata | Autoferry makalesi (yalnızca kıyas) | ⚠️ ölçek farklı | 3-4 |
| K4 | Kamera tespit ve hata | Johnson kriterleri (menzil ve olasılık modeli), Autoferry makalesi (kıyas) | ⚠️ model var, km ölçeğinde ölçüm yok | 3 |
| K5 | Yanlış alarm, sahte iz ömrü | CUAS Demo-4 | ✅ (iz seviyesinde) | 3 |
| K6 | Sisin kameraya etkisi | CEREMA modeli, RADIATE (nitel) | ⚠️ 60 m'ye kadar ölçülmüş | 3 |
| K7 | Karıştırmanın radara etkisi | NAWCWD el kitabı (J/S modeli), JKU Linz ve COSMOS (girişim ölçümleri) | ⚠️ kasıtlı karıştırma ölçümü yok | 3 |
| K8 | Konum bildirimi aralığı ve kaybı | Standartlar, LocaRDS, Fukuda ve ark. 2024 | ⚠️ ADS-B/AIS, dost birlik sistemi değil | 3 |
| K9 | Konum bildirimi sapması | LocaRDS (ADS-B ve MLAT farkı) | ⚠️ | 2-3 |
| K10 | Kesinti süreleri | — | ❌ | 4 |
| K11 | NIS eşiği | CUAS ki-kare değerleri | ⚠️ radarın kendi filtresi | 3 |

### Doğrulama

| # | İhtiyaç | Veri | Durum | Kanıt düzeyi |
|---|---|---|---|---|
| D1 | Çok sensörlü gerçek veri | Autoferry, AERPAW | ✅ | 1 |
| D2 | Bağımsız yer gerçeği | Autoferry (GNSS), AERPAW (RTK GNSS) | ✅ (Autoferry'de doğrulanmamış) | 1 |
| D3 | Çok hedef | Autoferry, DRaT | ✅ | 1 |
| D4 | Manevralı hedef | AERPAW | ✅ | 1 |
| D5 | Asenkron sensörler | Autoferry, AERPAW | ✅ | 1 |
| D6 | Bozulmuş sensör | AERPAW Opt1, Autoferry 2. ortam kameraları | ⚠️ az örnek | 1 |
| D7 | Sensör kesintisi | Autoferry (ölçüm silme), AERPAW (gerçek kopmalar) | ⚠️ | 1 |
| D8 | Konum bildirimi + bağımsız sensör | LocaRDS (ADS-B + MLAT) | ⚠️ radar/kamera yok | 2 |
| D9 | Dost/diğer etiketi | — | ❌ | 4 |
| D10 | Kara hedefleri | DRaT (tek sensör) | ⚠️ insan grubu yok | 1 |
| D11 | km ölçeği | LocaRDS (hava), HAXR (deniz) | ⚠️ | 2 |
| D12 | Kötü hava / karıştırma altında iz | COSMOS (girişim + GPS; A açık, B/E talep) | ⚠️ girişim var, sis ve kasıtlı karıştırma yok | 1-3 |

---

## 7. Eksik veriler

Araştırma sonunda açık kaynakla karşılanamayan ya da zayıf karşılanan
ihtiyaçlar. Bunları nasıl bulacağımız ayrıca tartışılacak.

| # | Eksik | Neden önemli | Şu an elimizdeki en iyi seçenek |
|---|---|---|---|
| E1 | **Dost/diğer etiketi gerçek veride** (D9) | Projenin kimlik iddiası tamamen simülasyonda kalıyor. | MAPFusion gelirse kısmen (AIS'li ve AIS'siz gemiler, elle eşleştirme etiketleriyle). Açık veride: HAXR'da AIS'li ve AIS'siz radar hedefleri; ham radar işlenmesi gerekir. |
| E2 | **Gerçek konum bildirimi + radar/kamera + bağımsız yer gerçeği bir arada** (D8) | Bias düzeltme ve konum bildirimi füzyonu gerçek veride sınanamıyor. | LocaRDS (radar/kamera yok). MAPFusion: 18 Ekim'de istendi. |
| E3 | **Kasıtlı radar karıştırması altında iz verisi** (D12, K7) | Karıştırma senaryosu ve güven mekanizmasının en güçlü bulgusu gerçek veride sınanamıyor. | Ölçüm: JKU Linz ve COSMOS (girişim). Model: NAWCWD el kitabının J/S denklemleri (5.3). Kasıtlı karıştırma verisi yok. |
| E4 | **Gerçek sis altında izleme verisi** (D12) | Sis senaryosu yalnızca ölçüme dayalı simülasyon olarak kalıyor. | CEREMA (model), RADIATE ve K-Radar (ham, kutu etiketli). |
| E5 | **km ölçeğinde kamera başarımı** (K4, K6) | Kamera modeli ve sis modeli 100 m altındaki ölçümlerden ekstrapolasyon. | Ölçüm yok. Model: Johnson kriterleri ve üreticilerin DRI mesafeleri (5.3). |
| E6 | **İnsan grubu hedefi** (D10, K2) | Sahadaki bir hedef türünün gerçek karşılığı yok. | Hareket: Moussaïd 2010 ve ETH/UCY (5.3). Çok sensörlü izleme verisi yok. |
| E7 | **Dost birlik konum bildirim sisteminin gerçek mesaj karakteristiği** (K8) | Gecikme ve mesaj kaybı ADS-B ve AIS'ten kabaca taşınıyor. | Standartlar, LocaRDS, Fukuda 2024. Denenebilir: APRS (amatör telsiz konum yayınları; doğrulanmadı). |
| E8 | **Sensör kesintisi istatistikleri** (K10) | Sensör kaybı senaryosunun süreleri varsayım. | Konum bildirimi için LocaRDS/OpenSky'daki mesaj boşlukları kullanılabilir. Radar ve kamera için yok. |
| E9 | **Autoferry yer gerçeğinin doğruluğu ve zaman eşlemesi** | Ana verideki bütün hatalar bu belirsizliği içeriyor. | 18 Ekim'de Vasstein'a soruldu. Beklerken lidar-yer gerçeği karşılaştırmasıyla anten ve zaman kayması kendimiz kestirilebilir. |
| E10 | **km ölçeğinde, sabit sensörlü kara/hava sahası, çok sensör, bağımsız yer gerçeği** | Projenin senaryosunun gerçek karşılığı. | Yok. Bileşen doğrulamasıyla dolaylı olarak karşılanıyor. |

**Mail dışındaki seçenekler:**
- **Danışman hocaya sormak:** Savunma sanayiinden bir bağlantısı varsa, bitirme
  projeleri için gizlilik sözleşmesiyle veri verilebiliyor. E1, E3 ve E10 için
  tek gerçekçi yol bu. Hocadan cevap bekleniyor.
- **Kendi küçük deneyimiz (E1, E6):** Ekipten biri telefonla konumunu yayınlar
  (dost), diğerleri yayınlamaz (diğer), hepsini bir kamera kaydeder. Radarsız
  ve kısa menzilli, ama dost/diğer ayrımını ve insan grubunu gerçek veride
  gösterir.

---

## 8. Kullanım planı

Her aşamanın sonunda gösterilebilir bir sonuç çıkar. Takvim sıkışırsa sondan
başlayarak adımlar "gelecek çalışma"ya alınır. Yalnızca 1. ve 2a. aşamalar
bile projeyi "sadece simülasyon" olmaktan çıkarır.

### Aşama 1: Simülasyonun kalibrasyonu

*Kod değişikliği en az; sonuçlar 3. kanıt düzeyine çıkar.*

| Ne yapılır | Veri | Proje kısmı |
|---|---|---|
| Hedef hızları, ivme σ, ω σ, IMM geçiş matrisi | CUAS, DRaT | `src/saha.py`, `src/kalman.py` |
| İnsan grubu hızı (1.5 → ~1.1-1.2 m/s) ve dönüşleri | Moussaïd 2010, ETH/UCY | `src/saha.py` |
| Kamera menzili ve mesafeye bağlı tespit olasılığı | Johnson kriterleri | `src/sensorler.py` |
| İz onay ve silme eşikleri, yanlış alarm oranı | CUAS Demo-4 | `src/fuzyon.py`, `src/sensorler.py` |
| NIS toleransının gerçek ki-kare dağılımıyla karşılaştırılması | CUAS | `src/fuzyon.py` |
| Görüş mesafesine bağlı sis modeli | CEREMA | Sis senaryosu |
| Mesafeye ve yöne bağlı karıştırma modeli (J/S); gürültü mü aldatıcı mı karıştırıcı olduğuna karar | NAWCWD el kitabı | Karıştırma senaryosu |
| Karıştırma modelinin ölçümlerle karşılaştırılması | JKU Linz, COSMOS | Karıştırma senaryosu |
| Konum bildirimi aralığı için kaynak | Standartlar, Fukuda 2024 | `src/sensorler.py` |
| Sis varsayımı için kaynak | RADIATE | README |

**Çıktı:** Güncellenmiş parametrelerle yeniden 30 + 30 tekrarlı simülasyon.
Eski ve yeni sonuçlar yan yana; hangi parametrenin hangi veriden geldiğini
gösteren tablo.

### Aşama 2: Autoferry ile gerçek veri testi

*Kanıt düzeyi 1.*

**Gereken kod:**
- JSON okuyucu.
- Yer gerçeğinin ölçüm anlarına ara değerlenmesi.
- Makaleyle aynı eşleşme eşikleri.
- Yer gerçeği kontrolleri (sıçrama, boşluk, imkânsız hız).

**Adımlar:**
- **2a: Radar + lidar.** İkisi de (x, y) verdiği için mevcut kod neredeyse
  olduğu gibi çalışır.
- **2b: Kameraların eklenmesi.** Açı ölçüm modeli (EKF). İz başlatmayı yalnızca
  radar ve lidar yapar (makaledeki gibi). Güven ablasyonu (açık/kapalı) 2.
  ortamda yapılır.
- **2c: Ek deneyler.**
  - Sensör kaybı: gerçek ölçümler silinerek.
  - Anten ve zaman kayması kestirimi: düzeltilmiş ve düzeltilmemiş sonuçlar
    yan yana.

### Aşama 3: AERPAW ile gerçek İHA testi

*Kanıt düzeyi 1.*

**Gereken kod:**
- Enlem-boylamdan yerel x-y'ye dönüşüm.
- Kutupsal radar ölçüm modeli (EKF).
- CEP'ten kovaryans üretme.

**Adımlar:**
1. Önce bir uçuşta radar izi, RF konumları ve RTK yer gerçeği üst üste
   çizilir; veri kullanılabilir mi kontrol edilir.
2. Sadece radar, sadece RF ve füzyon, GPS'e göre karşılaştırılır.
3. NIS güveni Opt1'in ilk koşusu ile `rerun` arasında karşılaştırılır.

### Aşama 4: İsteğe bağlı genişletmeler

| Veri | Ne sınanır | Kanıt düzeyi |
|---|---|---|
| LocaRDS | ADS-B (konum bildirimi) + MLAT ile km ölçeğinde füzyon ve bias kestirimi | 2 |
| DRaT | Çok sayıda kara hedefinde radar izleme, ilişkilendirme ve kimlik | 1 |
| HAXR | AIS ile radar arasındaki sapma; çok radarlı tutarlılık | 2 |

---

## 9. Değerlendirme kuralları

1. **Ayar/test ayrımı:** Ayarlar, eşikler ve dışlama kuralları ayar verisinde
   belirlenir ve test sonuçlarına bakılmadan sabitlenir.
   - **Autoferry:** Ayar 1. ortam (2-6), test 2. ortam (13, 16, 17, 22).
     Ölçüm gürültüsü de yalnızca 1. ortamdan kestirilir.
   - **AERPAW:** Erken test uçuşlarında yalnızca USRP verisi var, radar ve RF
     yok. Bu yüzden ayar seti radar ve RF içeren uçuşlardan seçilmeli (ör.
     Opt1-3 ve birkaç takımın uçuşları ayar, kalanlar test). Bölünme veriye
     bakılmadan önce yazılır.
   - **DRaT:** Ayar serbest akış, test sıkışık trafik.
2. **Yer gerçeği düzeltmeleri** (ör. Autoferry'de anten ve zaman kayması)
   öncesi ve sonrası yan yana raporlanır.
3. **Yer gerçeği kontrollerinin** kuralları önceden yazılır. Dışlanan her parça
   gerekçesiyle listelenir.
4. **Referanssız izler** (yer gerçeği olmayan gerçek tekneler) "yanlış iz"
   sayılmaz, ayrı kategoride raporlanır. Ayrım kuralı ayar verisinde sabitlenir.
5. **Güven ablasyonu** gerçek veride de yapılır. Ölçüm gürültüsü yalnızca temiz
   ayar verisinden kestirilir; aksi halde güven, sensör bozulduğu için değil R
   yanlış olduğu için düşer.
6. **Sensör kaybı deneyleri** "sağlamlık testi" başlığıyla ayrı raporlanır.
7. **Raporlama:**
   - Her senaryo ayrı verilir; ortalamalar bootstrap güven aralıklarıyla.
   - "30/30" yerine "4 test senaryosunun 3'ünde" gibi gerçek sayılar kullanılır.
   - Füzyonun kötü olduğu durumlar da raporlanır.
   - Farklı veri setlerinin sonuçları tek ortalamada birleştirilmez.
8. **Her sonuç kanıt düzeyiyle birlikte** sunulur (bkz. 3. bölüm).

### Raporlama şablonu

| İddia | Veri | Kanıt düzeyi | Sonuç | Sınırlama |
|---|---|---|---|---|
| ör. Güven mekanizması bozulan sensörü fark eder | Autoferry 2. ortam; AERPAW Opt1 | Gerçek veri | (doldurulacak) | 4 test senaryosu; tek antenli yer gerçeği; tek bozulma örneği |
| ör. Karıştırmada füzyon tek sensörden iyidir | Simülasyon, 30 seed | Ölçüme dayalı simülasyon | (doldurulacak) | Girişim modeli 77 GHz otomotiv radarından |

---

## 10. Yapılmayacaklar

| Yöntem | Neden |
|---|---|
| Farklı veri setlerini tek sahnede birleştirmek | Gerçekte yaşanmamış, yapay bir sahne üretir. |
| Sahte AIS / konum bildirimi üretmek, gerçek veriye yapay bias eklemek | Ölçülmemiş bir sensör ya da hata icat eder. |
| Gerçek veriye sahte yanlış alarm ya da karıştırma eklemek | Veri karma hâle gelir; gerçek veri sonucu gibi sunulamaz. Yapılırsa ana sonuçlardan ayrı ve "karma veri" etiketiyle. |
| AIS / ADS-B'yi bağımsız yer gerçeği gibi sunmak | Hedefin kendi bildirimidir; yalnızca yaklaşık referans. |
| Simülasyon gürültülerini Autoferry değerlerine çekmek | Farklı sensör ve ölçek; değerler yer gerçeği hatasını da içerir. Yalnızca kıyas için kullanılır. |
| Parametreleri test verisinde ayarlamak | Sonucu iyimser gösterir. |
| Kötü sonuç veren senaryoları sonradan dışlamak | Seçici raporlama. |

---

## 11. Doğrulama notları

Bu raporda geçen veri setlerinin sayfaları 13 Ekim 2026'da tek tek açılıp
kontrol edildi. Önceki belgelerdeki bilgilerle farklı çıkan noktalar:

| Konu | Önceki bilgi | Kontrol sonucu |
|---|---|---|
| AERPAW yer gerçeği | Belirsiz | Veri makalesinde İHA'da **RTK destekli GNSS** olduğu yazıyor. İrtifa 25 m. Radar ve RF güncelleme hızları makalenin okunan kısmında yok. |
| AERPAW ayar seti | "Erken uçuşlar" | Erken uçuşlarda radar ve RF verisi yok (yalnızca USRP). Ayar seti radarlı uçuşlardan seçilmeli. |
| DLR radar + AIS | "Talep üzerine; NATO/AB" | Sayfada iki veri seti var. 1.si HAXR'ın kendisi, açık. 2.si talep formu ve ihracat kontrolüyle. "NATO/AB" ifadesi sayfanın okunan kısmında görülmedi. |
| HAXR | — | Zenodo'da iki sürüm (1.0.0 ve 1.1.0); doğru bağlantı 1.1.0 (19824555). |
| FFI Odin USV | Veri seti | Bağlantı bir Stone Soup makalesi; veri bağlantısı yok. |
| CUAS | İHA ve kuş izleri | İnsan ve araç izleri de var; ham CSV'lerde iz yönetimi ve ki-kare alanları var. |
| WHUT-MSFVessel | ~6 saat | Sayfa kaydın 12 aya yayıldığını söylüyor; toplam süre yazmıyor. |
| LocaRDS | "~50.9 milyon uçak konumu, nanosaniye TOA" | Sayfada "50 milyondan fazla yayın, 222 milyondan fazla ölçüm". Nanosaniye çözünürlük ve MLAT sayfada açıkça yazmıyor; belgelerden kontrol edilmeli. |
| CEREMA / Bijelic | 2019, görüş 10-60 m | Makale IEEE IV **2018**'de yayımlanmış (arXiv'e 2019'da yüklenmiş). Görüş aralıkları 10-20, 20-30, 30-40 ve 50-60 m (40-50 m yok). |
| COSMOS | 2021, talep üzerine | Kasım 2021'de toplanmış, Ocak 2022'de yayımlanmış. **Repository A (777) açık erişimli**; B (785) ve E (788) talep üzerine. Ayrı bir veri makalesi yok; bağlı yayın Pirkani'nin doktora tezi (2024). Raporun giriş bölümü tarihi "Eylül 2021" diye veriyor, diğer her yer Kasım; büyük olasılıkla yazım hatası. |
| COSMOS A'nın içeriği | — | 777'deki Readme "1b, 2g, 2d" diyor; veri raporunun iki sürümü (Rev B ve Rev C) "1b, 2g, 3d" diyor. Zip açılınca kesinleşecek. |
| Autoferry yer gerçeği | Alıcı türü belirsiz | Makaleye göre Gunnerus ve Jetboat'ta ZED-F9P + PPK, Havfruen'de Ellipse-D. Çalışan antenler senaryoya göre Tablo 2-3'te (5.1'de özetlendi). |
| MAPFusion | İndirme yolu yok | Makalede veri paylaşım beyanı yok. Bağımsız yer gerçeği yalnızca bir gemide (GoPro GPS, 3-5 m). Radar izleri ARPA'nın elle hedef seçme modundan. |
| Lille GNSS aldatma | Etalab 2.0, 33.7 GB | **Doğrulanamadı:** sayfa bot korumasıyla erişime kapalıydı. |
| OpenSky 2020 (Zenodo 4419079) | Konum bildirimi kalibrasyonu | Yalnızca uçuş listesi; kullanılamaz. |
| RADIATE | Kamera bozulma oranları | Makalede kameranın siste bozulmasına dair sayı yok; yalnızca radarın başarımı ölçülmüş. |

Okunamayan sayfalar: MUT (PMC13230884) ve Svanström drone verisi (PMC8573135)
CAPTCHA gösterdi; TSMS-Drone olduğu düşünülen *Scientific Data* 2026 makalesi
giriş istedi; Lille sayfası bot korumasıyla kapalıydı. Bunlar tarayıcıdan elle
kontrol edilmeli.

---

## 12. Açık sorular

### Yazarlarla iletişim (18 Ekim 2026)

| Konu | Kime | Durum | Ne istendi |
|---|---|---|---|
| Autoferry | Kjetil Vasstein (CC: E. Brekke, Ø. K. Helgesen) | Gönderildi | Yer gerçeğinin referans noktası, anten konumları, zaman eşlemesi, doğruluk |
| MAPFusion | Prof. Ryan Wen Liu | Gönderildi | AIS, ARPA radar izleri, GNSS/cayro, eşleştirme etiketleri, Zhoudou 16 GPS kaydı; ham video hariç |
| COSMOS B ve E | "Request a copy" formları + Prof. Marina Gashinova | Bekliyor | 2d ve 3d senaryoları; GPS doğruluğu; işlenmiş tespit var mı. A'nın içeriği kontrol edildikten sonra gönderilecek. |

Cevap gelmezse 1 Kasım 2026 civarında hatırlatma gönderilecek.

### Diğer açık sorular

- **Autoferry:** Mayıs 2021 kaydında hedef GNSS doğruluğu, zaman eşlemesi ve
  anten konumları. Vasstein'a soruldu (yukarıda).
- **Kamera modeli:** Johnson hesabı için bir kamera modeli (çözünürlük ve görüş
  açısı) ve hedeflerin kritik boyutları seçilmeli. Ayrıca bizim kameramızın
  "menzili" tespit mi, tanıma mı olarak tanımlanacak, karar verilmeli.
- **Karıştırıcı türü:** Simülasyondaki karıştırıcı gürültü karıştırıcısı mı,
  aldatıcı karıştırıcı mı? Model buna göre değişir (bkz. 5.3).
- **AERPAW:**
  - Lisans Dryad sayfasında belirtilmemiş; kontrol edilmeli.
  - Radar ve RF güncelleme hızları ile doğrulukları veri makalesinin
    PDF'inden okunmalı.
  - LoRa paketlerinin `data` alanında İHA kendi konumunu gönderiyor mu? (Bu
    yalnızca bir tahmin.) Gönderiyorsa, gerçek gecikmesi ve kaybı olan bir
    konum bildirimi kaynağı olur.
- **LocaRDS:** Zaman damgası çözünürlüğü ve MLAT için gereken alıcı konumları;
  yarışma makalesinden ([arXiv 2209.13669](https://arxiv.org/abs/2209.13669))
  kontrol edilmeli.
- **Lille GNSS aldatma:** Sayfa ve yer gerçeğinin nasıl sağlandığı tarayıcıdan
  kontrol edilmeli.
- **JKU Linz:** Sahne geometrisi `documentation.pdf`'ten okunmalı.
- **COSMOS A:** Zip'te 3d mi, 2d mi olduğu (bkz. 11).
- **AIS ve ADS-B standartları:** Rapordaki mesaj aralıkları standartların
  kendisinden doğrulanmalı.

---

## 13. Kaynaklar

**Makaleler**

- Helgesen, Ø. K., Vasstein, K., Brekke, E. F., Stahl, A. (2022).
  Heterogeneous multi-sensor tracking for an autonomous surface vehicle in a
  littoral environment. *Ocean Engineering*, 252, 111168.
  [doi:10.1016/j.oceaneng.2022.111168](https://doi.org/10.1016/j.oceaneng.2022.111168)
- Vasstein, K. (2021). *A high fidelity digital twin framework for testing
  exteroceptive perception of autonomous vessels.* Yüksek lisans tezi, NTNU.
  [hdl.handle.net/11250/2781031](https://hdl.handle.net/11250/2781031)
- Hossen ve ark. (2026). Collection: UAV-Based Wireless Multi-modal
  Measurements from AERPAW Autonomous Data Mule (AADM) Challenge in Digital
  Twin and Real-World Environments.
  [arXiv:2602.16163](https://arxiv.org/abs/2602.16163)
- Bijelic, M., Gruber, T., Ritter, W. (2018). Benchmarking Image Sensors Under
  Adverse Weather Conditions for Autonomous Driving. *IEEE Intelligent Vehicles
  Symposium (IV)*. doi:10.1109/IVS.2018.8500659,
  [arXiv:1912.03238](https://arxiv.org/abs/1912.03238)
- Sheeny, M. ve ark. (2021). RADIATE: A Radar Dataset for Automotive
  Perception in Bad Weather. [arXiv:2010.09076](https://arxiv.org/abs/2010.09076)
- Paek, D.-H. ve ark. (2022). K-Radar: 4D Radar Object Detection for
  Autonomous Driving in Various Weather Conditions. *NeurIPS*.
  [arXiv:2206.08171](https://arxiv.org/abs/2206.08171)
- Liu, R. W., Liang, J., Wang, H., Bao, M. (2026). NavEYE: Vision-centered
  multi-sensor fusion-based situational awareness system for intelligent
  surface vehicles. *Ocean Engineering*, 363, 126781.
  [doi:10.1016/j.oceaneng.2026.126781](https://doi.org/10.1016/j.oceaneng.2026.126781),
  [arXiv:2607.03915](https://arxiv.org/abs/2607.03915)
- Moussaïd, M., Perozo, N., Garnier, S., Helbing, D., Theraulaz, G. (2010). The
  walking behaviour of pedestrian social groups and its impact on crowd
  dynamics. *PLoS ONE*, 5(4), e10047.
  [doi:10.1371/journal.pone.0010047](https://doi.org/10.1371/journal.pone.0010047)
- Fukuda, G., Tamaru, H., Kubo, N., Shoji, R. (2024). A study on AIS positional
  error analysis and transmission frequency requirements of attitude data for
  future vessel monitoring. *The Journal of Navigation*, 77(5-6), 677-694.
- Pirkani, A. A. (2024). *Characterisation and Mitigation of Radar Interference
  in Automotive Applications.* Doktora tezi, Birmingham Üniversitesi.
  [etheses.bham.ac.uk/id/eprint/14440](https://etheses.bham.ac.uk/id/eprint/14440)
- Naval Air Warfare Center Weapons Division (1999; 2013 güncellemesi).
  *Electronic Warfare and Radar Systems Engineering Handbook.* NAWCWD TP 8347.
  Açık erişim.
  [HTML sürümü](https://rfcafe.com/references/electrical/ew-radar-handbook/support-jamming.htm)
- Johnson kriterleri:
  [özet](https://en.wikipedia.org/wiki/Johnson%27s_criteria). Asıl kaynak
  Johnson, J. (1958), "Analysis of image forming systems", *Image Intensifier
  Symposium*; NATO STANAG 4347 bu yönteme dayanır.

**Veri setleri**

- Autoferry: [github.com/Autoferry/sensor_fusion_dataset](https://github.com/Autoferry/sensor_fusion_dataset)
- AERPAW AADM: [doi:10.5061/dryad.7d7wm3898](https://datadryad.org/dataset/doi:10.5061/dryad.7d7wm3898)
- CUAS (UAV vs. Bird Radar Tracks): [github.com/nrc-cnrc/CUAS-sensing-dataset](https://github.com/nrc-cnrc/CUAS-sensing-dataset)
- DRaT: [zenodo.org/records/20171110](https://zenodo.org/records/20171110)
- LocaRDS: [zenodo.org/records/4302249](https://zenodo.org/records/4302249)
- JKU Linz radar girişimi: [zenodo.org/records/21933926](https://zenodo.org/records/21933926)
- HAXR: [zenodo.org/records/19824555](https://zenodo.org/records/19824555)
- DLR deniz radarı veri setleri: [dlr.de](https://www.dlr.de/en/kn/about-us/departments/nautical-systems/real-world-marine-radar-datasets-for-target-tracking)
- COSMOS: [edata.bham.ac.uk/777](https://edata.bham.ac.uk/777/) (A, açık),
  [785](https://edata.bham.ac.uk/785) (B), 786 (C), 787 (D),
  [788](https://edata.bham.ac.uk/788) (E)
- ETH/UCY yaya yörüngeleri: [TIB kaydı](https://service.tib.eu/ldmservice/dataset/eth-and-ucy-datasets)
- 7V-Scanario: [github.com/UniBwTAS/7V-Scanario](https://github.com/UniBwTAS/7V-Scanario)
- Lille GNSS aldatma: [doi:10.57745/3C63J0](https://doi.org/10.57745/3C63J0)
- RADIATE: [pro.hw.ac.uk/radiate](http://pro.hw.ac.uk/radiate/)
- Pohang Canal: [registry.opendata.aws/pohang-canal-dataset](https://registry.opendata.aws/pohang-canal-dataset/)
- WHUT-MSFVessel: [github.com/yixiiii/Multi-Source-Fusion-for-Vessels](https://github.com/yixiiii/Multi-Source-Fusion-for-Vessels)
- FVessel: [github.com/gy65896/FVessel](https://github.com/gy65896/FVessel)
- MMAUD: [github.com/ntu-aris/MMAUD](https://github.com/ntu-aris/MMAUD)
- FGI Jammer Test 2023: doi:10.23729/fd-06d27736-45cb-3ca2-aff8-725d42c6caeb

**Standartlar**

- ITU-R M.1371: Technical characteristics for an automatic identification
  system using time division multiple access in the VHF maritime mobile band.
- RTCA DO-260B: Minimum Operational Performance Standards for 1090 MHz
  Extended Squitter ADS-B.
