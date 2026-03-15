"""
============================================================
  BÖLÜM 2 — DERS İÇİ CANLI KODLAMA ÖRNEKLERİ — ÇÖZÜMLER
============================================================

Bu dosya ders_ici_ornekler.py dosyasındaki tüm örneklerin
çözümlerini içerir. Dersten ÖNCE öğrencilerle paylaşmayın!
============================================================
"""

import os
import csv
import json
import math

ORNEK_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "ornek_dosyalar")
os.makedirs(ORNEK_DIR, exist_ok=True)


# ============================================================
#  HAFTA 4 — Listeler ve Tuple
# ============================================================

# ────────────────────────────────────────────────────────────
# Çözüm 4.1 ★ — Ölçüm Serisi İşlemleri
# ────────────────────────────────────────────────────────────

print("=" * 50)
print("Çözüm 4.1 — Ölçüm Serisi İşlemleri")
print("=" * 50)

olcumler = [7.2, 6.8, 7.5, 6.5, 8.1, 7.0, 6.9, 7.8, 7.3, 6.7]
print(f"Başlangıç: {olcumler}")

# a) Ekleme
olcumler.append(7.4)
olcumler.append(6.6)
print(f"Eklemeden sonra: {olcumler}")

# b) İlk elemanı çıkar
olcumler.remove(7.2)
print(f"7.2 çıkarıldı: {olcumler}")

# c) Sıralama
olcumler.sort()
print(f"Sıralı: {olcumler}")

# d) En küçük ve en büyük 3
print(f"En küçük 3: {olcumler[:3]}")
print(f"En büyük 3: {olcumler[-3:]}")

# e) Ortalamanın üzeri
ortalama = sum(olcumler) / len(olcumler)
ort_uzeri = [o for o in olcumler if o > ortalama]
print(f"Ortalama: {ortalama:.2f}")
print(f"Ort. üzeri: {ort_uzeri}")

# f) Ters çevir
olcumler.reverse()
print(f"Ters: {olcumler}")


# ────────────────────────────────────────────────────────────
# Çözüm 4.2 ★★ — Matris İşlemleri
# ────────────────────────────────────────────────────────────

print("\n" + "=" * 50)
print("Çözüm 4.2 — Matris İşlemleri")
print("=" * 50)

matris = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# a) Yazdırma
print("\nMatris:")
for satir in matris:
    for eleman in satir:
        print(f"{eleman:3}", end="")
    print()

# b) Köşegen
kosegen = [matris[i][i] for i in range(len(matris))]
print(f"\nKöşegen: {kosegen} → Toplam: {sum(kosegen)}")

# c) Satır toplamları
satir_toplamlari = [sum(satir) for satir in matris]
print(f"Satır toplamları: {satir_toplamlari}")

# d) Sütun toplamları
sutun_sayisi = len(matris[0])
sutun_toplamlari = []
for j in range(sutun_sayisi):
    toplam = 0
    for satir in matris:
        toplam += satir[j]
    sutun_toplamlari.append(toplam)
print(f"Sütun toplamları: {sutun_toplamlari}")

# e) Transpoz
transpoz = [[matris[i][j] for i in range(len(matris))] for j in range(len(matris[0]))]
print("\nTranspoz:")
for satir in transpoz:
    for eleman in satir:
        print(f"{eleman:3}", end="")
    print()


# ────────────────────────────────────────────────────────────
# Çözüm 4.3 ★★ — List Comprehension Atölyesi
# ────────────────────────────────────────────────────────────

print("\n" + "=" * 50)
print("Çözüm 4.3 — List Comprehension Atölyesi")
print("=" * 50)

# a) Küpler
# for ile:
kupler_v1 = []
for i in range(1, 21):
    kupler_v1.append(i ** 3)
# comprehension ile:
kupler_v2 = [i ** 3 for i in range(1, 21)]
print(f"\na) Küpler: {kupler_v2[:5]}... (ilk 5)")

# b) Kelime uzunlukları
cumle = "Python ile veri bilimi araştırması yapmak çok verimli"
# for ile:
uzunluklar_v1 = []
for kelime in cumle.split():
    uzunluklar_v1.append(len(kelime))
