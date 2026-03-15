"""
============================================================
  BÖLÜM 1 — DERS İÇİ CANLI KODLAMA ÖRNEKLERİ
============================================================

Bu dosya derste canlı olarak kodlanacak örnekleri içerir.
Her örnek için:
  - Problem tanımı ve beklenen çıktı verilmiştir
  - Çözüm kısmı boş bırakılmıştır → derste canlı kodlanacak
  - Zorluk seviyesi yıldızla belirtilmiştir (★ kolay → ★★★ zor)

İpucu: Öğrencilere önce problemi okuyun, birlikte düşünün,
       sonra adım adım kodlayın.
============================================================
"""


# ============================================================
#  HAFTA 1 — Python'a Giriş
# ============================================================

# ────────────────────────────────────────────────────────────
# Örnek 1.1 ★ — Kartvizit Oluşturucu
# ────────────────────────────────────────────────────────────
# Bir araştırmacının bilgilerini değişkenlere atayın ve
# aşağıdaki formatta ekrana yazdırın.
#
# Beklenen çıktı:
# ┌──────────────────────────────────┐
# │  Dr. Ayşe Yılmaz                │
# │  Biyoloji Bölümü                │
# │  İstanbul Üniversitesi          │
# │  ayse.yilmaz@uni.edu.tr         │
# │  Tel: +90 212 555 0001          │
# └──────────────────────────────────┘
#
# Öğretim noktaları:
#   - Değişken tanımlama
#   - print() ve string birleştirme
#   - f-string'e ilk bakış

# --- ÇÖZÜM ---




# ────────────────────────────────────────────────────────────
# Örnek 1.2 ★ — Birim Dönüştürücü
# ────────────────────────────────────────────────────────────
# Araştırma laboratuvarında sık kullanılan birim dönüşümleri:
#   a) 2500 mL → Litre
#   b) 0.045 kg → gram ve miligram
#   c) 72 saat → gün ve kalan saat
#   d) 37.5 °C → Fahrenheit ve Kelvin
#
# Her dönüşümü bir değişkene atayıp sonucu yazdırın.
#
# Beklenen çıktı:
#   2500 mL = 2.5 L
#   0.045 kg = 45.0 g = 45000.0 mg
#   72 saat = 3 gün 0 saat
#   37.5 °C = 99.5 °F = 310.65 K
#
# Öğretim noktaları:
#   - Aritmetik operatörler (/, //, %)
#   - float ve int farkı
#   - f-string formatlama

# --- ÇÖZÜM ---




# ────────────────────────────────────────────────────────────
# Örnek 1.3 ★★ — Deney Özeti Hesaplayıcı
# ────────────────────────────────────────────────────────────
# Bir deneyde 6 farklı ölçüm alınmıştır:
#   olcumler: 12.3, 11.8, 12.7, 12.1, 13.0, 11.5
#
# Hesaplayın ve yazdırın:
#   - Toplam
#   - Ortalama (mean)
#   - En büyük ve en küçük değer
#   - Aralık (range) = max - min
#   - Ortalamanın üzerindeki ölçüm sayısı (elle sayarak)
#
# Beklenen çıktı:
#   === Deney Özeti ===
#   Ölçüm sayısı:  6
#   Toplam:         73.40
#   Ortalama:       12.23
#   Min:            11.50
#   Max:            13.00
#   Aralık:         1.50
#   Ort. üzeri:     3 ölçüm
#
# Öğretim noktaları:
#   - Birden fazla değişkenle çalışma
#   - min(), max() fonksiyonları
#   - Formatlı çıktı (:.2f)
#   - Bool → int dönüşümü (True = 1)

# --- ÇÖZÜM ---




# ────────────────────────────────────────────────────────────
# Örnek 1.4 ★★ — Tip Dönüşümü Bulmacası
# ────────────────────────────────────────────────────────────
# Aşağıdaki ifadelerin sonuçlarını ÖNCE öğrencilere sorun,
# sonra birlikte çalıştırın. Sürpriz sonuçları tartışın.
#
# Her birinin çıktısını ve tipini yazdırın:
#   a) 10 / 3
#   b) 10 // 3
#   c) 10 % 3
#   d) "5" + "3"
#   e) int("5") + int("3")
#   f) str(5) + str(3)
#   g) float("inf") > 999999999
#   h) bool("")
#   i) bool("False")       ← sürpriz!
#   j) bool(0) vs bool(0.0) vs bool(None)
#   k) type(True + True)   ← sürpriz!
#
# Öğretim noktaları:
#   - / vs // farkı
#   - String + ile birleştirme vs sayı toplama
#   - bool() dönüşüm kuralları (truthy/falsy)
#   - Python'da True = 1, False = 0

