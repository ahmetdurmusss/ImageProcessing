# 📘 GeeksForGeeks OpenCV Uygulama Notları

Bu depo, GeeksForGeeks platformundaki OpenCV derslerinden yola çıkılarak hazırlanmış uygulamalı görüntü işleme örneklerini içermektedir. Her klasör, belirli bir konuya odaklanmakta ve ilgili Jupyter Notebook dosyalarıyla birlikte örnek görsellerle desteklenmektedir.

> 💡 Kodlar eğitim amacıyla yeniden yapılandırılmış, açıklamalar ve uygulama odaklı geliştirmeler tarafımdan eklenmiştir.

---

## 📂 Klasör Yapısı

### `klasor1/` – Giriş
- OpenCV'ye genel bakış
- Kurulum ve temel kullanım (`openCVGiris.ipynb`)

### `klasor2/` – Temel Görüntü İşlemleri
- Görüntü okuma, yazma ve görüntüleme
- Bitwise işlemler
- Renk uzayı dönüşümleri (BGR ↔ HSV)
- Aritmetik işlemler

📁 Görseller: `materyal/klasor2/`

### `klasor3/` – İleri Görüntü İşleme Teknikleri  
- Görüntü kırpma, döndürme, yeniden boyutlandırma  
- Histogram çizimi  
- Erozyon, dilation, açılma ve kapanma işlemleri  
- Canny kenar tespiti  
- ROI, gamma/log dönüşümü, adaptif eşikleme  

📁 Detaylı açıklama için: [klasor3/README.md](./klasor3/README.md)  
📁 Görseller: `materyal/klasor3/`

### `klasor4/` – Köşe ve Nesne Tespiti
- Harris ve Shi-Tomasi köşe tespiti
- Yuvarlak nesne ve belge köşe tanıma
- Chessboard örnekleri

📁 Görseller: `materyal/klasor4/`

---

## 📌 Gereksinimler

Python ortamı için aşağıdaki kütüphaneler gereklidir:

```bash
pip install opencv-python numpy matplotlib
```

📜 Kaynak
Bu çalışmalar, GeeksForGeeks OpenCV Tutorial Serisi temel alınarak geliştirilmiştir.
📎 İçerikler kişisel eğitim amaçlı derlenmiş olup, ticari kullanım durumlarında orijinal kaynağın lisans koşulları dikkate alınmalıdır.
