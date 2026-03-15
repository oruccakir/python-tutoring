"""
============================================================
  BÖLÜM 1 — TEMEL KAVRAMLAR
  Hafta 1: Python'a Giriş
============================================================

İçindekiler:
  1.1  Python nedir? Neden Python?
  1.2  İlk program: print(), yorum satırları, kod yapısı
  1.3  Değişkenler ve veri tipleri (int, float, str, bool)
  1.4  Kullanıcıdan veri alma: input() ve tip dönüşümleri
  1.5  Uygulamalar
============================================================
"""

# ============================================================
# 1.1 — PYTHON NEDİR? NEDEN PYTHON?
# ============================================================
#
# Python, 1991 yılında Guido van Rossum tarafından geliştirilmiş,
# yüksek seviyeli, yorumlanan (interpreted) bir programlama dilidir.
#
# Araştırmacılar için neden Python?
#   - Okunması ve yazması kolay (sözde koda yakın sözdizimi)
#   - Veri bilimi ekosistemi çok güçlü (NumPy, Pandas, Matplotlib, SciPy)
#   - Makine öğrenmesi kütüphaneleri (Scikit-learn, TensorFlow, PyTorch)
#   - Büyük ve aktif topluluk, bol kaynak
#   - Hemen hemen her alanda kullanılabilir
#
# Kurulum:
#   - python.org adresinden Python 3.x indirin
#   - Alternatif: Anaconda (veri bilimi için hazır paketlerle gelir)
#   - Geliştirme ortamı: VS Code, PyCharm veya Jupyter Notebook
#
# Python'u çalıştırmanın yolları:
#   1. Terminal/komut satırı: python dosya_adi.py
#   2. İnteraktif mod: terminalde "python" yazıp Enter
#   3. Jupyter Notebook: hücre hücre çalıştırma (araştırma için ideal)


# ============================================================
# 1.2 — İLK PROGRAM: print(), YORUM SATIRLARI, KOD YAPISI
# ============================================================

# --- print() fonksiyonu ---
# Ekrana çıktı vermek için kullanılır.
# Python'daki en temel ve en çok kullanacağınız fonksiyon.

print("Merhaba Dünya!")
print("Python öğrenmeye başlıyoruz!")

# Birden fazla değeri virgülle ayırarak yazdırma
print("Python", "versiyonu:", 3)

# sep parametresi: değerler arasındaki ayırıcıyı belirler
print("2024", "03", "15", sep="-")       # 2024-03-15
print("ad", "soyad", "yaş", sep=" | ")   # ad | soyad | yaş

# end parametresi: satır sonundaki karakteri belirler (varsayılan: \n)
print("Satır 1", end=" -> ")
print("Satır 2")   # Çıktı: Satır 1 -> Satır 2

# Boş satır yazdırma
print()

# --- Yorum satırları ---
# Tek satırlık yorum: # işareti ile başlar
# Python bu satırları çalıştırmaz, sadece açıklama amaçlıdır

# Bu bir yorum satırıdır
print("Bu çalışır")  # Satır sonunda da yorum yazılabilir

# Çok satırlık yorum/açıklama için üç tırnak kullanılır:
"""
Bu bir çok satırlık
yorum veya docstring'dir.
Genellikle fonksiyon ve sınıf açıklamaları için kullanılır.
"""

# --- Kod yapısı ---
# Python'da girintileme (indentation) çok önemlidir!
# Diğer dillerde süslü parantez {} kullanılırken,
# Python'da kod blokları girintileme ile belirlenir.
# Standart: 4 boşluk (space) kullanılır.

# Örnek (şimdilik sadece yapıyı görmek için):
if True:
    print("Bu satır girintili — if bloğunun içinde")
    print("Bu da aynı bloğun içinde")
print("Bu satır girintisiz — if bloğunun dışında")


# ============================================================
# 1.3 — DEĞİŞKENLER VE VERİ TİPLERİ
# ============================================================

# --- Değişken nedir? ---
# Değişken, bir değeri bellekte saklayan ve ona isim veren yapıdır.
# Python'da değişken tanımlamak için tip belirtmeye gerek yoktur.
# Python tipi otomatik olarak belirler (dynamic typing).

# --- Değişken oluşturma ---
isim = "Ayşe"
yas = 28
boy = 1.72
ogrenci_mi = True

print(isim)         # Ayşe
print(yas)          # 28
print(boy)          # 1.72
print(ogrenci_mi)   # True