# --- ÇÖZÜM ---




# ============================================================
#  HAFTA 2 — Operatörler ve Koşullu İfadeler
# ============================================================

# ────────────────────────────────────────────────────────────
# Örnek 2.1 ★ — Araştırma Bütçesi Kontrolü
# ────────────────────────────────────────────────────────────
# Bir araştırma projesinin bütçe bilgileri:
#   toplam_butce = 50000
#   harcanan = 32750
#   planlanan_harcama = 12000
#
# Programınız şunları hesaplayıp yazdırsın:
#   - Kalan bütçe
#   - Kullanım yüzdesi
#   - Planlanan harcama yapılabilir mi? (kalan >= planlanan)
#   - Bütçe durumu:
#       %80 üzeri kullanıldıysa → "Dikkat: Bütçe kritik seviyede!"
#       %50 üzeri → "Bütçe kontrol altında."
#       Altı → "Bütçe rahat."
#
# Beklenen çıktı:
#   === Bütçe Raporu ===
#   Toplam:    50,000 TL
#   Harcanan:  32,750 TL
#   Kalan:     17,250 TL
#   Kullanım:  %65.5
#   Planlanan harcama (12,000 TL): Yapılabilir ✓
#   Durum: Bütçe kontrol altında.
#
# Öğretim noktaları:
#   - Karşılaştırma operatörleri
#   - if-elif-else
#   - f-string ile binlik ayırıcı ({:,})

# --- ÇÖZÜM ---




# ────────────────────────────────────────────────────────────
# Örnek 2.2 ★★ — Denek Uygunluk Kontrolü
# ────────────────────────────────────────────────────────────
# Bir klinik araştırmaya katılım kriterleri:
#   - Yaş: 18-65 arası (dahil)
#   - BMI: 18.5-30.0 arası (dahil)
#   - Kronik hastalık: olmamalı
#   - Son 6 ayda başka araştırmaya katılmamış olmalı
#
# Aşağıdaki 4 adayı değerlendirin:
#   Aday 1: yaş=25, bmi=22.5, kronik=False, son_arastirma=False
#   Aday 2: yaş=70, bmi=24.0, kronik=False, son_arastirma=False
#   Aday 3: yaş=35, bmi=32.1, kronik=False, son_arastirma=False
#   Aday 4: yaş=45, bmi=27.3, kronik=True,  son_arastirma=False
#
# Her aday için:
#   - Uygun mu? (Evet/Hayır)
#   - Uygun değilse hangi kriter(ler) sağlanmadı?
#
# Beklenen çıktı:
#   Aday 1: UYGUN
#   Aday 2: UYGUN DEĞİL — Yaş kriteri sağlanmadı (70)
#   Aday 3: UYGUN DEĞİL — BMI kriteri sağlanmadı (32.1)
#   Aday 4: UYGUN DEĞİL — Kronik hastalık mevcut
#
# Öğretim noktaları:
#   - and ile birden fazla koşul birleştirme
#   - Zincirleme karşılaştırma (18 <= yas <= 65)
#   - Her koşulu ayrı ayrı kontrol etme

# --- ÇÖZÜM ---




# ────────────────────────────────────────────────────────────
# Örnek 2.3 ★★ — Akademik Not Dönüştürücü
# ────────────────────────────────────────────────────────────
# Farklı üniversiteler farklı not sistemi kullanır.
# Bir dönüştürücü yazın:
#
# Girdi: harf notu (string) → Çıktı: 4'lük sistem ve açıklama
#
#   AA → 4.0  (Mükemmel)
#   BA → 3.5  (Çok İyi)
#   BB → 3.0  (İyi)
#   CB → 2.5  (Ortanın Üstü)
#   CC → 2.0  (Orta)
#   DC → 1.5  (Koşullu)
#   DD → 1.0  (Koşullu)
#   FF → 0.0  (Başarısız)
#
# Test notları: "BA", "CC", "FF", "XY" (geçersiz)
#
# Beklenen çıktı:
#   BA → 3.5 / 4.0 (Çok İyi)
#   CC → 2.0 / 4.0 (Orta)
#   FF → 0.0 / 4.0 (Başarısız)
#   XY → Geçersiz not!
#
# Öğretim noktaları:
#   - if-elif zinciri VEYA match-case kullanımı
#   - Her iki yöntemle de çözüp karşılaştırma yapılabilir

