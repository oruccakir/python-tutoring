"""
============================================================
  BÖLÜM 2 — VERİ YAPILARI VE FONKSİYONLAR
  Hafta 4: Listeler ve Tuple
============================================================

İçindekiler:
  4.1  Liste oluşturma ve indeksleme
  4.2  Liste dilimleme (slicing)
  4.3  Liste metodları
  4.4  List comprehension
  4.5  Tuple yapısı ve kullanımı
  4.6  Liste ve Tuple karşılaştırma
  4.7  Uygulamalar
============================================================
"""

# ============================================================
# 4.1 — LİSTE OLUŞTURMA VE İNDEKSLEME
# ============================================================

print("=== Liste Oluşturma ===\n")

# --- Liste nedir? ---
# Liste, birden fazla değeri sıralı şekilde saklayan veri yapısıdır.
# Değiştirilebilir (mutable) — eleman eklenebilir, çıkarılabilir, değiştirilebilir.
# Farklı veri tiplerini bir arada tutabilir.

# --- Liste oluşturma yolları ---

# Boş liste
bos_liste = []
bos_liste2 = list()

# Değerlerle oluşturma
sayilar = [10, 20, 30, 40, 50]
meyveler = ["elma", "armut", "muz", "çilek"]
karisik = [42, "Python", 3.14, True, None]

print(f"sayilar:  {sayilar}")
print(f"meyveler: {meyveler}")
print(f"karisik:  {karisik}")
print(f"Tip: {type(sayilar)}")

# range() ile liste oluşturma
sifirdan_ona = list(range(10))       # [0, 1, 2, ..., 9]
cift_sayilar = list(range(0, 20, 2)) # [0, 2, 4, ..., 18]
print(f"\nrange(10):      {sifirdan_ona}")
print(f"range(0,20,2):  {cift_sayilar}")

# String'den liste
harfler = list("Python")
print(f"list('Python'): {harfler}")

# --- İndeksleme ---
print("\n--- İndeksleme ---")
notlar = [85, 92, 78, 95, 88, 72, 90]
#          0   1   2   3   4   5   6    → pozitif indeks
#         -7  -6  -5  -4  -3  -2  -1   → negatif indeks

print(f"Liste:    {notlar}")
print(f"notlar[0]:  {notlar[0]}")     # 85 (ilk eleman)
print(f"notlar[3]:  {notlar[3]}")     # 95
print(f"notlar[-1]: {notlar[-1]}")    # 90 (son eleman)
print(f"notlar[-2]: {notlar[-2]}")    # 72 (sondan ikinci)

# --- Eleman değiştirme ---
print("\n--- Eleman Değiştirme ---")
notlar[2] = 80  # 78 → 80
print(f"notlar[2] = 80 → {notlar}")

# --- len() — liste uzunluğu ---
print(f"\nlen(notlar): {len(notlar)}")

# --- Üyelik kontrolü: in ---
print(f"\n95 in notlar:   {95 in notlar}")     # True
print(f"100 in notlar:  {100 in notlar}")      # False
print(f"100 not in notlar: {100 not in notlar}")  # True


# ============================================================
# 4.2 — LİSTE DİLİMLEME (SLICING)
# ============================================================

print("\n\n=== Liste Dilimleme ===\n")

veriler = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

print(f"veriler:       {veriler}")
print(f"veriler[2:5]:  {veriler[2:5]}")     # [30, 40, 50]
print(f"veriler[:4]:   {veriler[:4]}")       # [10, 20, 30, 40]
print(f"veriler[6:]:   {veriler[6:]}")       # [70, 80, 90, 100]
print(f"veriler[::2]:  {veriler[::2]}")      # [10, 30, 50, 70, 90]
print(f"veriler[::-1]: {veriler[::-1]}")     # ters çevrilmiş
print(f"veriler[-3:]:  {veriler[-3:]}")      # [80, 90, 100] (son 3)

# Dilimle değiştirme
kopya = veriler[:]  # tam kopya
kopya[1:4] = [200, 300, 400]
print(f"\nkopya[1:4] = [200,300,400] → {kopya}")


# ============================================================
# 4.3 — LİSTE METODLARI
# ============================================================

