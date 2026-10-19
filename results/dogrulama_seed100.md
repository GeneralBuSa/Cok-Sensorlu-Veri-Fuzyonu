| Senaryo | Konfigürasyon | RMSE (m) | GOSPA (m) | Kaçırma (%) | Yanlış iz | ID switch | Etiket doğruluğu (%) |
|---|---|---:|---:|---:|---:|---:|---:|
| normal | Sadece radar | 13.4 ± 0.5 | 33.8 ± 1.1 | 1.4 ± 0.1 | 0.0 ± 0.0 | 0.0 ± 0.2 | 60.0 ± 0.0 |
| normal | Sadece kamera | 9.7 ± 1.5 | 177.2 ± 1.8 | 31.7 ± 0.4 | 0.0 ± 0.0 | 0.7 ± 0.8 | 72.1 ± 0.3 |
| normal | Sadece konum bildirimi | 40.5 ± 0.2 | 313.2 ± 0.3 | 60.8 ± 0.2 | 0.0 ± 0.0 | 0.0 ± 0.2 | 100.0 ± 0.0 |
| normal | Füzyon (güven ağırlıklandırma kapalı) | 8.7 ± 0.5 | 21.0 ± 1.3 | 1.1 ± 0.1 | 0.0 ± 0.2 | 0.0 ± 0.0 | 100.0 ± 0.0 |
| normal | Füzyon (IMM kapalı, sadece CV) | 13.0 ± 1.0 | 26.3 ± 1.5 | 1.2 ± 0.1 | 0.0 ± 0.2 | 1.0 ± 0.0 | 100.0 ± 0.0 |
| normal | **Füzyon** | 8.7 ± 0.5 | 21.0 ± 1.3 | 1.1 ± 0.1 | 0.0 ± 0.2 | 0.0 ± 0.0 | 100.0 ± 0.0 |
| sis | Sadece radar | 13.4 ± 0.5 | 33.8 ± 1.1 | 1.4 ± 0.1 | 0.0 ± 0.0 | 0.0 ± 0.2 | 60.0 ± 0.0 |
| sis | Sadece kamera | 18.0 ± 2.4 | 322.1 ± 2.5 | 67.0 ± 0.8 | 0.0 ± 0.2 | 1.3 ± 1.5 | 84.3 ± 1.1 |
| sis | Sadece konum bildirimi | 40.4 ± 0.2 | 313.3 ± 0.3 | 60.9 ± 0.1 | 0.0 ± 0.0 | 0.0 ± 0.2 | 100.0 ± 0.0 |
| sis | Füzyon (güven ağırlıklandırma kapalı) | 12.6 ± 0.7 | 35.5 ± 4.2 | 1.2 ± 0.1 | 1.2 ± 1.0 | 0.3 ± 0.7 | 100.0 ± 0.0 |
| sis | Füzyon (IMM kapalı, sadece CV) | 15.2 ± 1.0 | 34.7 ± 1.8 | 1.5 ± 0.1 | 0.0 ± 0.0 | 1.0 ± 0.2 | 100.0 ± 0.0 |
| sis | **Füzyon** | 11.1 ± 0.6 | 27.4 ± 1.2 | 1.1 ± 0.1 | 0.0 ± 0.0 | 0.0 ± 0.2 | 100.0 ± 0.0 |
| karistirma | Sadece radar | 34.7 ± 3.1 | 114.1 ± 6.7 | 10.4 ± 1.5 | 0.1 ± 0.4 | 1.6 ± 0.7 | 65.5 ± 0.8 |
| karistirma | Sadece kamera | 9.8 ± 1.3 | 177.6 ± 2.0 | 31.8 ± 0.5 | 0.0 ± 0.0 | 0.7 ± 0.7 | 72.1 ± 0.3 |
| karistirma | Sadece konum bildirimi | 40.5 ± 0.2 | 313.4 ± 0.4 | 60.9 ± 0.2 | 0.0 ± 0.0 | 0.2 ± 0.4 | 100.0 ± 0.0 |
| karistirma | Füzyon (güven ağırlıklandırma kapalı) | 11.3 ± 1.9 | 152.3 ± 9.2 | 1.2 ± 0.2 | 42.7 ± 4.9 | 0.7 ± 0.9 | 100.0 ± 0.0 |
| karistirma | Füzyon (IMM kapalı, sadece CV) | 17.1 ± 4.6 | 33.1 ± 9.9 | 1.3 ± 0.2 | 0.1 ± 0.3 | 1.2 ± 0.4 | 100.0 ± 0.0 |
| karistirma | **Füzyon** | 9.7 ± 0.8 | 23.0 ± 1.7 | 1.1 ± 0.1 | 0.1 ± 0.3 | 0.0 ± 0.0 | 100.0 ± 0.0 |
| sensor_kaybi | Sadece radar | 14.1 ± 0.8 | 116.8 ± 1.5 | 23.8 ± 0.2 | 0.0 ± 0.0 | 5.1 ± 0.3 | 60.0 ± 0.1 |
| sensor_kaybi | Sadece kamera | 9.5 ± 1.4 | 254.8 ± 1.8 | 54.7 ± 0.5 | 0.0 ± 0.0 | 4.3 ± 0.4 | 75.5 ± 0.6 |
| sensor_kaybi | Sadece konum bildirimi | 40.5 ± 0.2 | 329.9 ± 0.2 | 68.8 ± 0.1 | 0.0 ± 0.0 | 2.0 ± 0.0 | 100.0 ± 0.0 |
| sensor_kaybi | Füzyon (güven ağırlıklandırma kapalı) | 10.5 ± 0.7 | 41.5 ± 1.0 | 4.6 ± 0.1 | 0.0 ± 0.0 | 3.1 ± 0.3 | 100.0 ± 0.0 |
| sensor_kaybi | Füzyon (IMM kapalı, sadece CV) | 14.1 ± 0.7 | 48.0 ± 1.1 | 5.0 ± 0.3 | 0.0 ± 0.0 | 4.2 ± 0.5 | 100.0 ± 0.0 |
| sensor_kaybi | **Füzyon** | 10.5 ± 0.7 | 41.6 ± 1.1 | 4.6 ± 0.1 | 0.0 ± 0.0 | 3.1 ± 0.3 | 100.0 ± 0.0 |