# --- ÇÖZÜM ---




# ────────────────────────────────────────────────────────────
# Örnek 2.4 ★★★ — Üçgen Sınıflandırıcı
# ────────────────────────────────────────────────────────────
# Kullanıcıdan (burada sabit değer) üç kenar uzunluğu alın.
# Programınız:
#   1. Önce bu kenarlarla üçgen oluşturulup oluşturulamayacağını kontrol etsin
#      (Üçgen eşitsizliği: herhangi iki kenar toplamı > üçüncü kenar)
#   2. Üçgen oluşturulabiliyorsa türünü belirlesin:
#      - Eşkenar (üç kenar eşit)
#      - İkizkenar (iki kenar eşit)
#      - Çeşitkenar (hepsi farklı)
#   3. Ayrıca açılarına göre:
#      - Dik üçgen mi? (Pisagor: a² + b² = c²)
#
# Test değerleri:
#   a=3, b=4, c=5   → Çeşitkenar, Dik üçgen
#   a=5, b=5, c=5   → Eşkenar
#   a=1, b=2, c=10   → Üçgen oluşturulamaz
#   a=5, b=5, c=7   → İkizkenar
#
# Öğretim noktaları:
#   - İç içe koşullar
#   - Mantıksal operatörler (and, or)
#   - Matematiksel formüllerin koda dönüştürülmesi

# --- ÇÖZÜM ---




# ============================================================
#  HAFTA 3 — Döngüler ve String İşlemleri
# ============================================================

# ────────────────────────────────────────────────────────────
# Örnek 3.1 ★ — Çarpım Tablosu
# ────────────────────────────────────────────────────────────
# İstenen bir sayının çarpım tablosunu yazdırın (1-10).
#
# sayi = 7 için beklenen çıktı:
#   === 7 Çarpım Tablosu ===
#    7 x  1 =   7
#    7 x  2 =  14
#    7 x  3 =  21
#    ...
#    7 x 10 =  70
#
# Öğretim noktaları:
#   - for + range()
#   - f-string hizalama

# --- ÇÖZÜM ---




# ────────────────────────────────────────────────────────────
# Örnek 3.2 ★★ — Asal Sayı Bulucu
# ────────────────────────────────────────────────────────────
# 2'den 100'e kadar olan tüm asal sayıları bulup yazdırın.
# Sonunda toplam kaç asal sayı bulunduğunu yazdırın.
#
# Beklenen çıktı:
#   2 3 5 7 11 13 17 19 23 29 31 37 41 43 47
#   53 59 61 67 71 73 79 83 89 97
#   Toplam: 25 asal sayı
#
# Öğretim noktaları:
#   - İç içe döngü
#   - break ile erken çıkış
#   - for-else yapısı (opsiyonel)
#   - Verimlilik: √n'e kadar kontrol yeterli

# --- ÇÖZÜM ---




# ────────────────────────────────────────────────────────────
# Örnek 3.3 ★★ — Deney Verisi Analizi (Döngü ile)
# ────────────────────────────────────────────────────────────
# Bir deneyde günlük sıcaklık ölçümleri alınmıştır:
#   olcumler = [36.6, 37.2, 36.8, 38.5, 37.1, 39.2, 36.9,
#               37.8, 38.1, 36.5, 37.4, 38.8, 37.0, 36.7]
#
# Döngü kullanarak (NumPy/Pandas KULLANMADAN) hesaplayın:
#   a) Ortalama sıcaklık
#   b) En yüksek ve en düşük sıcaklık + hangi günlerde
#   c) 37.5 üzerindeki "ateşli" günlerin sayısı ve yüzdesi
#   d) Ardışık iki gün arası en büyük fark
#
# Beklenen çıktı:
#   === Sıcaklık Analiz Raporu ===
#   Gün sayısı:        14
#   Ortalama:          37.47 °C
#   En düşük:          36.50 °C (Gün 10)
#   En yüksek:         39.20 °C (Gün 6)
#   Ateşli günler:     5 / 14 (%35.7)
#   Max günlük fark:   1.70 °C (Gün 5→6)
#
# Öğretim noktaları:
#   - for döngüsü ile liste gezme
#   - enumerate() kullanımı
#   - Birden fazla değişkeni döngü içinde güncelleme
#   - İndeks takibi

