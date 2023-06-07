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
    statu1 = input("Lütfen 1. Çalışanın Statüsünü giriniz (işletme, yazılım, gıda, diğer):")
    statu2 = input("Lütfen 2. Çalışanın Statüsünü giriniz (işletme, yazılım, gıda, diğer):")
    statu3 = input("Lütfen 3. Çalışanın Statüsünü giriniz (işletme, yazılım, gıda, diğer):")
    
    maviyaka1 = MaviYaka("63728564719", "Arda", "Demir", 28, "erkek", "Türk", 3, 19000, 5)
    maviyaka2 = MaviYaka("35467182930", "Gizem", "Üzel", 35, "kadın", "Türk", 6, 21000, 8)
    maviyaka3 = MaviYaka("29200304265", "Josefıne", "Frida", 42, "kadın", "Norveçli", 9, 23000, 6)
    print("Mavi Yaka Bilgileri:")
    print(maviyaka1)
    print(maviyaka2)
    print(maviyaka3)
    print()
    
    #BeyazYaka sınıfı için nesneler oluşturuldu
    statu1 = input("Lütfen 1. Çalışanın Statüsünü giriniz (işletme, yazılım, gıda, diğer):")
    statu2 = input("Lütfen 2. Çalışanın Statüsünü giriniz (işletme, yazılım, gıda, diğer):")
    statu3 = input("Lütfen 3. Çalışanın Statüsünü giriniz (işletme, yazılım, gıda, diğer):")
    
    
    beyazyaka1 = BeyazYaka("1234567890", "Ersin", "Albayrak", 30, "erkek", "Türk", 3, 18000, 3000)
    beyazyaka2 = BeyazYaka("9876543210", "Hilal", "Keskiner", 35, "kadın", "Türk", 5, 14000, 1700)
    beyazyaka3 = BeyazYaka("5678901234", "İlayda", "Köse", 28, "kadın", "Türk", 2, 12000, 1100)
    print("Beyaz Yaka Bilgileri:")
    print(beyazyaka1)
    print(beyazyaka2)
    print(beyazyaka3)
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

    # Maaşı 15000 tl üstünde olan kişilerin toplam sayısı
    maasi_ustunde_olanlarin_sayisi(df)

 

     #Maaşı 15000 tl üstünde olan kişilerin toplam sayısı
     
def maasi_ustunde_olanlarin_sayisi(df):

       maasi_ustunde_olanlar = df[df['maas'] > 15000]
       toplam_sayi = len(maasi_ustunde_olanlar)
       print(f"Maaşı 15000 TL üzerinde olanların toplam sayısı: {toplam_sayi}")

       grup_ortalamalari_hesapla(df)
       maasi_ustunde_olanlarin_sayisi(df)
       df.sort_values(by='yeni_maas', inplace=True)
       print("Yeni Maaşa Göre Sıralı DataFrame:")
       print(df)

  
    
    
    #Yeni maaşa göre DataFrame'i küçükten büyüğe sıralanacak
    
df.sort_values(by='yeni_maas', inplace=True)
print("Yeni Maaşa Göre Sıralı DataFrame:")
print(df)



    #Tecrübesi 3 seneden fazla olan beyaz yakalılar bulunacak
    
tecrube_fazla_beyaz_yakalar =df[(df['nesne'] == 'Issiz') & (df['tecrube'] > 3)]
print("Tecrübesi 3 seneden fazla olan Beyaz Yakalılar:")
print(tecrube_fazla_beyaz_yakalar)



    #Yeni maaşı 10000 tl üzerinde olanlar için:2-5 satır olanları tc_no ve yeni_maaş sütunları yazdırılacak
    
yuksek_maasli_calisanlar = df[(df['yeni_maas'] > 10000) & (df.index >= 2) & (df.index <= 5)][['tc_no', 'yeni_maas']]
print("Yeni maaşı 10000 TL üzerinde olan 2-5 satır arası çalışanlar:")
print(yuksek_maasli_calisanlar)
      

     #Var olan DataFrame'den ad, soyad, sektör ve yeni maaşı içeren yeni bir DataFrame elde edilecek
     
yeni_dataframe = df[['ad', 'soyad', 'sektor', 'yeni_maas']]
print("Yeni DataFrame:")
print(yeni_dataframe)