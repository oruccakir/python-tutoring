"""
============================================================
  BÖLÜM 1 — TEMEL KAVRAMLAR
  Hafta 2: Operatörler ve Koşullu İfadeler
============================================================

İçindekiler:
  2.1  Aritmetik operatörler
  2.2  Karşılaştırma operatörleri
  2.3  Mantıksal operatörler
  2.4  Atama operatörleri
  2.5  if, elif, else yapıları
  2.6  İç içe koşullar ve ternary operatör
  2.7  match-case (Python 3.10+)
  2.8  Uygulamalar
============================================================
"""

# ============================================================
# 2.1 — ARİTMETİK OPERATÖRLER
# ============================================================

print("=== Aritmetik Operatörler ===\n")

a = 17
b = 5

# Temel operatörler
print(f"{a} + {b}  = {a + b}")      # Toplama        → 22
print(f"{a} - {b}  = {a - b}")      # Çıkarma        → 12
print(f"{a} * {b}  = {a * b}")      # Çarpma         → 85
print(f"{a} / {b}  = {a / b}")      # Bölme (float)  → 3.4
print(f"{a} // {b} = {a // b}")     # Tam bölme      → 3
print(f"{a} % {b}  = {a % b}")      # Mod (kalan)    → 2
print(f"{a} ** {b} = {a ** b}")     # Üs alma        → 1419857

# İşlem önceliği (matematik kuralları geçerli):
# 1. Parantez ()
# 2. Üs alma **
# 3. Çarpma/Bölme *, /, //, %
# 4. Toplama/Çıkarma +, -

sonuc = 2 + 3 * 4       # 14 (3*4=12, 12+2=14)
sonuc2 = (2 + 3) * 4    # 20 (2+3=5, 5*4=20)
print(f"\n2 + 3 * 4   = {sonuc}")
print(f"(2 + 3) * 4 = {sonuc2}")

# Araştırmada sık kullanılan hesaplamalar
print("\n--- Araştırma Örneği: Yüzde Hesaplama ---")
toplam_denek = 120
basarili = 87
basari_orani = (basarili / toplam_denek) * 100
print(f"Başarı oranı: {basari_orani:.1f}%")    # 72.5%

# Mod operatörü kullanım alanları
print("\n--- Mod Operatörü Kullanımları ---")
sayi = 24
print(f"{sayi} çift mi? {sayi % 2 == 0}")        # True
print(f"{sayi}, 3'e bölünür mü? {sayi % 3 == 0}")  # True


# ============================================================
# 2.2 — KARŞILAŞTIRMA OPERATÖRLERİ
# ============================================================

print("\n\n=== Karşılaştırma Operatörleri ===\n")

x = 10
y = 20

# Karşılaştırma operatörleri her zaman bool (True/False) döndürür
print(f"{x} == {y}  → {x == y}")     # Eşit mi?              False
print(f"{x} != {y}  → {x != y}")     # Eşit değil mi?        True
print(f"{x} > {y}   → {x > y}")      # Büyük mü?             False
print(f"{x} < {y}   → {x < y}")      # Küçük mü?             True
print(f"{x} >= {y}  → {x >= y}")     # Büyük veya eşit mi?   False
print(f"{x} <= {y}  → {x <= y}")     # Küçük veya eşit mi?   True

# DİKKAT: = (atama) vs == (karşılaştırma)
# sayi = 5    → sayi değişkenine 5 değerini ata
# sayi == 5   → sayi, 5'e eşit mi? (True/False döner)

# String karşılaştırma
print(f"\n'abc' == 'abc' → {'abc' == 'abc'}")   # True
print(f"'abc' == 'ABC' → {'abc' == 'ABC'}")     # False (büyük-küçük harf farklı)
print(f"'a' < 'b'      → {'a' < 'b'}")          # True (alfabetik sıra)

# Zincirleme karşılaştırma (Python'a özel güzel bir özellik!)
yas = 25
print(f"\n18 <= {yas} <= 65 → {18 <= yas <= 65}")   # True
# Bu, diğer dillerde şöyle yazılır: yas >= 18 and yas <= 65


# ============================================================
# 2.3 — MANTIKSAL OPERATÖRLER
# ============================================================

print("\n\n=== Mantıksal Operatörler ===\n")