# comprehension ile:
uzunluklar_v2 = [len(k) for k in cumle.split()]
print(f"b) Kelime uzunlukları: {uzunluklar_v2}")

# c) Eleman eleman çarpım
a = [1, 2, 3, 4, 5]
b = [10, 20, 30, 40, 50]
# for ile:
carpim_v1 = []
for i in range(len(a)):
    carpim_v1.append(a[i] * b[i])
# comprehension ile:
carpim_v2 = [x * y for x, y in zip(a, b)]
print(f"c) Eleman çarpımı: {carpim_v2}")

# d) Sesli harf içeren kelimeler
kelimeler = ["araba", "trn", "elma", "krk", "inek", "brk", "oda"]
sesliler = set("aeıioöuüAEIİOÖUÜ")
# comprehension ile:
sesli_kelimeler = [k for k in kelimeler if any(h in sesliler for h in k)]
print(f"d) Sesli harf içerenler: {sesli_kelimeler}")

# e) 3 ve 5'e bölünenler
bolunebilen = [s for s in range(1, 101) if s % 3 == 0 and s % 5 == 0]
print(f"e) 3 ve 5'e bölünenler: {bolunebilen}")


# ────────────────────────────────────────────────────────────
# Çözüm 4.4 ★★★ — Öğrenci Sıralama Sistemi
# ────────────────────────────────────────────────────────────

print("\n" + "=" * 50)
print("Çözüm 4.4 — Öğrenci Sıralama Sistemi")
print("=" * 50)

ogrenciler = [
    ("Ayşe Yılmaz", "Biyoloji", [88, 92, 85]),
    ("Mehmet Kaya", "Fizik", [72, 68, 75]),
    ("Fatma Demir", "Kimya", [95, 91, 98]),
    ("Ali Çelik", "Biyoloji", [60, 55, 62]),
    ("Zeynep Ak", "Fizik", [83, 87, 80]),
    ("Can Öz", "Kimya", [78, 82, 76]),
    ("Elif Tan", "Biyoloji", [91, 89, 93]),
    ("Burak Şen", "Fizik", [65, 70, 68]),
]

# a) Ortalama hesapla
ogr_ortalamalar = []
for isim, bolum, notlar in ogrenciler:
    ort = sum(notlar) / len(notlar)
    ogr_ortalamalar.append((isim, bolum, notlar, ort))

# b) Sıralama
sirali = sorted(ogr_ortalamalar, key=lambda x: x[3], reverse=True)

# d) Sınıf ortalaması
sinif_ort = sum(o[3] for o in ogr_ortalamalar) / len(ogr_ortalamalar)
ort_alti = sum(1 for o in ogr_ortalamalar if o[3] < sinif_ort)

# e) Tablo
print(f"\n{'Sıra':>4}  {'İsim':<18} {'Bölüm':<12} {'Ort.':>7}  Durum")
print("─" * 55)
for i, (isim, bolum, notlar, ort) in enumerate(sirali, 1):
    yildiz = "★" if ort >= 90 else ""
    print(f"{i:>4}  {isim:<18} {bolum:<12} {ort:>7.2f}  {yildiz}")

# c) Bölüm birincileri
print(f"\n=== Bölüm Birincileri ===")
bolumler = {}
for isim, bolum, notlar, ort in ogr_ortalamalar:
    if bolum not in bolumler or ort > bolumler[bolum][1]:
        bolumler[bolum] = (isim, ort)

for bolum in sorted(bolumler.keys()):
    isim, ort = bolumler[bolum]
    print(f"  {bolum:<12}: {isim} ({ort:.2f})")

print(f"\nSınıf Ortalaması: {sinif_ort:.2f}")
print(f"Ortalamanın altı: {ort_alti} öğrenci")


# ============================================================
#  HAFTA 5 — Sözlükler, Kümeler ve Fonksiyonlar
# ============================================================

# ────────────────────────────────────────────────────────────
# Çözüm 5.1 ★ — Deney Envanteri
# ────────────────────────────────────────────────────────────

