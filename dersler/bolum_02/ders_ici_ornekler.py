"""
============================================================
  BÖLÜM 2 — DERS İÇİ CANLI KODLAMA ÖRNEKLERİ
============================================================

Bu dosya derste canlı olarak kodlanacak örnekleri içerir.
Her örnek için:
  - Problem tanımı ve beklenen çıktı verilmiştir
  - Çözüm kısmı boş bırakılmıştır → derste canlı kodlanacak
  - Zorluk seviyesi yıldızla belirtilmiştir (★ kolay → ★★★ zor)
============================================================
"""


# ============================================================
#  HAFTA 4 — Listeler ve Tuple
# ============================================================

# ────────────────────────────────────────────────────────────
# Örnek 4.1 ★ — Ölçüm Serisi İşlemleri
# ────────────────────────────────────────────────────────────
# Bir deneyde alınan pH ölçüm sonuçları:
#   olcumler = [7.2, 6.8, 7.5, 6.5, 8.1, 7.0, 6.9, 7.8, 7.3, 6.7]
#
# Liste metodlarını kullanarak:
#   a) Listeye 7.4 ve 6.6 değerlerini ekleyin
#   b) İlk ölçümü (7.2) listeden çıkarın
#   c) Listeyi küçükten büyüğe sıralayın
#   d) En küçük 3 ve en büyük 3 ölçümü gösterin (dilimleme ile)
#   e) Ortalamanın üzerindeki ölçümleri yeni bir listeye alın
#   f) Orijinal listeyi ters çevirin
#
# Beklenen çıktı:
#   Başlangıç:  [7.2, 6.8, 7.5, 6.5, 8.1, 7.0, 6.9, 7.8, 7.3, 6.7]
#   Eklemeden sonra: [..., 7.4, 6.6]
#   7.2 çıkarıldı: [...]
#   Sıralı:     [6.5, 6.6, 6.7, 6.8, 6.9, 7.0, 7.3, 7.4, 7.5, 7.8, 8.1]
#   En küçük 3: [6.5, 6.6, 6.7]
#   En büyük 3: [7.5, 7.8, 8.1]
#   Ortalama: 7.15
#   Ort. üzeri: [7.3, 7.4, 7.5, 7.8, 8.1]
#
# Öğretim noktaları:
#   - append, remove, sort, reverse
#   - Dilimleme [:3] ve [-3:]
#   - Liste üzerinde döngü ve filtreleme

# --- ÇÖZÜM ---




# ────────────────────────────────────────────────────────────
# Örnek 4.2 ★★ — Matris İşlemleri
# ────────────────────────────────────────────────────────────
# Aşağıdaki 3x3 matrisi liste listesi olarak oluşturun ve:
#
#   matris = [
#       [1, 2, 3],
#       [4, 5, 6],
#       [7, 8, 9]
#   ]
#
#   a) Matrisin tüm elemanlarını yazdırın (satır satır, formatlı)
#   b) Köşegen elemanları bulun ve toplamını hesaplayın (1+5+9)
#   c) Her satırın toplamını hesaplayın
#   d) Her sütunun toplamını hesaplayın
#   e) Matrisin transpozunu alın (satır↔sütun)
#
# Beklenen çıktı:
#   Matris:
#     1  2  3
#     4  5  6
#     7  8  9
#
#   Köşegen: [1, 5, 9] → Toplam: 15
#   Satır toplamları: [6, 15, 24]
#   Sütun toplamları: [12, 15, 18]
#
#   Transpoz:
#     1  4  7
#     2  5  8
#     3  6  9
#
# Öğretim noktaları:
#   - İç içe listeler (2D yapı)
#   - İç içe döngüler
#   - İndeksleme: matris[satir][sutun]
#   - List comprehension ile transpoz

# --- ÇÖZÜM ---




# ────────────────────────────────────────────────────────────
# Örnek 4.3 ★★ — List Comprehension Atölyesi
# ────────────────────────────────────────────────────────────
# Aşağıdaki her birini ÖNCE for döngüsü ile, SONRA list
# comprehension ile yazın. Sonuçları karşılaştırın.
#
#   a) 1-20 arası sayıların küplerini içeren liste
#   b) Bir cümledeki kelimelerin uzunluklarını içeren liste
#      cumle = "Python ile veri bilimi araştırması yapmak çok verimli"
#   c) İki listenin eleman eleman çarpımı
#      a = [1, 2, 3, 4, 5]
#      b = [10, 20, 30, 40, 50]
#   d) Sadece sesli harf içeren kelimeleri filtreleyen liste
#      kelimeler = ["araba", "trn", "elma", "krk", "inek", "brk", "oda"]
#   e) 1-100 arası hem 3'e hem 5'e bölünebilen sayılar
#
# Öğretim noktaları:
#   - for döngüsü → comprehension dönüşümü
#   - Koşullu comprehension (if)
#   - zip() ile paralel iterasyon
#   - any() ile kontrol