# and → her iki koşul da True ise True
# or  → en az bir koşul True ise True
# not → tersini alır

a = True
b = False

print(f"True and True   → {True and True}")     # True
print(f"True and False  → {True and False}")     # False
print(f"False and False → {False and False}")    # False

print(f"\nTrue or True   → {True or True}")      # True
print(f"True or False  → {True or False}")       # True
print(f"False or False → {False or False}")      # False

print(f"\nnot True  → {not True}")               # False
print(f"not False → {not False}")                # True

# Pratik örnek
yas = 25
gelir = 5000

print(f"\nYaş: {yas}, Gelir: {gelir}")
print(f"Yaş > 18 AND Gelir > 3000 → {yas > 18 and gelir > 3000}")  # True
print(f"Yaş > 30 OR Gelir > 3000  → {yas > 30 or gelir > 3000}")   # True
print(f"NOT (Yaş > 30)            → {not (yas > 30)}")              # True

# Kısa devre değerlendirme (Short-circuit evaluation)
# and: ilk False'ta durur
# or:  ilk True'da durur
# Bu, performans ve güvenlik açısından önemlidir
print("\n--- Kısa Devre Değerlendirme ---")
x = 0
# x != 0 False olduğu için, 10/x hiç hesaplanmaz (ZeroDivisionError olmaz!)
sonuc = x != 0 and 10 / x > 2
print(f"x=0 için (x != 0 and 10/x > 2) → {sonuc}")  # False


# ============================================================
# 2.4 — ATAMA OPERATÖRLERİ
# ============================================================

print("\n\n=== Atama Operatörleri ===\n")

x = 10          # Basit atama
print(f"x = 10    → x = {x}")

x += 5          # x = x + 5
print(f"x += 5    → x = {x}")    # 15

x -= 3          # x = x - 3
print(f"x -= 3    → x = {x}")    # 12

x *= 2          # x = x * 2
print(f"x *= 2    → x = {x}")    # 24

x /= 4          # x = x / 4
print(f"x /= 4   → x = {x}")    # 6.0

x //= 2         # x = x // 2
print(f"x //= 2  → x = {x}")    # 3.0

x **= 3         # x = x ** 3
print(f"x **= 3  → x = {x}")    # 27.0

x %= 5          # x = x % 5
print(f"x %= 5   → x = {x}")    # 2.0


# ============================================================
# 2.5 — if, elif, else YAPILARI
# ============================================================

print("\n\n=== Koşullu İfadeler ===\n")

# --- Basit if ---
sicaklik = 35

if sicaklik > 30:
    print(f"{sicaklik}°C — Hava çok sıcak!")
    print("Bol su için.")

# --- if-else ---
print("\n--- if-else ---")
not_ortalamasi = 72

if not_ortalamasi >= 50:
    print(f"Not: {not_ortalamasi} — Geçtiniz!")
else:
    print(f"Not: {not_ortalamasi} — Kaldınız.")

# --- if-elif-else ---
print("\n--- if-elif-else ---")
puan = 85

if puan >= 90:
    harf = "AA"
elif puan >= 85:
    harf = "BA"
elif puan >= 80:
    harf = "BB"
elif puan >= 75:
    harf = "CB"
elif puan >= 70:
    harf = "CC"
elif puan >= 65:
    harf = "DC"
elif puan >= 60:
    harf = "DD"
elif puan >= 50:
    harf = "FD"
else:
    harf = "FF"

print(f"Puan: {puan} → Harf notu: {harf}")

# ÖNEMLİ: elif sırası önemlidir!
# Python yukarıdan aşağıya kontrol eder ve ilk True olan bloğu çalıştırır.
# Sonraki elif/else'leri atlar.

# --- Birden fazla koşul (and, or) ---
print("\n--- Birleşik Koşullar ---")
yas = 28
egitim = "doktora"

if yas >= 25 and egitim == "doktora":
    print("Araştırma görevlisi olabilirsiniz.")

# --- Boş blok: pass ---
# Henüz yazmak istemediğiniz bir blok için pass kullanılır
deger = 42
if deger > 100:
    pass  # TODO: Bu durumu daha sonra ele alacağız
else:
    print(f"Değer 100'den küçük: {deger}")


# ============================================================
# 2.6 — İÇ İÇE KOŞULLAR VE TERNARY OPERATÖR
# ============================================================

