# Gerçek Zamanlı Nesne Tanıma ve Takip Uygulamaları

Bu klasör, gerçek zamanlı video analiziyle nesne ve şekil tanıma, hareket izleme ve yüz/organ tespiti gibi ileri düzey OpenCV konularını içermektedir. `cv2` kütüphanesi ile pratik uygulamalar üzerinden çalışılmıştır.

## 📘 İçerik Listesi

| Dosya Adı                         | Açıklama                                              |
|----------------------------------|-------------------------------------------------------|
| 00_shapeDetect.py                | Görüntüde şekil tespiti (daire, üçgen, dikdörtgen)    |
| 01_real-time-ShapeDetect.py      | Kamera ile gerçek zamanlı şekil tanıma                |
| 02_backgroundSubtraction.py      | Arka plan çıkarma (`MOG2`, `KNN`)                     |
| 03_objectDetection-w-HSV.py      | HSV ile nesne renge göre tespiti                      |
| 04_mouseEvents.py                | Fare etkileşimi ile çizim işlemleri (`setMouseCallback`) |
| 05_using-face-features.py        | Yüz özelliklerini kullanarak nesne bulma             |
| 06_using-hand-features.py        | El hareketleriyle etkileşim                           |
| 07_eye-tracking.py               | Göz takip algoritması (basit blob tespiti ile)        |

## 📁 Destek Dosyaları
İlgili görseller ve medya dosyaları `materyal/klasor11/` klasöründe yer almaktadır.

## 🧰 Gereksinimler
```bash
pip install opencv-python