print("\n\n=== Liste Metodları ===\n")

# --- Eleman ekleme ---
print("--- Eleman Ekleme ---")
ogrenciler = ["Ayşe", "Mehmet", "Fatma"]
print(f"Başlangıç: {ogrenciler}")

ogrenciler.append("Ali")               # Sona ekle
print(f"append('Ali'):      {ogrenciler}")

ogrenciler.insert(1, "Zeynep")         # Belirli konuma ekle
print(f"insert(1,'Zeynep'): {ogrenciler}")

ogrenciler.extend(["Can", "Elif"])      # Birden fazla eleman ekle
print(f"extend([...]):      {ogrenciler}")

# --- Eleman çıkarma ---
print("\n--- Eleman Çıkarma ---")
ogrenciler.remove("Mehmet")            # Değere göre çıkar (ilk bulunan)
print(f"remove('Mehmet'):   {ogrenciler}")

cikan = ogrenciler.pop()               # Son elemanı çıkar ve döndür
print(f"pop():              {ogrenciler}  → çıkan: {cikan}")

cikan2 = ogrenciler.pop(0)             # İndekse göre çıkar
print(f"pop(0):             {ogrenciler}  → çıkan: {cikan2}")

# del ile silme
del ogrenciler[1]
print(f"del [1]:            {ogrenciler}")

# clear — tüm elemanları sil
# ogrenciler.clear()

# --- Sıralama ---
print("\n--- Sıralama ---")
puanlar = [78, 92, 85, 63, 91, 70, 88]
print(f"Orijinal: {puanlar}")

puanlar.sort()                          # Küçükten büyüğe (yerinde değiştirir)
print(f"sort():            {puanlar}")

puanlar.sort(reverse=True)              # Büyükten küçüğe
print(f"sort(reverse):     {puanlar}")

# sorted() — orijinali değiştirmez, yeni liste döndürür
orijinal = [3, 1, 4, 1, 5, 9, 2, 6]
sirali = sorted(orijinal)
print(f"\norijinal:        {orijinal}")
print(f"sorted():        {sirali}")
print(f"orijinal hala:   {orijinal}")

# --- Ters çevirme ---
print("\n--- Ters Çevirme ---")
harfler = ["a", "b", "c", "d"]
harfler.reverse()
print(f"reverse(): {harfler}")

# --- Arama ve sayma ---
print("\n--- Arama ve Sayma ---")
notlar = [85, 92, 78, 92, 88, 72, 92]
print(f"notlar: {notlar}")
print(f"count(92):  {notlar.count(92)}")     # 3
print(f"index(88):  {notlar.index(88)}")     # 4 (ilk bulunan indeks)

# --- Kopyalama ---
print("\n--- Kopyalama (ÖNEMLİ!) ---")
# DİKKAT: = ile atama kopya oluşturmaz, aynı listeye referans verir!
a = [1, 2, 3]
b = a           # b ve a aynı listeyi gösterir!
b.append(4)
print(f"a = [1,2,3]; b = a; b.append(4)")
print(f"a: {a}")  # [1, 2, 3, 4] ← a da değişti!
print(f"b: {b}")  # [1, 2, 3, 4]

# Doğru kopyalama yolları:
c = [1, 2, 3]
d = c.copy()    # Yöntem 1: .copy()
e = c[:]        # Yöntem 2: dilimleme
f = list(c)     # Yöntem 3: list()

d.append(999)
print(f"\nc:        {c}")   # [1, 2, 3] ← değişmedi
print(f"d.copy(): {d}")     # [1, 2, 3, 999]


# ============================================================
# 4.4 — LIST COMPREHENSION
# ============================================================

print("\n\n=== List Comprehension ===\n")

# List comprehension, bir satırda liste oluşturmanın kısa ve okunabilir yoludur.
# Sözdizimi: [ifade for eleman in koleksiyon]
# Opsiyonel filtre: [ifade for eleman in koleksiyon if koşul]

# --- Temel kullanım ---
print("--- Temel ---")

# Geleneksel yol:
kareler_v1 = []
for i in range(1, 11):
    kareler_v1.append(i ** 2)