print("\n\n=== İç İçe Koşullar ===\n")

# --- İç içe (nested) if ---
yas = 22
ogrenci = True

if yas >= 18:
    print("Yetişkin")
    if ogrenci:
        print("  → Öğrenci indirimi uygulanır")
    else:
        print("  → Tam ücret uygulanır")
else:
    print("18 yaş altı — giriş yasak")

# DİKKAT: Çok fazla iç içe koşuldan kaçının.
# 3-4 seviye derinlik okunabilirliği bozar.
# Bunun yerine and/or ile birleştirmeyi tercih edin.

# --- Ternary (koşullu ifade) ---
print("\n--- Ternary Operatör ---")

# Uzun yol:
yas = 20
if yas >= 18:
    durum = "yetişkin"
else:
    durum = "çocuk"

# Kısa yol (ternary):
durum = "yetişkin" if yas >= 18 else "çocuk"
print(f"Yaş {yas}: {durum}")

# Ternary örnekleri
sayi = -5
isaret = "pozitif" if sayi > 0 else "negatif veya sıfır"
print(f"{sayi} → {isaret}")

puan = 75
sonuc = "Geçti" if puan >= 50 else "Kaldı"
print(f"Puan {puan}: {sonuc}")


# ============================================================
# 2.7 — match-case (Python 3.10+)
# ============================================================

print("\n\n=== match-case (Python 3.10+) ===\n")

# match-case, diğer dillerdeki switch-case yapısına benzer
# Python 3.10 ile gelmiştir

gun = "Pazartesi"

match gun:
    case "Pazartesi":
        print("Haftanın ilk günü — yeni başlangıç!")
    case "Cuma":
        print("Hafta sonu yaklaşıyor!")
    case "Cumartesi" | "Pazar":    # Birden fazla değer: | (veya)
        print("Hafta sonu — dinlenme zamanı!")
    case _:                         # default (hiçbiri eşleşmezse)
        print(f"{gun} — normal bir iş günü")

# match-case ile sayısal aralıklar (guard clause)
not_degeri = 85

match not_degeri:
    case n if n >= 90:
        print(f"{n} → Pekiyi")
    case n if n >= 70:
        print(f"{n} → İyi")
    case n if n >= 50:
        print(f"{n} → Orta")
    case _:
        print(f"{not_degeri} → Başarısız")

# HTTP durum kodları örneği
http_kodu = 404

match http_kodu:
    case 200:
        print("OK — Başarılı")
    case 301:
        print("Yönlendirme")
    case 404:
        print("Sayfa bulunamadı")
    case 500:
        print("Sunucu hatası")
    case _:
        print(f"Bilinmeyen kod: {http_kodu}")


# ============================================================
# 2.8 — UYGULAMALAR
# ============================================================

print("\n" + "=" * 50)
print("UYGULAMALAR")
print("=" * 50)

# ----- Uygulama 1: Not Hesaplama Sistemi -----
print("\n--- Uygulama 1: Not Hesaplama Sistemi ---")

vize = 65
final = 78
odev = 90

# Ağırlıklı ortalama: Vize %30, Final %50, Ödev %20
agirlikli_ort = vize * 0.30 + final * 0.50 + odev * 0.20

print(f"Vize: {vize}")
print(f"Final: {final}")
print(f"Ödev: {odev}")
print(f"Ağırlıklı Ortalama: {agirlikli_ort:.1f}")

if agirlikli_ort >= 90:
    harf = "AA"
    durum = "Geçti"
elif agirlikli_ort >= 85:
    harf = "BA"
    durum = "Geçti"
elif agirlikli_ort >= 80:
    harf = "BB"
    durum = "Geçti"
elif agirlikli_ort >= 75:
    harf = "CB"
    durum = "Geçti"
elif agirlikli_ort >= 70:
    harf = "CC"
    durum = "Geçti"
elif agirlikli_ort >= 60:
    harf = "DC"
    durum = "Koşullu Geçti"
elif agirlikli_ort >= 50:
    harf = "DD"
    durum = "Koşullu Geçti"
else:
    harf = "FF"
    durum = "Kaldı"

print(f"Harf Notu: {harf} — {durum}")

# Final notu kontrolü
if final < 50:
    print("⚠ DİKKAT: Final notu 50'nin altında — dersten kaldınız!")