print("\n" + "=" * 50)
print("Çözüm 5.1 — Deney Envanteri")
print("=" * 50)

envanter = {
    "pipet_ucu_1000": {"stok": 500, "min_stok": 100, "birim_fiyat": 0.25},
    "eldiven_M": {"stok": 45, "min_stok": 50, "birim_fiyat": 1.20},
    "etanol_96": {"stok": 12, "min_stok": 5, "birim_fiyat": 45.00},
    "petri_kabi": {"stok": 30, "min_stok": 50, "birim_fiyat": 3.50},
    "santrifuj_tupu": {"stok": 200, "min_stok": 100, "birim_fiyat": 0.80},
}

# a) Tablo
print(f"\n{'Ürün':<20} {'Stok':>5} {'Min':>5} {'Fiyat':>8} {'Değer':>10} {'Durum':>10}")
print("─" * 62)

toplam_deger = 0
siparis_listesi = []

for urun, bilgi in envanter.items():
    deger = bilgi["stok"] * bilgi["birim_fiyat"]
    toplam_deger += deger
    durum = "✓ OK" if bilgi["stok"] >= bilgi["min_stok"] else "⚠ DÜŞÜK"
    print(f"{urun:<20} {bilgi['stok']:>5} {bilgi['min_stok']:>5} "
          f"{bilgi['birim_fiyat']:>8.2f} {deger:>10.2f} {durum:>10}")

    # e) Sipariş listesi
    if bilgi["stok"] < bilgi["min_stok"]:
        ihtiyac = bilgi["min_stok"] - bilgi["stok"]
        maliyet = ihtiyac * bilgi["birim_fiyat"]
        siparis_listesi.append((urun, ihtiyac, maliyet))

# b) Uyarılar
if siparis_listesi:
    print(f"\n⚠ SİPARİŞ GEREKLİ:")
    for urun, ihtiyac, maliyet in siparis_listesi:
        print(f"  {urun}: {ihtiyac} adet gerekli (tahmini maliyet: {maliyet:.2f} TL)")

# c) Toplam
print(f"\nToplam envanter değeri: {toplam_deger:.2f} TL")

# d) Stok ekleme
def stok_ekle(envanter, urun, miktar):
    if urun in envanter:
        envanter[urun]["stok"] += miktar
        print(f"  {urun}: +{miktar} eklendi → yeni stok: {envanter[urun]['stok']}")
    else:
        print(f"  Ürün bulunamadı: {urun}")

print()
stok_ekle(envanter, "eldiven_M", 100)


# ────────────────────────────────────────────────────────────
# Çözüm 5.2 ★★ — Anket Analizi (Küme İşlemleri)
# ────────────────────────────────────────────────────────────

print("\n" + "=" * 50)
print("Çözüm 5.2 — Anket Analizi (Küme İşlemleri)")
print("=" * 50)

python_ws = {"Ayşe", "Mehmet", "Fatma", "Ali", "Zeynep", "Can"}
istatistik_ws = {"Mehmet", "Fatma", "Elif", "Burak", "Zeynep"}
ml_ws = {"Fatma", "Ali", "Elif", "Can", "Deniz"}

# a) Kayıt sayıları
print(f"\nPython: {len(python_ws)}, İstatistik: {len(istatistik_ws)}, ML: {len(ml_ws)}")

# b) Toplam benzersiz
tumu = python_ws | istatistik_ws | ml_ws
print(f"Toplam benzersiz öğrenci: {len(tumu)}")

# c) Üçüne de katılan
ucune_de = python_ws & istatistik_ws & ml_ws
print(f"Üçüne de katılan: {ucune_de}")

# d) Sadece Python
sadece_python = python_ws - istatistik_ws - ml_ws
print(f"Sadece Python: {sadece_python}")

# e) Python & İstatistik, ML hariç
py_ist_ml_haric = (python_ws & istatistik_ws) - ml_ws
print(f"Python & İstatistik (ML hariç): {py_ist_ml_haric}")

# f) Tam olarak 2 workshop
# İki workshop'un kesişiminde olup üçüncüde olmayanların birleşimi
tam_iki = set()
for kisi in tumu:
    sayac = (kisi in python_ws) + (kisi in istatistik_ws) + (kisi in ml_ws)
    if sayac == 2:
        tam_iki.add(kisi)