# List comprehension ile:
kareler_v2 = [i ** 2 for i in range(1, 11)]

print(f"Kareler: {kareler_v2}")

# --- Koşullu comprehension ---
print("\n--- Koşullu ---")
sayilar = list(range(1, 21))

ciftler = [s for s in sayilar if s % 2 == 0]
print(f"Çift sayılar: {ciftler}")

buyuk_notlar = [n for n in [85, 42, 91, 67, 78, 55, 93] if n >= 70]
print(f"70+ notlar:   {buyuk_notlar}")

# --- if-else ile comprehension ---
print("\n--- if-else ---")
sonuclar = ["Geçti" if n >= 50 else "Kaldı" for n in [85, 42, 91, 37, 78]]
print(f"Sonuçlar: {sonuclar}")

# --- İç içe comprehension ---
print("\n--- İç İçe ---")
matris = [[i * j for j in range(1, 5)] for i in range(1, 4)]
print("Matris:")
for satir in matris:
    print(f"  {satir}")

# --- String işlemleri ile ---
print("\n--- String ile ---")
isimler = ["  Ayşe  ", "mehmet", "FATMA", "  ali "]
temiz_isimler = [isim.strip().title() for isim in isimler]
print(f"Temiz isimler: {temiz_isimler}")

# --- Performans notu ---
# List comprehension genellikle for döngüsünden daha hızlıdır
# Ama okunabilirliği korumak önemli — çok karmaşık comprehension'lardan kaçının


# ============================================================
# 4.5 — TUPLE YAPISI VE KULLANIMI
# ============================================================

print("\n\n=== Tuple ===\n")

# Tuple, listeye benzer ama DEĞİŞTİRİLEMEZ (immutable) bir veri yapısıdır.
# Parantez () ile oluşturulur.

# --- Tuple oluşturma ---
koordinat = (41.0082, 28.9784)     # İstanbul koordinatları
renkler = ("kırmızı", "yeşil", "mavi")
tek_elemanli = (42,)                # Tek elemanlı tuple: virgül şart!
bos_tuple = ()

print(f"koordinat:    {koordinat}")
print(f"renkler:      {renkler}")
print(f"tek_elemanli: {tek_elemanli}")
print(f"type:         {type(koordinat)}")

# DİKKAT: Parantez olmadan da tuple oluşturulabilir
degerler = 1, 2, 3
print(f"1, 2, 3:      {degerler} → {type(degerler)}")

# --- İndeksleme ve dilimleme (listeyle aynı) ---
print(f"\nrenkler[0]:    {renkler[0]}")
print(f"renkler[-1]:   {renkler[-1]}")
print(f"renkler[1:]:   {renkler[1:]}")

# --- Tuple DEĞİŞTİRİLEMEZ ---
# koordinat[0] = 40.0   # ← TypeError!
# Bu özellik güvenlik ve bütünlük sağlar

# --- Tuple unpacking (çözme) ---
print("\n--- Tuple Unpacking ---")
enlem, boylam = koordinat
print(f"Enlem: {enlem}, Boylam: {boylam}")

# Birden fazla değer döndüren fonksiyonlarda yaygın
# def bolme(a, b):
#     return a // b, a % b
# bolum, kalan = bolme(17, 5)

# Değişken değeri takas etme (Pythonic yol)
x, y = 10, 20
x, y = y, x     # Takas!
print(f"Takas sonrası: x={x}, y={y}")

# * ile kalan elemanları toplama
ilk, *ortalar, son = [1, 2, 3, 4, 5]
print(f"ilk={ilk}, ortalar={ortalar}, son={son}")

# --- Tuple metodları (sadece 2 tane) ---
print("\n--- Tuple Metodları ---")
notlar_tuple = (85, 92, 78, 92, 88, 72, 92)
print(f"count(92): {notlar_tuple.count(92)}")  # 3
print(f"index(88): {notlar_tuple.index(88)}")  # 4

# --- Named Tuple (bonus) ---
print("\n--- Named Tuple ---")
from collections import namedtuple

