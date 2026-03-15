"""
============================================================
  BÖLÜM 2 — VERİ YAPILARI VE FONKSİYONLAR
  Hafta 6: Dosya İşlemleri ve Hata Yönetimi
============================================================

İçindekiler:
  6.1  Dosya okuma (open, read, readline, readlines)
  6.2  Dosya yazma (write, writelines)
  6.3  with bloğu ve dosya modları
  6.4  CSV dosyaları ile çalışma
  6.5  JSON dosyaları ile çalışma
  6.6  try, except, finally — hata yönetimi
  6.7  Hata türleri ve özel hatalar
  6.8  Uygulamalar
============================================================
"""

import os

# Örnek dosyalar için geçici klasör
ORNEK_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "ornek_dosyalar")
os.makedirs(ORNEK_DIR, exist_ok=True)


# ============================================================
# 6.1 — DOSYA OKUMA
# ============================================================

print("=== Dosya Okuma ===\n")

# Önce bir örnek dosya oluşturalım
dosya_yolu = os.path.join(ORNEK_DIR, "deneme.txt")
with open(dosya_yolu, "w", encoding="utf-8") as f:
    f.write("Birinci satır: Python programlama\n")
    f.write("İkinci satır: Veri bilimi\n")
    f.write("Üçüncü satır: Makine öğrenmesi\n")
    f.write("Dördüncü satır: İstatistik\n")
    f.write("Beşinci satır: Araştırma yöntemleri\n")

# --- read() — tüm dosyayı oku ---
print("--- read() ---")
dosya = open(dosya_yolu, "r", encoding="utf-8")
icerik = dosya.read()
dosya.close()           # Dosyayı kapatmayı unutmayın!
print(icerik)

# --- readline() — tek satır oku ---
print("--- readline() ---")
dosya = open(dosya_yolu, "r", encoding="utf-8")
satir1 = dosya.readline()
satir2 = dosya.readline()
print(f"Satır 1: {satir1.strip()}")
print(f"Satır 2: {satir2.strip()}")
dosya.close()

# --- readlines() — tüm satırları liste olarak oku ---
print("\n--- readlines() ---")
dosya = open(dosya_yolu, "r", encoding="utf-8")
satirlar = dosya.readlines()
dosya.close()
print(f"Satır sayısı: {len(satirlar)}")
print(f"İlk satır:    {satirlar[0].strip()}")

# --- for döngüsü ile satır satır (en verimli yol) ---
print("\n--- for döngüsü ---")
dosya = open(dosya_yolu, "r", encoding="utf-8")
for i, satir in enumerate(dosya, 1):
    print(f"  {i}: {satir.strip()}")
dosya.close()


# ============================================================
# 6.2 — DOSYA YAZMA
# ============================================================

print("\n\n=== Dosya Yazma ===\n")

# --- write() ---
cikti_yolu = os.path.join(ORNEK_DIR, "cikti.txt")
dosya = open(cikti_yolu, "w", encoding="utf-8")    # "w" = yazma modu (üzerine yazar)
dosya.write("Bu ilk satır.\n")
dosya.write("Bu ikinci satır.\n")
dosya.close()
print(f"'{cikti_yolu}' oluşturuldu.")

# --- "a" modu — ekleme (append) ---
dosya = open(cikti_yolu, "a", encoding="utf-8")
dosya.write("Bu eklenen satır.\n")
dosya.close()

# --- writelines() — liste olarak yazma ---
satirlar = ["Satır A\n", "Satır B\n", "Satır C\n"]
dosya = open(cikti_yolu, "a", encoding="utf-8")
dosya.writelines(satirlar)
dosya.close()

# Sonucu okuyalım
with open(cikti_yolu, "r", encoding="utf-8") as f:
    print(f.read())

# --- Dosya modları ---
# "r"  → Okuma (varsayılan). Dosya yoksa hata.
# "w"  → Yazma. Dosya varsa siler, yoksa oluşturur.
# "a"  → Ekleme. Dosyanın sonuna yazar.
# "x"  → Oluşturma. Dosya varsa hata verir.
# "r+" → Okuma + Yazma.
# "b"  → Binary mod (örn: "rb", "wb")


# ============================================================
# 6.3 — with BLOĞU
# ============================================================

print("\n=== with Bloğu ===\n")

# with bloğu dosyayı otomatik kapatır.
# Manuel close() çağırmaya gerek kalmaz.
# Hata oluşsa bile dosya güvenle kapatılır.