# ----- Uygulama 2: Basit Menü Programı -----
print("\n--- Uygulama 2: İstatistik Hesaplayıcı Menü ---")

# Normalde input() ile alınır, burada örnek olarak sabit değer
secim = "2"

print("=== İstatistik Hesaplayıcı ===")
print("1. Ortalama hesapla")
print("2. Yüzde hesapla")
print("3. BMI hesapla")
print(f"Seçiminiz: {secim}")

# Örnek veriler
if secim == "1":
    deger1, deger2, deger3 = 80, 90, 70
    ort = (deger1 + deger2 + deger3) / 3
    print(f"Ortalama: {ort:.2f}")
elif secim == "2":
    parca = 45
    butun = 200
    yuzde = (parca / butun) * 100
    print(f"{parca}/{butun} = %{yuzde:.1f}")
elif secim == "3":
    kilo = 70
    boy = 1.75
    bmi = kilo / (boy ** 2)
    print(f"BMI: {bmi:.1f}")
else:
    print("Geçersiz seçim!")


# ----- Uygulama 3: P-değeri Yorumlama -----
print("\n--- Uygulama 3: P-değeri Yorumlama ---")

p_degeri = 0.03
alfa = 0.05

print(f"P-değeri: {p_degeri}")
print(f"Anlamlılık düzeyi (α): {alfa}")

if p_degeri < 0.001:
    print("Sonuç: Çok güçlü kanıt (***)")
    print("H₀ reddedilir — İstatistiksel olarak çok anlamlı")
elif p_degeri < 0.01:
    print("Sonuç: Güçlü kanıt (**)")
    print("H₀ reddedilir — İstatistiksel olarak anlamlı")
elif p_degeri < alfa:
    print("Sonuç: Kanıt var (*)")
    print("H₀ reddedilir — İstatistiksel olarak anlamlı")
else:
    print("Sonuç: Yeterli kanıt yok")
    print("H₀ reddedilemez — İstatistiksel olarak anlamlı değil")


# ----- Uygulama 4: Vücut Kitle İndeksi Sınıflandırma -----
print("\n--- Uygulama 4: BMI Sınıflandırma ---")

kilo = 82
boy = 1.75
bmi = kilo / (boy ** 2)

print(f"Kilo: {kilo} kg, Boy: {boy} m")
print(f"BMI: {bmi:.1f}")

if bmi < 18.5:
    kategori = "Zayıf"
elif bmi < 25:
    kategori = "Normal"
elif bmi < 30:
    kategori = "Fazla kilolu"
elif bmi < 35:
    kategori = "Obez (Sınıf I)"
elif bmi < 40:
    kategori = "Obez (Sınıf II)"
else:
    kategori = "Obez (Sınıf III)"

print(f"Kategori: {kategori}")


# ============================================================
# ALIŞTIRMALAR (Öğrenciler İçin)
# ============================================================
"""
Alıştırma 1: Kullanıcıdan bir sayı alın. Sayının pozitif, negatif
   veya sıfır olduğunu belirleyin. Ayrıca çift mi tek mi olduğunu yazdırın.

Alıştırma 2: Kullanıcıdan üç sınav notu alın.
   - Ağırlıklı ortalamayı hesaplayın (30%, 30%, 40%)
   - Harf notunu belirleyin
   - Geçti/Kaldı durumunu yazdırın

Alıştırma 3: Kullanıcıdan bir yıl alın ve artık yıl olup olmadığını
   kontrol edin.
   Kural: 4'e bölünüyorsa artık yıl, AMA 100'e bölünüyorsa değil,
          AMA 400'e bölünüyorsa yine artık yıl.
   (Örnek: 2000→artık, 1900→değil, 2024→artık)

Alıştırma 4: Kullanıcıdan bir p-değeri ve anlamlılık düzeyi (α) alın.
   Sonucun istatistiksel olarak anlamlı olup olmadığını ve
   anlamlılık seviyesini (*,**,***) belirleyen program yazın.

Alıştırma 5: Kullanıcıdan saat bilgisi (0-23) alıp
   günün hangi dilimine ait olduğunu belirleyin:
   00-05: Gece, 06-11: Sabah, 12-17: Öğleden sonra, 18-23: Akşam
"""
