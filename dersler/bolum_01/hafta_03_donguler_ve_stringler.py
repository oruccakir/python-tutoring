"""
============================================================
  BÖLÜM 1 — TEMEL KAVRAMLAR
  Hafta 3: Döngüler ve String İşlemleri
============================================================

İçindekiler:
  3.1  for döngüsü ve range()
  3.2  while döngüsü
  3.3  break, continue, pass
  3.4  İç içe döngüler
  3.5  String metodları
  3.6  String formatlama (f-string)
  3.7  String dilimleme (slicing)
  3.8  Uygulamalar
============================================================
"""

# ============================================================
# 3.1 — for DÖNGÜSÜ VE range()
# ============================================================

print("=== for Döngüsü ===\n")

# --- Temel for döngüsü ---
# Bir koleksiyon veya dizi üzerinde iterasyon yapar

# String üzerinde döngü
print("--- String üzerinde döngü ---")
for harf in "Python":
    print(harf, end=" ")
print()  # yeni satır

# Liste üzerinde döngü
print("\n--- Liste üzerinde döngü ---")
meyveler = ["elma", "armut", "muz", "çilek"]
for meyve in meyveler:
    print(f"  Meyve: {meyve}")

# --- range() fonksiyonu ---
print("\n--- range() fonksiyonu ---")

# range(n) → 0'dan n-1'e kadar
print("range(5):", end=" ")
for i in range(5):
    print(i, end=" ")    # 0 1 2 3 4
print()

# range(başlangıç, bitiş) → başlangıçtan bitiş-1'e kadar
print("range(2, 8):", end=" ")
for i in range(2, 8):
    print(i, end=" ")    # 2 3 4 5 6 7
print()

# range(başlangıç, bitiş, adım) → adım kadar atlayarak
print("range(0, 20, 3):", end=" ")
for i in range(0, 20, 3):
    print(i, end=" ")    # 0 3 6 9 12 15 18
print()

# Geriye doğru sayma
print("range(10, 0, -1):", end=" ")
for i in range(10, 0, -1):
    print(i, end=" ")    # 10 9 8 7 6 5 4 3 2 1
print()

# --- enumerate() — indeksle birlikte döngü ---
print("\n--- enumerate() ---")
gunler = ["Pazartesi", "Salı", "Çarşamba", "Perşembe", "Cuma"]
for indeks, gun in enumerate(gunler):
    print(f"  {indeks}: {gun}")

# Başlangıç indeksi belirleyerek
print("\n--- enumerate() başlangıç indeksi ---")
for sira, gun in enumerate(gunler, start=1):
    print(f"  {sira}. gün: {gun}")

# --- Toplam hesaplama ---
print("\n--- Toplam hesaplama ---")
toplam = 0
for i in range(1, 101):    # 1'den 100'e kadar
    toplam += i
print(f"1'den 100'e toplam: {toplam}")   # 5050


# ============================================================
# 3.2 — while DÖNGÜSÜ
# ============================================================

print("\n\n=== while Döngüsü ===\n")

# while: koşul True olduğu sürece çalışır

# --- Basit while ---
print("--- Basit sayaç ---")
sayac = 1
while sayac <= 5:
    print(f"  Sayaç: {sayac}")
    sayac += 1      # Bu satır olmazsa sonsuz döngü!

# --- while ile toplam ---
print("\n--- Tek sayıların toplamı (1-20) ---")
toplam = 0
sayi = 1
while sayi <= 20:
    if sayi % 2 == 1:   # tek sayı kontrolü
        toplam += sayi
    sayi += 1
print(f"Toplam: {toplam}")   # 100

# --- while ile yakınsama (araştırmada sık kullanılır) ---
print("\n--- Newton-Raphson ile √2 hesaplama ---")
tahmin = 1.0
hedef = 2
tolerans = 1e-10
iterasyon = 0

while abs(tahmin * tahmin - hedef) > tolerans:
    tahmin = (tahmin + hedef / tahmin) / 2
    iterasyon += 1

print(f"√2 ≈ {tahmin:.15f}")
print(f"İterasyon sayısı: {iterasyon}")

# --- while True ve break ---
print("\n--- while True ile menü simülasyonu ---")
komutlar = ["hesapla", "göster", "çıkış"]  # input() yerine simülasyon
for komut in komutlar:
    if komut == "çıkış":
        print("  Program sonlandırılıyor...")
        break
    print(f"  Komut çalıştırıldı: {komut}")

