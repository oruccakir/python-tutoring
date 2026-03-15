"""
============================================================
  BÖLÜM 1 — DERS İÇİ CANLI KODLAMA ÖRNEKLERİ — ÇÖZÜMLER
============================================================

Bu dosya ders_ici_ornekler.py dosyasındaki tüm örneklerin
çözümlerini içerir. Dersten ÖNCE öğrencilerle paylaşmayın!
============================================================
"""

# ============================================================
#  HAFTA 1 — Python'a Giriş
# ============================================================

# ────────────────────────────────────────────────────────────
# Çözüm 1.1 ★ — Kartvizit Oluşturucu
# ────────────────────────────────────────────────────────────

print("=" * 50)
print("Çözüm 1.1 — Kartvizit Oluşturucu")
print("=" * 50)

unvan = "Dr."
ad = "Ayşe"
soyad = "Yılmaz"
bolum = "Biyoloji Bölümü"
universite = "İstanbul Üniversitesi"
email = "ayse.yilmaz@uni.edu.tr"
telefon = "+90 212 555 0001"

print("┌──────────────────────────────────┐")
print(f"│  {unvan} {ad} {soyad:<22}│")
print(f"│  {bolum:<32}│")
print(f"│  {universite:<32}│")
print(f"│  {email:<32}│")
print(f"│  Tel: {telefon:<26}│")
print("└──────────────────────────────────┘")


# ────────────────────────────────────────────────────────────
# Çözüm 1.2 ★ — Birim Dönüştürücü
# ────────────────────────────────────────────────────────────

print("\n" + "=" * 50)
print("Çözüm 1.2 — Birim Dönüştürücü")
print("=" * 50)

# a) mL → L
ml = 2500
litre = ml / 1000
print(f"{ml} mL = {litre} L")

# b) kg → g → mg
kg = 0.045
gram = kg * 1000
miligram = kg * 1_000_000
print(f"{kg} kg = {gram} g = {miligram} mg")

# c) saat → gün ve kalan saat
toplam_saat = 72
gun = toplam_saat // 24
kalan_saat = toplam_saat % 24
print(f"{toplam_saat} saat = {gun} gün {kalan_saat} saat")

# d) °C → °F ve K
celsius = 37.5
fahrenheit = (celsius * 9 / 5) + 32
kelvin = celsius + 273.15
print(f"{celsius} °C = {fahrenheit} °F = {kelvin} K")


# ────────────────────────────────────────────────────────────
# Çözüm 1.3 ★★ — Deney Özeti Hesaplayıcı
# ────────────────────────────────────────────────────────────

print("\n" + "=" * 50)
print("Çözüm 1.3 — Deney Özeti Hesaplayıcı")
print("=" * 50)

o1, o2, o3, o4, o5, o6 = 12.3, 11.8, 12.7, 12.1, 13.0, 11.5
olcum_sayisi = 6

toplam = o1 + o2 + o3 + o4 + o5 + o6
ortalama = toplam / olcum_sayisi
en_kucuk = min(o1, o2, o3, o4, o5, o6)
en_buyuk = max(o1, o2, o3, o4, o5, o6)
aralik = en_buyuk - en_kucuk

# Bool → int: True = 1, False = 0
ort_uzeri = ((o1 > ortalama) + (o2 > ortalama) + (o3 > ortalama)
             + (o4 > ortalama) + (o5 > ortalama) + (o6 > ortalama))

print("=== Deney Özeti ===")
print(f"Ölçüm sayısı:  {olcum_sayisi}")
print(f"Toplam:         {toplam:.2f}")
print(f"Ortalama:       {ortalama:.2f}")
print(f"Min:            {en_kucuk:.2f}")
print(f"Max:            {en_buyuk:.2f}")
print(f"Aralık:         {aralik:.2f}")
print(f"Ort. üzeri:     {ort_uzeri} ölçüm")


# ────────────────────────────────────────────────────────────
# Çözüm 1.4 ★★ — Tip Dönüşümü Bulmacası
# ────────────────────────────────────────────────────────────

