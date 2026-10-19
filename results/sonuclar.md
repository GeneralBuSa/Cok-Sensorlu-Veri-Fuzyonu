| Senaryo | Konfigürasyon | RMSE (m) | GOSPA (m) | Kaçırma (%) | Yanlış iz | ID switch | Etiket doğruluğu (%) |
|---|---|---:|---:|---:|---:|---:|---:|
| normal | Sadece radar | 13.4 ± 0.7 | 34.2 ± 1.5 | 1.5 ± 0.1 | 0.0 ± 0.0 | 0.1 ± 0.3 | 60.0 ± 0.1 |
| normal | Sadece kamera | 9.4 ± 1.0 | 177.2 ± 2.0 | 31.8 ± 0.5 | 0.0 ± 0.0 | 0.6 ± 0.8 | 72.2 ± 0.3 |
| normal | Sadece konum bildirimi | 40.5 ± 0.2 | 313.3 ± 0.3 | 60.8 ± 0.1 | 0.0 ± 0.0 | 0.0 ± 0.2 | 100.0 ± 0.0 |
| normal | Füzyon (güven ağırlıklandırma kapalı) | 8.6 ± 0.6 | 21.1 ± 0.9 | 1.1 ± 0.1 | 0.0 ± 0.0 | 0.0 ± 0.0 | 100.0 ± 0.0 |
| normal | Füzyon (IMM kapalı, sadece CV) | 12.7 ± 0.8 | 26.2 ± 1.1 | 1.2 ± 0.1 | 0.0 ± 0.0 | 1.0 ± 0.0 | 100.0 ± 0.0 |
| normal | **Füzyon** | 8.6 ± 0.6 | 21.1 ± 0.9 | 1.1 ± 0.1 | 0.0 ± 0.0 | 0.0 ± 0.0 | 100.0 ± 0.0 |
| sis | Sadece radar | 13.4 ± 0.7 | 34.2 ± 1.5 | 1.5 ± 0.1 | 0.0 ± 0.0 | 0.1 ± 0.3 | 60.0 ± 0.1 |
| sis | Sadece kamera | 17.0 ± 2.2 | 322.0 ± 3.7 | 67.1 ± 1.5 | 0.0 ± 0.2 | 0.9 ± 0.5 | 84.6 ± 2.6 |
| sis | Sadece konum bildirimi | 40.5 ± 0.2 | 313.3 ± 0.3 | 60.8 ± 0.1 | 0.0 ± 0.0 | 0.1 ± 0.3 | 100.0 ± 0.0 |
| sis | Füzyon (güven ağırlıklandırma kapalı) | 12.6 ± 1.1 | 37.2 ± 6.1 | 1.2 ± 0.1 | 1.6 ± 1.4 | 1.0 ± 1.3 | 100.0 ± 0.0 |
| sis | Füzyon (IMM kapalı, sadece CV) | 15.0 ± 0.9 | 34.8 ± 1.7 | 1.5 ± 0.2 | 0.0 ± 0.0 | 1.0 ± 0.0 | 100.0 ± 0.0 |
| sis | **Füzyon** | 11.2 ± 0.9 | 27.6 ± 1.5 | 1.2 ± 0.1 | 0.0 ± 0.0 | 0.1 ± 0.3 | 100.0 ± 0.0 |
| karistirma | Sadece radar | 35.1 ± 3.3 | 115.3 ± 6.7 | 10.6 ± 1.7 | 0.1 ± 0.3 | 1.6 ± 0.8 | 65.6 ± 0.9 |
| karistirma | Sadece kamera | 9.5 ± 1.2 | 177.3 ± 1.4 | 31.8 ± 0.4 | 0.0 ± 0.0 | 0.6 ± 0.7 | 72.1 ± 0.3 |
| karistirma | Sadece konum bildirimi | 40.4 ± 0.2 | 313.3 ± 0.5 | 60.9 ± 0.2 | 0.0 ± 0.0 | 0.0 ± 0.2 | 100.0 ± 0.0 |
| karistirma | Füzyon (güven ağırlıklandırma kapalı) | 11.5 ± 2.3 | 155.4 ± 10.0 | 1.3 ± 0.2 | 45.4 ± 4.2 | 1.0 ± 1.5 | 100.0 ± 0.0 |
| karistirma | Füzyon (IMM kapalı, sadece CV) | 15.7 ± 1.0 | 29.7 ± 1.2 | 1.2 ± 0.1 | 0.0 ± 0.0 | 1.0 ± 0.2 | 100.0 ± 0.0 |
| karistirma | **Füzyon** | 9.6 ± 0.8 | 23.1 ± 2.1 | 1.1 ± 0.1 | 0.0 ± 0.2 | 0.0 ± 0.0 | 100.0 ± 0.0 |
| sensor_kaybi | Sadece radar | 13.8 ± 0.4 | 116.7 ± 1.0 | 23.8 ± 0.2 | 0.0 ± 0.0 | 5.0 ± 0.0 | 60.0 ± 0.1 |
| sensor_kaybi | Sadece kamera | 9.5 ± 1.5 | 254.8 ± 2.1 | 54.8 ± 0.6 | 0.0 ± 0.0 | 4.3 ± 0.6 | 75.6 ± 0.7 |
| sensor_kaybi | Sadece konum bildirimi | 40.4 ± 0.2 | 329.9 ± 0.2 | 68.8 ± 0.1 | 0.0 ± 0.0 | 2.0 ± 0.0 | 100.0 ± 0.0 |
| sensor_kaybi | Füzyon (güven ağırlıklandırma kapalı) | 10.2 ± 0.5 | 41.1 ± 1.0 | 4.6 ± 0.1 | 0.0 ± 0.0 | 3.0 ± 0.0 | 100.0 ± 0.0 |
| sensor_kaybi | Füzyon (IMM kapalı, sadece CV) | 14.0 ± 0.8 | 47.7 ± 1.4 | 5.0 ± 0.2 | 0.0 ± 0.0 | 4.2 ± 0.4 | 100.0 ± 0.0 |
| sensor_kaybi | **Füzyon** | 10.2 ± 0.5 | 41.1 ± 1.0 | 4.6 ± 0.1 | 0.0 ± 0.0 | 3.0 ± 0.0 | 100.0 ± 0.0 |