# --- ÇÖZÜM ---




# ────────────────────────────────────────────────────────────
# Örnek 3.4 ★★ — Yıldız Desenleri
# ────────────────────────────────────────────────────────────
# Aşağıdaki 3 deseni iç içe döngü kullanarak yazdırın.
# n = 5 için:
#
# Desen A (Dik üçgen):    Desen B (Piramit):     Desen C (Elmas):
# *                           *                       *
# **                         ***                     ***
# ***                       *****                   *****
# ****                     *******                 *******
# *****                   *********               *********
#                                                  *******
#                                                   *****
#                                                    ***
#                                                     *
#
# Öğretim noktaları:
#   - İç içe for döngüsü
#   - String çarpımı ("*" * n)
#   - Boşluk ve hizalama hesabı

# --- ÇÖZÜM ---




# ────────────────────────────────────────────────────────────
# Örnek 3.5 ★★ — E-posta Doğrulayıcı
# ────────────────────────────────────────────────────────────
# Verilen e-posta adreslerini kontrol edin.
# Geçerli bir e-posta için kurallar:
#   - Tam olarak bir adet @ işareti içermeli
#   - @ işaretinden önce en az 1 karakter olmalı
#   - @ işaretinden sonra en az bir "." olmalı
#   - "." ile bitmemeli
#   - Boşluk içermemeli
#
# Test e-postaları:
#   emails = [
#       "ahmet@uni.edu.tr",
#       "ayse@lab",
#       "hata@@mail.com",
#       "@domain.com",
#       "test@domain.",
#       "kullanici adi@mail.com",
#       "fatma.dr@hastane.gov.tr",
#   ]
#
# Beklenen çıktı:
#   ahmet@uni.edu.tr          → Geçerli ✓
#   ayse@lab                  → Geçersiz: '@' sonrası '.' yok
#   hata@@mail.com            → Geçersiz: Birden fazla '@'
#   @domain.com               → Geçersiz: '@' öncesi boş
#   test@domain.              → Geçersiz: '.' ile bitiyor
#   kullanici adi@mail.com    → Geçersiz: Boşluk içeriyor
#   fatma.dr@hastane.gov.tr   → Geçerli ✓
#
# Öğretim noktaları:
#   - String metodları: count(), split(), endswith()
#   - "in" operatörü
#   - Birden fazla koşulun sırayla kontrol edilmesi

# --- ÇÖZÜM ---




# ────────────────────────────────────────────────────────────
# Örnek 3.6 ★★★ — DNA Dizisi Analizi
# ────────────────────────────────────────────────────────────
# Verilen bir DNA dizisini analiz edin.
#
#   dna = "ATCGATCGAATTCCGGAATCGATCGCCTTAAGG"
#
# Hesaplayın ve yazdırın:
#   a) Her nükleotidin sayısı ve yüzdesi (A, T, C, G)
#   b) GC oranı (G+C sayısı / toplam) — tür tespitinde önemli
#   c) Tamamlayıcı dizi (A↔T, G↔C)
#   d) Verilen kısa dizinin (motif) DNA'da kaç kez geçtiği
#      motif = "ATC"
#   e) RNA'ya transkripsiyon (T → U)
#
# Beklenen çıktı:
#   === DNA Analiz Raporu ===
#   Dizi uzunluğu: 33
#
#   Nükleotid dağılımı:
#     A: 8  (%24.2)
#     T: 8  (%24.2)
#     C: 9  (%27.3)
#     G: 8  (%24.2)
#
#   GC oranı: %51.5
#
#   Tamamlayıcı dizi:
#     5'- ATCGATCGAATTCCGGAATCGATCGCCTTAAGG -3'
#     3'- TAGCTAGCTTAAGGCCTTAGCTAGCGGAATTCC -5'
#
#   "ATC" motifi 4 kez bulundu.
#   RNA: AUCGAUCGAAUUCCGGAAUCGAUCGCCUUAAGG
#
# Öğretim noktaları:
#   - String üzerinde döngü
#   - count() ve replace()
#   - Koşullu string oluşturma (for + if)
#   - Araştırma bağlamında Python kullanımı