print("\n" + "=" * 50)
print("Çözüm 1.4 — Tip Dönüşümü Bulmacası")
print("=" * 50)

print(f"a) 10 / 3         = {10 / 3}  → {type(10 / 3).__name__}")
print(f"b) 10 // 3        = {10 // 3}  → {type(10 // 3).__name__}")
print(f"c) 10 % 3         = {10 % 3}  → {type(10 % 3).__name__}")
print(f"d) '5' + '3'      = {'5' + '3'}  → {type('5' + '3').__name__}")
print(f"e) int('5')+int('3') = {int('5') + int('3')}  → {type(int('5') + int('3')).__name__}")
print(f"f) str(5)+str(3)  = {str(5) + str(3)}  → {type(str(5) + str(3)).__name__}")
print(f"g) float('inf') > 999999999 = {float('inf') > 999999999}")
print(f"h) bool('')       = {bool('')}")
print(f"i) bool('False')  = {bool('False')}  ← Sürpriz! Dolu string = True")
print(f"j) bool(0)={bool(0)}, bool(0.0)={bool(0.0)}, bool(None)={bool(None)}")
print(f"k) True + True    = {True + True}  → {type(True + True).__name__}  ← Sürpriz!")


# ============================================================
#  HAFTA 2 — Operatörler ve Koşullu İfadeler
# ============================================================

# ────────────────────────────────────────────────────────────
# Çözüm 2.1 ★ — Araştırma Bütçesi Kontrolü
# ────────────────────────────────────────────────────────────

print("\n" + "=" * 50)
print("Çözüm 2.1 — Araştırma Bütçesi Kontrolü")
print("=" * 50)

toplam_butce = 50000
harcanan = 32750
planlanan_harcama = 12000

kalan = toplam_butce - harcanan
kullanim_yuzde = (harcanan / toplam_butce) * 100
yapilabilir = kalan >= planlanan_harcama

print("=== Bütçe Raporu ===")
print(f"Toplam:    {toplam_butce:,} TL")
print(f"Harcanan:  {harcanan:,} TL")
print(f"Kalan:     {kalan:,} TL")
print(f"Kullanım:  %{kullanim_yuzde:.1f}")

if yapilabilir:
    print(f"Planlanan harcama ({planlanan_harcama:,} TL): Yapılabilir ✓")
else:
    print(f"Planlanan harcama ({planlanan_harcama:,} TL): Yapılamaz ✗")

if kullanim_yuzde > 80:
    print("Durum: Dikkat: Bütçe kritik seviyede!")
elif kullanim_yuzde > 50:
    print("Durum: Bütçe kontrol altında.")
else:
    print("Durum: Bütçe rahat.")


# ────────────────────────────────────────────────────────────
# Çözüm 2.2 ★★ — Denek Uygunluk Kontrolü
# ────────────────────────────────────────────────────────────

print("\n" + "=" * 50)
print("Çözüm 2.2 — Denek Uygunluk Kontrolü")
print("=" * 50)

adaylar = [
    ("Aday 1", 25, 22.5, False, False),
    ("Aday 2", 70, 24.0, False, False),
    ("Aday 3", 35, 32.1, False, False),
    ("Aday 4", 45, 27.3, True, False),
]

for ad, yas, bmi, kronik, son_arastirma in adaylar:
    sorunlar = []

    if not (18 <= yas <= 65):
        sorunlar.append(f"Yaş kriteri sağlanmadı ({yas})")
    if not (18.5 <= bmi <= 30.0):
        sorunlar.append(f"BMI kriteri sağlanmadı ({bmi})")
    if kronik:
        sorunlar.append("Kronik hastalık mevcut")
    if son_arastirma:
        sorunlar.append("Son 6 ayda araştırmaya katılmış")

    if not sorunlar:
        print(f"{ad}: UYGUN")
    else:
        print(f"{ad}: UYGUN DEĞİL — {', '.join(sorunlar)}")


# ────────────────────────────────────────────────────────────
# Çözüm 2.3 ★★ — Akademik Not Dönüştürücü
# ────────────────────────────────────────────────────────────