# --- for vs while: Ne zaman hangisini kullanmalı? ---
# for  → kaç kez döneceğini biliyorsan (liste, range, dosya satırları)
# while → koşula bağlı döngüler (kullanıcı girişi, yakınsama, dosya okuma)


# ============================================================
# 3.3 — break, continue, pass
# ============================================================

print("\n\n=== break, continue, pass ===\n")

# --- break: döngüyü tamamen sonlandırır ---
print("--- break ---")
for i in range(1, 11):
    if i == 6:
        print(f"  {i} bulundu, döngü durduruluyor!")
        break
    print(f"  i = {i}")

# --- continue: mevcut iterasyonu atlar, sonrakine geçer ---
print("\n--- continue ---")
print("Tek sayılar:", end=" ")
for i in range(1, 11):
    if i % 2 == 0:      # çift sayıları atla
        continue
    print(i, end=" ")   # 1 3 5 7 9
print()

# --- pass: hiçbir şey yapma (yer tutucu) ---
print("\n--- pass ---")
for i in range(5):
    if i == 3:
        pass    # TODO: bu durum için özel işlem yapılacak
    else:
        print(f"  i = {i}")

# --- for-else: döngü break olmadan biterse else çalışır ---
print("\n--- for-else ---")
aranan = 7
sayilar = [2, 4, 6, 8, 10]

for s in sayilar:
    if s == aranan:
        print(f"{aranan} bulundu!")
        break
else:
    print(f"{aranan} listede bulunamadı.")


# ============================================================
# 3.4 — İÇ İÇE DÖNGÜLER
# ============================================================

print("\n\n=== İç İçe Döngüler ===\n")

# --- Çarpım tablosu ---
print("--- Çarpım Tablosu (1-5) ---")
for i in range(1, 6):
    for j in range(1, 6):
        print(f"{i*j:4}", end="")
    print()

# --- Desen oluşturma ---
print("\n--- Üçgen desen ---")
for i in range(1, 6):
    print("* " * i)

# --- Araştırma örneği: parametre tarama ---
print("\n--- Parametre Tarama (Grid Search benzeri) ---")
ogrenme_oranlari = [0.01, 0.05, 0.1]
batch_boyutlari = [16, 32, 64]

print(f"{'LR':>6} | {'Batch':>5} | {'Kombinasyon':>15}")
print("-" * 35)
for lr in ogrenme_oranlari:
    for batch in batch_boyutlari:
        print(f"{lr:>6} | {batch:>5} | lr={lr}, batch={batch}")


# ============================================================
# 3.5 — STRING METODLARI
# ============================================================

print("\n\n=== String Metodları ===\n")

metin = "  Merhaba Dünya! Python Öğreniyoruz.  "
print(f"Orijinal: '{metin}'")

# --- Büyük/küçük harf ---
print(f"\n--- Büyük/Küçük Harf ---")
print(f"upper():      '{metin.upper()}'")
print(f"lower():      '{metin.lower()}'")
print(f"title():      '{'merhaba dünya'.title()}'")
print(f"capitalize(): '{'merhaba dünya'.capitalize()}'")
print(f"swapcase():   '{'Merhaba'.swapcase()}'")

# --- Boşluk temizleme ---
print(f"\n--- Boşluk Temizleme ---")
print(f"strip():  '{metin.strip()}'")
print(f"lstrip(): '{metin.lstrip()}'")
print(f"rstrip(): '{metin.rstrip()}'")

# --- Arama ve kontrol ---
print(f"\n--- Arama ve Kontrol ---")
cumle = "Python programlama dili çok güçlüdür"
print(f"Metin: '{cumle}'")
print(f"find('dili'):     {cumle.find('dili')}")         # 23 (indeks)
print(f"find('Java'):     {cumle.find('Java')}")         # -1 (bulunamadı)
print(f"count('o'):       {cumle.count('o')}")           # 2
print(f"startswith('Py'): {cumle.startswith('Py')}")     # True
print(f"endswith('dür'):  {cumle.endswith('dür')}")      # True
print(f"'dili' in cumle:  {'dili' in cumle}")            # True

# --- Değiştirme ---
print(f"\n--- Değiştirme ---")
print(f"replace: '{cumle.replace('Python', 'Java')}'")

# --- Bölme ve birleştirme ---
print(f"\n--- Bölme (split) ve Birleştirme (join) ---")
csv_satir = "Ahmet,25,İstanbul,Doktora"
parcalar = csv_satir.split(",")
print(f"split(','):  {parcalar}")        # ['Ahmet', '25', 'İstanbul', 'Doktora']

