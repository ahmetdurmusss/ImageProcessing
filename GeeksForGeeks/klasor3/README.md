# 🧪 Görüntü İşleme: İleri Teknikler

Bu klasör, OpenCV kullanarak yapılan ileri düzey görüntü işleme tekniklerini içermektedir. Uygulamalar Jupyter Notebook ortamında yürütülmüş, her konu adım adım görsellerle desteklenmiştir.

---

## 📘 İçerik Listesi

| Dosya Adı                                     | Açıklama                                              |
|----------------------------------------------|-------------------------------------------------------|
| `goruntudeGoruntuErisimi.ipynb`              | Piksel değerlerine erişim ve düzenleme işlemleri      |
| `goruntudeGoruntuKirpma.ipynb`               | Görüntü kırpma (cropping)                             |
| `goruntudeGoruntuKopyalama.ipynb`            | Görselin belirli bir kısmını başka bir bölgeye taşıma |
| `goruntudeGoruntuDonme.ipynb`                | Dönme matrisi ile görüntü döndürme                    |
| `goruntudeBoyutlandirma.ipynb`               | Yeniden boyutlandırma (`resize`) işlemleri           |
| `goruntudeHistogram.ipynb`                   | Görüntü histogramı çizimi                             |
| `goruntudeErozyon.ipynb`                     | Erozyon (görseli küçültme, kontur inceltme)           |
| `goruntudeDilation.ipynb`                    | Dilation (görseli genişletme)                         |
| `goruntudeOpening.ipynb`                     | Gürültü temizleme için açılma işlemi                  |
| `goruntudeClosing.ipynb`                     | Küçük boşlukları kapatmak için kapanma işlemi        |
| `goruntudeKenarBulma.ipynb`                  | Canny algoritması ile kenar tespiti                   |
| `goruntudeROI.ipynb`                         | ROI: Görüntünün belirli bölgesine erişim              |
| `goruntudeTersGoruntu.ipynb`                 | Görüntü renklerinin tersine çevrilmesi (negatif)      |
| `goruntudeLogTransform.ipynb`                | Logaritmik dönüşüm ile parlaklık ayarlama             |
| `goruntudeGammaTransform.ipynb`              | Gamma düzeltme (kontrast kontrolü)                    |
| `goruntudeThreshold.ipynb`                   | Basit thresholding (eşikleme)                         |
| `goruntudeAdaptiveThreshold.ipynb`           | Uyarlanabilir threshold (lokal eşikleme)              |

---

## 🧾 Görsel Materyaller

Tüm notebook dosyaları `../materyal/klasor3/` dizinindeki görselleri kullanır.  
Görseller doğrudan notebook içinde yüklenmiştir.

---

## ⚙️ Gereksinimler

```bash
pip install opencv-python numpy matplotlib