# --- ÇÖZÜM ---




# ────────────────────────────────────────────────────────────
# Örnek 4.4 ★★★ — Öğrenci Sıralama Sistemi
# ────────────────────────────────────────────────────────────
# Aşağıdaki öğrenci verilerini tuple listesi olarak alın:
#
#   ogrenciler = [
#       ("Ayşe Yılmaz", "Biyoloji", [88, 92, 85]),
#       ("Mehmet Kaya", "Fizik", [72, 68, 75]),
#       ("Fatma Demir", "Kimya", [95, 91, 98]),
#       ("Ali Çelik", "Biyoloji", [60, 55, 62]),
#       ("Zeynep Ak", "Fizik", [83, 87, 80]),
#       ("Can Öz", "Kimya", [78, 82, 76]),
#       ("Elif Tan", "Biyoloji", [91, 89, 93]),
#       ("Burak Şen", "Fizik", [65, 70, 68]),
#   ]
#
# Programınız:
#   a) Her öğrencinin not ortalamasını hesaplayıp listeye eklesin
#   b) Ortalamaya göre tüm öğrencileri sıralasın (yüksekten düşüğe)
#   c) Her bölüm için ayrı ayrı en başarılı öğrenciyi bulsun
#   d) Sınıf ortalamasını ve ortalamanın altında kalan öğrenci sayısını bulsun
#   e) Sonuçları tablo formatında yazdırsın
#
# Beklenen çıktı:
#   === Genel Sıralama ===
#   Sıra  İsim              Bölüm        Ort.    Durum
#   ─────────────────────────────────────────────────────
#    1    Fatma Demir        Kimya        94.67   ★
#    2    Elif Tan           Biyoloji     91.00   ★
#    ...
#
#   === Bölüm Birincileri ===
#   Biyoloji: Elif Tan (91.00)
#   Fizik:    Zeynep Ak (83.33)
#   Kimya:    Fatma Demir (94.67)
#
#   Sınıf Ortalaması: 78.63
#   Ortalamanın altı: 3 öğrenci
#
# Öğretim noktaları:
#   - Tuple unpacking
#   - sorted() + lambda
#   - Sözlük ile gruplama
#   - Formatlı tablo çıktısı

# --- ÇÖZÜM ---




# ============================================================
#  HAFTA 5 — Sözlükler, Kümeler ve Fonksiyonlar
# ============================================================

# ────────────────────────────────────────────────────────────
# Örnek 5.1 ★ — Deney Envanteri
# ────────────────────────────────────────────────────────────
# Bir laboratuvar envanter sistemi oluşturun:
#
#   envanter = {
#       "pipet_ucu_1000": {"stok": 500, "min_stok": 100, "birim_fiyat": 0.25},
#       "eldiven_M": {"stok": 45, "min_stok": 50, "birim_fiyat": 1.20},
#       "etanol_96": {"stok": 12, "min_stok": 5, "birim_fiyat": 45.00},
#       "petri_kabi": {"stok": 30, "min_stok": 50, "birim_fiyat": 3.50},
#       "santrifuj_tupu": {"stok": 200, "min_stok": 100, "birim_fiyat": 0.80},
#   }
#
# Programınız:
#   a) Tüm envanteri tablo olarak göstersin
#   b) Stoku minimum seviyenin altında olan ürünleri uyarı ile listelesin
#   c) Toplam envanter değerini hesaplasın
#   d) Belirli bir ürüne stok ekleyen fonksiyon
#   e) Sipariş listesi: min_stok'un altındaki ürünlerin
#      ihtiyaç miktarını (min_stok - stok) hesaplasın
#
# Beklenen çıktı:
#   === Laboratuvar Envanteri ===
#   Ürün               Stok   Min    Fiyat    Değer    Durum
#   ──────────────────────────────────────────────────────────
#   pipet_ucu_1000      500    100    0.25   125.00    ✓ OK
#   eldiven_M            45     50    1.20    54.00    ⚠ DÜŞÜK
#   ...
#
#   ⚠ SİPARİŞ GEREKLİ:
#     eldiven_M: 5 adet gerekli (tahmini maliyet: 6.00 TL)
#     petri_kabi: 20 adet gerekli (tahmini maliyet: 70.00 TL)
#
#   Toplam envanter değeri: XXX.XX TL
#
# Öğretim noktaları:
#   - İç içe sözlükler
#   - Sözlük üzerinde döngü (.items())
#   - Koşullu kontrol ve formatlı çıktı