print("\n" + "=" * 50)
print("Çözüm 2.3 — Akademik Not Dönüştürücü")
print("=" * 50)

test_notlari = ["BA", "CC", "FF", "XY"]

# Yöntem 1: if-elif
print("--- if-elif ile ---")
for not_harf in test_notlari:
    if not_harf == "AA":
        puan, aciklama = 4.0, "Mükemmel"
    elif not_harf == "BA":
        puan, aciklama = 3.5, "Çok İyi"
    elif not_harf == "BB":
        puan, aciklama = 3.0, "İyi"
    elif not_harf == "CB":
        puan, aciklama = 2.5, "Ortanın Üstü"
    elif not_harf == "CC":
        puan, aciklama = 2.0, "Orta"
    elif not_harf == "DC":
        puan, aciklama = 1.5, "Koşullu"
    elif not_harf == "DD":
        puan, aciklama = 1.0, "Koşullu"
    elif not_harf == "FF":
        puan, aciklama = 0.0, "Başarısız"
    else:
        print(f"{not_harf} → Geçersiz not!")
        continue

    print(f"{not_harf} → {puan} / 4.0 ({aciklama})")

# Yöntem 2: match-case
print("\n--- match-case ile ---")
for not_harf in test_notlari:
    match not_harf:
        case "AA": puan, aciklama = 4.0, "Mükemmel"
        case "BA": puan, aciklama = 3.5, "Çok İyi"
        case "BB": puan, aciklama = 3.0, "İyi"
        case "CB": puan, aciklama = 2.5, "Ortanın Üstü"
        case "CC": puan, aciklama = 2.0, "Orta"
        case "DC": puan, aciklama = 1.5, "Koşullu"
        case "DD": puan, aciklama = 1.0, "Koşullu"
        case "FF": puan, aciklama = 0.0, "Başarısız"
        case _:
            print(f"{not_harf} → Geçersiz not!")
            continue

    print(f"{not_harf} → {puan} / 4.0 ({aciklama})")


# ────────────────────────────────────────────────────────────
# Çözüm 2.4 ★★★ — Üçgen Sınıflandırıcı
# ────────────────────────────────────────────────────────────

print("\n" + "=" * 50)
print("Çözüm 2.4 — Üçgen Sınıflandırıcı")
print("=" * 50)

test_ucgenler = [
    (3, 4, 5),
    (5, 5, 5),
    (1, 2, 10),
    (5, 5, 7),
]

for a, b, c in test_ucgenler:
    print(f"\nKenarlar: a={a}, b={b}, c={c}")

    # 1. Üçgen oluşturulabilir mi?
    if a + b <= c or a + c <= b or b + c <= a:
        print("  → Üçgen oluşturulamaz!")
        continue

    # 2. Kenarlarına göre tür
    if a == b == c:
        tur = "Eşkenar"
    elif a == b or b == c or a == c:
        tur = "İkizkenar"
    else:
        tur = "Çeşitkenar"

    # 3. Dik üçgen kontrolü (en büyük kenar = hipotenüs)
    kenarlar = sorted([a, b, c])
    dik_mi = kenarlar[0]**2 + kenarlar[1]**2 == kenarlar[2]**2

    sonuc = f"  → {tur}"
    if dik_mi:
        sonuc += ", Dik üçgen"
    print(sonuc)


# ============================================================
#  HAFTA 3 — Döngüler ve String İşlemleri
# ============================================================

# ────────────────────────────────────────────────────────────
# Çözüm 3.1 ★ — Çarpım Tablosu
# ────────────────────────────────────────────────────────────

print("\n" + "=" * 50)
print("Çözüm 3.1 — Çarpım Tablosu")
print("=" * 50)

sayi = 7
print(f"\n=== {sayi} Çarpım Tablosu ===")
for i in range(1, 11):
    print(f" {sayi} x {i:2} = {sayi * i:3}")


# ────────────────────────────────────────────────────────────
# Çözüm 3.2 ★★ — Asal Sayı Bulucu
# ────────────────────────────────────────────────────────────

