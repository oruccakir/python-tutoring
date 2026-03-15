"""
============================================================
  BÖLÜM 2 — VERİ YAPILARI VE FONKSİYONLAR
  Hafta 5: Sözlükler, Kümeler ve Fonksiyonlar
============================================================

İçindekiler:
  5.1  Dictionary (Sözlük) oluşturma ve erişim
  5.2  Dictionary metodları
  5.3  Dictionary comprehension
  5.4  Set (Küme) yapısı ve küme işlemleri
  5.5  Fonksiyon tanımlama, parametreler, return
  5.6  *args, **kwargs, varsayılan parametreler
  5.7  Lambda fonksiyonları ve yerleşik fonksiyonlar
  5.8  Uygulamalar
============================================================
"""

# ============================================================
# 5.1 — DICTIONARY (SÖZLÜK) OLUŞTURMA VE ERİŞİM
# ============================================================

print("=== Dictionary (Sözlük) ===\n")

# Sözlük, anahtar-değer (key-value) çiftlerinden oluşan veri yapısıdır.
# Sıralıdır (Python 3.7+), değiştirilebilir, anahtarlar benzersiz olmalıdır.

# --- Oluşturma ---
bos_sozluk = {}
bos_sozluk2 = dict()

ogrenci = {
    "ad": "Ayşe",
    "soyad": "Yılmaz",
    "yas": 28,
    "bolum": "Biyoloji",
    "doktora_yili": 3,
    "notlar": [85, 92, 78],
}

print(f"ogrenci: {ogrenci}")
print(f"Tip: {type(ogrenci)}")

# --- Erişim ---
print(f"\n--- Erişim ---")
print(f"ogrenci['ad']:     {ogrenci['ad']}")
print(f"ogrenci['bolum']:  {ogrenci['bolum']}")

# get() — anahtar yoksa hata vermez, None döndürür
print(f"get('yas'):        {ogrenci.get('yas')}")
print(f"get('email'):      {ogrenci.get('email')}")           # None
print(f"get('email','yok'):{ogrenci.get('email', 'yok')}")    # varsayılan değer

# DİKKAT: Olmayan anahtara [] ile erişim → KeyError!
# ogrenci['email']  ← KeyError!

# --- Ekleme ve güncelleme ---
print(f"\n--- Ekleme/Güncelleme ---")
ogrenci["email"] = "ayse@uni.edu.tr"   # Yeni anahtar ekle
ogrenci["yas"] = 29                     # Mevcut değeri güncelle
print(f"Güncel: {ogrenci}")

# --- Silme ---
print(f"\n--- Silme ---")
silinen = ogrenci.pop("doktora_yili")
print(f"pop('doktora_yili'): {silinen}")
print(f"Kalan anahtarlar: {list(ogrenci.keys())}")

# del ile silme
del ogrenci["email"]

# --- Üyelik kontrolü (anahtarlarda arar) ---
print(f"\n'ad' in ogrenci:    {'ad' in ogrenci}")       # True
print(f"'email' in ogrenci: {'email' in ogrenci}")      # False

# --- Döngü ile gezme ---
print("\n--- Döngü ---")
kisi = {"ad": "Mehmet", "yas": 35, "sehir": "Ankara"}

# Anahtarlar
print("Anahtarlar:")
for anahtar in kisi:
    print(f"  {anahtar}")

# Değerler
print("Değerler:")
for deger in kisi.values():
    print(f"  {deger}")

# Anahtar-değer çiftleri
print("Çiftler:")
for anahtar, deger in kisi.items():
    print(f"  {anahtar}: {deger}")


# ============================================================
# 5.2 — DICTIONARY METODLARI
# ============================================================

print("\n\n=== Dictionary Metodları ===\n")

stok = {"pipet": 50, "eldiven": 200, "tüp": 150}

# keys(), values(), items()
print(f"keys():   {list(stok.keys())}")
print(f"values(): {list(stok.values())}")
print(f"items():  {list(stok.items())}")

# update() — birleştirme
stok.update({"eldiven": 180, "maske": 100})
print(f"\nupdate(): {stok}")