kelimeler = cumle.split()
print(f"split():     {kelimeler}")       # boşlukla böler

# join — split'in tersi
birlesik = " - ".join(parcalar)
print(f"join(' - '): '{birlesik}'")      # Ahmet - 25 - İstanbul - Doktora

# --- Kontrol metodları ---
print(f"\n--- Kontrol Metodları ---")
print(f"'12345'.isdigit():    {'12345'.isdigit()}")       # True
print(f"'abc'.isalpha():      {'abc'.isalpha()}")         # True
print(f"'abc123'.isalnum():   {'abc123'.isalnum()}")      # True
print(f"'   '.isspace():      {'   '.isspace()}")         # True
print(f"'Hello'.istitle():    {'Hello'.istitle()}")       # True

# --- len() — string uzunluğu ---
print(f"\nlen('{cumle}'): {len(cumle)}")


# ============================================================
# 3.6 — STRING FORMATLAMA (f-string)
# ============================================================

print("\n\n=== String Formatlama ===\n")

isim = "Ayşe"
yas = 28
boy = 1.68

# --- Yöntem 1: String birleştirme (eski ve kötü yol) ---
print("1. Birleştirme: " + isim + " " + str(yas) + " yaşında")

# --- Yöntem 2: % operatörü (eski Python) ---
print("2. %% operatörü: %s %d yaşında" % (isim, yas))

# --- Yöntem 3: .format() metodu ---
print("3. format(): {} {} yaşında".format(isim, yas))

# --- Yöntem 4: f-string (Python 3.6+ — ÖNERİLEN) ---
print(f"4. f-string: {isim} {yas} yaşında")

# --- f-string formatlama seçenekleri ---
print("\n--- Sayı Formatlama ---")
pi = 3.14159265358979

print(f"Varsayılan:    {pi}")
print(f"2 ondalık:     {pi:.2f}")       # 3.14
print(f"4 ondalık:     {pi:.4f}")       # 3.1416
print(f"Bilimsel:      {pi:.2e}")       # 3.14e+00
print(f"Yüzde:         {0.856:.1%}")    # 85.6%

# Büyük sayılar
buyuk = 1234567890
print(f"\nBinlik ayırıcı: {buyuk:,}")          # 1,234,567,890
print(f"Binlik (nokta): {buyuk:_}")            # 1_234_567_890

# --- Hizalama ---
print("\n--- Hizalama ---")
print(f"{'Sol':<20}|")       # Sola hizala (20 karakter)
print(f"{'Orta':^20}|")     # Ortala
print(f"{'Sağ':>20}|")      # Sağa hizala

# Tablo oluşturma
print("\n--- Tablo ---")
baslik = f"{'Denek':>8} | {'Ölçüm 1':>10} | {'Ölçüm 2':>10} | {'Ortalama':>10}"
print(baslik)
print("-" * len(baslik))

denekler = [("D001", 23.5, 24.1), ("D002", 19.8, 20.3), ("D003", 31.2, 30.8)]
for denek, o1, o2 in denekler:
    ort = (o1 + o2) / 2
    print(f"{denek:>8} | {o1:>10.2f} | {o2:>10.2f} | {ort:>10.2f}")

# --- f-string içinde ifade kullanma ---
print(f"\n2 + 3 = {2 + 3}")
print(f"{'merhaba'.upper()}")
print(f"{'Çift' if 10 % 2 == 0 else 'Tek'}")


# ============================================================
# 3.7 — STRING DİLİMLEME (SLICING)
# ============================================================

print("\n\n=== String Dilimleme (Slicing) ===\n")

metin = "Python Programlama"
#        0123456789...
# İndeksler: P=0, y=1, t=2, h=3, o=4, n=5, ' '=6, P=7 ...

print(f"Metin: '{metin}'")
print(f"Uzunluk: {len(metin)}")

# --- İndeksleme (tek karakter) ---
print(f"\n--- İndeksleme ---")
print(f"metin[0]  = '{metin[0]}'")      # P (ilk karakter)
print(f"metin[7]  = '{metin[7]}'")      # P
print(f"metin[-1] = '{metin[-1]}'")     # a (son karakter)
print(f"metin[-2] = '{metin[-2]}'")     # m (sondan ikinci)