print(f"Tam olarak 2 workshop: {tam_iki}")

# g) Sadece 1 workshop
sadece_bir = set()
for kisi in tumu:
    sayac = (kisi in python_ws) + (kisi in istatistik_ws) + (kisi in ml_ws)
    if sayac == 1:
        sadece_bir.add(kisi)
print(f"Sadece 1 workshop: {sadece_bir}")


# ────────────────────────────────────────────────────────────
# Çözüm 5.3 ★★ — Fonksiyon Fabrikası
# ────────────────────────────────────────────────────────────

print("\n" + "=" * 50)
print("Çözüm 5.3 — Fonksiyon Fabrikası")
print("=" * 50)

def ortalama(*sayilar):
    return sum(sayilar) / len(sayilar)

def standart_sapma(*sayilar):
    ort = ortalama(*sayilar)
    varyans = sum((x - ort) ** 2 for x in sayilar) / len(sayilar)
    return math.sqrt(varyans)

def z_skoru(deger, ort, std):
    if std == 0:
        return 0
    return (deger - ort) / std

def normallesir(liste, yontem="minmax"):
    if yontem == "minmax":
        mn, mx = min(liste), max(liste)
        aralik = mx - mn
        if aralik == 0:
            return [0] * len(liste)
        return [(x - mn) / aralik for x in liste]
    elif yontem == "zscore":
        ort = ortalama(*liste)
        std = standart_sapma(*liste)
        return [z_skoru(x, ort, std) for x in liste]

def aykiri_bul(liste, esik=2.0):
    ort = ortalama(*liste)
    std = standart_sapma(*liste)
    return [x for x in liste if abs(z_skoru(x, ort, std)) > esik]

# Test
veri = [12, 15, 18, 22, 25, 28, 31, 35, 120]

ort = ortalama(*veri)
std = standart_sapma(*veri)
z_skorlari = [round(z_skoru(x, ort, std), 2) for x in veri]
minmax = [round(x, 2) for x in normallesir(veri, "minmax")]
aykirilar = aykiri_bul(veri, esik=2.0)

print(f"\nVeri: {veri}")
print(f"Ortalama: {ort:.2f}")
print(f"Std: {std:.2f}")
print(f"Z-skorları: {z_skorlari}")
print(f"Min-Max normalize: {minmax}")
print(f"Aykırı değerler (|z| > 2): {aykirilar}")


# ────────────────────────────────────────────────────────────
# Çözüm 5.4 ★★★ — Kelime Bulutu Hazırlığı
# ────────────────────────────────────────────────────────────

print("\n" + "=" * 50)
print("Çözüm 5.4 — Kelime Bulutu Hazırlığı")
print("=" * 50)

abstract = """
Machine learning algorithms have revolutionized the field of
data science and artificial intelligence. Deep learning models,
particularly neural networks, have shown remarkable performance
in image recognition, natural language processing, and predictive
analytics. This study examines the application of machine learning
techniques in medical diagnosis, focusing on the accuracy of deep
learning models compared to traditional statistical methods.
Our results demonstrate that deep learning achieves significantly
higher accuracy in complex pattern recognition tasks.
"""

stopwords = {"the", "a", "an", "of", "in", "and", "to", "that",
             "this", "have", "has", "had", "on", "for", "our",
             "is", "are", "was", "were", "been", "be", "its"}

# a) Temizleme
temiz_kelimeler = []
for kelime in abstract.lower().split():
    temiz = kelime.strip(".,;:!?()\"'")
    if temiz:
        temiz_kelimeler.append(temiz)

# b) Stopword filtreleme
filtreli = [k for k in temiz_kelimeler if k not in stopwords]

# c) Kelime frekansları
frekans = {}
for kelime in filtreli:
    frekans[kelime] = frekans.get(kelime, 0) + 1

