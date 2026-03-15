# 🎤 Hafta 1 — Python'a Giriş — Sunum Scripti

> Bu doküman, `hafta_01_pythona_giris.py` dosyasını anlatırken rehber olarak kullanılmak üzere hazırlanmıştır.

---

## 📌 Açılış (1-2 dk)

**Söyle:**
> "Bugün Python'a giriş yapıyoruz. Bu ders sonunda Python'un ne olduğunu, neden bu kadar popüler olduğunu öğreneceksiniz. İlk programınızı yazacak, değişkenleri ve veri tiplerini tanıyacak, kullanıcıdan veri almayı öğreneceksiniz."

**İçindekiler listesini göster** (satır 7-13) ve kısaca bahset:
> "Bugün beş ana başlığımız var: Python nedir, ilk programımız, değişkenler, kullanıcı girdisi ve uygulamalar."

---

## 1️⃣ Python Nedir? Neden Python? (satır 16-38)

### Tanım
**Söyle:**
> "Python, 1991 yılında Guido van Rossum tarafından geliştirilmiş bir programlama dili. Yüksek seviyeli ve yorumlanan — yani interpreted — bir dil. Yüksek seviyeli demek insan diline yakın, yorumlanan demek yazdığınız kodu satır satır çalıştırıyor, derleme (compile) aşaması yok."

### Neden Python?
**Söyle:**
> "Araştırmacılar için neden Python diye sorarsak:"

- ✅ **Kolay okunur** — "Sözdizimi (syntax) neredeyse İngilizce gibi. Sözde koda (pseudocode) çok yakın."
- ✅ **Güçlü ekosistem** — "NumPy, Pandas, Matplotlib, SciPy gibi kütüphaneler veri bilimi için biçilmiş kaftan."
- ✅ **Makine öğrenmesi** — "Scikit-learn, TensorFlow, PyTorch... Bu alandaki neredeyse tüm büyük kütüphaneler Python'da."
- ✅ **Büyük topluluk** — "Bir sorunla karşılaştığınızda Stack Overflow'da, GitHub'da hemen çözüm bulabilirsiniz."

### Kurulum & Çalıştırma
**Söyle:**
> "Kurulum için python.org'dan Python 3.x indirebilirsiniz. Veri bilimi için Anaconda da çok güzel bir seçenek — hazır paketlerle geliyor."

> "Python'u üç şekilde çalıştırabilirsiniz:
> 1. **Terminal'de** `python dosya_adi.py` yazarak,
> 2. **İnteraktif mod'da** terminal'e `python` yazıp tek tek komut girerek,
> 3. **Jupyter Notebook'ta** hücre hücre çalıştırarak — araştırma için en ideal yol."

---

## 2️⃣ İlk Program: print(), Yorum Satırları, Kod Yapısı (satır 41-90)

### print() Fonksiyonu
**Söyle:**
> "Python'daki en temel fonksiyon: `print()`. Ekrana bir şey yazdırmak istediğimizde kullanırız."

**Kodu çalıştır ve göster** (satır 49-50):
```python
print("Merhaba Dünya!")
print("Python öğrenmeye başlıyoruz!")
```
> "İşte ilk programımız. Bu kadar basit!"

### Birden fazla değer yazdırma
**Göster** (satır 53):
```python
print("Python", "versiyonu:", 3)
```
> "Virgülle ayırarak birden fazla şeyi tek `print` ile yazdırabiliyoruz. Python aralarına otomatik boşluk koyuyor."

### sep parametresi
**Göster** (satır 56-57):
```python
print("2024", "03", "15", sep="-")       # 2024-03-15
print("ad", "soyad", "yaş", sep=" | ")   # ad | soyad | yaş
```
> "`sep` parametresiyle değerler arasındaki ayırıcıyı değiştirebiliyoruz. Varsayılan olarak boşluk var ama biz tire, dikey çizgi gibi şeyler koyabiliyoruz."

