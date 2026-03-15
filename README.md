# Python Programlama Dersi — Araştırmacılar İçin

Doktora öğrencileri ve araştırmacılar için Python programlama müfredatı.
Temel programlamadan başlayıp veri bilimi ve bilimsel hesaplama araçlarına uzanan bir yol haritası.

## Müfredat Yapısı

Kurs 5 ana bölümden oluşmaktadır:

1. **Temel Kavramlar** (Hafta 1-3)
2. **Veri Yapıları ve Fonksiyonlar** (Hafta 4-6)
3. **Nesne Yönelimli Programlama** (Hafta 7-9)
4. **Bilimsel Python ve Veri Analizi** (Hafta 10-13)
5. **İleri Veri Bilimi ve Araştırma Projesi** (Hafta 14-16)

Her hafta için detaylı ders planları `dersler/` klasöründe bulunmaktadır.

---

## Bölüm 1: Temel Kavramlar (Hafta 1-3)

### Hafta 1 — Python'a Giriş
| Ders | Konu | Süre |
|------|------|------|
| 1.1 | Python nedir? Kurulum ve geliştirme ortamı (VS Code / PyCharm) | 45 dk |
| 1.2 | İlk program: `print()`, yorum satırları, kod yapısı | 45 dk |
| 1.3 | Değişkenler ve veri tipleri (`int`, `float`, `str`, `bool`) | 60 dk |
| 1.4 | Kullanıcıdan veri alma: `input()` ve tip dönüşümleri | 45 dk |
| **Uygulama** | Basit hesap makinesi, sıcaklık çevirici | 60 dk |

### Hafta 2 — Operatörler ve Koşullu İfadeler
| Ders | Konu | Süre |
|------|------|------|
| 2.1 | Aritmetik, karşılaştırma ve mantıksal operatörler | 45 dk |
| 2.2 | `if`, `elif`, `else` yapıları | 60 dk |
| 2.3 | İç içe koşullar ve ternary operatör | 45 dk |
| 2.4 | `match-case` (Python 3.10+) | 30 dk |
| **Uygulama** | Not hesaplama sistemi, basit menü programı | 60 dk |

### Hafta 3 — Döngüler ve String İşlemleri
| Ders | Konu | Süre |
|------|------|------|
| 3.1 | `for` döngüsü ve `range()` fonksiyonu | 60 dk |
| 3.2 | `while` döngüsü, `break`, `continue`, `pass` | 60 dk |
| 3.3 | String metodları ve formatlama (f-string) | 45 dk |
| 3.4 | String dilimleme (slicing) ve indeksleme | 45 dk |
| **Uygulama** | Sayı tahmin oyunu, palindrom kontrolü | 60 dk |

---

## Bölüm 2: Veri Yapıları ve Fonksiyonlar (Hafta 4-6)

### Hafta 4 — Listeler ve Tuple
| Ders | Konu | Süre |
|------|------|------|
| 4.1 | Liste oluşturma, indeksleme, dilimleme | 60 dk |
| 4.2 | Liste metodları (`append`, `remove`, `sort`, `pop`...) | 45 dk |
| 4.3 | List comprehension | 45 dk |
| 4.4 | Tuple yapısı ve kullanım alanları | 30 dk |
| **Uygulama** | Öğrenci not sistemi, alışveriş listesi uygulaması | 60 dk |

### Hafta 5 — Sözlükler, Kümeler ve Fonksiyonlar
| Ders | Konu | Süre |
|------|------|------|
| 5.1 | Dictionary oluşturma ve metodları | 60 dk |
| 5.2 | Set (küme) yapısı ve küme işlemleri | 30 dk |
| 5.3 | Fonksiyon tanımlama, parametreler, `return` | 60 dk |
| 5.4 | `*args`, `**kwargs`, varsayılan parametreler | 45 dk |
| **Uygulama** | Telefon rehberi, kelime frekansı analizi | 60 dk |

### Hafta 6 — Dosya İşlemleri ve Hata Yönetimi
| Ders | Konu | Süre |
|------|------|------|
| 6.1 | Dosya okuma/yazma (`open`, `read`, `write`) | 60 dk |
| 6.2 | `with` bloğu ve dosya modları | 30 dk |
| 6.3 | CSV ve JSON dosyaları ile çalışma | 45 dk |
| 6.4 | `try`, `except`, `finally` — hata yönetimi | 60 dk |
| **Uygulama** | Not defteri uygulaması (dosyaya kayıt), log parser | 60 dk |