# --- Dilimleme [başlangıç:bitiş] ---
print(f"\n--- Dilimleme ---")
print(f"metin[0:6]   = '{metin[0:6]}'")     # Python
print(f"metin[7:]    = '{metin[7:]}'")       # Programlama
print(f"metin[:6]    = '{metin[:6]}'")       # Python (0'dan 6'ya)
print(f"metin[-9:]   = '{metin[-9:]}'")      # rogramlama
print(f"metin[:]     = '{metin[:]}'")        # Python Programlama (kopya)

# --- Adımlı dilimleme [başlangıç:bitiş:adım] ---
print(f"\n--- Adımlı Dilimleme ---")
print(f"metin[::2]   = '{metin[::2]}'")     # Pto rgalm (her 2. karakter)
print(f"metin[::-1]  = '{metin[::-1]}'")    # Ters çevir

# --- String'ler değiştirilemez (immutable) ---
# metin[0] = "J"   # ← Bu HATA verir! TypeError
# Bunun yerine yeni string oluşturulur:
yeni_metin = "J" + metin[1:]
print(f"\nDeğiştirme:   '{yeni_metin}'")   # Jython Programlama

# --- Pratik örnekler ---
print(f"\n--- Pratik Örnekler ---")

dosya_adi = "deney_sonuclari_2024.csv"
uzanti = dosya_adi.split(".")[-1]
isim = dosya_adi.split(".")[0]
print(f"Dosya: {dosya_adi}")
print(f"İsim: {isim}, Uzantı: {uzanti}")

# TC Kimlik numarası maskeleme
tc = "12345678901"
maskeli = tc[:3] + "*****" + tc[-3:]
print(f"TC: {maskeli}")         # 123*****901

# E-posta domain çıkarma
email = "ahmet@university.edu.tr"
domain = email.split("@")[1]
print(f"Domain: {domain}")      # university.edu.tr


# ============================================================
# 3.8 — UYGULAMALAR
# ============================================================

print("\n" + "=" * 50)
print("UYGULAMALAR")
print("=" * 50)

# ----- Uygulama 1: Sayı Tahmin Oyunu -----
print("\n--- Uygulama 1: Sayı Tahmin Oyunu (Simülasyon) ---")

# Gerçek oyunda random modülü ve input() kullanılır
# Burada mantığı göstermek için simülasyon yapıyoruz
gizli_sayi = 42
tahminler = [20, 50, 40, 45, 42]
max_deneme = 10
deneme = 0

for tahmin in tahminler:
    deneme += 1
    if tahmin == gizli_sayi:
        print(f"  Tahmin {deneme}: {tahmin} → Doğru! {deneme} denemede buldunuz!")
        break
    elif tahmin < gizli_sayi:
        print(f"  Tahmin {deneme}: {tahmin} → Daha büyük!")
    else:
        print(f"  Tahmin {deneme}: {tahmin} → Daha küçük!")
else:
    print(f"  {max_deneme} denemede bulamadınız. Sayı: {gizli_sayi}")


# ----- Uygulama 2: Palindrom Kontrolü -----
print("\n--- Uygulama 2: Palindrom Kontrolü ---")

def palindrom_kontrol(metin):
    """Bir metnin palindrom olup olmadığını kontrol eder."""
    temiz = metin.lower().replace(" ", "")
    return temiz == temiz[::-1]

test_kelimeleri = ["kayak", "Aba", "python", "Ana", "madam"]
for kelime in test_kelimeleri:
    sonuc = "palindrom" if palindrom_kontrol(kelime) else "palindrom değil"
    print(f"  '{kelime}' → {sonuc}")


# ----- Uygulama 3: Kelime İstatistikleri -----
print("\n--- Uygulama 3: Metin İstatistikleri ---")

metin = """Python programlama dili araştırmacılar için vazgeçilmez bir araçtır.
Python ile veri analizi yapabilir, grafikler oluşturabilir ve
makine öğrenmesi modelleri geliştirebilirsiniz. Python topluluğu
dünya genelinde çok aktiftir."""

kelimeler = metin.split()
satirlar = metin.strip().split("\n")
karakterler = len(metin)
benzersiz_kelimeler = set(kelimeler)  # set ile tekrarları kaldır

print(f"Karakter sayısı:           {karakterler}")
print(f"Kelime sayısı:             {len(kelimeler)}")
print(f"Benzersiz kelime sayısı:   {len(benzersiz_kelimeler)}")
print(f"Satır sayısı:              {len(satirlar)}")
print(f"Ortalama kelime/satır:     {len(kelimeler)/len(satirlar):.1f}")