print("\n" + "=" * 50)
print("Çözüm 3.2 — Asal Sayı Bulucu")
print("=" * 50)

asal_sayac = 0
for sayi in range(2, 101):
    asal = True
    for bolen in range(2, int(sayi**0.5) + 1):
        if sayi % bolen == 0:
            asal = False
            break

    if asal:
        print(sayi, end=" ")
        asal_sayac += 1

print(f"\nToplam: {asal_sayac} asal sayı")


# ────────────────────────────────────────────────────────────
# Çözüm 3.3 ★★ — Deney Verisi Analizi (Döngü ile)
# ────────────────────────────────────────────────────────────

print("\n" + "=" * 50)
print("Çözüm 3.3 — Deney Verisi Analizi")
print("=" * 50)

olcumler = [36.6, 37.2, 36.8, 38.5, 37.1, 39.2, 36.9,
            37.8, 38.1, 36.5, 37.4, 38.8, 37.0, 36.7]

# a) Ortalama
toplam = 0
for o in olcumler:
    toplam += o
ortalama = toplam / len(olcumler)

# b) Min ve max + gün numaraları
en_dusuk = olcumler[0]
en_yuksek = olcumler[0]
min_gun = 1
max_gun = 1

for i, o in enumerate(olcumler, start=1):
    if o < en_dusuk:
        en_dusuk = o
        min_gun = i
    if o > en_yuksek:
        en_yuksek = o
        max_gun = i

# c) Ateşli günler (> 37.5)
atesli = 0
for o in olcumler:
    if o > 37.5:
        atesli += 1

# d) Ardışık günler arası en büyük fark
max_fark = 0
fark_gun = 1
for i in range(1, len(olcumler)):
    fark = abs(olcumler[i] - olcumler[i - 1])
    if fark > max_fark:
        max_fark = fark
        fark_gun = i  # i. ve (i+1). gün arası

print("=== Sıcaklık Analiz Raporu ===")
print(f"Gün sayısı:        {len(olcumler)}")
print(f"Ortalama:          {ortalama:.2f} °C")
print(f"En düşük:          {en_dusuk:.2f} °C (Gün {min_gun})")
print(f"En yüksek:         {en_yuksek:.2f} °C (Gün {max_gun})")
print(f"Ateşli günler:     {atesli} / {len(olcumler)} (%{atesli/len(olcumler)*100:.1f})")
print(f"Max günlük fark:   {max_fark:.2f} °C (Gün {fark_gun}→{fark_gun+1})")


# ────────────────────────────────────────────────────────────
# Çözüm 3.4 ★★ — Yıldız Desenleri
# ────────────────────────────────────────────────────────────

print("\n" + "=" * 50)
print("Çözüm 3.4 — Yıldız Desenleri")
print("=" * 50)

n = 5

# Desen A — Dik üçgen
print("\nDesen A (Dik üçgen):")
for i in range(1, n + 1):
    print("*" * i)

# Desen B — Piramit
print("\nDesen B (Piramit):")
for i in range(1, n + 1):
    bosluk = " " * (n - i)
    yildiz = "*" * (2 * i - 1)
    print(bosluk + yildiz)

# Desen C — Elmas
print("\nDesen C (Elmas):")
# Üst yarı
for i in range(1, n + 1):
    bosluk = " " * (n - i)
    yildiz = "*" * (2 * i - 1)
    print(bosluk + yildiz)
# Alt yarı
for i in range(n - 1, 0, -1):
    bosluk = " " * (n - i)
    yildiz = "*" * (2 * i - 1)
    print(bosluk + yildiz)


# ────────────────────────────────────────────────────────────
# Çözüm 3.5 ★★ — E-posta Doğrulayıcı
# ────────────────────────────────────────────────────────────

print("\n" + "=" * 50)
print("Çözüm 3.5 — E-posta Doğrulayıcı")
print("=" * 50)

emails = [
    "ahmet@uni.edu.tr",
    "ayse@lab",
    "hata@@mail.com",
    "@domain.com",
    "test@domain.",
    "kullanici adi@mail.com",
    "fatma.dr@hastane.gov.tr",
]