### end parametresi
**Göster** (satır 60-61):
```python
print("Satır 1", end=" -> ")
print("Satır 2")   # Çıktı: Satır 1 -> Satır 2
```
> "`end` parametresi, satır sonuna ne konacağını belirler. Normalde `\\n` yani yeni satır. Burada onu değiştirdik, iki print tek satırda çıktı."

### Yorum Satırları
**Söyle:**
> "Yorumlar kodun insanlar tarafından okunmasını kolaylaştırır. Python bunları çalıştırmaz."

- **Tek satırlık:** `#` işareti ile başlar
- **Çok satırlık:** Üçlü tırnak `"""..."""` ile yazılır *(docstring olarak da kullanılır)*

**Göster** (satır 70-78):
```python
# Bu bir yorum satırıdır
print("Bu çalışır")  # Satır sonunda da yorum yazılabilir

"""
Bu bir çok satırlık
yorum veya docstring'dir.
"""
```

### Kod Yapısı — Girintileme (Indentation)
**⚠️ Önemli nokta — vurgula:**
> "Python'da girintileme çok önemli! C, Java gibi dillerde süslü parantez `{}` kullanılıyor ama Python'da kod blokları boşluklarla (girintilemeyle) belirlenir. Standart **4 boşluk**. Bu yanlışsa Python hata verir."

**Göster** (satır 87-90):
```python
if True:
    print("Bu satır girintili — if bloğunun içinde")
    print("Bu da aynı bloğun içinde")
print("Bu satır girintisiz — if bloğunun dışında")
```
> "Bakın, `if`'ten sonra iki nokta üst üste `:` koyuyoruz ve altına 4 boşluk girinti veriyoruz. Bu blok, `if` koşulunun içinde. Girintisiz satır ise dışında."

---

## 3️⃣ Değişkenler ve Veri Tipleri (satır 93-185)

### Değişken Nedir?
**Söyle:**
> "Değişken, bir değeri bellekte saklayıp ona isim veren yapıdır. Kutulara benzetebilirsiniz — kutunun üstüne isim yazıyorsunuz, içine değer koyuyorsunuz."

> "Python'da değişken tanımlarken tip belirtmeye gerek yok. `int x = 5` gibi yazmıyoruz. Sadece `x = 5` diyoruz, Python tipi kendisi anlıyor. Buna **dynamic typing** deniyor."

### Değişken Oluşturma
**Göster** (satır 103-111):
```python
isim = "Ayşe"          # string
yas = 28               # int
boy = 1.72             # float
ogrenci_mi = True      # bool
```
> "Bakın dört farklı tipte değişken oluşturduk. Python tipini otomatik belirledi."

### İsimlendirme Kuralları
**Söyle (sırayla):**
> "Değişken isimlendirmede kurallar var:"

| ✅ Doğru | ❌ Yanlış |
|---|---|
| Harf veya `_` ile başlamalı | Rakamla başlayamaz (`2sayi`) |
| Harf, rakam, `_` içerebilir | Boşluk içeremez (`iki kelime`) |
| Büyük-küçük harf duyarlı | Python anahtar kelimesi olamaz (`if`, `for`) |

**Python konvansiyonu — vurgula:**
> "Python'da **snake_case** kullanıyoruz: `ogrenci_sayisi`. camelCase veya PascalCase değil. Sabitler için `BÜYÜK_HARF` kullanılır: `MAX_DENEME = 5`."

### Dört Temel Veri Tipi
**Sırasıyla göster ve açıkla:**

**1. `int` — Tam sayı** (satır 129-133):
> "Tam sayılar. Pozitif, negatif olabilir. Büyük sayılarda alt çizgi kullanıp okunabilirlik sağlayabilirsiniz: `1_000_000`."

**2. `float` — Ondalıklı sayı** (satır 135-139):
> "Ondalıklı sayılar. Pi sayısı, sıcaklık gibi. Bilimsel gösterim de kullanabilirsiniz: `6.022e23`."

**3. `str` — String (metin)** (satır 141-150):
> "Metinler. Çift tırnak veya tek tırnak — ikisi de olur. Çok satırlı string için üçlü tırnak."

