# 🤖 Yapay Zeka Yardımcısı - GUI Rehberi

Grafik Arayüz (GUI) ile uygulamayı kolayca kullanabilirsiniz.

## 🚀 Başlarken

### GUI Uygulamasını Çalıştırma

**Seçenek 1: Launcher ile başlatın**
```bash
python launcher.py
```
Açılan menüden `1. GUI (Grafik Arayüz)` seçeneğini seçin.

**Seçenek 2: Doğrudan GUI uygulamasını çalıştırın**
```bash
python gui_app.py
```

## 📖 Sekme Rehberi

### 1. 💬 Chatbot Sekmesi

Yapay Zeka ile sohbet edin!

**Özellikleri:**
- 💭 Doğal dil konuşması
- ⏰ Saat/tarih bilgisi sorgulama
- 😊 Arkadaş canlı konuşma
- 🎯 Dinamik yanıtlar

**Kullanım:**
1. Mesaj yazınız
2. Enter tuşuna basın veya "📤 Gönder" butonuna tıklayın
3. AI'ın yanıtını göreceksiniz
4. Çıkmak için "çıkış" yazıp gönder tuşuna basın

**İpuçları:**
- "Çıkış", "quit" veya "exit" yazarak sohbeti sonlandırabilirsiniz
- Geçmişi temizlemek için "🗑️ Temizle" butonunu kullanın

---

### 2. 📝 Metin Analizi Sekmesi

Yazılı metinleri detaylı şekilde analiz edin!

**Analiz Edilen Veriler:**
- 📊 Kelime ve cümle sayım
- 🔝 En sık kullanılan kelimeler (Top 5)
- 📈 Karakter istatistikleri
- 📐 Ortalama uzunluklar

**Kullanım:**
1. Analiz etmek istediğiniz metni metin alanına yapıştırın
2. "🔍 Analiz Et" butonuna tıklayın
3. Detaylı sonuçları göreceksiniz

**Örnek:**
```
Girdi: "Türkiye güzel bir ülkedir. Türkiye'nin birçok tarihi yeri vardır."
Çıktı: Kelime sayısı: 11, Cümle sayısı: 2, En sık kelime: Türkiye (2)
```

---

### 3. 📊 İstatistikler Sekmesi

Metinlerin ayrıntılı istatistiklerini hesaplayın!

**Gösterilen Metrikler:**
- 📈 Karakter, kelime, cümle sayıları
- 📏 Ortalama kelime ve cümle uzunlukları
- 🔬 Arşiv veri analizi

**Kullanım:**
1. Metin alanına metin yazın veya yapıştırın
2. "📈 İstatistikleri Hesapla" butonuna tıklayın
3. Kapsamlı istatistikleri göreceksiniz

---

### 4. 🗂️ Dosya Yönetimi Sekmesi

Bilgisayarınızda dosya ve klasörleri yönetin!

**Özellikler:**
- 📂 Klasör içeriğini listele
- 📄 Dosya boyutlarını göster
- 🔍 Dosya ve klasörleri ayırt et
- 📋 Dosya bilgilerini görüntüle

**Kullanım:**
1. **Klasör Seçme:**
   - Otomatik olarak mevcut klasör gösterilir
   - "📂 Klasör Seç" butonuyla başka bir klasör seçin
   - Veya Klasör Yolu alanına doğrudan yolu yazın

2. **Dosyaları Listeleme:**
   - "📋 Dosyaları Listele" butonuna tıklayın
   - Klasördeki tüm dosyalar ve alt klasörler gösterilir
   - Dosya boyutları da listelenir

**İpuçları:**
- 📁 işareti klasörü, 📄 işareti dosyayı gösterir
- Dosya boyutu byte cinsinden gösterilir

---

### 5. 📈 Kelime Frekansı Sekmesi

En sık kullanılan kelimeleri görselleştirilmiş grafiklerle gösteyin!

**Özellikler:**
- 🔍 Kelime oluşum sıklığı hesabı
- 📊 Grafik gösterimi (hBar grafiği)
- 🎯 Özelleştirilebilir sonuç sayısı
- 📋 Sıralı liste

