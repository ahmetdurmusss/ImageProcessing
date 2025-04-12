# 🎓 Udemy OpenCV Eğitim Notları

Bu repoda, Udemy platformunda sunulan OpenCV eğitimini temel alarak hazırlanmış Python örnek dosyaları yer almaktadır. Her klasör, belirli bir konu başlığını ele almakta ve konunun pratik yönü Jupyter veya Python script dosyaları aracılığıyla gösterilmektedir.

> 🧠 Tüm içerik, öğrenme amacıyla yeniden yapılandırılmıştır. Kodlar, video içeriğiyle senkronize olacak şekilde düzenlenmiş; açıklamalar ve geliştirmeler eklenmiştir.

---

## 📂 Klasörler ve İçerikler

### `klasor6/` – Temel Video ve Görüntü İşlemleri
- Görüntü okuma, gösterme, kaydetme
- Video yakalama (`VideoCapture`)
- Görüntü yeniden boyutlandırma ve video kaydetme

### `klasor7/` – Çekirdek ve Grafik Fonksiyonları
- Çekirdek (kernel) oluşturma
- Temel görüntü matematiği işlemleri
- `draw` ve `trackbar` kullanımı, yazı yazma

### `klasor8/` – Renk Uzayı, Maskeleme ve Filtreleme
- HSV renk uzayıyla renk ayrımı
- ROI, piksel işleme, histogram
- Bitwise işlemler, `warpAffine`, kenar tespiti (`Canny`, `Sobel`)
- Erozyon, eşikleme, köşe tespiti

### `klasor9/` – Kontur Algılama ve Şekil Özellikleri
- Kontur çıkarımı (`cv2.findContours`)
- Moment hesaplama, kontur alanı
- Convex Hull ve konveks kusur analizi

### `klasor10/` – Hough Dönüşümleri
- Doğru tespiti: `cv2.HoughLines`, `HoughLinesP`
- Daire tespiti: `cv2.HoughCircles`
- Gerçek zamanlı video üzerinde uygulama

### `klasor11/` – Şekil Tanıma ve Yüz Takibi
- Şekil ve nesne tanıma (`HSV`, `Contours`)
- Arka plan çıkarma
- Yüz/göz/eller üzerinden nesne takibi
- `mouse event` ve `eye-tracking` uygulamaları

### `klasor12/` – İleri Görüntü Teknikleri
- Görüntü karşılaştırma (template matching)
- Görüntü çözünürlüğü ayarlama
- Bulanıklaştırma, morfolojik işlemler
- Görüntü dönüşümleri

### `materyal/` – Görsel ve Video Kaynakları
- Eğitim boyunca kullanılan .jpg ve .mp4 formatındaki görsel/video dosyaları
- Her klasöre özel örnek içeriklere ait referans dosyalar

---

## 📌 Kullanım Notları

- Her klasörde örnek dosyalar `.py` formatındadır, doğrudan çalıştırılabilir.
- Görsel/video dosyaları `materyal/` klasöründe organize edilmiştir.
- Kodlar, açıklamalı ve modüler biçimde yapılandırılmıştır.
- OpenCV, NumPy gibi temel kütüphanelerin kurulu olması gerekmektedir.

Kurulum önerisi:
```bash
pip install opencv-python numpy
