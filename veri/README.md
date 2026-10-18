# veri/

Projede kullanılan gerçek veri setlerinin indirildiği klasör. Bu README
dışındaki her şey git'e eklenmez (`.gitignore`). Veri setlerinin seçilme
gerekçesi `docs/veri_seti_arastirmasi.md`, ihtiyaç tablosu
`docs/veri_ihtiyac_tablosu.xlsx` dosyasındadır.

| Klasör | Veri seti | Boyut | Erişim | Kaynak |
|---|---|---:|---|---|
| `autoferry/` | Autoferry sensör füzyonu veri seti | ~6 MB | Açık, CC0 | https://github.com/Autoferry/sensor_fusion_dataset |
| `cuas/` | CUAS: UAV vs. Bird Radar Tracks | belirtilmemiş | Açık, CC BY 4.0 | https://github.com/nrc-cnrc/CUAS-sensing-dataset |
| `aerpaw/` | AERPAW AADM | 7.7 GB | Açık | https://datadryad.org/dataset/doi:10.5061/dryad.7d7wm3898 |
| `cosmos/A_777/` | COSMOS Repository A (1b, 2g, 3d girişimli) | 9 GB | Açık, CC BY 4.0 | https://edata.bham.ac.uk/777/ |
| `cosmos/B_785/` | COSMOS Sub-Dataset B (2d) | 6 GB | Talep formu | https://edata.bham.ac.uk/785/ |
| `cosmos/E_788/` | COSMOS Sub-Dataset E (3d) | 7 GB | Talep formu | https://edata.bham.ac.uk/788/ |
| `jku_linz/` | JKU Linz 77 GHz radar girişimi | 2.6 GB | Açık, CC BY 4.0 | https://zenodo.org/records/21933926 |
| `drat/` | DRaT otoyol radarı | 91 MB | Açık, CC BY 4.0 | https://zenodo.org/records/20171110 |
| `eth_ucy/` | ETH/UCY yaya yörüngeleri | küçük | Yalnızca araştırma | https://service.tib.eu/ldmservice/dataset/eth-and-ucy-datasets |
| `locards/` | LocaRDS (ADS-B, isteğe bağlı) | 3.6 GB | Açık, CC BY-SA 4.0 | https://zenodo.org/records/4302249 |
| `haxr/` | HAXR (isteğe bağlı) | 5.4 GB | Açık, CC BY 4.0 | https://zenodo.org/records/19824555 |
| `7v_scanario/` | 7V-Scanario (isteğe bağlı) | belirtilmemiş | Lisans talep üzerine | https://github.com/UniBwTAS/7V-Scanario |
| `mapfusion/` | MAPFusion (yazardan istendi) | — | Mail bekleniyor | https://arxiv.org/abs/2607.03915 |
| `kaynaklar/` | Makale PDF'leri ve veri belgeleri | — | — | — |

## Kurallar

- Her veri setini kendi klasörüne, indirildiği hâliyle koy. Ham dosyaları
  değiştirme; işlenmiş çıktılar için alt klasör aç (ör. `autoferry/islenmis/`).
- İndirdiğin tarihi ve sürümü (ör. Zenodo sürüm numarası) aşağıya not et.
- Büyük zip'leri açtıktan sonra, yer gerekirse zip'i silebilirsin; yeniden
  indirilebilirler.

## İndirme kaydı

| Veri seti | İndirme tarihi | Sürüm / not |
|---|---|---|
| | | |