# Python kelimesinin geçme sayısı
python_sayisi = metin.lower().count("python")
print(f"'Python' geçme sayısı:     {python_sayisi}")


# ----- Uygulama 4: Basit Şifreleme (Caesar Cipher) -----
print("\n--- Uygulama 4: Caesar Şifreleme ---")

def caesar_sifrele(metin, kayma):
    """Caesar şifreleme — her harfi kayma kadar kaydırır."""
    sonuc = ""
    for karakter in metin:
        if karakter.isalpha():
            # ASCII değerini kullan
            baz = ord('A') if karakter.isupper() else ord('a')
            yeni = chr((ord(karakter) - baz + kayma) % 26 + baz)
            sonuc += yeni
        else:
            sonuc += karakter   # harf değilse aynen bırak
    return sonuc

orijinal = "Hello World"
kayma = 3
sifreli = caesar_sifrele(orijinal, kayma)
cozulmus = caesar_sifrele(sifreli, -kayma)

print(f"Orijinal:  {orijinal}")
print(f"Şifreli:   {sifreli}")
print(f"Çözülmüş:  {cozulmus}")


# ----- Uygulama 5: Araştırma Verisi Formatı Dönüştürme -----
print("\n--- Uygulama 5: CSV Satır İşleme ---")

csv_verisi = """isim,yas,bolum,puan
Ayşe Yılmaz,28,Biyoloji,92.5
Mehmet Kaya,31,Fizik,88.3
Fatma Demir,26,Kimya,95.1
Ali Çelik,29,Matematik,79.8"""

satirlar = csv_verisi.strip().split("\n")
baslik = satirlar[0].split(",")

print(f"{'Sıra':>4} | ", end="")
for b in baslik:
    print(f"{b:>12}", end=" | ")
print()
print("-" * 65)

for i, satir in enumerate(satirlar[1:], start=1):
    degerler = satir.split(",")
    isim = degerler[0]
    yas = degerler[1]
    bolum = degerler[2]
    puan = float(degerler[3])

    durum = "Basarili" if puan >= 80 else "Destek"
    print(f"{i:>4} | {isim:>12} | {yas:>12} | {bolum:>12} | {puan:>12.1f} | {durum}")


# ----- Uygulama 6: FizzBuzz (Klasik Programlama Problemi) -----
print("\n--- Uygulama 6: FizzBuzz ---")
# 1-30 arası: 3'e bölünenlere Fizz, 5'e bölünenlere Buzz,
# ikisine de bölünenlere FizzBuzz yaz

for i in range(1, 31):
    if i % 15 == 0:
        print("FizzBuzz", end=" ")
    elif i % 3 == 0:
        print("Fizz", end=" ")
    elif i % 5 == 0:
        print("Buzz", end=" ")
    else:
        print(i, end=" ")
print()


# ============================================================
# ALIŞTIRMALAR (Öğrenciler İçin)
# ============================================================
"""
Alıştırma 1: 1'den N'e kadar olan sayıların toplamını ve ortalamasını
   hesaplayan program yazın (N kullanıcıdan alınır).

Alıştırma 2: Kullanıcıdan bir cümle alıp:
   - Kelime sayısını
   - En uzun kelimeyi
   - Ünlü harf sayısını
   - Cümlenin tersini yazdırın.

Alıştırma 3: Kullanıcıdan bir sayı alıp asal olup olmadığını
   kontrol eden program yazın.

Alıştırma 4: Fibonacci serisinin ilk N elemanını yazdıran
   program yazın (0, 1, 1, 2, 3, 5, 8, 13, ...).

Alıştırma 5: Kullanıcıdan bir metin ve aranacak kelime alıp:
   - Kelimenin metinde kaç kez geçtiğini
   - İlk ve son geçtiği indeksi
   - Kelimeyi başka bir kelimeyle değiştirilmiş halini yazdırın.

Alıştırma 6: Bir DNA dizisi (string) verildiğinde:
   - Her nükleotidin (A, T, G, C) sayısını ve yüzdesini hesaplayın
   - Tamamlayıcı dizisini oluşturun (A↔T, G↔C)
   Örnek: "ATCGGCTAA" → Tamamlayıcı: "TAGCCGATT"

Alıştırma 7: Kullanıcıdan alınan metni "başlık formatına" (Title Case)
   çevirin, AMA "ve", "ile", "için", "bir" gibi edatları
   küçük harf bırakın (ilk kelime hariç).
   Örnek: "python ile veri analizi için rehber"
        → "Python ile Veri Analizi için Rehber"
"""
