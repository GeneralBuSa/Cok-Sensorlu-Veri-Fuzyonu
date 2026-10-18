| Senaryo | Konfigürasyon | RMSE (m) | GOSPA (m) | Kaçırma (%) | Yanlış iz | ID switch | Etiket doğruluğu (%) |
|---|---|---:|---:|---:|---:|---:|---:|
| normal | Sadece radar | 19.5 ± 0.7 | 47.0 ± 1.6 | 1.4 ± 0.1 | 0.0 ± 0.0 | 0.0 ± 0.0 | 60.0 ± 0.0 |
| normal | Sadece kamera | 11.2 ± 1.2 | 204.2 ± 2.5 | 34.8 ± 0.5 | 0.0 ± 0.0 | 0.8 ± 0.9 | 70.8 ± 0.4 |
| normal | Sadece konum bildirimi | 40.7 ± 0.2 | 313.2 ± 0.0 | 60.8 ± 0.0 | 0.0 ± 0.0 | 0.0 ± 0.0 | 100.0 ± 0.0 |
| normal | Füzyon (güven ağırlıklandırma kapalı) | 11.8 ± 0.6 | 27.7 ± 1.3 | 1.1 ± 0.1 | 0.0 ± 0.2 | 0.0 ± 0.0 | 100.0 ± 0.0 |
| normal | **Füzyon** | 11.8 ± 0.6 | 27.7 ± 1.3 | 1.1 ± 0.1 | 0.0 ± 0.2 | 0.0 ± 0.0 | 100.0 ± 0.0 |
| sis | Sadece radar | 19.5 ± 0.7 | 47.0 ± 1.6 | 1.4 ± 0.1 | 0.0 ± 0.0 | 0.0 ± 0.0 | 60.0 ± 0.0 |
| sis | Sadece kamera | 25.6 ± 3.2 | 322.8 ± 2.2 | 67.1 ± 0.8 | 0.1 ± 0.3 | 1.0 ± 0.6 | 84.1 ± 1.1 |
| sis | Sadece konum bildirimi | 40.6 ± 0.2 | 313.3 ± 0.2 | 60.8 ± 0.1 | 0.0 ± 0.0 | 0.0 ± 0.0 | 100.0 ± 0.0 |
| sis | Füzyon (güven ağırlıklandırma kapalı) | 19.2 ± 1.6 | 50.7 ± 6.0 | 1.2 ± 0.2 | 1.7 ± 1.3 | 2.3 ± 2.5 | 100.0 ± 0.0 |
| sis | **Füzyon** | 15.1 ± 0.5 | 36.3 ± 1.3 | 1.1 ± 0.1 | 0.1 ± 0.3 | 0.0 ± 0.0 | 100.0 ± 0.0 |
| karistirma | Sadece radar | 59.8 ± 3.6 | 156.1 ± 6.8 | 13.6 ± 2.1 | 0.5 ± 0.6 | 3.0 ± 1.1 | 65.2 ± 1.3 |
| karistirma | Sadece kamera | 11.2 ± 0.9 | 204.8 ± 2.6 | 34.9 ± 0.5 | 0.0 ± 0.0 | 0.6 ± 0.7 | 70.8 ± 0.3 |
| karistirma | Sadece konum bildirimi | 40.7 ± 0.2 | 313.3 ± 0.3 | 60.9 ± 0.1 | 0.0 ± 0.0 | 0.0 ± 0.0 | 100.0 ± 0.0 |
| karistirma | Füzyon (güven ağırlıklandırma kapalı) | 19.0 ± 4.0 | 162.5 ± 9.3 | 1.4 ± 0.4 | 41.7 ± 4.7 | 1.4 ± 1.5 | 100.0 ± 0.0 |
| karistirma | **Füzyon** | 14.3 ± 1.6 | 31.7 ± 2.7 | 1.2 ± 0.2 | 0.1 ± 0.3 | 0.0 ± 0.2 | 100.0 ± 0.0 |
| sensor_kaybi | Sadece radar | 20.0 ± 0.9 | 126.8 ± 1.7 | 23.7 ± 0.2 | 0.0 ± 0.0 | 5.0 ± 0.0 | 60.0 ± 0.1 |
| sensor_kaybi | Sadece kamera | 12.0 ± 1.6 | 282.9 ± 2.9 | 58.0 ± 0.6 | 0.0 ± 0.0 | 4.3 ± 0.7 | 73.6 ± 0.7 |
| sensor_kaybi | Sadece konum bildirimi | 40.7 ± 0.2 | 330.1 ± 0.3 | 68.9 ± 0.2 | 0.0 ± 0.0 | 2.0 ± 0.2 | 100.0 ± 0.0 |
| sensor_kaybi | Füzyon (güven ağırlıklandırma kapalı) | 13.8 ± 0.6 | 48.8 ± 1.2 | 4.6 ± 0.1 | 0.0 ± 0.0 | 3.0 ± 0.0 | 100.0 ± 0.0 |
| sensor_kaybi | **Füzyon** | 13.8 ± 0.6 | 48.8 ± 1.2 | 4.6 ± 0.1 | 0.0 ± 0.0 | 3.0 ± 0.0 | 100.0 ± 0.0 |

| Senaryo | Füzyonun en iyi tek sensörden düşük olduğu koşu: RMSE | GOSPA |
|---|---:|---:|
| normal | 6/30 | 30/30 |
| sis | 30/30 | 30/30 |
| karistirma | 0/30 | 30/30 |
| sensor_kaybi | 4/30 | 30/30 |

| Senaryo | Bias kestirimi x (m) | Bias kestirimi y (m) | Kestirim hatası (m) |
|---|---:|---:|---:|
| normal | 35.4 ± 2.0 | -20.3 ± 2.6 | 2.8 ± 1.7 |
| sis | 35.3 ± 1.9 | -20.1 ± 2.6 | 2.7 ± 1.6 |
| karistirma | 35.3 ± 1.8 | -20.2 ± 2.5 | 2.6 ± 1.6 |
| sensor_kaybi | 35.4 ± 2.0 | -20.1 ± 2.6 | 2.7 ± 1.8 |

Mann-Whitney U testi, füzyon: seed 42-71 ile bu küme (iki yönlü; p > 0.05 ise anlamlı fark yok)

| Senaryo | GOSPA p | RMSE p |
|---|---:|---:|
| normal | 0.23 | 0.20 |
| sis | 0.77 | 0.51 |
| karistirma | 0.30 | 0.45 |
| sensor_kaybi | 0.67 | 0.26 |
