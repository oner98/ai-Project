# 🤖 Yapay Zeka Yardımcısı

Çok fonksiyonlu bir Python tabanlı yapay zeka yardımcı programı. Metin analizi, veri işleme, chatbot ve otomasyon görevleri için tasarlanmıştır.

## 📋 Özellikler

### 1. **Chatbot** 💬
- İnsan benzeri konuşma
- Saat/tarih bilgisi sorgulama
- Dinamik karşılama ve veda mesajları

### 2. **Metin Analizi** 📝
- Çok yönlü metin analizi
- Duygu analizi (pozitif/negatif/nötr)
- İstatistiksel bilgiler

### 3. **Metin İstatistikleri** 📊
- Karakter ve kelime sayısı
- Cümle analizi
- Ortalama uzunluk hesaplaması

### 4. **Veri İşleme** 💾
- Metin dosyaları okuma/yazma
- JSON dosya desteği
- CSV dosya işlemleri

### 5. **Dosya Yönetimi** 🗂️
- Klasör içi dosya listeleme
- Dosya boyutu kontrolü
- Dosya oluşturma ve silme

### 6. **Kelime Frekansı Analizi** 📈
- En sık kullanılan kelimeleri bulma
- Frekans istatistikleri
- Özelleştirilebilir sonuç sayısı

### 7. **Duygu Analizi** 😊
- Metindeki duyguları tanıma
- Detaylı duygu raporu
- Pozitif/negatif/nötr sınıflandırması

## 🚀 Başlangıç

### Gereksinimler
- Python 3.7+
- pip (Python paket yöneticisi)

### Kurulum

1. **Proje klasörüne gir:**
```bash
cd "c:\Users\Filibeli\OneDrive\Desktop\AI project"
```

2. **Gerekli paketleri yükle:**
```bash
pip install -r requirements.txt
```

3. **Programı çalıştır:**

#### Seçenek 1: GUI (Grafik Arayüz) ✨ - ÖNERİLEN
```bash
python launcher.py
```
Açılan menüden `1. GUI (Grafik Arayüz)` seçeneğini seçin.

**Veya doğrudan:**
```bash
python gui_app.py
```

#### Seçenek 2: CLI (Komut Satırı)
```bash
python main.py
```

## 📖 Kullanım Örneği

### GUI Arayüzü (Önerilen)

Uygulama 6 farklı sekmede organize edilmiş intuitive gürafik arayüzü sunmaktadır:

- **💬 Chatbot:** Yapay Zeka ile doğal dil konuşması
- **📝 Metin Analizi:** Metinler için detaylı analiz
- **📊 İstatistikler:** Metin istatistiklerini hesapla
- **🗂️ Dosya Yönetimi:** Bilgisayarda dosya ve klasörleri yönet
- **📈 Kelime Frekansı:** En sık kullanılan kelimeleri görselleştir
- **😊 Duygu Analizi:** Metinlerin duygusal tonunu analiz et

Detaylı GUI rehberi için `GUI_REHBERI.md` dosyasını okuyunuz.

### CLI Arayüzü

```
🤖 YAPAY ZEKA YARDIMCISINA HOŞGELDINIZ!
Lütfen bir işlem seçiniz.

==================================================
🤖 YAPay ZEKa YARDIMCISI
==================================================

1. Chatbot
2. Metin Analizi
3. Metin İstatistikleri
4. Veri İşleme (Dosya Okuma/Yazma)
5. Dosya Yönetimi
6. Kelime Frekansı Analizi
7. Duygu Analizi
0. Çıkış
==================================================

Seçim (0-7): 1
```

## 🎨 GUI Özellikleri

✨ **Modern Tasarım**
- Temiz ve kullanıcı dostu arayüz
- Renkli sekme sistemi
- İkon ve emoji ile görsel zenginlik
- Duyarlı tasarım

🔧 **Kullanım Kolaylığı**
- Metin alanlarına sürükle-bırak desteği (kopyala-yapıştır)
- Görselleştirilmiş sonuçlar
- Hızlı erişim menüleri
- Detaylı hata mesajları

📊 **Güçlü Özellikler**
- Tüm CLI özellikleri GUI'de sunulu
- Dosya seçme diyalogları
- Grafik gösterimler
- Gelişmiş metin işleme

## 🛠️ Modüller

### `gui_app.py` 🆕
Grafik arayüz uygulaması. Tkinter kullanarak modern ve kullanıcı dostu bir arayüz sağlar.
- Tabletli sekme sistemi
- Metin giriş/çıkış alanları
- Dosya seçme diyalogları
- Görselleştirilmiş sonuçlar
- 6 farklı ana özellik sekmesi

### `launcher.py` 🆕
Başlatıcı program. CLI ve GUI arasında seçim yapmayı sağlar.
- Kolay menü seçimi
- Hata yönetimi
- Modül kontrol sistemi

### `ai_assistant.py`
Ana yapay zeka sınıfı. Chatbot, zaman bilgisi ve duygu analizi fonksiyonları içerir.

### `text_processor.py`
Metin işleme ve analiz araçları:
- Metin temizleme
- Tokenization
- Kelime frekansı
- İstatistik hesaplama

### `data_handler.py`
Dosya ve veri yönetimi:
- Metin dosyası okuma/yazma
- JSON işlemleri
- CSV desteği
- Dosya bilgisi alma

### `main.py`
Komut satırı arayüzü ve program kontrol satırı.

## 🎯 Gelecek Güncellemeler

- [ ] Web arayüzü (Flask/Django)
- [ ] Machine Learning entegrasyonu
- [ ] Daha gelişmiş NLP özellikleri
- [ ] Veritabanı desteği
- [ ] API geliştirme
- [ ] Daha fazla dil desteği

## 📝 Lisans

Bu proje açık kaynak olarak sunulmaktadır.

## 👨‍💻 Geliştirici

Tarafından oluşturuldu: AI Asistanı

## 📞 İletişim

Sorunlar, öneriler ve geri bildirim için iletişime geçiniz.

---

**Keyifli kullanımlar! 🎉**