# setdefault() — yoksa ekle, varsa dokunma
stok.setdefault("pipet", 999)   # pipet zaten var → değişmez
stok.setdefault("baget", 30)    # baget yok → eklenir
print(f"setdefault(): {stok}")

# copy()
stok_kopya = stok.copy()

# Tüm değerlerin toplamı
print(f"\nToplam stok: {sum(stok.values())}")


# ============================================================
# 5.3 — DICTIONARY COMPREHENSION
# ============================================================

print("\n\n=== Dictionary Comprehension ===\n")

# {anahtar: deger for eleman in koleksiyon}

# Kareleri sözlük olarak
kareler = {x: x**2 for x in range(1, 11)}
print(f"Kareler: {kareler}")

# Koşullu
cift_kareler = {x: x**2 for x in range(1, 11) if x % 2 == 0}
print(f"Çift kareler: {cift_kareler}")

# İki listeden sözlük
ogrenciler = ["Ayşe", "Mehmet", "Fatma"]
puanlar = [85, 72, 91]
not_sozluk = {ogr: puan for ogr, puan in zip(ogrenciler, puanlar)}
print(f"Not sözlüğü: {not_sozluk}")

# Kelime uzunlukları
kelimeler = ["Python", "veri", "bilimi", "araştırma"]
uzunluklar = {k: len(k) for k in kelimeler}
print(f"Uzunluklar: {uzunluklar}")


# ============================================================
# 5.4 — SET (KÜME) YAPISI VE KÜME İŞLEMLERİ
# ============================================================

print("\n\n=== Set (Küme) ===\n")

# Set, benzersiz (tekrarsız) elemanlardan oluşan, sırasız bir koleksiyondur.
# Matematikteki küme kavramına karşılık gelir.

# --- Oluşturma ---
meyveler = {"elma", "armut", "muz", "elma", "çilek", "muz"}
print(f"meyveler: {meyveler}")  # tekrarlar otomatik kaldırılır

sayilar = set([1, 2, 2, 3, 3, 3, 4])
print(f"sayilar:  {sayilar}")   # {1, 2, 3, 4}

bos_set = set()  # DİKKAT: {} boş sözlük oluşturur, set değil!

# Listeden tekrarları kaldırma
tekrarli = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
benzersiz = list(set(tekrarli))
print(f"\nTekrarlı:  {tekrarli}")
print(f"Benzersiz: {benzersiz}")

# --- Eleman ekleme/çıkarma ---
print("\n--- Eleman İşlemleri ---")
renkler = {"kırmızı", "yeşil", "mavi"}
renkler.add("sarı")
print(f"add('sarı'):    {renkler}")

renkler.discard("yeşil")     # Yoksa hata vermez
print(f"discard('yeşil'): {renkler}")

# renkler.remove("mor")       # Yoksa KeyError!

# --- Küme işlemleri ---
print("\n--- Küme İşlemleri ---")
A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}

print(f"A = {A}")
print(f"B = {B}")
print(f"A | B  (birleşim):  {A | B}")            # {1,2,3,4,5,6,7,8}
print(f"A & B  (kesişim):   {A & B}")             # {4, 5}
print(f"A - B  (fark):      {A - B}")             # {1, 2, 3}
print(f"B - A  (fark):      {B - A}")             # {6, 7, 8}
print(f"A ^ B  (sym. fark): {A ^ B}")             # {1,2,3,6,7,8}

# Alt küme kontrolü
print(f"\n{{1,2}} <= A (alt küme):  { {1,2} <= A}")   # True
print(f"A >= {{1,2}} (üst küme):   {A >= {1,2}}")     # True

# --- Frozen set (değiştirilemez küme) ---
sabit = frozenset([1, 2, 3])
# sabit.add(4)  # ← Hata! Değiştirilemez


# ============================================================
# 5.5 — FONKSİYON TANIMLAMA, PARAMETRELER, RETURN
# ============================================================

print("\n\n=== Fonksiyonlar ===\n")

# Fonksiyon: Belirli bir görevi yerine getiren, tekrar kullanılabilir kod bloğu.
# def anahtar kelimesi ile tanımlanır.