for email in emails:
    hata = None

    if " " in email:
        hata = "Boşluk içeriyor"
    elif email.count("@") != 1:
        hata = "Birden fazla '@'" if email.count("@") > 1 else "'@' işareti yok"
    elif email.startswith("@"):
        hata = "'@' öncesi boş"
    elif email.endswith("."):
        hata = "'.' ile bitiyor"
    else:
        domain = email.split("@")[1]
        if "." not in domain:
            hata = "'@' sonrası '.' yok"

    if hata:
        print(f"{email:<30} → Geçersiz: {hata}")
    else:
        print(f"{email:<30} → Geçerli ✓")


# ────────────────────────────────────────────────────────────
# Çözüm 3.6 ★★★ — DNA Dizisi Analizi
# ────────────────────────────────────────────────────────────

print("\n" + "=" * 50)
print("Çözüm 3.6 — DNA Dizisi Analizi")
print("=" * 50)

dna = "ATCGATCGAATTCCGGAATCGATCGCCTTAAGG"
uzunluk = len(dna)

# a) Her nükleotidin sayısı ve yüzdesi
print(f"\n=== DNA Analiz Raporu ===")
print(f"Dizi uzunluğu: {uzunluk}")
print(f"\nNükleotid dağılımı:")
for nuk in "ATCG":
    sayi = dna.count(nuk)
    yuzde = (sayi / uzunluk) * 100
    print(f"  {nuk}: {sayi}  (%{yuzde:.1f})")

# b) GC oranı
gc_sayi = dna.count("G") + dna.count("C")
gc_orani = (gc_sayi / uzunluk) * 100
print(f"\nGC oranı: %{gc_orani:.1f}")

# c) Tamamlayıcı dizi
tamamlayici = ""
for nuk in dna:
    if nuk == "A":
        tamamlayici += "T"
    elif nuk == "T":
        tamamlayici += "A"
    elif nuk == "G":
        tamamlayici += "C"
    elif nuk == "C":
        tamamlayici += "G"

print(f"\nTamamlayıcı dizi:")
print(f"  5'- {dna} -3'")
print(f"  3'- {tamamlayici} -5'")

# d) Motif arama
motif = "ATC"
motif_sayisi = dna.count(motif)
print(f"\n\"{motif}\" motifi {motif_sayisi} kez bulundu.")

# e) RNA transkripsiyon
rna = dna.replace("T", "U")
print(f"RNA: {rna}")


# ────────────────────────────────────────────────────────────
# Çözüm 3.7 ★★★ — Basit Şifre Gücü Ölçer
# ────────────────────────────────────────────────────────────

print("\n" + "=" * 50)
print("Çözüm 3.7 — Şifre Gücü Ölçer")
print("=" * 50)

sifreler = ["abc", "Parola123", "Tr5!", "G3l1$m1$_S1fr3!!", "12345678"]
ozel_karakterler = "!@#$%^&*_-"

print("\n=== Şifre Gücü Analizi ===")
for sifre in sifreler:
    puan = 0

    # Uzunluk kontrolü
    if len(sifre) >= 8:
        puan += 1

    # Büyük harf
    buyuk_var = False
    for k in sifre:
        if k.isupper():
            buyuk_var = True
            break
    if buyuk_var:
        puan += 1

    # Küçük harf
    kucuk_var = False
    for k in sifre:
        if k.islower():
            kucuk_var = True
            break
    if kucuk_var:
        puan += 1

    # Rakam
    rakam_var = False
    for k in sifre:
        if k.isdigit():
            rakam_var = True
            break
    if rakam_var:
        puan += 1

    # Özel karakter
    ozel_var = False
    for k in sifre:
        if k in ozel_karakterler:
            ozel_var = True
            break
    if ozel_var:
        puan += 1

    # Bonus uzunluk
    if len(sifre) >= 12:
        puan += 1

    # Güç seviyesi
    if puan <= 2:
        seviye = "Zayıf"
    elif puan <= 4:
        seviye = "Orta"
    else:
        seviye = "Güçlü"

    # Görsel bar
    bar = "■" * puan + "□" * (6 - puan)
    print(f'  "{sifre}"' + " " * (22 - len(sifre)) + f"→ [{bar}] {seviye:<10} ({puan}/6)")