| Senaryo | Füzyonun en iyi tek sensörden düşük olduğu koşu: RMSE | GOSPA |
|---|---:|---:|
| normal | 24/30 | 30/30 |
| sis | 30/30 | 30/30 |
| karistirma | 13/30 | 30/30 |
| sensor_kaybi | 5/30 | 30/30 |

| Senaryo | Bias kestirimi x (m) | Bias kestirimi y (m) | Kestirim hatası (m) |
|---|---:|---:|---:|
| normal | 35.4 ± 2.1 | -19.8 ± 2.3 | 2.7 ± 1.5 |
| sis | 35.3 ± 2.2 | -19.7 ± 2.5 | 2.9 ± 1.5 |
| karistirma | 35.4 ± 2.2 | -19.6 ± 2.3 | 2.8 ± 1.5 |
| sensor_kaybi | 35.5 ± 2.1 | -19.7 ± 2.5 | 2.8 ± 1.7 |

Filtre tutarlılığı: konum NEES'i. Tutarlı bir filtrede ANEES ≈ 2 olur ve noktaların ~%95'i %95 kabul bandında kalır.

| Senaryo | Füzyon (IMM) ANEES | IMM bantta (%) | Sadece CV ANEES | CV bantta (%) | İHA-1 ANEES (IMM / CV) |
|---|---:|---:|---:|---:|---:|
| normal | 1.81 | 68 | 3.53 | 63 | 2.2 / 9.8 |
| sis | 2.20 | 60 | 3.50 | 57 | 2.4 / 8.3 |
| karistirma | 1.92 | 70 | 3.83 | 65 | 2.4 / 11.0 |
| sensor_kaybi | 1.87 | 73 | 3.15 | 66 | 2.3 / 7.9 |

Mann-Whitney U testi, füzyon: seed 42-71 ile bu küme (iki yönlü; p > 0.05 ise anlamlı fark yok)

| Senaryo | GOSPA p | RMSE p |
|---|---:|---:|
| normal | 0.25 | 0.46 |
| sis | 0.99 | 0.73 |
| karistirma | 0.77 | 0.51 |
| sensor_kaybi | 0.14 | 0.09 |