Ogrenci = namedtuple("Ogrenci", ["ad", "bolum", "not_ort"])
ogr1 = Ogrenci("Ayşe", "Biyoloji", 3.7)
print(f"Ad: {ogr1.ad}, Bölüm: {ogr1.bolum}, Ortalama: {ogr1.not_ort}")


# ============================================================
# 4.6 — LİSTE VS TUPLE KARŞILAŞTIRMA
# ============================================================

print("\n\n=== Liste vs Tuple ===\n")

print(f"{'Özellik':<25} {'Liste':>12} {'Tuple':>12}")
print("-" * 50)
print(f"{'Sözdizimi':<25} {'[1, 2, 3]':>12} {'(1, 2, 3)':>12}")
print(f"{'Değiştirilebilir':<25} {'Evet':>12} {'Hayır':>12}")
print(f"{'Hız':<25} {'Yavaş':>12} {'Hızlı':>12}")
print(f"{'Bellek':<25} {'Fazla':>12} {'Az':>12}")
print(f"{'Dict anahtarı':<25} {'Hayır':>12} {'Evet':>12}")

# Ne zaman hangisi?
# Liste → Değişecek koleksiyonlar (öğrenci listesi, ölçümler, yapılacaklar)
# Tuple → Sabit değerler (koordinat, RGB renk, veritabanı satırı, fonksiyon dönüşü)


# ============================================================
# 4.7 — UYGULAMALAR
# ============================================================

print("\n" + "=" * 50)
print("UYGULAMALAR")
print("=" * 50)

# ----- Uygulama 1: Öğrenci Not Sistemi -----
print("\n--- Uygulama 1: Öğrenci Not Sistemi ---")

ogrenci_notlari = [
    ("Ayşe", [85, 92, 78]),
    ("Mehmet", [70, 65, 80]),
    ("Fatma", [95, 88, 91]),
    ("Ali", [55, 62, 48]),
]

print(f"{'İsim':<10} {'Vize':>6} {'Final':>6} {'Ödev':>6} {'Ort':>8} {'Durum':>10}")
print("-" * 50)

for isim, notlar in ogrenci_notlari:
    ort = notlar[0] * 0.3 + notlar[1] * 0.4 + notlar[2] * 0.3
    durum = "Geçti" if ort >= 60 else "Kaldı"
    print(f"{isim:<10} {notlar[0]:>6} {notlar[1]:>6} {notlar[2]:>6} {ort:>8.1f} {durum:>10}")


# ----- Uygulama 2: Alışveriş Listesi -----
print("\n--- Uygulama 2: Alışveriş Listesi ---")

alisveris = [
    ("Pipet ucu (1000μL)", 3, 125.50),
    ("Eldiven (kutu)", 5, 85.00),
    ("Etanol (%96)", 2, 210.00),
    ("Petri kabı (paket)", 10, 45.75),
]

print(f"{'Ürün':<25} {'Adet':>5} {'Birim':>10} {'Toplam':>12}")
print("-" * 55)

genel_toplam = 0
for urun, adet, fiyat in alisveris:
    satir_toplam = adet * fiyat
    genel_toplam += satir_toplam
    print(f"{urun:<25} {adet:>5} {fiyat:>10.2f} {satir_toplam:>12.2f}")

print("-" * 55)
print(f"{'GENEL TOPLAM':<42} {genel_toplam:>12.2f} TL")


# ============================================================
# ALIŞTIRMALAR (Öğrenciler İçin)
# ============================================================
"""
Alıştırma 1: Bir sayı listesi alıp şunları döndüren fonksiyonlar yazın:
   - En büyük 3 elemanı (sıralı)
   - Ortalamanın üzerindeki elemanları
   - Çift ve tek sayıları ayrı listelere ayırma

Alıştırma 2: İki listeyi "zip" kullanmadan eşleştirip
   tuple listesi oluşturan program yazın.

Alıştırma 3: Bir matrisin (liste listesi) transpozunu alan
   (satır↔sütun değiştiren) program yazın.

Alıştırma 4: Verilen bir listeden tekrarlı elemanları kaldırıp
   orijinal sırayı koruyan program yazın.

Alıştırma 5: İki sıralı listeyi birleştirip sıralı tek bir liste
   oluşturan program yazın (merge sort mantığı).
"""