# d) En sık 10
sirali = sorted(frekans.items(), key=lambda x: x[1], reverse=True)
print(f"\n=== En Sık 10 Kelime ===")
for kelime, sayi in sirali[:10]:
    bar = "████" * sayi
    print(f"  {kelime:<18} {bar} {sayi}")

# e) Bigram frekansları
bigram_frekans = {}
for i in range(len(filtreli) - 1):
    bigram = f"{filtreli[i]} {filtreli[i+1]}"
    bigram_frekans[bigram] = bigram_frekans.get(bigram, 0) + 1

bigram_sirali = sorted(bigram_frekans.items(), key=lambda x: x[1], reverse=True)
print(f"\n=== En Sık 5 Bigram ===")
for bigram, sayi in bigram_sirali[:5]:
    bar = "████" * sayi
    print(f"  {bigram:<22} {bar} {sayi}")


# ============================================================
#  HAFTA 6 — Dosya İşlemleri ve Hata Yönetimi
# ============================================================

# ────────────────────────────────────────────────────────────
# Çözüm 6.1 ★ — Log Dosyası Analizi
# ────────────────────────────────────────────────────────────

print("\n" + "=" * 50)
print("Çözüm 6.1 — Log Dosyası Analizi")
print("=" * 50)

log_verileri = [
    "2024-03-15 08:00:12 INFO  Sistem başlatıldı",
    "2024-03-15 08:05:23 INFO  Kullanıcı girişi: ahmet",
    "2024-03-15 08:12:45 WARN  Disk kullanımı %85",
    "2024-03-15 08:30:01 ERROR Veritabanı bağlantısı kesildi",
    "2024-03-15 08:30:15 INFO  Veritabanı yeniden bağlandı",
    "2024-03-15 09:00:00 INFO  Yedekleme başladı",
    "2024-03-15 09:15:33 WARN  Yedekleme yavaş",
    "2024-03-15 09:30:00 INFO  Yedekleme tamamlandı",
    "2024-03-15 10:00:12 ERROR Bellek yetersiz",
    "2024-03-15 10:05:00 WARN  Servis yeniden başlatılıyor",
    "2024-03-15 10:05:30 INFO  Servis başlatıldı",
]

# a) Log dosyasını oluştur
log_yolu = os.path.join(ORNEK_DIR, "sistem.log")
with open(log_yolu, "w", encoding="utf-8") as f:
    for satir in log_verileri:
        f.write(satir + "\n")

# b) Analiz
seviye_sayac = {}
hatalar = []
ilk_zaman = None
son_zaman = None

with open(log_yolu, "r", encoding="utf-8") as f:
    for satir in f:
        satir = satir.strip()
        parcalar = satir.split()
        zaman = parcalar[1]
        seviye = parcalar[2]

        if ilk_zaman is None:
            ilk_zaman = zaman
        son_zaman = zaman

        seviye_sayac[seviye] = seviye_sayac.get(seviye, 0) + 1

        if seviye == "ERROR":
            hatalar.append(satir)

print(f"\n=== Log Analizi ===")
print(f"Toplam kayıt:  {sum(seviye_sayac.values())}")
for seviye in ["INFO", "WARN", "ERROR"]:
    print(f"  {seviye}:  {seviye_sayac.get(seviye, 0)}")

# c) Error'ları ayrı dosyaya yaz
error_yolu = os.path.join(ORNEK_DIR, "errors.log")
with open(error_yolu, "w", encoding="utf-8") as f:
    for hata in hatalar:
        f.write(hata + "\n")
print(f"\nHata kayıtları → {error_yolu}")

# d) Zaman aralığı
print(f"Zaman aralığı: {ilk_zaman} - {son_zaman}")


# ────────────────────────────────────────────────────────────
# Çözüm 6.2 ★★ — CSV Araştırma Verisi İşleyici
# ────────────────────────────────────────────────────────────

print("\n" + "=" * 50)
print("Çözüm 6.2 — CSV Araştırma Verisi İşleyici")
print("=" * 50)