# --- ÇÖZÜM ---




# ────────────────────────────────────────────────────────────
# Örnek 5.2 ★★ — Anket Analizi (Küme İşlemleri)
# ────────────────────────────────────────────────────────────
# Bir üniversitede 3 farklı workshop'a kayıt olan öğrenciler:
#
#   python_ws = {"Ayşe", "Mehmet", "Fatma", "Ali", "Zeynep", "Can"}
#   istatistik_ws = {"Mehmet", "Fatma", "Elif", "Burak", "Zeynep"}
#   ml_ws = {"Fatma", "Ali", "Elif", "Can", "Deniz"}
#
# Küme işlemleri ile bulun:
#   a) Her workshop'a kaç kişi kayıtlı?
#   b) En az bir workshop'a kayıtlı toplam kaç benzersiz öğrenci var?
#   c) Üç workshop'a da katılan öğrenciler
#   d) Sadece Python workshop'una katılan öğrenciler
#   e) Python VE İstatistik'e katılıp ML'ye katılmayan öğrenciler
#   f) Tam olarak iki workshop'a katılan öğrenciler
#   g) Sadece bir workshop'a katılan öğrenciler
#
# Beklenen çıktı:
#   Python: 6, İstatistik: 5, ML: 5
#   Toplam benzersiz öğrenci: 8
#   Üçüne de katılan: {'Fatma'}
#   Sadece Python: {'Ayşe'}
#   Python & İstatistik (ML hariç): {'Mehmet', 'Zeynep'}
#   Tam olarak 2 workshop: {'Mehmet', 'Ali', 'Zeynep', 'Can', 'Elif'}
#   Sadece 1 workshop: {'Ayşe', 'Burak', 'Deniz'}
#
# Öğretim noktaları:
#   - Küme operatörleri: |, &, -, ^
#   - Birden fazla küme operasyonunu birleştirme
#   - Gerçek dünya problemi → küme çözümü

# --- ÇÖZÜM ---




# ────────────────────────────────────────────────────────────
# Örnek 5.3 ★★ — Fonksiyon Fabrikası
# ────────────────────────────────────────────────────────────
# Araştırma hesaplamalarında sık kullanılan fonksiyonları yazın:
#
#   a) ortalama(*sayilar) — değişken sayıda argüman alıp ortalama döndürür
#   b) standart_sapma(*sayilar) — standart sapmayı hesaplar
#   c) z_skoru(deger, ortalama, std) — z-skorunu hesaplar: (x - μ) / σ
#   d) normallesir(liste, yontem="minmax") — listeyi normalize eder
#      yontem="minmax" → (x - min) / (max - min)
#      yontem="zscore" → (x - mean) / std
#   e) aykiri_bul(liste, esik=2.0) — z-skoru eşik'ten büyük olanları bulur
#
# Test verisi:
#   veri = [12, 15, 18, 22, 25, 28, 31, 35, 120]  # 120 aykırı değer
#
# Beklenen çıktı:
#   Ortalama: 34.00
#   Std:      32.39
#   Z-skorları: [-0.68, -0.59, -0.49, -0.37, -0.28, -0.19, -0.09, 0.03, 2.66]
#   Min-Max normalize: [0.00, 0.03, 0.06, 0.09, 0.12, 0.15, 0.18, 0.21, 1.00]
#   Aykırı değerler (|z| > 2): [120]
#
# Öğretim noktaları:
#   - *args kullanımı
#   - Varsayılan parametreler
#   - Fonksiyonların birbirini çağırması
#   - math.sqrt importu

# --- ÇÖZÜM ---




