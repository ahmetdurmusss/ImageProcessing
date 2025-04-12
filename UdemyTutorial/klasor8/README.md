# 🎨 Görüntü İşlemede Renk Uzayı, Filtreleme ve Kenar Tespiti

Bu klasör, OpenCV ile görüntü işleme sürecinde kullanılan temel teknikleri ve dönüşümleri içermektedir. Piksel işlemleri, renk uzayları, morfolojik operasyonlar ve kenar tespiti gibi uygulamalar adım adım gösterilmektedir.

## 📘 İçerik Listesi

| Dosya Adı                     | Açıklama                                      |
|------------------------------|-----------------------------------------------|
| 000_pixels.py                | Piksel okuma ve RGB değerlerine erişim        |
| 001_roi.py                   | ROI (Region of Interest) kullanımı            |
| 002_addFunc.py               | Görüntü toplama işlemleri (`add`, `addWeighted`) |
| 003_addWeightedFunc.py       | Karıştırma (blend) işlemleri                  |
| 004_color-space.py           | Renk uzayları: BGR ↔ HSV, GRAY, LAB vb.       |
| 005_color-space-Vid.py       | Canlı videoda renk uzayı dönüşümü             |
| 006_example_find-HSV-Code.py | HSV ile renk maskesi oluşturma örneği        |
| 007_smoothing.py             | Bulanıklaştırma: `blur`, `GaussianBlur`      |
| 008_bitWise.py               | Bit düzeyinde `AND`, `OR`, `XOR`, `NOT` işlemleri |
| 009_warpAffine.py            | Görüntü döndürme ve öteleme işlemleri         |
| 010_getRotationMatrix2D.py   | Açılı döndürme (rotation matrix ile)          |
| 011_tresh.py                 | Eşikleme (binary, inverse, adaptive)          |
| 012_erosion.py               | Erozyon (morfolojik işlem)                    |
| 013_histogram.py             | Görüntü histogramı oluşturma ve gösterme      |
| 014_corner-detection.py      | Köşe tespiti (Harris, Shi-Tomasi)             |
| 015_canny-edgeDetect.py      | Canny kenar tespiti                           |

## 📁 Gereçler
Görsel dosyalar için `../materyal/klasor8/` klasörüne göz atınız.

## 🧰 Gereksinimler
```bash
pip install opencv-python