# ────────────────────────────────────────────────────────────
# Çözüm 3.8 ★★★ — Histogram Çizici (Metin Tabanlı)
# ────────────────────────────────────────────────────────────

print("\n" + "=" * 50)
print("Çözüm 3.8 — Histogram Çizici")
print("=" * 50)

anket_sonuclari = [
    ("Çok Memnun", 45),
    ("Memnun", 82),
    ("Kararsız", 23),
    ("Memnun Değil", 15),
    ("Hiç Memnun Değil", 8),
]
toplam_katilimci = 173

print(f"\n=== Memnuniyet Anketi Sonuçları (n={toplam_katilimci}) ===\n")

for kategori, sayi in anket_sonuclari:
    yuzde = (sayi / toplam_katilimci) * 100
    tam_blok = sayi // 2
    yarim_blok = "▌" if sayi % 2 == 1 else ""
    bar = "█" * tam_blok + yarim_blok
    print(f"  {kategori:<18}| {bar} {sayi} (%{yuzde:.1f})")


# ────────────────────────────────────────────────────────────
# Çözüm 3.9 ★★★ — Collatz Conjecture Görselleştirici
# ────────────────────────────────────────────────────────────

print("\n" + "=" * 50)
print("Çözüm 3.9 — Collatz Conjecture")
print("=" * 50)

baslangic = 27
sayi = baslangic
seri = [sayi]

while sayi != 1:
    if sayi % 2 == 0:
        sayi = sayi // 2
    else:
        sayi = sayi * 3 + 1
    seri.append(sayi)

# Seriyi yazdır (kısaltılmış)
print(f"\nBaşlangıç: {baslangic}")
if len(seri) > 15:
    gosterim = " → ".join(str(s) for s in seri[:8])
    gosterim += " → ... → "
    gosterim += " → ".join(str(s) for s in seri[-4:])
    print(gosterim)
else:
    print(" → ".join(str(s) for s in seri))

# İstatistikler
en_buyuk = seri[0]
for s in seri:
    if s > en_buyuk:
        en_buyuk = s

print(f"\nAdım sayısı: {len(seri) - 1}")
print(f"Ulaşılan en büyük değer: {en_buyuk}")