# ────────────────────────────────────────────────────────────
# Örnek 5.4 ★★★ — Kelime Bulutu Hazırlığı
# ────────────────────────────────────────────────────────────
# Bir araştırma makalesinin abstract'ı verilmiştir. Kelime
# bulutu (word cloud) hazırlamak için analiz yapın.
#
#   abstract = """
#   Machine learning algorithms have revolutionized the field of
#   data science and artificial intelligence. Deep learning models,
#   particularly neural networks, have shown remarkable performance
#   in image recognition, natural language processing, and predictive
#   analytics. This study examines the application of machine learning
#   techniques in medical diagnosis, focusing on the accuracy of deep
#   learning models compared to traditional statistical methods.
#   Our results demonstrate that deep learning achieves significantly
#   higher accuracy in complex pattern recognition tasks.
#   """
#
#   stopwords = {"the", "a", "an", "of", "in", "and", "to", "that",
#                "this", "have", "has", "had", "on", "for", "our",
#                "is", "are", "was", "were", "been", "be", "its"}
#
# Programınız (sözlük ve küme kullanarak):
#   a) Tüm kelimeleri küçük harfe çevirip noktalama temizlesin
#   b) Stopword'leri filtresin
#   c) Kelime frekanslarını sözlük olarak hesaplasın
#   d) En sık 10 kelimeyi sıralı listelesin
#   e) Bigram (ardışık 2 kelime) frekanslarını hesaplasın
#   f) Sonuçları metin tabanlı bar chart olarak göstersin
#
# Beklenen çıktı:
#   === En Sık 10 Kelime ===
#   learning       ████████████████ 4
#   deep           ████████████ 3
#   models         ████████ 2
#   machine        ████████ 2
#   accuracy       ████████ 2
#   ...
#
#   === En Sık 5 Bigram ===
#   deep learning      ████████████ 3
#   machine learning   ████████ 2
#   ...
#
# Öğretim noktaları:
#   - Sözlük + küme birlikte kullanım
#   - String temizleme pipeline
#   - sorted() + lambda
#   - Bigram kavramı (NLP'ye giriş motivasyonu)

# --- ÇÖZÜM ---




# ============================================================
#  HAFTA 6 — Dosya İşlemleri ve Hata Yönetimi
# ============================================================

# ────────────────────────────────────────────────────────────
# Örnek 6.1 ★ — Log Dosyası Analizi
# ────────────────────────────────────────────────────────────
# Aşağıdaki log verilerini bir dosyaya yazın, sonra analiz edin.
#
#   log_verileri = [
#       "2024-03-15 08:00:12 INFO  Sistem başlatıldı",
#       "2024-03-15 08:05:23 INFO  Kullanıcı girişi: ahmet",
#       "2024-03-15 08:12:45 WARN  Disk kullanımı %85",
#       "2024-03-15 08:30:01 ERROR Veritabanı bağlantısı kesildi",
#       "2024-03-15 08:30:15 INFO  Veritabanı yeniden bağlandı",
#       "2024-03-15 09:00:00 INFO  Yedekleme başladı",
#       "2024-03-15 09:15:33 WARN  Yedekleme yavaş",
#       "2024-03-15 09:30:00 INFO  Yedekleme tamamlandı",
#       "2024-03-15 10:00:12 ERROR Bellek yetersiz",
#       "2024-03-15 10:05:00 WARN  Servis yeniden başlatılıyor",
#       "2024-03-15 10:05:30 INFO  Servis başlatıldı",
#   ]
#
# Analiz edin:
#   a) Log dosyasını oluşturun
#   b) Dosyayı okuyup her log seviyesinin sayısını bulun
#   c) Sadece ERROR loglarını ayrı dosyaya yazın
#   d) Zaman aralığını (ilk log - son log) hesaplayın
#
# Beklenen çıktı:
#   === Log Analizi ===
#   Toplam kayıt:  11
#   INFO:   6
#   WARN:   3
#   ERROR:  2
#
#   Hata kayıtları → errors.log dosyasına yazıldı
#   Zaman aralığı: 08:00:12 - 10:05:30
#
# Öğretim noktaları:
#   - Dosya yazma ve okuma
#   - String split() ile ayrıştırma
#   - Sözlük ile sayma
#   - with bloğu

# --- ÇÖZÜM ---