**4. `bool` — Boolean** (satır 152-155):
> "Mantıksal değerler: `True` veya `False`. Dikkat: baş harfler büyük! `true` yazsanız hata verir."

### type() Fonksiyonu
**Göster** (satır 157-162):
> "`type()` fonksiyonuyla bir değişkenin veya değerin tipini öğrenebilirsiniz. Debugging için çok işe yarar."

### Çoklu Atama
**Göster** (satır 166-171):
```python
x, y, z = 10, 20, 30       # Tek satırda üç değişken
a = b = c = 0               # Hepsine aynı değer
```
> "Python'da tek satırda birden fazla değişkene değer atayabilirsiniz. Pratik bir kısayol."

### Değişken Değerini Değiştirme
**Göster** (satır 174-179):
```python
sayac = 0
sayac = 1          # üstüne yazdık
sayac = sayac + 1  # mevcut değere 1 ekledik
```
> "Değişkenler 'değişken' oldukları için değerleri değişebilir. `sayac = sayac + 1` çok sık kullanacağınız bir kalıp."

### None Tipi
**Göster** (satır 182-185):
> "`None`, 'henüz değeri yok' anlamına gelir. Diğer dillerdeki `null`'un karşılığı. Bir değişkeni tanımlayıp henüz değer atamak istemediğinizde kullanırsınız."

---

## 4️⃣ Kullanıcıdan Veri Alma: input() ve Tip Dönüşümleri (satır 188-242)

### input() Fonksiyonu
**Söyle:**
> "`input()` fonksiyonu kullanıcıdan klavye ile veri almamızı sağlar."

**⚠️ Kritik uyarı — vurgula:**
> "**Çok önemli:** `input()` her zaman **string** döndürür! Kullanıcı 25 yazsa bile, Python bunu `\"25\"` yani metin olarak alır. Matematiksel işlem yapabilmek için tip dönüşümü yapmamız gerekir."

### Tip Dönüşümleri (Type Casting)

**Sırasıyla göster:**

**str → int** (satır 207-210):
```python
yas_str = "25"
yas_int = int(yas_str)
print(yas_int + 5)       # 30 (matematiksel toplama)
print(yas_str + "5")     # 255 (string birleştirme!)
```
> "Bakın buradaki farka dikkat! `int` olarak toplarsak 30, `str` olarak toplarsak (birleştirirsek) 255. Çok farklı sonuçlar! Bu yüzden tip dönüşümü hayati önem taşıyor."

**str → float** (satır 213-215):
> "Ondalıklı sayı için `float()` kullanıyoruz."

**int → str** (satır 218-220):
> "Tam sayıyı metne çevirmek için `str()`. Metin birleştirme yapacaksanız bunu kullanırsınız."

**float → int** (satır 227-230):
```python
pi = 3.99
tam_pi = int(pi)
print(tam_pi)   # 3 (dikkat: 4 değil!)
```
> "**Dikkat!** `int()` yuvarlamaz, ondalık kısmı keser! 3.99 → 3 olur, 4 değil. Yuvarlama istiyorsanız `round()` fonksiyonu kullanacaksınız."

**bool dönüşümleri** (satır 233-237):
> "Her şey boolean'a çevrilebilir. Genel kural: **sıfır, boş ve None → False**, geri kalan her şey **True**."

```python
bool(1)      # True       bool(0)      # False
bool("abc")  # True       bool("")     # False
bool(None)   # False
```

### input() ile Sayı Alma — Doğru Yol
**Göster** (satır 240-242):
```python
yas = int(input("Yaşınız: "))
boy = float(input("Boyunuz (m): "))
```
> "`input()`'u `int()` veya `float()` ile sarmalıyoruz. Böylece kullanıcıdan string alıp hemen sayıya çeviriyoruz."

---

## 5️⃣ Uygulamalar (satır 245-330)

> "Şimdi öğrendiklerimizi pratikle pekiştirelim."

### Uygulama 1: Basit Hesap Makinesi (satır 253-273)
**Söyle:**
> "İki sayı üzerinde dört işlem ve birkaç ek işlem yapıyoruz."