# --- Basit fonksiyon ---
def selamla():
    print("Merhaba! Fonksiyon çalıştı.")

selamla()

# --- Parametreli fonksiyon ---
def selamla_kisi(isim):
    print(f"Merhaba, {isim}!")

selamla_kisi("Ayşe")

# --- return ile değer döndürme ---
def kare_al(sayi):
    return sayi ** 2

sonuc = kare_al(7)
print(f"\nkare_al(7) = {sonuc}")

# --- Birden fazla değer döndürme ---
def istatistik(sayilar):
    toplam = sum(sayilar)
    ortalama = toplam / len(sayilar)
    en_buyuk = max(sayilar)
    en_kucuk = min(sayilar)
    return toplam, ortalama, en_buyuk, en_kucuk

t, ort, mx, mn = istatistik([10, 20, 30, 40, 50])
print(f"\nToplam={t}, Ortalama={ort}, Max={mx}, Min={mn}")

# --- Varsayılan parametreler ---
print("\n--- Varsayılan Parametreler ---")

def guc(taban, us=2):
    """Bir sayının üssünü hesaplar. Varsayılan üs: 2 (kare)."""
    return taban ** us

print(f"guc(5)    = {guc(5)}")      # 25 (5²)
print(f"guc(5, 3) = {guc(5, 3)}")   # 125 (5³)

# --- Keyword (isimli) argümanlar ---
print("\n--- Keyword Argümanlar ---")

def ogrenci_bilgi(ad, bolum, yil=1):
    print(f"  {ad} — {bolum}, {yil}. yıl")

ogrenci_bilgi("Ayşe", "Biyoloji", 3)
ogrenci_bilgi(bolum="Fizik", ad="Mehmet")      # sıra farketmez
ogrenci_bilgi("Fatma", yil=2, bolum="Kimya")


# ============================================================
# 5.6 — *args, **kwargs
# ============================================================

print("\n\n=== *args ve **kwargs ===\n")

# --- *args: değişken sayıda pozisyonel argüman ---
def toplam_hesapla(*sayilar):
    """İstenen sayıda argüman alıp toplar."""
    print(f"  Gelen argümanlar: {sayilar} (tip: {type(sayilar).__name__})")
    return sum(sayilar)

print(f"toplam(1,2,3):   {toplam_hesapla(1, 2, 3)}")
print(f"toplam(10,20):   {toplam_hesapla(10, 20)}")

# --- **kwargs: değişken sayıda isimli argüman ---
def deney_kaydi(**bilgiler):
    """İstenen sayıda isimli argüman alır."""
    print("  Deney Kaydı:")
    for anahtar, deger in bilgiler.items():
        print(f"    {anahtar}: {deger}")

print()
deney_kaydi(tarih="2024-03-15", denek_sayisi=30, sicaklik=22.5)

# --- *args ve **kwargs birlikte ---
def esnek_fonksiyon(zorunlu, *args, **kwargs):
    print(f"\n  zorunlu: {zorunlu}")
    print(f"  args:    {args}")
    print(f"  kwargs:  {kwargs}")

esnek_fonksiyon("test", 1, 2, 3, renk="mavi", boyut=10)


# ============================================================
# 5.7 — LAMBDA VE YERLEŞİK FONKSİYONLAR
# ============================================================

print("\n\n=== Lambda ve Yerleşik Fonksiyonlar ===\n")

# --- Lambda: tek satırlık anonim fonksiyon ---
kare = lambda x: x ** 2
print(f"lambda kare(5): {kare(5)}")

toplam = lambda a, b: a + b
print(f"lambda toplam(3,4): {toplam(3, 4)}")

# --- sorted() ile lambda ---
print("\n--- sorted() + lambda ---")
ogrenciler = [("Ayşe", 85), ("Mehmet", 72), ("Fatma", 91), ("Ali", 68)]

# Puana göre sıralama
puana_gore = sorted(ogrenciler, key=lambda x: x[1])
print(f"Puana göre (artan):  {puana_gore}")

puana_gore_azalan = sorted(ogrenciler, key=lambda x: x[1], reverse=True)
print(f"Puana göre (azalan): {puana_gore_azalan}")