# ────────────────────────────────────────────────────────────
# Örnek 6.2 ★★ — CSV Araştırma Verisi İşleyici
# ────────────────────────────────────────────────────────────
# Aşağıdaki deney verilerini CSV dosyasına yazın, sonra analiz edin.
#
#   baslik = ["denek_id", "yas", "cinsiyet", "grup", "pre_test", "post_test"]
#   veriler = [
#       ["D001", 25, "K", "deney",    45, 72],
#       ["D002", 31, "E", "kontrol",  52, 55],
#       ["D003", 28, "K", "deney",    38, 68],
#       ["D004", 35, "E", "deney",    41, 75],
#       ["D005", 22, "K", "kontrol",  48, 50],
#       ["D006", 29, "E", "kontrol",  55, 58],
#       ["D007", 33, "K", "deney",    43, 71],
#       ["D008", 27, "E", "kontrol",  50, 52],
#       ["D009", 30, "K", "deney",    39, 69],
#       ["D010", 26, "E", "kontrol",  47, 49],
#   ]
#
# Analiz edin:
#   a) CSV dosyasını oluşturun
#   b) Her denek için fark (post - pre) sütunu hesaplayın
#   c) Grup bazlı (deney vs kontrol) ortalama farkları karşılaştırın
#   d) Cinsiyet bazlı ortalama farkları karşılaştırın
#   e) Sonuçları yeni bir CSV dosyasına yazın
#   f) Özet istatistikleri yazdırın
#
# Beklenen çıktı:
#   === Araştırma Sonuçları ===
#
#   Grup Karşılaştırması:
#     Deney grubu    (n=5): Pre=41.2, Post=71.0, Fark=+29.8
#     Kontrol grubu  (n=5): Pre=50.4, Post=52.8, Fark=+2.4
#     Gruplar arası fark: 27.4 puan
#
#   Cinsiyet Karşılaştırması:
#     Kadın (n=5): Ortalama fark=+21.4
#     Erkek (n=5): Ortalama fark=+10.8
#
#   Sonuçlar 'analiz_sonuclari.csv' dosyasına kaydedildi.
#
# Öğretim noktaları:
#   - csv.writer ve csv.DictReader
#   - Grup bazlı hesaplama (gruplama mantığı)
#   - Hesaplanmış sütun ekleme
#   - Araştırma verisi iş akışı

# --- ÇÖZÜM ---




# ────────────────────────────────────────────────────────────
# Örnek 6.3 ★★ — JSON Konfigürasyon Yöneticisi
# ────────────────────────────────────────────────────────────
# Bir araştırma projesi için konfigürasyon yönetim sistemi yazın.
#
# Fonksiyonlar:
#   a) varsayilan_config() → varsayılan ayarları döndürür
#   b) config_yukle(dosya_yolu) → JSON dosyasından config okur,
#      dosya yoksa varsayılanı oluşturup döndürür
#   c) config_guncelle(config, **kwargs) → belirli ayarları günceller
#   d) config_kaydet(config, dosya_yolu) → JSON dosyasına kaydeder
#
# Varsayılan config:
#   {
#       "proje_adi": "Yeni Araştırma",
#       "arastirmaci": "Bilinmiyor",
#       "veri_klasoru": "./veri",
#       "cikti_klasoru": "./sonuclar",
#       "parametreler": {
#           "alfa": 0.05,
#           "iterasyon": 1000,
#           "seed": 42
#       },
#       "log_seviyesi": "INFO",
#       "otomatik_yedekleme": true
#   }
#
# Beklenen çıktı:
#   Config dosyası bulunamadı, varsayılan oluşturuluyor...
#   Config yüklendi: Yeni Araştırma
#   Güncelleme: proje_adi → "Sıcaklık Etkisi Deneyi"
#   Güncelleme: arastirmaci → "Dr. Yılmaz"
#   Config kaydedildi: ./config.json
#   Güncel config:
#   {
#     "proje_adi": "Sıcaklık Etkisi Deneyi",
#     "arastirmaci": "Dr. Yılmaz",
#     ...
#   }
#
# Öğretim noktaları:
#   - json.load / json.dump
#   - **kwargs ile esnek güncelleme
#   - FileNotFoundError yakalama
#   - Dosya bazlı konfigürasyon yönetimi pattern'i

# --- ÇÖZÜM ---