**Önemli operatörleri vurgula:**

| Operatör | Açıklama | Örnek (15, 4) | Sonuç |
|---|---|---|---|
| `/` | Normal bölme | `15 / 4` | `3.75` |
| `//` | Tam bölme | `15 // 4` | `3` |
| `%` | Mod (kalan) | `15 % 4` | `3` |
| `**` | Üs alma | `15 ** 4` | `50625` |

> "Burada `/` ile `//` farkına dikkat edin. `/` ondalıklı sonuç verir. `//` ondalık kısmı atar. `%` ise bölme işleminden kalanı verir."

**f-string'i fark ettir:**
> "Burada `f\"...\"` formatını kullanıyoruz — buna f-string deniyor. Süslü parantez `{}` içine değişken adı yazıyorsunuz, Python onu değeriyle değiştiriyor. Çok pratik."

### Uygulama 2: Sıcaklık Çevirici (satır 276-289)
**Söyle:**
> "Celsius → Fahrenheit ve Kelvin çevirisi. Formüller basit ama Python'un bunları nasıl hesapladığını görmek güzel."

**`:.2f` formatını açıkla:**
> "`:.2f` demek 2 ondalık basamağa yuvarla demek. Çıktıyı daha düzgün göstermek için kullanıyoruz."

### Uygulama 3: Araştırma Verisi Hesaplama (satır 292-317)
**Söyle:**
> "Bu örnek size daha yakın — bir deneydeki ölçüm sonuçlarının ortalamasını, min-max ve aralığını hesaplıyoruz."

> "`max()` ve `min()` Python'un hazır fonksiyonları. İleride listelerle çok daha kolay yapacağız ama şimdilik bu yöntemi bilmeniz yeterli."

### Uygulama 4: BMI Hesaplayıcı (satır 320-329)
**Söyle:**
> "Vücut Kitle İndeksi hesaplama. Formül: kilo bölü boy'un karesi. `boy ** 2` ile üs alıyoruz."

---

## 📝 Alıştırmalar — Kapanış (satır 332-355)

**Söyle:**
> "Son olarak sizin için alıştırmalar var. Bunları mutlaka deneyin çünkü programlama yaparak öğrenilir."

**Kısaca listele:**
1. **Kişisel bilgi** — Kendi bilgilerinizi değişkenlere atayın
2. **Tip dönüşümleri** — Verilen dönüşümleri yapın *(özellikle `bool("True")` tuzağına dikkat!)*
3. **Dört işlem** — `input()` ile iki sayı alıp hesap yapın
4. **Daire hesaplama** — Yarıçaptan çevre ve alan
5. **Saat-dakika** — Toplam dakikaya çevirin

**⚠️ Alıştırma 2 için ipucu ver:**
> "`bool(\"True\")` ne döndürür dersiniz? `True` döndürür — ama `\"True\"` stringi gerçekten True boolean mu? Hayır! `bool()` boş olmayan her string için `True` döndürür. `bool(\"False\")` bile `True`'dur! Bu çok sık yapılan bir hatadır."

---

## 🎬 Kapanış

**Söyle:**
> "Bugün Python'ın temellerini gördük: print ile çıktı, değişkenler ve veri tipleri, input ile kullanıcıdan veri alma ve tip dönüşümleri. Gelecek hafta operatörleri ve koşullu ifadeleri (if-else) göreceğiz. Alıştırmaları mutlaka yapın, sorularınız olursa çekinmeyin."

---

> **💡 Sunum İpuçları:**
> - Her bölümde önce kodu göster, sonra çalıştır, sonra açıkla
> - `type()` fonksiyonunu sık kullan — öğrenciler veri tipini görsel olarak görsün
> - `str + int` hatasını canlı göster (hata mesajını okumayı öğretmek için)
> - `int(3.99) → 3` örneğini mutlaka yap — bu çok şaşırtıyor
> - f-string'i ilk gördüklerinde açıkla, sonra doğal olarak kullan