# Grafik (ilk 20 adım)
print(f"\nGrafik (ilk 20 adım, her █ ≈ {en_buyuk // 50}):")
olcek = max(en_buyuk // 50, 1)
for i, deger in enumerate(seri[:20]):
    bar = "█" * (deger // olcek)
    print(f"  {i:>3}. {bar} {deger}")


# ============================================================
# BONUS ÇÖZÜMLER
# ============================================================

# ────────────────────────────────────────────────────────────
# Bonus 1 ★★★ — Mini İstatistik Hesaplayıcı
# ────────────────────────────────────────────────────────────

print("\n" + "=" * 50)
print("Bonus 1 — Mini İstatistik Hesaplayıcı")
print("=" * 50)

import math

veri = [14, 22, 8, 31, 17, 25, 19, 27, 11, 23, 29, 16, 20, 35, 13]
n = len(veri)

# a) Ortalama
toplam = 0
for v in veri:
    toplam += v
ortalama = toplam / n

# b) Medyan
sirali = sorted(veri)
if n % 2 == 1:
    medyan = sirali[n // 2]
else:
    medyan = (sirali[n // 2 - 1] + sirali[n // 2]) / 2

# c) Standart sapma
kare_fark_toplam = 0
for v in veri:
    kare_fark_toplam += (v - ortalama) ** 2
std = math.sqrt(kare_fark_toplam / n)

print(f"\n=== İstatistik Raporu ===")
print(f"n      = {n}")
print(f"Mean   = {ortalama:.2f}")
print(f"Median = {medyan}")
print(f"Std    = {std:.2f}")

# d) Frekans tablosu (5'li aralıklar)
print(f"\nFrekans Tablosu:")
aralik_baslangic = 5
aralik_bitis = 40

for alt in range(aralik_baslangic, aralik_bitis, 5):
    ust = alt + 5
    frekans = 0
    for v in veri:
        if alt <= v < ust:
            frekans += 1
    if frekans > 0:
        bar = "██" * frekans
        print(f"  {alt:>2}-{ust:<2} | {bar} {frekans}")


# ────────────────────────────────────────────────────────────
# Bonus 2 ★★★ — Araştırma Makale Özet Analizi
# ────────────────────────────────────────────────────────────

print("\n" + "=" * 50)
print("Bonus 2 — Araştırma Makale Özet Analizi")
print("=" * 50)

abstract = """
This study investigates the effects of climate change on
biodiversity in Mediterranean ecosystems. We analyzed data from
150 species across 12 different habitats over a period of 20 years.
Our results indicate that temperature increases of 1.5 degrees
Celsius led to a 23 percent decline in species diversity.
Furthermore, precipitation changes significantly affected
habitat distribution patterns. The findings suggest that
conservation strategies must be adapted to account for ongoing
climate variability. This research provides critical evidence
for policy makers working on environmental protection frameworks.
"""

stopwords = {"the", "a", "an", "of", "in", "on", "to", "for",
             "and", "that", "this", "is", "are", "was", "were",
             "we", "our", "be"}

# Temizlik
temiz = abstract.strip()

# a) Kelime sayısı
kelimeler = temiz.split()
print(f"\nToplam kelime sayısı: {len(kelimeler)}")

# b) Cümle sayısı
cumle_sayisi = temiz.count(".")
print(f"Cümle sayısı: {cumle_sayisi}")

# c) Ortalama cümle uzunluğu
print(f"Ortalama cümle uzunluğu: {len(kelimeler) / cumle_sayisi:.1f} kelime")

# d) En sık 5 kelime (stopword hariç)
# Kelime frekanslarını elle sayalım
kelime_frekanslari = {}
for kelime in kelimeler:
    temiz_kelime = kelime.lower().strip(".,;:!?")
    if temiz_kelime not in stopwords and len(temiz_kelime) > 1:
        if temiz_kelime in kelime_frekanslari:
            kelime_frekanslari[temiz_kelime] += 1
        else:
            kelime_frekanslari[temiz_kelime] = 1

# En sık 5'i bul (sort olmadan, döngüyle)
print(f"\nEn sık kullanılan 5 kelime:")
kullanilan = []
for _ in range(5):
    en_cok_kelime = ""
    en_cok_sayi = 0
    for kelime, sayi in kelime_frekanslari.items():
        if sayi > en_cok_sayi and kelime not in kullanilan:
            en_cok_kelime = kelime
            en_cok_sayi = sayi
    if en_cok_kelime:
        kullanilan.append(en_cok_kelime)
        print(f"  {en_cok_kelime:<20} ({en_cok_sayi} kez)")

# e) Metindeki sayıları bul
print(f"\nMetindeki sayılar:")
for kelime in kelimeler:
    temiz_kelime = kelime.strip(".,;:!?")
    # Sayı kontrolü (tam sayı veya ondalık)
    nokta_cikarilmis = temiz_kelime.replace(".", "", 1)
    if nokta_cikarilmis.isdigit():
        print(f"  {temiz_kelime}")

# f) Okunabilirlik: ortalama kelime uzunluğu
toplam_karakter = 0
for kelime in kelimeler:
    temiz_kelime = kelime.strip(".,;:!?")
    toplam_karakter += len(temiz_kelime)
ort_kelime_uzunlugu = toplam_karakter / len(kelimeler)
print(f"\nOrtalama kelime uzunluğu: {ort_kelime_uzunlugu:.1f} karakter")

if ort_kelime_uzunlugu > 6:
    print("→ Akademik/teknik metin (yüksek okunabilirlik seviyesi gerektirir)")
elif ort_kelime_uzunlugu > 5:
    print("→ Orta seviye metin")
else:
    print("→ Kolay okunan metin")