# ────────────────────────────────────────────────────────────
# Örnek 6.4 ★★★ — Güvenli Veri Okuyucu
# ────────────────────────────────────────────────────────────
# Gerçek araştırma verisi genellikle "kirli"dir: eksik değerler,
# yanlış formatlar, beklenmeyen karakterler içerir.
#
# Aşağıdaki "kirli" CSV verisini güvenli şekilde okuyan,
# hataları loglayan program yazın:
#
#   kirli_veri = '''denek_id,yas,boy,kilo,kan_basinci
# D001,25,1.75,70,120/80
# D002,abc,1.68,65,130/85
# D003,28,,72,125/82
# D004,35,1.80,HATA,118/76
# D005,-5,1.72,68,140/90
# D006,42,1.65,58,
# D007,30,1.78,82,135/88
# D008,999,1.70,75,122/78
# '''
#
# Programınız:
#   a) Veriyi satır satır okusun
#   b) Her satırda tip dönüşümü yaparken hataları yakalasın
#   c) Geçersiz yaş (< 0 veya > 120), eksik değer, format hatası gibi
#      sorunları loglasın
#   d) Temiz ve hatalı satırları ayırsın
#   e) Temiz veriyi yeni CSV'ye, hata logunu ayrı dosyaya yazsın
#   f) Özet rapor versin
#
# Beklenen çıktı:
#   === Veri Temizleme Raporu ===
#   Toplam satır:     8
#   Temiz satır:      3
#   Hatalı satır:     5
#
#   Hatalar:
#     Satır 2 (D002): Yaş sayısal değil: 'abc'
#     Satır 3 (D003): Eksik değer: boy
#     Satır 4 (D004): Kilo sayısal değil: 'HATA'
#     Satır 5 (D005): Geçersiz yaş: -5
#     Satır 6 (D006): Eksik değer: kan_basinci
#     Satır 8 (D008): Geçersiz yaş: 999
#
#   Temiz veri → temiz_veri.csv (3 kayıt)
#   Hata logu → hata_log.txt
#
# Öğretim noktaları:
#   - try-except iç içe kullanımı
#   - Birden fazla hata türü yakalama
#   - raise ile özel doğrulama
#   - Veri temizleme (data cleaning) iş akışı
#   - Log dosyası oluşturma

# --- ÇÖZÜM ---




# ============================================================
# BONUS — BÖLÜM 2 BÜTÜNLEŞİK ÖRNEKLER
# ============================================================

# ────────────────────────────────────────────────────────────
# Bonus 1 ★★★ — Mini Veritabanı Sistemi
# ────────────────────────────────────────────────────────────
# Sözlük listesi tabanlı bir mini veritabanı sistemi yazın.
#
# Fonksiyonlar:
#   vt_ekle(db, kayit)           → kayıt ekler
#   vt_sil(db, alan, deger)      → eşleşen kaydı siler
#   vt_filtre(db, **kriterler)   → kriterlere uyan kayıtları döndürür
#   vt_sirala(db, alan, ters=False) → belirtilen alana göre sıralar
#   vt_grupla(db, alan)          → belirtilen alana göre gruplar
#   vt_ozet(db, sayisal_alan)    → ortalama, min, max, std hesaplar
#   vt_kaydet(db, dosya_yolu)    → JSON olarak kaydeder
#   vt_yukle(dosya_yolu)         → JSON'dan yükler
#
# Test verisi:
#   db = []
#   vt_ekle(db, {"ad": "Ayşe", "bolum": "Biyoloji", "puan": 88, "yil": 2})
#   vt_ekle(db, {"ad": "Mehmet", "bolum": "Fizik", "puan": 72, "yil": 3})
#   vt_ekle(db, {"ad": "Fatma", "bolum": "Biyoloji", "puan": 95, "yil": 1})
#   vt_ekle(db, {"ad": "Ali", "bolum": "Fizik", "puan": 65, "yil": 2})
#   vt_ekle(db, {"ad": "Zeynep", "bolum": "Kimya", "puan": 82, "yil": 1})
#
# Beklenen çıktı:
#   Biyoloji öğrencileri:
#     Ayşe (88), Fatma (95)
#
#   Puana göre (azalan):
#     Fatma: 95, Ayşe: 88, Zeynep: 82, Mehmet: 72, Ali: 65
#
#   Bölüm grupları:
#     Biyoloji: 2 öğrenci, ort: 91.5
#     Fizik: 2 öğrenci, ort: 68.5
#     Kimya: 1 öğrenci, ort: 82.0
#
#   Puan özeti: ort=80.4, min=65, max=95, std=10.78
#
#   Veritabanı kaydedildi → ogrenci_db.json
#
# Öğretim noktaları:
#   - Hafta 4-5-6 konularının tamamını birleştirme
#   - Fonksiyon tasarımı
#   - Sözlük listesi ile veri yönetimi
#   - JSON ile kalıcılık (persistence)
#   - Bu örnek → Pandas'a geçiş motivasyonu

# --- ÇÖZÜM ---