# --- map(): her elemana fonksiyon uygula ---
print("\n--- map() ---")
sayilar = [1, 2, 3, 4, 5]
kareler = list(map(lambda x: x**2, sayilar))
print(f"Kareler: {kareler}")

sicaklik_c = [0, 20, 37, 100]
sicaklik_f = list(map(lambda c: c * 9/5 + 32, sicaklik_c))
print(f"°C → °F: {sicaklik_f}")

# --- filter(): koşula uyan elemanları filtrele ---
print("\n--- filter() ---")
sayilar = list(range(1, 21))
ciftler = list(filter(lambda x: x % 2 == 0, sayilar))
print(f"Çift sayılar: {ciftler}")

# --- zip(): listeleri eşleştir ---
print("\n--- zip() ---")
isimler = ["Ayşe", "Mehmet", "Fatma"]
yaslar = [28, 35, 26]
sehirler = ["İstanbul", "Ankara", "İzmir"]

for isim, yas, sehir in zip(isimler, yaslar, sehirler):
    print(f"  {isim}, {yas} yaş, {sehir}")

# --- enumerate(): indeksli döngü ---
print("\n--- enumerate() ---")
for i, isim in enumerate(isimler, start=1):
    print(f"  {i}. {isim}")


# ============================================================
# 5.8 — UYGULAMALAR
# ============================================================

print("\n" + "=" * 50)
print("UYGULAMALAR")
print("=" * 50)

# ----- Uygulama 1: Kelime Frekansı Analizi -----
print("\n--- Uygulama 1: Kelime Frekansı ---")

metin = "python veri bilimi python analiz python veri görselleştirme veri bilimi"
kelimeler = metin.split()

frekans = {}
for kelime in kelimeler:
    frekans[kelime] = frekans.get(kelime, 0) + 1

sirali = sorted(frekans.items(), key=lambda x: x[1], reverse=True)
for kelime, sayi in sirali:
    bar = "█" * (sayi * 3)
    print(f"  {kelime:<20} {bar} ({sayi})")


# ----- Uygulama 2: Telefon Rehberi -----
print("\n--- Uygulama 2: Telefon Rehberi ---")

rehber = {}

def rehbere_ekle(isim, numara):
    rehber[isim] = numara
    print(f"  Eklendi: {isim} → {numara}")

def rehberde_ara(isim):
    sonuc = rehber.get(isim, "Bulunamadı")
    print(f"  Arama '{isim}': {sonuc}")

rehbere_ekle("Dr. Yılmaz", "0532-111-2233")
rehbere_ekle("Lab Asistanı", "0555-444-5566")
rehbere_ekle("Kütüphane", "0212-555-0001")

rehberde_ara("Dr. Yılmaz")
rehberde_ara("Dekan")

print(f"\n  Rehber ({len(rehber)} kişi):")
for isim, numara in sorted(rehber.items()):
    print(f"    {isim}: {numara}")


# ============================================================
# ALIŞTIRMALAR (Öğrenciler İçin)
# ============================================================
"""
Alıştırma 1: Bir metin alıp her karakterin frekansını hesaplayan
   fonksiyon yazın. Sonucu frekansa göre sıralı sözlük olarak döndürün.

Alıştırma 2: İki sözlüğü birleştiren (ortak anahtarlarda değerleri
   toplayan) bir fonksiyon yazın.

Alıştırma 3: Bir öğrenci veritabanı (sözlük listesi) üzerinde:
   - Belirli bir bölümdeki öğrencileri filtreleyen
   - Not ortalamasına göre sıralayan
   - İstatistik özetini çıkaran fonksiyonlar yazın.

Alıştırma 4: Küme işlemleri ile:
   - İki dersi aynı anda alan öğrencileri bulun (kesişim)
   - En az bir dersi alan öğrencileri bulun (birleşim)
   - Sadece bir dersi alan öğrencileri bulun (simetrik fark)

Alıştırma 5: Parametre olarak fonksiyon alan bir fonksiyon yazın.
   Örnek: apply_to_list(liste, fonksiyon) — listedeki her elemana
   verilen fonksiyonu uygulasın.
"""
