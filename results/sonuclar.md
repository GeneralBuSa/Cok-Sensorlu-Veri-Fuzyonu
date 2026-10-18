| Senaryo | Konfigürasyon | RMSE (m) | GOSPA (m) | Kaçırma (%) | Yanlış iz | ID switch | Etiket doğruluğu (%) |
|---|---|---:|---:|---:|---:|---:|---:|
| normal | Sadece radar | 19.5 ± 0.6 | 47.4 ± 1.6 | 1.5 ± 0.1 | 0.0 ± 0.0 | 0.0 ± 0.0 | 60.0 ± 0.1 |
| normal | Sadece kamera | 11.2 ± 0.8 | 204.4 ± 2.8 | 34.9 ± 0.6 | 0.0 ± 0.0 | 0.6 ± 0.7 | 70.8 ± 0.4 |
| normal | Sadece konum bildirimi | 40.7 ± 0.2 | 313.3 ± 0.2 | 60.8 ± 0.1 | 0.0 ± 0.0 | 0.0 ± 0.0 | 100.0 ± 0.0 |
| normal | Füzyon (güven ağırlıklandırma kapalı) | 12.0 ± 0.6 | 28.0 ± 1.0 | 1.1 ± 0.1 | 0.0 ± 0.0 | 0.0 ± 0.0 | 100.0 ± 0.0 |
| normal | **Füzyon** | 12.0 ± 0.6 | 28.0 ± 1.0 | 1.1 ± 0.1 | 0.0 ± 0.0 | 0.0 ± 0.0 | 100.0 ± 0.0 |
| sis | Sadece radar | 19.5 ± 0.6 | 47.4 ± 1.6 | 1.5 ± 0.1 | 0.0 ± 0.0 | 0.0 ± 0.0 | 60.0 ± 0.1 |
| sis | Sadece kamera | 25.5 ± 3.3 | 322.9 ± 2.5 | 67.0 ± 1.0 | 0.1 ± 0.3 | 1.0 ± 0.7 | 84.4 ± 1.5 |
| sis | Sadece konum bildirimi | 40.7 ± 0.2 | 313.3 ± 0.2 | 60.8 ± 0.1 | 0.0 ± 0.0 | 0.0 ± 0.2 | 100.0 ± 0.0 |
| sis | Füzyon (güven ağırlıklandırma kapalı) | 20.0 ± 2.8 | 53.0 ± 10.1 | 1.3 ± 0.3 | 1.7 ± 1.5 | 2.7 ± 3.1 | 100.0 ± 0.0 |
| sis | **Füzyon** | 15.2 ± 0.6 | 36.4 ± 1.4 | 1.1 ± 0.1 | 0.0 ± 0.0 | 0.0 ± 0.0 | 100.0 ± 0.0 |
| karistirma | Sadece radar | 61.0 ± 3.9 | 156.2 ± 7.5 | 13.3 ± 1.7 | 0.3 ± 0.5 | 3.4 ± 1.2 | 65.1 ± 1.2 |
| karistirma | Sadece kamera | 11.2 ± 0.8 | 203.9 ± 1.7 | 34.8 ± 0.4 | 0.0 ± 0.0 | 0.5 ± 0.7 | 70.8 ± 0.3 |
| karistirma | Sadece konum bildirimi | 40.6 ± 0.2 | 313.3 ± 0.3 | 60.8 ± 0.1 | 0.0 ± 0.0 | 0.0 ± 0.2 | 100.0 ± 0.0 |
| karistirma | Füzyon (güven ağırlıklandırma kapalı) | 20.4 ± 4.5 | 165.8 ± 11.1 | 1.5 ± 0.4 | 43.9 ± 4.1 | 2.0 ± 1.5 | 100.0 ± 0.0 |
| karistirma | **Füzyon** | 14.5 ± 1.4 | 32.6 ± 5.5 | 1.1 ± 0.1 | 0.1 ± 0.3 | 0.0 ± 0.0 | 100.0 ± 0.0 |
| sensor_kaybi | Sadece radar | 20.0 ± 0.7 | 127.1 ± 1.4 | 23.8 ± 0.2 | 0.0 ± 0.0 | 5.0 ± 0.0 | 60.0 ± 0.1 |
| sensor_kaybi | Sadece kamera | 11.9 ± 1.8 | 282.3 ± 2.8 | 58.0 ± 0.6 | 0.0 ± 0.0 | 4.3 ± 0.7 | 73.7 ± 0.8 |
| sensor_kaybi | Sadece konum bildirimi | 40.7 ± 0.2 | 330.1 ± 0.4 | 68.9 ± 0.2 | 0.0 ± 0.0 | 2.0 ± 0.0 | 100.0 ± 0.0 |
| sensor_kaybi | Füzyon (güven ağırlıklandırma kapalı) | 14.0 ± 0.6 | 49.0 ± 1.3 | 4.6 ± 0.1 | 0.0 ± 0.0 | 3.0 ± 0.0 | 100.0 ± 0.0 |
| sensor_kaybi | **Füzyon** | 14.0 ± 0.6 | 49.0 ± 1.3 | 4.6 ± 0.1 | 0.0 ± 0.0 | 3.0 ± 0.0 | 100.0 ± 0.0 |

| Senaryo | Füzyonun en iyi tek sensörden düşük olduğu koşu: RMSE | GOSPA |
|---|---:|---:|
| normal | 4/30 | 30/30 |
| sis | 30/30 | 30/30 |
| karistirma | 0/30 | 30/30 |
| sensor_kaybi | 3/30 | 30/30 |

| Senaryo | Bias kestirimi x (m) | Bias kestirimi y (m) | Kestirim hatası (m) |
|---|---:|---:|---:|
| normal | 36.2 ± 2.5 | -20.6 ± 2.4 | 3.1 ± 2.0 |
| sis | 36.2 ± 2.7 | -20.5 ± 2.4 | 3.3 ± 1.8 |
| karistirma | 36.0 ± 2.7 | -20.4 ± 2.3 | 3.2 ± 1.8 |
| sensor_kaybi | 36.3 ± 2.6 | -20.5 ± 2.3 | 3.2 ± 1.8 |