---

## Bölüm 3: Nesne Yönelimli Programlama (Hafta 7-9)

### Hafta 7 — OOP Temelleri
| Ders | Konu | Süre |
|------|------|------|
| 7.1 | Sınıf ve nesne kavramı | 60 dk |
| 7.2 | `__init__`, instance değişkenleri, metodlar | 60 dk |
| 7.3 | Encapsulation (kapsülleme) ve property | 45 dk |
| **Uygulama** | Banka hesabı sınıfı, Araç sınıfı | 60 dk |

### Hafta 8 — OOP İleri Kavramlar
| Ders | Konu | Süre |
|------|------|------|
| 8.1 | Kalıtım (Inheritance) | 60 dk |
| 8.2 | Çok biçimlilik (Polymorphism) | 45 dk |
| 8.3 | Soyut sınıflar ve arayüzler (`ABC`) | 45 dk |
| 8.4 | Sihirli metodlar (`__str__`, `__repr__`, `__len__`...) | 45 dk |
| **Uygulama** | Şekil hiyerarşisi, hayvan sınıf ağacı | 60 dk |

### Hafta 9 — Modüller ve Paket Yönetimi
| Ders | Konu | Süre |
|------|------|------|
| 9.1 | Modül ve paket oluşturma, `import` sistemi | 60 dk |
| 9.2 | `pip` ve sanal ortamlar (`venv`) | 45 dk |
| 9.3 | Popüler standart kütüphaneler (`os`, `sys`, `datetime`, `random`) | 45 dk |
| 9.4 | `requirements.txt` ve proje yapısı | 30 dk |
| **Uygulama** | Kendi modülünü yaz ve paketini oluştur | 60 dk |

---

## Bölüm 4: Bilimsel Python ve Veri Analizi (Hafta 10-13)

### Hafta 10 — NumPy: Sayısal Hesaplama
| Ders | Konu | Süre |
|------|------|------|
| 10.1 | NumPy nedir? Kurulum, `ndarray` oluşturma | 45 dk |
| 10.2 | Array indeksleme, dilimleme, yeniden şekillendirme (`reshape`) | 60 dk |
| 10.3 | Vektörel işlemler, broadcasting, performans karşılaştırması | 60 dk |
| 10.4 | Lineer cebir (`linalg`), istatistiksel fonksiyonlar (`mean`, `std`, `corrcoef`) | 45 dk |
| **Uygulama** | Deney verisi üzerinde istatistiksel analiz, matris işlemleri | 60 dk |

### Hafta 11 — Pandas: Veri Manipülasyonu
| Ders | Konu | Süre |
|------|------|------|
| 11.1 | Series ve DataFrame oluşturma, CSV/Excel okuma-yazma | 60 dk |
| 11.2 | Veri seçme, filtreleme, sıralama (`loc`, `iloc`, boolean indexing) | 60 dk |
| 11.3 | Eksik veri yönetimi (`NaN`, `dropna`, `fillna`) | 45 dk |
| 11.4 | `groupby`, `pivot_table`, `merge` — veri birleştirme ve özetleme | 60 dk |
| **Uygulama** | Gerçek araştırma verisini temizleme ve keşifsel analiz | 60 dk |

### Hafta 12 — Matplotlib ve Seaborn: Veri Görselleştirme
| Ders | Konu | Süre |
|------|------|------|
| 12.1 | Matplotlib temelleri: `plot`, `scatter`, `bar`, `hist` | 60 dk |
| 12.2 | Grafik özelleştirme: başlık, eksen, legend, renk, stil | 45 dk |
| 12.3 | Alt grafikler (`subplots`) ve çoklu figürler | 45 dk |
| 12.4 | Seaborn ile istatistiksel görselleştirme (`heatmap`, `boxplot`, `violinplot`, `pairplot`) | 60 dk |
| **Uygulama** | Araştırma verisiyle yayın kalitesinde grafik hazırlama | 60 dk |

### Hafta 13 — SciPy ve İstatistiksel Analiz
| Ders | Konu | Süre |
|------|------|------|
| 13.1 | SciPy ekosistemi: `scipy.stats` ile tanımlayıcı istatistikler | 45 dk |
| 13.2 | Hipotez testleri: t-test, ANOVA, ki-kare testi | 60 dk |
| 13.3 | Eğri uydurma (`curve_fit`) ve regresyon analizi | 60 dk |
| 13.4 | Jupyter Notebook kullanımı ve araştırma iş akışı | 45 dk |
| **Uygulama** | Deney sonuçlarına istatistiksel test uygulama ve raporlama | 60 dk |