**Kullanım:**
1. Analiz etmek istediğiniz metni girin
2. "Kaç kelime gösterilsin?" seçeneğinde sayı belirleyin (1-50)
3. "🔍 Analiz Et" butonuna tıklayın
4. Kelime frekansını grafik ve tablo şeklinde göreceksiniz

**Örnek Çıktı:**
```
📈 KELİME FREKANS ANALİZİ (Top 10)
================================================
1. python        | ████████████████ 25
2. program       | ██████████ 14
3. data          | ████████ 12
4. function      | ██████ 8
5. test          | ████ 5
```

---

### 6. 😊 Duygu Analizi Sekmesi

Metinlerin duygusal tonunu analiz edin!

**Tespit Edilen Duygular:**
- 😊 Pozitif (mutluluğun göstergesi)
- 😢 Negatif (kızgınlık, üzüntü)
- 😐 Nötr (tarafsız)

**Kullanım:**
1. Analiz etmek istediğiniz metni girin
2. "🔍 Duygu Analizi Yap" butonuna tıklayın
3. Metnin duygusal sınıflandırmasını göreceksiniz

**Örnek:**
```
Girdi: "Harika bir gün geçirdim! Çok mutluyum!"
Çıktı: POZITIF - Sevindirici kelimelerin sıklığı yüksektir.

Girdi: "Çok kötü oldu. Hayal kırıklığına uğradım."
Çıktı: NEGATİF - Olumsuz kelimelerin varlığı belirgindir.
```

---

## ⌨️ Klavye Kısayolları

| Kısayol | Açıklama |
|---------|----------|
| Enter (Chatbot'ta) | Mesajı gönder |
| Ctrl+A | Tüm metni seç |
| Ctrl+C | Kopyala |
| Ctrl+V | Yapıştır |

---

## 🎨 GUI Özellikleri

### Tasarım Avantajları:
- ✨ Modern ve temiz arayüz
- 🎯 Kullanıcı dostu menüler
- 📱 Duyarlı tasarım
- 🌈 Renkli sekme sistemi
- 📊 Görselleştirilmiş sonuçlar
- 💾 Otomatik veri işleme

### Tema Renkleri:
- 🔵 Ana Renk: Mavi (#3498db)
- ⚫ Başlık Rengi: Koyu Gri (#2c3e50)
- 🔴 Vurgu Rengi: Kırmızı (#e74c3c)
- ⚪ Arka Plan: Açık Gri (#f0f0f0)

---

## ⚙️ Sistem Gereksinimleri

- **Python:** 3.7 veya üzeri
- **İşletim Sistemi:** Windows, macOS, Linux
- **RAM:** Minimum 512 MB (2 GB önerilir)
- **Disk Alanı:** ~50 MB

---

## 🐛 Sorun Giderme

### Problem: GUI penceresi açılmıyor
**Çözüm:**
```bash
# Tkinter'ı yükleyin
python -m pip install --upgrade tkinter
```

### Problem: Türkçe karakterler gösterilmiyor
**Çözüm:**
- Dosyanın UTF-8 kodlamasında olduğundan emin olun
- Uygulamayı yeniden başlatın

### Problem: Modülü bulunamıyor hatası
**Çözüm:**
```bash
$ Proje klasörünün içinde olduğunuzdan emin olun
$ Tüm gerekli modülleri yükleyin
pip install -r requirements.txt
```

---

## 📚 Ek Kaynaklar

- Tkinter Dokümantasyonu: https://docs.python.org/3/library/tkinter.html
- Python GUI Rehberi: https://docs.python.org/3/howto/tkinter.html

---

## 💡 İpuçları ve Püf Noktaları

1. **Büyük Metinler:** Çok büyük metinler için kelime frekansı analizi biraz zaman alabilir
2. **Dosya İşlemleri:** Dosya yönetimi sekmesinde yalnızca okuma işlemleri yapılır
3. **Duygu Analizi:** En iyi sonuçlar Türkçe metinler için verilir
4. **Chatbot:** Arkadaş canlı yanıtlar için tabii bir dille yazın

---

## 🤝 Geri Bildirim

Sorunlar veya öneriler için:
- GitHub Issues
- Email: support@example.com

---

**Versiyon:** 1.0  
**Son Güncelleme:** 2026  
**Dil:** Türkçe 🇹🇷