# ÖNERİLEN YOL — her zaman with kullanın:
with open(dosya_yolu, "r", encoding="utf-8") as dosya:
    for satir in dosya:
        print(f"  {satir.strip()}")

# 'dosya' değişkeni burada hala erişilebilir ama kapalıdır
print(f"\nDosya kapalı mı? {dosya.closed}")  # True

# --- Birden fazla dosya ile çalışma ---
girdi_yolu = dosya_yolu
cikti_yolu2 = os.path.join(ORNEK_DIR, "kopya.txt")

with open(girdi_yolu, "r", encoding="utf-8") as girdi, \
     open(cikti_yolu2, "w", encoding="utf-8") as cikti:
    for satir in girdi:
        cikti.write(satir.upper())

print("\nKopya dosyası (büyük harfle):")
with open(cikti_yolu2, "r", encoding="utf-8") as f:
    print(f.read())


# ============================================================
# 6.4 — CSV DOSYALARI İLE ÇALIŞMA
# ============================================================

print("=== CSV Dosyaları ===\n")

import csv

# --- CSV yazma ---
csv_yolu = os.path.join(ORNEK_DIR, "denekler.csv")

veriler = [
    ["denek_id", "yas", "grup", "olcum_1", "olcum_2"],
    ["D001", 25, "kontrol", 23.5, 24.1],
    ["D002", 31, "deney", 28.3, 29.7],
    ["D003", 28, "kontrol", 22.8, 23.2],
    ["D004", 35, "deney", 30.1, 31.5],
    ["D005", 22, "deney", 27.6, 28.9],
    ["D006", 29, "kontrol", 24.0, 23.8],
]