| Senaryo | Füzyonun en iyi tek sensörden düşük olduğu koşu: RMSE | GOSPA |
|---|---:|---:|
| normal | 25/30 | 30/30 |
| sis | 30/30 | 30/30 |
| karistirma | 12/30 | 30/30 |
| sensor_kaybi | 8/30 | 30/30 |

| Senaryo | Bias kestirimi x (m) | Bias kestirimi y (m) | Kestirim hatası (m) |
|---|---:|---:|---:|
| normal | 36.1 ± 2.6 | -19.9 ± 2.4 | 3.2 ± 1.7 |
| sis | 36.1 ± 2.5 | -20.0 ± 2.4 | 3.2 ± 1.6 |
| karistirma | 35.9 ± 2.6 | -19.9 ± 2.2 | 3.1 ± 1.7 |
| sensor_kaybi | 36.1 ± 2.5 | -19.8 ± 2.3 | 3.0 ± 1.8 |

Filtre tutarlılığı: konum NEES'i. Tutarlı bir filtrede ANEES ≈ 2 olur ve noktaların ~%95'i %95 kabul bandında kalır.

| Senaryo | Füzyon (IMM) ANEES | IMM bantta (%) | Sadece CV ANEES | CV bantta (%) | İHA-1 ANEES (IMM / CV) |
|---|---:|---:|---:|---:|---:|
| normal | 1.88 | 74 | 3.58 | 69 | 2.1 / 9.7 |
| sis | 2.23 | 64 | 3.50 | 62 | 2.4 / 8.1 |
| karistirma | 1.96 | 72 | 3.88 | 67 | 2.3 / 11.0 |
| sensor_kaybi | 1.85 | 72 | 3.18 | 65 | 2.1 / 8.0 |
