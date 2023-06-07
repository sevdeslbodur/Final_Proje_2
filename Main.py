import pandas as pd
from Insan import Insan
from Issiz import Issiz
from Calisan import Calisan
from MaviYaka import MaviYaka

try:
    # Insan sınıfı için 2 nesne oluşturuldu
    
    kisi1 = Insan("16473829036", "Rory", "Gilmore", "20", "kadın", "Amerikalı")
    kisi2 = Insan("26473890241", "Ege", "Bodur", "30", "erkek", "Türk")
    print(kisi1)
    print(kisi2)
    
    # Issiz sınıf için 3 nesne oluşturuldu

    Issiz1 = Issiz("16483947562", "Dilay", "Yücel", "38", "kadın", "Türk", "beyaz yaka")
    Issiz1.tecrubeler = {
        "yönetici": 5,
        "beyaz yaka": 3,
        "mavi yaka": 6
    }
    print("1. işsiz bilgileri:")
    print(Issiz1)
    print()

    Issiz2 = Issiz("76859374582", "Ümmü", "Bodur", "27", "kadın", "Türk", "mavi yaka")
    Issiz2.tecrubeler = {
        "yönetici": 1,
        "beyaz yaka": 2,
        "mavi yaka": 3
    }

    Issiz3 = Issiz("34259079685", "Begüm", "Keleş", "29", "kadın", "Türk", "yönetici")
    Issiz3.tecrubeler = {
        "yönetici": 1,
        "beyaz yaka": 2,
        "mavi yaka": 2
    }

    # Çalışan sınıfı için nesneler oluşturuldu
    
    statu1 = input("Lütfen 1. Çalışanın Statüsünü giriniz (işletme, yazılım, gıda, diğer):")
    statu2 = input("Lütfen 2. Çalışanın Statüsünü giriniz (işletme, yazılım, gıda, diğer):")
    statu3 = input("Lütfen 3. Çalışanın Statüsünü giriniz (işletme, yazılım, gıda, diğer):")

    calisan1 = Calisan("53627859481", "Sıla", "Ceylan", 28, "kadın", "Türk", statu1, 3, 15000)
    calisan2 = Calisan("24354625347", "Oğuz", "Çelik", 35, "erkek", "Türk", statu2, 6, 20000)
    calisan3 = Calisan("76859037584", "Ece", "Akbaş", 42, "erkek", "Türk", statu3, 9, 25000)
    print("Çalışan Bilgileri:")
    print(calisan1)
    print(calisan2)
    print(calisan3)
    print()

    # MaviYaka sınıfı için nesneler oluşturuldu
    
    maviyaka1 = MaviYaka("63728564719", "Arda", "Demir", 28, "erkek", "Türk", 3, 19000, 5)
    maviyaka2 = MaviYaka("35467182930", "Gizem", "Üzel", 35, "kadın", "Türk", 6, 21000, 8)
    maviyaka3 = MaviYaka("29200304265", "Josefıne", "Frida", 42, "kadın", "Norveçli", 9, 23000, 6)
    print("Mavi Yaka Bilgileri:")
    print(maviyaka1)
    print(maviyaka2)
    print(maviyaka3)
    print()

except Exception as e:
    print("Bir hata oluştu:", e)
    


    

# Boş bir DataFrame oluşturuldu

df = pd.DataFrame(columns=['nesne', 'tc_no', 'ad', 'soyad', 'yas', 'cinsiyet', 'uyruk', 'sektor', 'tecrube', 'maas', 'yipranma_payi', 'tesvik_primi', 'yeni_maas'])
df.fillna(0, inplace=True)


def grup_ortalamalari_hesapla(df):
    

    # Çalışanlar gruplandırıldı
    calisan_gruplar = df[df['nesne'] == 'Calisan'].groupby('sektor')

    print("Calisanlar için Grup Ortalamalari:")
    for sektor, grup in calisan_gruplar:
        ortalama_tecrube = grup['tecrube'].mean()
        ortalama_yeni_maas = grup['yeni_maas'].mean()
        print(f"{sektor} sektörü için Ortalama Tecrübe: {ortalama_tecrube:.2f}, Ortalama Yeni Maaş: {ortalama_yeni_maas:.2f}")

    print()

    # Mavi Yaka için gruplandırma
    
    maviyaka_gruplar = df[df['nesne'] == 'MaviYaka'].groupby('uyruk')

    print("Mavi Yaka için Grup Ortalamalari:")
    for uyruk, grup in maviyaka_gruplar:
        ortalama_tecrube = grup['tecrube'].mean()
        ortalama_yeni_maas = grup['yeni_maas'].mean()
        print(f"{uyruk} uyruk için Ortalama Tecrübe: {ortalama_tecrube:.2f}, Ortalama Yeni Maaş: {ortalama_yeni_maas:.2f}")

    print()

    # Beyaz Yaka için gruplandırma
    
    beyazyaka_gruplar = df[df['nesne'] == 'Issiz'].groupby('cinsiyet')

    print("Beyaz Yaka için Grup Ortalamalari:")
    for cinsiyet, grup in beyazyaka_gruplar:
        ortalama_tecrube = grup['tecrube'].mean()
        ortalama_yeni_maas = grup['yeni_maas'].mean()
        print(f"{cinsiyet} cinsiyet için Ortalama Tecrübe: {ortalama_tecrube:.2f}, Ortalama Yeni Maaş: {ortalama_yeni_maas:.2f}")

    print()
    
grup_ortalamalari_hesapla(df)