# --- Değişken isimlendirme kuralları ---
# ✓ Harf veya alt çizgi (_) ile başlamalı
# ✓ Harf, rakam ve alt çizgi içerebilir
# ✓ Büyük-küçük harf duyarlıdır (case-sensitive)
# ✗ Rakamla başlayamaz
# ✗ Python anahtar kelimeleri kullanılamaz (if, for, while, class vb.)
# ✗ Boşluk içeremez

# İsimlendirme konvansiyonu (Python stili — snake_case):
ogrenci_sayisi = 30         # ✓ snake_case (önerilen)
# ogrenciSayisi = 30        # ✗ camelCase (Python'da tercih edilmez)
# OgrenciSayisi = 30        # ✗ PascalCase (sınıf isimleri için ayrılmış)
MAX_DENEME = 5              # ✓ UPPER_CASE (sabitler için)

# --- Temel veri tipleri ---

# 1) int — Tam sayı
sayi = 42
negatif_sayi = -10
buyuk_sayi = 1_000_000  # Alt çizgi ile okunabilirlik (1000000 ile aynı)
print(type(sayi))       # <class 'int'>

# 2) float — Ondalıklı sayı
pi = 3.14159
sicaklik = -2.5
bilimsel = 6.022e23     # Bilimsel gösterim: 6.022 × 10²³
print(type(pi))         # <class 'float'>

# 3) str — Metin (string)
ad = "Mehmet"
soyad = 'Yılmaz'        # Tek tırnak da kullanılabilir
universite = "İstanbul Teknik Üniversitesi"

# Çok satırlı string
adres = """Atatürk Bulvarı
No: 42, Kat: 3
Ankara"""
print(type(ad))          # <class 'str'>

# 4) bool — Mantıksal değer (True / False)
python_kolay = True
hata_var = False
print(type(python_kolay))  # <class 'bool'>

# --- type() fonksiyonu ---
# Bir değişkenin tipini öğrenmek için type() kullanılır
print(type(42))         # <class 'int'>
print(type(3.14))       # <class 'float'>
print(type("merhaba"))  # <class 'str'>
print(type(True))       # <class 'bool'>

# --- Çoklu atama ---
# Birden fazla değişkene aynı anda değer atanabilir
x, y, z = 10, 20, 30
print(x, y, z)          # 10 20 30

# Aynı değeri birden fazla değişkene atama
a = b = c = 0
print(a, b, c)          # 0 0 0

# --- Değişken değerini değiştirme ---
sayac = 0
print(sayac)   # 0
sayac = 1
print(sayac)   # 1
sayac = sayac + 1
print(sayac)   # 2

# --- None tipi ---
# Bir değişkenin "değeri yok" anlamında kullanılır
sonuc = None
print(sonuc)        # None
print(type(sonuc))  # <class 'NoneType'>


# ============================================================
# 1.4 — KULLANICIDAN VERİ ALMA: input() VE TİP DÖNÜŞÜMLERİ
# ============================================================

# --- input() fonksiyonu ---
# Kullanıcıdan klavyeden veri almak için kullanılır.
# input() her zaman STRİNG (metin) döndürür!

# isim = input("Adınız: ")
# print("Merhaba", isim)

# ÖNEMLİ: input() her zaman string döndürür!
# sayi = input("Bir sayı girin: ")
# print(type(sayi))   # <class 'str'>  ← sayı değil, metin!

# --- Tip dönüşümleri (Type Casting) ---
# Bir veri tipini başka bir veri tipine çevirmek

# str → int
yas_str = "25"
yas_int = int(yas_str)
print(yas_int + 5)       # 30 (matematiksel toplama)
print(yas_str + "5")     # 255 (string birleştirme — çok farklı!)

# str → float
boy_str = "1.75"
boy_float = float(boy_str)
print(boy_float)          # 1.75

# int → str
sayi = 42
sayi_str = str(sayi)
print("Cevap: " + sayi_str)   # Cevap: 42

# int → float
tam = 5
ondalik = float(tam)
print(ondalik)            # 5.0

# float → int (ondalık kısım kesilir, yuvarlanmaz!)
pi = 3.99
tam_pi = int(pi)
print(tam_pi)             # 3 (dikkat: 4 değil!)

# bool dönüşümleri
print(bool(1))      # True
print(bool(0))      # False
print(bool(""))     # False (boş string)
print(bool("abc"))  # True (dolu string)
print(bool(None))   # False

# --- Kullanıcıdan sayı alma (doğru yol) ---
# yas = int(input("Yaşınız: "))
# boy = float(input("Boyunuz (m): "))
# print(f"Yaşınız: {yas}, Boyunuz: {boy}")