---

## Bölüm 5: İleri Veri Bilimi ve Araştırma Projesi (Hafta 14-16)

### Hafta 14 — Scikit-learn ile Makine Öğrenmesine Giriş
| Ders | Konu | Süre |
|------|------|------|
| 14.1 | ML temel kavramları: eğitim/test verisi, özellik mühendisliği | 45 dk |
| 14.2 | Regresyon modelleri (Linear, Ridge, Lasso) | 60 dk |
| 14.3 | Sınıflandırma modelleri (Logistic Regression, Random Forest, SVM) | 60 dk |
| 14.4 | Model değerlendirme: cross-validation, confusion matrix, ROC | 45 dk |
| **Uygulama** | Araştırma verisine uygun model seçimi ve değerlendirme | 60 dk |

### Hafta 15 — Araştırma Araçları ve Otomasyon
| Ders | Konu | Süre |
|------|------|------|
| 15.1 | Web scraping ile veri toplama (`requests`, `BeautifulSoup`) | 45 dk |
| 15.2 | Büyük veri dosyaları: chunk okuma, `parquet` formatı | 45 dk |
| 15.3 | Tekrarlanabilir araştırma: `venv`, `requirements.txt`, seed sabitleme | 45 dk |
| 15.4 | Git ile versiyon kontrolü ve Jupyter + Git iş akışı | 45 dk |
| **Uygulama** | Araştırma pipeline'ı oluşturma (veri toplama → analiz → grafik) | 60 dk |

### Hafta 16 — Araştırma Projesi ve Sunum
Öğrenciler kendi araştırma verileriyle uçtan uca bir analiz projesi yapar:

| Aşama | İçerik |
|-------|--------|
| **Veri Hazırlama** | Kendi araştırma verisini Pandas ile temizleme ve düzenleme |
| **Analiz** | İstatistiksel testler ve/veya makine öğrenmesi modeli uygulama |
| **Görselleştirme** | Yayın kalitesinde Matplotlib/Seaborn grafikleri |
| **Raporlama** | Jupyter Notebook ile tekrarlanabilir analiz raporu |
| **Sunum** | Bulgularını sunma ve kod incelemesi |

#### Örnek Proje Fikirleri (Alana Göre)

| Alan | Proje |
|------|-------|
| Biyoloji / Tıp | Deney sonuçlarında istatistiksel karşılaştırma ve survival analizi |
| Sosyal Bilimler | Anket verisi analizi, metin madenciliği |
| Mühendislik | Sensör verisi işleme ve anomali tespiti |
| Eğitim Bilimleri | Öğrenci performans verisi analizi ve tahmin modeli |
| Çevre Bilimleri | İklim/hava kalitesi verisi zaman serisi analizi |

---

## Değerlendirme Kriterleri

| Kriter | Ağırlık |
|--------|---------|
| Haftalık uygulamalar | %30 |
| Rehberli proje | %30 |
| Bağımsız proje | %30 |
| Derse katılım | %10 |

---

## Her Ders İçin Standart Akış

```
1. Kısa tekrar (önceki ders) .............. 5-10 dk
2. Yeni konu anlatımı (teori + canlı kod) . 20-30 dk
3. Birlikte uygulama ...................... 15-20 dk
4. Bağımsız alıştırma .................... 15-20 dk
5. Soru-cevap ve özet .................... 5-10 dk
```

## Kaynaklar

**Python Temelleri:**
- [Python Resmi Dokümantasyonu](https://docs.python.org/3/)
- [Real Python](https://realpython.com/)

**Veri Bilimi Kütüphaneleri:**
- [NumPy Dokümantasyonu](https://numpy.org/doc/)
- [Pandas Dokümantasyonu](https://pandas.pydata.org/docs/)
- [Matplotlib Dokümantasyonu](https://matplotlib.org/stable/)
- [Seaborn Dokümantasyonu](https://seaborn.pydata.org/)
- [SciPy Dokümantasyonu](https://docs.scipy.org/doc/scipy/)
- [Scikit-learn Dokümantasyonu](https://scikit-learn.org/stable/)

**Kitaplar:**
- *Python Data Science Handbook* — Jake VanderPlas (ücretsiz online)
- *Python for Data Analysis* — Wes McKinney