# --- ÇÖZÜM ---




# ────────────────────────────────────────────────────────────
# Örnek 3.7 ★★★ — Basit Şifre Gücü Ölçer
# ────────────────────────────────────────────────────────────
# Verilen şifrelerin gücünü ölçen program yazın.
#
# Puanlama sistemi:
#   +1 puan: 8 karakter veya daha uzun
#   +1 puan: En az bir büyük harf içeriyor
#   +1 puan: En az bir küçük harf içeriyor
#   +1 puan: En az bir rakam içeriyor
#   +1 puan: En az bir özel karakter içeriyor (!@#$%^&*_-)
#   +1 puan: 12 karakter veya daha uzun (bonus)
#
# Güç seviyeleri:
#   0-2: Zayıf
#   3-4: Orta
#   5-6: Güçlü
#
# Test şifreleri:
#   sifreler = ["abc", "Parola123", "Tr5!", "G3l1$m1$_S1fr3!!", "12345678"]
#
# Beklenen çıktı:
#   === Şifre Gücü Analizi ===
#   "abc"                → [■□□□□□] Zayıf      (1/6)
#   "Parola123"          → [■■■■□□] Orta       (4/6)
#   "Tr5!"               → [■■■■□□] Orta       (4/6)
#   "G3l1$m1$_S1fr3!!"   → [■■■■■■] Güçlü     (6/6)
#   "12345678"           → [■■□□□□] Zayıf      (2/6)
#
# Öğretim noktaları:
#   - String metodları: isupper(), islower(), isdigit()
#   - for döngüsü ile karakter kontrolü
#   - any() fonksiyonu (opsiyonel — döngü ile de yapılabilir)
#   - Boolean → int (True = 1) kullanarak puan toplama

# --- ÇÖZÜM ---




# ────────────────────────────────────────────────────────────
# Örnek 3.8 ★★★ — Histogram Çizici (Metin Tabanlı)
# ────────────────────────────────────────────────────────────
# Bir anket sonucundaki cevapları metin tabanlı histogram
# olarak görselleştirin.
#
#   anket_sonuclari = [
#       ("Çok Memnun", 45),
#       ("Memnun", 82),
#       ("Kararsız", 23),
#       ("Memnun Değil", 15),
#       ("Hiç Memnun Değil", 8),
#   ]
#   toplam_katilimci = 173
#
# Beklenen çıktı (her █ = 2 kişi):
#
#   === Memnuniyet Anketi Sonuçları (n=173) ===
#
#   Çok Memnun       | ██████████████████████▌ 45 (%26.0)
#   Memnun           | █████████████████████████████████████████ 82 (%47.4)
#   Kararsız         | ███████████▌ 23 (%13.3)
#   Memnun Değil     | ███████▌ 15 (%8.7)
#   Hiç Memnun Değil | ████ 8 (%4.6)
#
# İpucu: "█" karakterini kullanın, her █ = 2 kişiyi temsil etsin.
#         Yarım kişi için "▌" kullanılabilir.
#
# Öğretim noktaları:
#   - for döngüsü ile tuple listesi gezme
#   - String çarpımı ("█" * n)
#   - f-string hizalama (sola: <, sağa: >)
#   - Yüzde hesaplama

# --- ÇÖZÜM ---