# ============================================================
# 1.5 — UYGULAMALAR
# ============================================================

print("\n" + "=" * 50)
print("UYGULAMALAR")
print("=" * 50)

# ----- Uygulama 1: Basit Hesap Makinesi -----
print("\n--- Uygulama 1: Basit Hesap Makinesi ---")

sayi1 = 15
sayi2 = 4

toplam = sayi1 + sayi2
fark = sayi1 - sayi2
carpim = sayi1 * sayi2
bolum = sayi1 / sayi2        # Normal bölme (float sonuç)
tam_bolum = sayi1 // sayi2   # Tam bölme (int sonuç)
kalan = sayi1 % sayi2        # Mod (kalan)
us = sayi1 ** sayi2          # Üs alma

print(f"{sayi1} + {sayi2} = {toplam}")
print(f"{sayi1} - {sayi2} = {fark}")
print(f"{sayi1} × {sayi2} = {carpim}")
print(f"{sayi1} ÷ {sayi2} = {bolum}")
print(f"{sayi1} // {sayi2} = {tam_bolum}")
print(f"{sayi1} % {sayi2} = {kalan}")
print(f"{sayi1} ^ {sayi2} = {us}")


# ----- Uygulama 2: Sıcaklık Çevirici -----
print("\n--- Uygulama 2: Sıcaklık Çevirici ---")

celsius = 37.5
fahrenheit = (celsius * 9 / 5) + 32
kelvin = celsius + 273.15

print(f"{celsius}°C = {fahrenheit}°F")
print(f"{celsius}°C = {kelvin} K")

# Tersine çeviri
fahrenheit_girdi = 98.6
celsius_sonuc = (fahrenheit_girdi - 32) * 5 / 9
print(f"{fahrenheit_girdi}°F = {celsius_sonuc:.2f}°C")  # :.2f → 2 ondalık basamak


# ----- Uygulama 3: Araştırma Verisi Hesaplama -----
print("\n--- Uygulama 3: Basit Araştırma Hesaplaması ---")

# Bir deneydeki ölçüm sonuçları
olcum_1 = 23.5
olcum_2 = 24.1
olcum_3 = 23.8
olcum_4 = 24.3
olcum_5 = 23.9

# Ortalama hesaplama
olcum_sayisi = 5
toplam = olcum_1 + olcum_2 + olcum_3 + olcum_4 + olcum_5
ortalama = toplam / olcum_sayisi

print(f"Ölçüm sayısı: {olcum_sayisi}")
print(f"Toplam: {toplam}")
print(f"Ortalama: {ortalama:.2f}")

# En büyük ve en küçük değer (şimdilik manuel)
en_buyuk = max(olcum_1, olcum_2, olcum_3, olcum_4, olcum_5)
en_kucuk = min(olcum_1, olcum_2, olcum_3, olcum_4, olcum_5)
aralik = en_buyuk - en_kucuk

print(f"Min: {en_kucuk}, Max: {en_buyuk}")
print(f"Aralık (Range): {aralik:.2f}")


# ----- Uygulama 4: BMI Hesaplayıcı -----
print("\n--- Uygulama 4: Vücut Kitle İndeksi (BMI) ---")

kilo = 75      # kg
boy = 1.78     # metre

bmi = kilo / (boy ** 2)
print(f"Kilo: {kilo} kg")
print(f"Boy: {boy} m")
print(f"BMI: {bmi:.1f}")


# ============================================================
# ALIŞTIRMALAR (Öğrenciler İçin)
# ============================================================
"""
Alıştırma 1: Kendi bilgilerinizi değişkenlere atayıp yazdırın
   - Adınız, soyadınız, yaşınız, bölümünüz, doktora yılınız

Alıştırma 2: Aşağıdaki dönüşümleri yapın ve sonuçları yazdırın
   - "3.14" → float
   - 100 → string
   - 0 → bool
   - "True" → ??? (dikkat: bu bool("True") ile bool dönüşümü farklıdır!)

Alıştırma 3: Kullanıcıdan iki sayı alıp dört işlem yapan program yazın
   (input() kullanarak)

Alıştırma 4: Kullanıcıdan daire yarıçapını alıp
   çevre ve alan hesaplayan program yazın
   (Çevre = 2πr, Alan = πr²)

Alıştırma 5: Kullanıcıdan saat ve dakika bilgisi alıp
   toplam dakikaya çeviren program yazın
   (Örnek: 2 saat 30 dakika = 150 dakika)
"""