baslik = ["denek_id", "yas", "cinsiyet", "grup", "pre_test", "post_test"]
veriler = [
    ["D001", 25, "K", "deney",   45, 72],
    ["D002", 31, "E", "kontrol", 52, 55],
    ["D003", 28, "K", "deney",   38, 68],
    ["D004", 35, "E", "deney",   41, 75],
    ["D005", 22, "K", "kontrol", 48, 50],
    ["D006", 29, "E", "kontrol", 55, 58],
    ["D007", 33, "K", "deney",   43, 71],
    ["D008", 27, "E", "kontrol", 50, 52],
    ["D009", 30, "K", "deney",   39, 69],
    ["D010", 26, "E", "kontrol", 47, 49],
]

# a) CSV yaz
csv_yolu = os.path.join(ORNEK_DIR, "arastirma_verisi.csv")
with open(csv_yolu, "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(baslik)
    writer.writerows(veriler)

# b-d) Analiz
grup_verileri = {"deney": [], "kontrol": []}
cinsiyet_verileri = {"K": [], "E": []}

with open(csv_yolu, "r", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    analiz_satirlari = []

    for satir in reader:
        pre = int(satir["pre_test"])
        post = int(satir["post_test"])
        fark = post - pre

        analiz_satirlari.append({**satir, "fark": fark})

        grup_verileri[satir["grup"]].append({"pre": pre, "post": post, "fark": fark})
        cinsiyet_verileri[satir["cinsiyet"]].append(fark)

print(f"\n=== Araştırma Sonuçları ===\n")
print("Grup Karşılaştırması:")
for grup, veri_listesi in grup_verileri.items():
    n = len(veri_listesi)
    pre_ort = sum(v["pre"] for v in veri_listesi) / n
    post_ort = sum(v["post"] for v in veri_listesi) / n
    fark_ort = sum(v["fark"] for v in veri_listesi) / n
    print(f"  {grup.title() + ' grubu':<16} (n={n}): Pre={pre_ort:.1f}, "
          f"Post={post_ort:.1f}, Fark=+{fark_ort:.1f}")

deney_fark = sum(v["fark"] for v in grup_verileri["deney"]) / len(grup_verileri["deney"])
kontrol_fark = sum(v["fark"] for v in grup_verileri["kontrol"]) / len(grup_verileri["kontrol"])
print(f"  Gruplar arası fark: {deney_fark - kontrol_fark:.1f} puan")

print(f"\nCinsiyet Karşılaştırması:")
for cinsiyet, farklar in cinsiyet_verileri.items():
    etiket = "Kadın" if cinsiyet == "K" else "Erkek"
    ort_fark = sum(farklar) / len(farklar)
    print(f"  {etiket} (n={len(farklar)}): Ortalama fark=+{ort_fark:.1f}")

# e) Sonuçları yeni CSV'ye yaz
sonuc_yolu = os.path.join(ORNEK_DIR, "analiz_sonuclari.csv")
with open(sonuc_yolu, "w", newline="", encoding="utf-8") as f:
    alanlar = list(analiz_satirlari[0].keys())
    writer = csv.DictWriter(f, fieldnames=alanlar)
    writer.writeheader()
    writer.writerows(analiz_satirlari)

print(f"\nSonuçlar '{sonuc_yolu}' dosyasına kaydedildi.")


# ────────────────────────────────────────────────────────────
# Çözüm 6.3 ★★ — JSON Konfigürasyon Yöneticisi
# ────────────────────────────────────────────────────────────

print("\n" + "=" * 50)
print("Çözüm 6.3 — JSON Konfigürasyon Yöneticisi")
print("=" * 50)

def varsayilan_config():
    return {
        "proje_adi": "Yeni Araştırma",
        "arastirmaci": "Bilinmiyor",
        "veri_klasoru": "./veri",
        "cikti_klasoru": "./sonuclar",
        "parametreler": {
            "alfa": 0.05,
            "iterasyon": 1000,
            "seed": 42
        },
        "log_seviyesi": "INFO",
        "otomatik_yedekleme": True
    }

def config_yukle(dosya_yolu):
    try:
        with open(dosya_yolu, "r", encoding="utf-8") as f:
            config = json.load(f)
            print(f"  Config yüklendi: {config['proje_adi']}")
            return config
    except FileNotFoundError:
        print("  Config dosyası bulunamadı, varsayılan oluşturuluyor...")
        config = varsayilan_config()
        config_kaydet(config, dosya_yolu)
        return config

def config_guncelle(config, **kwargs):
    for anahtar, deger in kwargs.items():
        config[anahtar] = deger
        print(f"  Güncelleme: {anahtar} → \"{deger}\"")
    return config

def config_kaydet(config, dosya_yolu):
    with open(dosya_yolu, "w", encoding="utf-8") as f:
        json.dump(config, f, ensure_ascii=False, indent=2)
    print(f"  Config kaydedildi: {dosya_yolu}")

# Test
config_yolu = os.path.join(ORNEK_DIR, "config.json")

# Önceki dosyayı sil (temiz test için)
if os.path.exists(config_yolu):
    os.remove(config_yolu)

print()
config = config_yukle(config_yolu)
config = config_guncelle(config,
                         proje_adi="Sıcaklık Etkisi Deneyi",
                         arastirmaci="Dr. Yılmaz")
config_kaydet(config, config_yolu)

print(f"\nGüncel config:")
print(json.dumps(config, ensure_ascii=False, indent=2))


# ────────────────────────────────────────────────────────────
# Çözüm 6.4 ★★★ — Güvenli Veri Okuyucu
# ────────────────────────────────────────────────────────────

print("\n" + "=" * 50)
print("Çözüm 6.4 — Güvenli Veri Okuyucu")
print("=" * 50)

kirli_veri = '''denek_id,yas,boy,kilo,kan_basinci
D001,25,1.75,70,120/80
D002,abc,1.68,65,130/85
D003,28,,72,125/82
D004,35,1.80,HATA,118/76
D005,-5,1.72,68,140/90
D006,42,1.65,58,
D007,30,1.78,82,135/88
D008,999,1.70,75,122/78
'''

# Kirli veriyi dosyaya yaz
kirli_yolu = os.path.join(ORNEK_DIR, "kirli_veri.csv")
with open(kirli_yolu, "w", encoding="utf-8") as f:
    f.write(kirli_veri)

temiz_kayitlar = []
hata_log = []

with open(kirli_yolu, "r", encoding="utf-8") as f:
    reader = csv.DictReader(f)

    for satir_no, satir in enumerate(reader, start=2):
        denek_id = satir["denek_id"]
        hatalar = []

        # Yaş kontrolü
        try:
            yas = int(satir["yas"])
            if yas < 0 or yas > 120:
                hatalar.append(f"Geçersiz yaş: {yas}")
        except ValueError:
            hatalar.append(f"Yaş sayısal değil: '{satir['yas']}'")

        # Boy kontrolü
        if not satir["boy"].strip():
            hatalar.append("Eksik değer: boy")
        else:
            try:
                float(satir["boy"])
            except ValueError:
                hatalar.append(f"Boy sayısal değil: '{satir['boy']}'")

        # Kilo kontrolü
        try:
            float(satir["kilo"])
        except ValueError:
            hatalar.append(f"Kilo sayısal değil: '{satir['kilo']}'")

        # Kan basıncı kontrolü
        if not satir["kan_basinci"].strip():
            hatalar.append("Eksik değer: kan_basinci")

        if hatalar:
            for hata in hatalar:
                hata_log.append(f"Satır {satir_no} ({denek_id}): {hata}")
        else:
            temiz_kayitlar.append(satir)

# Rapor
toplam = len(kirli_veri.strip().split("\n")) - 1  # başlık hariç
print(f"\n=== Veri Temizleme Raporu ===")
print(f"Toplam satır:     {toplam}")
print(f"Temiz satır:      {len(temiz_kayitlar)}")
print(f"Hatalı satır:     {toplam - len(temiz_kayitlar)}")

print(f"\nHatalar:")
for hata in hata_log:
    print(f"  {hata}")

# Temiz veriyi yaz
temiz_yolu = os.path.join(ORNEK_DIR, "temiz_veri.csv")
if temiz_kayitlar:
    with open(temiz_yolu, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=temiz_kayitlar[0].keys())
        writer.writeheader()
        writer.writerows(temiz_kayitlar)

# Hata logunu yaz
hata_yolu = os.path.join(ORNEK_DIR, "hata_log.txt")
with open(hata_yolu, "w", encoding="utf-8") as f:
    for hata in hata_log:
        f.write(hata + "\n")

print(f"\nTemiz veri → {temiz_yolu} ({len(temiz_kayitlar)} kayıt)")
print(f"Hata logu → {hata_yolu}")


# ============================================================
# BONUS ÇÖZÜMLER
# ============================================================

# ────────────────────────────────────────────────────────────
# Bonus 1 ★★★ — Mini Veritabanı Sistemi
# ────────────────────────────────────────────────────────────

print("\n" + "=" * 50)
print("Bonus 1 — Mini Veritabanı Sistemi")
print("=" * 50)

def vt_ekle(db, kayit):
    db.append(kayit)

def vt_sil(db, alan, deger):
    db[:] = [k for k in db if k.get(alan) != deger]

def vt_filtre(db, **kriterler):
    sonuc = db
    for alan, deger in kriterler.items():
        sonuc = [k for k in sonuc if k.get(alan) == deger]
    return sonuc

def vt_sirala(db, alan, ters=False):
    return sorted(db, key=lambda k: k[alan], reverse=ters)

def vt_grupla(db, alan):
    gruplar = {}
    for kayit in db:
        anahtar = kayit[alan]
        if anahtar not in gruplar:
            gruplar[anahtar] = []
        gruplar[anahtar].append(kayit)
    return gruplar

def vt_ozet(db, sayisal_alan):
    degerler = [k[sayisal_alan] for k in db]
    n = len(degerler)
    ort = sum(degerler) / n
    mn = min(degerler)
    mx = max(degerler)
    std = math.sqrt(sum((x - ort) ** 2 for x in degerler) / n)
    return {"n": n, "ortalama": ort, "min": mn, "max": mx, "std": std}

def vt_kaydet(db, dosya_yolu):
    with open(dosya_yolu, "w", encoding="utf-8") as f:
        json.dump(db, f, ensure_ascii=False, indent=2)

def vt_yukle(dosya_yolu):
    with open(dosya_yolu, "r", encoding="utf-8") as f:
        return json.load(f)

# Test
db = []
vt_ekle(db, {"ad": "Ayşe", "bolum": "Biyoloji", "puan": 88, "yil": 2})
vt_ekle(db, {"ad": "Mehmet", "bolum": "Fizik", "puan": 72, "yil": 3})
vt_ekle(db, {"ad": "Fatma", "bolum": "Biyoloji", "puan": 95, "yil": 1})
vt_ekle(db, {"ad": "Ali", "bolum": "Fizik", "puan": 65, "yil": 2})
vt_ekle(db, {"ad": "Zeynep", "bolum": "Kimya", "puan": 82, "yil": 1})

# Filtreleme
bio = vt_filtre(db, bolum="Biyoloji")
print(f"\nBiyoloji öğrencileri:")
for ogr in bio:
    print(f"  {ogr['ad']} ({ogr['puan']})")

# Sıralama
sirali = vt_sirala(db, "puan", ters=True)
print(f"\nPuana göre (azalan):")
print("  " + ", ".join(f"{o['ad']}: {o['puan']}" for o in sirali))

# Gruplama
gruplar = vt_grupla(db, "bolum")
print(f"\nBölüm grupları:")
for bolum, ogrenciler in sorted(gruplar.items()):
    puanlar = [o["puan"] for o in ogrenciler]
    ort = sum(puanlar) / len(puanlar)
    print(f"  {bolum}: {len(ogrenciler)} öğrenci, ort: {ort:.1f}")

# Özet
ozet = vt_ozet(db, "puan")
print(f"\nPuan özeti: ort={ozet['ortalama']:.1f}, min={ozet['min']}, "
      f"max={ozet['max']}, std={ozet['std']:.2f}")

# Kaydetme
db_yolu = os.path.join(ORNEK_DIR, "ogrenci_db.json")
vt_kaydet(db, db_yolu)
print(f"\nVeritabanı kaydedildi → {db_yolu}")