# ────────────────────────────────────────────────────────────
# Örnek 3.9 ★★★ — Collatz Conjecture Görselleştirici
# ────────────────────────────────────────────────────────────
# Collatz Hipotezi: Herhangi bir pozitif tam sayıdan başlayarak
#   - Sayı çift ise → 2'ye böl
#   - Sayı tek ise  → 3 ile çarp ve 1 ekle
# Bu işlemi tekrarlayınca her sayı sonunda 1'e ulaşır (kanıtlanmamış!).
#
# Verilen bir sayı için:
#   a) 1'e ulaşana kadar tüm seriyi yazdırın
#   b) Kaç adımda ulaştığını söyleyin
#   c) Serideki en büyük sayıyı bulun
#   d) Seriyi basit bir grafik olarak çizin
#
# baslangic = 27 için beklenen çıktı (kısaltılmış):
#   Başlangıç: 27
#   27 → 82 → 41 → 124 → 62 → 31 → ... → 4 → 2 → 1
#
#   Adım sayısı: 111
#   Ulaşılan en büyük değer: 9232
#
#   Grafik (ilk 40 adım, her █ ≈ 200):
#   ████████████████████████████████████████████████ 9232
#   ████████████████████████ 4616
#   ████████████ 2308
#   ...
#
# Öğretim noktaları:
#   - while döngüsü (bitiş koşulu belirsiz)
#   - if-else ile çift/tek kontrolü
#   - Sayaç ve max takibi
#   - Matematiksel bir problemin koda dönüştürülmesi

# --- ÇÖZÜM ---




# ============================================================
# BONUS — HAFTALAR ARASI BÜTÜNLEŞIK ÖRNEKLER
# ============================================================

# ────────────────────────────────────────────────────────────
# Bonus 1 ★★★ — Mini İstatistik Hesaplayıcı
# ────────────────────────────────────────────────────────────
# NumPy KULLANMADAN, sadece döngü ve temel operatörlerle
# bir veri setinin istatistiklerini hesaplayın.
#
# veri = [14, 22, 8, 31, 17, 25, 19, 27, 11, 23, 29, 16, 20, 35, 13]
#
# Hesaplayın:
#   a) Ortalama (mean)
#   b) Medyan (ortanca değer — sıralayıp ortadakini bulun)
#   c) Standart sapma (std) — formül:
#      std = sqrt( sum((xi - mean)^2) / n )
#   d) Veriyi 5'li aralıklarla gruplandırıp frekans tablosu oluşturun
#
# Beklenen çıktı:
#   === İstatistik Raporu ===
#   n    = 15
#   Mean = 20.67
#   Median = 20
#   Std  = 7.40
#
#   Frekans Tablosu:
#    5-10 | ██ 1
#   10-15 | ██████ 3
#   15-20 | ████████ 4
#   20-25 | ████████ 4
#   25-30 | ████ 2
#   30-35 | ██ 1
#
# İpucu: Standart sapma için math.sqrt() kullanabilirsiniz.
#        import math → math.sqrt(deger)
#
# Öğretim noktaları:
#   - Tüm Hafta 1-3 konularının birleşimi
#   - İstatistik formüllerini kodlama
#   - Liste sıralama: sorted()
#   - Bu örnekle "NumPy bunu tek satırda yapar" motivasyonu

# --- ÇÖZÜM ---




# ────────────────────────────────────────────────────────────
# Bonus 2 ★★★ — Araştırma Makale Özet Analizi
# ────────────────────────────────────────────────────────────
# Bir araştırma makalesinin abstract'ını analiz edin.
#
# abstract = """
# This study investigates the effects of climate change on
# biodiversity in Mediterranean ecosystems. We analyzed data from
# 150 species across 12 different habitats over a period of 20 years.
# Our results indicate that temperature increases of 1.5 degrees
# Celsius led to a 23 percent decline in species diversity.
# Furthermore, precipitation changes significantly affected
# habitat distribution patterns. The findings suggest that
# conservation strategies must be adapted to account for ongoing
# climate variability. This research provides critical evidence
# for policy makers working on environmental protection frameworks.
# """
#
# Analiz edin ve yazdırın:
#   a) Toplam kelime sayısı
#   b) Toplam cümle sayısı (. ile biten)
#   c) Ortalama cümle uzunluğu (kelime/cümle)
#   d) En sık kullanılan 5 kelime (stopword'ler hariç)
#      Stopwords: "the", "a", "an", "of", "in", "on", "to", "for",
#                 "and", "that", "this", "is", "are", "was", "were",
#                 "we", "our", "be"
#   e) Metindeki tüm sayıları bulun ve listeleyin
#   f) Okunabilirlik skoru (basit): ortalama kelime uzunluğu
#
# Öğretim noktaları:
#   - String metodları: split(), lower(), strip(), replace()
#   - Döngü içinde sayaç yönetimi
#   - "in" operatörü ile filtreleme
#   - Gerçek dünya metin analizi motivasyonu

# --- ÇÖZÜM ---