with open(csv_yolu, "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerows(veriler)
print(f"'{csv_yolu}' oluşturuldu.")

# --- CSV okuma (csv.reader) ---
print("\n--- csv.reader ---")
with open(csv_yolu, "r", encoding="utf-8") as f:
    reader = csv.reader(f)
    baslik = next(reader)     # İlk satır = başlık
    print(f"Sütunlar: {baslik}")

    for satir in reader:
        print(f"  {satir}")

# --- CSV okuma (csv.DictReader — sözlük olarak) ---
print("\n--- csv.DictReader ---")
with open(csv_yolu, "r", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for satir in reader:
        print(f"  {satir['denek_id']}: yaş={satir['yas']}, "
              f"grup={satir['grup']}, ölçüm1={satir['olcum_1']}")

# --- CSV DictWriter ile yazma ---
csv_yolu2 = os.path.join(ORNEK_DIR, "sonuclar.csv")
alanlar = ["denek_id", "ortalama", "durum"]

with open(csv_yolu2, "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=alanlar)
    writer.writeheader()
    writer.writerow({"denek_id": "D001", "ortalama": 23.8, "durum": "normal"})
    writer.writerow({"denek_id": "D002", "ortalama": 29.0, "durum": "yüksek"})

print(f"\n'{csv_yolu2}' oluşturuldu.")

# --- Manuel CSV okuma (csv modülü olmadan) ---
print("\n--- Manuel CSV okuma ---")
with open(csv_yolu, "r", encoding="utf-8") as f:
    for i, satir in enumerate(f):
        parcalar = satir.strip().split(",")
        if i == 0:
            print(f"  Başlık: {parcalar}")
        else:
            print(f"  Satır {i}: {parcalar}")


# ============================================================
# 6.5 — JSON DOSYALARI İLE ÇALIŞMA
# ============================================================

print("\n\n=== JSON Dosyaları ===\n")

import json

# JSON (JavaScript Object Notation):
# - API'lerden gelen verinin standart formatı
# - Python sözlük/liste yapısına çok benzer
# - İnsan tarafından okunabilir

# --- Python nesnesi → JSON string ---
deney = {
    "baslik": "Sıcaklık Etkisi Deneyi",
    "tarih": "2024-03-15",
    "arastirmaci": "Dr. Yılmaz",
    "denek_sayisi": 30,
    "parametreler": {
        "sicaklik": [20, 25, 30, 35],
        "nem": 60
    },
    "sonuclar": [
        {"grup": "kontrol", "ortalama": 23.5, "std": 2.1},
        {"grup": "deney", "ortalama": 28.7, "std": 3.4}
    ]
}

# json.dumps() — Python dict → JSON string
json_str = json.dumps(deney, ensure_ascii=False, indent=2)
print("JSON string:")
print(json_str)

# --- JSON dosyaya yazma ---
json_yolu = os.path.join(ORNEK_DIR, "deney.json")
with open(json_yolu, "w", encoding="utf-8") as f:
    json.dump(deney, f, ensure_ascii=False, indent=2)
print(f"\n'{json_yolu}' oluşturuldu.")

# --- JSON dosyadan okuma ---
print("\n--- JSON okuma ---")
with open(json_yolu, "r", encoding="utf-8") as f:
    okunan = json.load(f)

print(f"Başlık: {okunan['baslik']}")
print(f"Araştırmacı: {okunan['arastirmaci']}")
print(f"Denek sayısı: {okunan['denek_sayisi']}")

for sonuc in okunan["sonuclar"]:
    print(f"  {sonuc['grup']}: ort={sonuc['ortalama']}, std={sonuc['std']}")

# --- json.loads() — JSON string → Python dict ---
json_metin = '{"ad": "Ayşe", "yas": 28, "aktif": true}'
python_dict = json.loads(json_metin)
print(f"\nJSON → Python: {python_dict}")
print(f"Tip: {type(python_dict)}")

# JSON ↔ Python tip eşleşmesi:
# JSON    → Python
# object  → dict
# array   → list
# string  → str
# number  → int / float
# true    → True
# false   → False
# null    → None


# ============================================================
# 6.6 — try, except, finally — HATA YÖNETİMİ
# ============================================================

print("\n\n=== Hata Yönetimi ===\n")

# Python'da hatalar (exceptions) programı durdurur.
# try-except ile hataları yakalayıp yönetebiliriz.

# --- Temel try-except ---
print("--- Temel try-except ---")
try:
    sonuc = 10 / 0
except ZeroDivisionError:
    print("Hata: Sıfıra bölme yapılamaz!")

# --- Hata mesajını yakalama ---
print("\n--- Hata mesajı ---")
try:
    sayi = int("abc")
except ValueError as e:
    print(f"Hata yakalandı: {e}")

# --- Birden fazla hata türü ---
print("\n--- Birden fazla except ---")
def guvenli_bol(a, b):
    try:
        sonuc = a / b
        return sonuc
    except ZeroDivisionError:
        print("  Hata: Sıfıra bölünemez!")
        return None
    except TypeError:
        print("  Hata: Geçersiz veri tipi!")
        return None

print(f"10 / 3 = {guvenli_bol(10, 3)}")
print(f"10 / 0 = {guvenli_bol(10, 0)}")
print(f"10 / 'a' = {guvenli_bol(10, 'a')}")

# --- try-except-else-finally ---
print("\n--- try-except-else-finally ---")

def dosya_oku(yol):
    try:
        f = open(yol, "r", encoding="utf-8")
        icerik = f.read()
    except FileNotFoundError:
        print(f"  Dosya bulunamadı: {yol}")
    except PermissionError:
        print(f"  Dosya izni yok: {yol}")
    else:
        # Hata OLMADIĞINDA çalışır
        print(f"  Dosya başarıyla okundu ({len(icerik)} karakter)")
    finally:
        # Her durumda çalışır (hata olsa da olmasa da)
        print("  İşlem tamamlandı.")

dosya_oku(dosya_yolu)
print()
dosya_oku("/var/olmayan_dosya.txt")

# --- Genel hata yakalama ---
print("\n--- Genel hata yakalama ---")
try:
    x = [1, 2, 3]
    print(x[10])
except Exception as e:
    print(f"Bir hata oluştu: {type(e).__name__}: {e}")


# ============================================================
# 6.7 — HATA TÜRLERİ VE ÖZEL HATALAR
# ============================================================

print("\n\n=== Yaygın Hata Türleri ===\n")

# Yaygın hata türleri
hatalar = {
    "ValueError":      "Yanlış değer:     int('abc')",
    "TypeError":       "Yanlış tip:       '2' + 2",
    "IndexError":      "Geçersiz indeks:  [1,2,3][10]",
    "KeyError":        "Geçersiz anahtar: {}['yok']",
    "FileNotFoundError": "Dosya yok:      open('yok.txt')",
    "ZeroDivisionError": "Sıfıra bölme:  1/0",
    "AttributeError":  "Yanlış metod:    (5).append(1)",
    "NameError":       "Tanımsız değişken: print(xyz)",
    "ImportError":     "Modül bulunamadı: import yok_modul",
}

for hata, aciklama in hatalar.items():
    print(f"  {hata:<22} → {aciklama}")

# --- raise: Manuel hata fırlatma ---
print("\n--- raise ---")

def yas_kontrol(yas):
    if not isinstance(yas, (int, float)):
        raise TypeError(f"Yaş sayı olmalı, {type(yas).__name__} verildi")
    if yas < 0 or yas > 150:
        raise ValueError(f"Geçersiz yaş: {yas}")
    return True

try:
    yas_kontrol(25)
    print("  25 → Geçerli")
    yas_kontrol(-5)
except ValueError as e:
    print(f"  Hata: {e}")

try:
    yas_kontrol("yirmi")
except TypeError as e:
    print(f"  Hata: {e}")


# ============================================================
# 6.8 — UYGULAMALAR
# ============================================================

print("\n" + "=" * 50)
print("UYGULAMALAR")
print("=" * 50)

# ----- Uygulama 1: Not Defteri (Dosya Tabanlı) -----
print("\n--- Uygulama 1: Not Defteri ---")

notlar_yolu = os.path.join(ORNEK_DIR, "notlar.txt")

def not_ekle(dosya_yolu, not_metni):
    from datetime import datetime
    zaman = datetime.now().strftime("%Y-%m-%d %H:%M")
    with open(dosya_yolu, "a", encoding="utf-8") as f:
        f.write(f"[{zaman}] {not_metni}\n")
    print(f"  Not eklendi: {not_metni}")

def notlari_goster(dosya_yolu):
    try:
        with open(dosya_yolu, "r", encoding="utf-8") as f:
            icerik = f.read()
            if icerik.strip():
                print(icerik)
            else:
                print("  Henüz not yok.")
    except FileNotFoundError:
        print("  Not dosyası bulunamadı.")

not_ekle(notlar_yolu, "Deney protokolü güncellendi")
not_ekle(notlar_yolu, "Lab toplantısı saat 14:00")
not_ekle(notlar_yolu, "Makale taslağı Dr. Yılmaz'a gönderildi")
print()
notlari_goster(notlar_yolu)


# ----- Uygulama 2: Deney Verisi İşleme -----
print("--- Uygulama 2: CSV Veri İşleme ---")

with open(csv_yolu, "r", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    kontrol = []
    deney_grubu = []

    for satir in reader:
        ort = (float(satir["olcum_1"]) + float(satir["olcum_2"])) / 2
        if satir["grup"] == "kontrol":
            kontrol.append(ort)
        else:
            deney_grubu.append(ort)

print(f"\n  Kontrol grubu ({len(kontrol)} denek):")
print(f"    Ölçümler: {kontrol}")
print(f"    Ortalama: {sum(kontrol)/len(kontrol):.2f}")

print(f"  Deney grubu ({len(deney_grubu)} denek):")
print(f"    Ölçümler: {deney_grubu}")
print(f"    Ortalama: {sum(deney_grubu)/len(deney_grubu):.2f}")

fark = sum(deney_grubu)/len(deney_grubu) - sum(kontrol)/len(kontrol)
print(f"  Gruplar arası fark: {fark:.2f}")


# ============================================================
# ALIŞTIRMALAR (Öğrenciler İçin)
# ============================================================
"""
Alıştırma 1: Bir metin dosyasını satır satır okuyup:
   - Toplam satır sayısını
   - Toplam kelime sayısını
   - En uzun satırı
   yazdıran fonksiyon yazın.

Alıştırma 2: Bir CSV dosyasındaki sayısal sütunun ortalamasını,
   medyanını ve standart sapmasını hesaplayan fonksiyon yazın.
   Hatalı satırları (sayısal olmayan değerler) atlayıp raporlayın.

Alıştırma 3: JSON formatında bir konfigürasyon dosyası oluşturup
   okuyan program yazın. Dosya yoksa varsayılan değerlerle oluşturun.

Alıştırma 4: Bir klasördeki tüm .txt dosyalarını bulan ve
   her birinin kelime sayısını raporlayan program yazın.

Alıştırma 5: Güvenli kullanıcı girişi fonksiyonu yazın:
   - Sayı istenen yerde sayı girilene kadar tekrar sorsun
   - Belirli bir aralıkta olmasını zorunlu tutsun
   - Maksimum deneme sayısı olsun
"""
