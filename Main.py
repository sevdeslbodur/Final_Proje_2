#Main.py
import pandas as pd

#Insan sınıfı için 2 nesne oluşturuldu
from Insan import Insan
kisi1= Insan("16473829036","Rory","Gilmore","20","kadın","Amerikalı")
kisi2= Insan("26473890241","Ege","Bodur","30","erkek","Türk")
print(kisi1)
print(kisi2)

Issiz1.tecrubeler= {
   "yönetici":5,
   "beyaz yaka":3,
   "mavi yaka":6,
}

Issiz1= Issiz("16483947562","Dilay","Yücel","38","kadın","Türk","beyaz yaka",Issiz1.tecrubeler)
print("1.işsiz bilgileri:")
print(İssiz1)
print()

Issiz2.tecrübeler={
    "yönetici":1,
    "beyaz yaka":2,
    "mavi yaka ":3,
}

Issiz2= Issiz("76859374582","Ümmü","Bodur","27","kadın","Türk","mavi yaka",Issiz2.tecrubeler)

Issiz3.tecrubeler={
    "yönetici":1,
    "beyaz yaka":2,
    "mavi yaka":2
}

Issiz3= Issiz("34259079685","Begüm","Keleş","29","kadın","Türk","yönetici",Issiz3.tecrubeler)

# Nesneler oluşturuldu
  
    statu1 = input("Lütfen 1. Çalışanın Statüsünü giriniz (işletme,yazılım,gıda,diğer):")
    statu2 = input("Lütfen 2. Çalışanın Statüsünü giriniz (işletme,yazılım,gıda,diğer):")
    statu3 = input("Lütfen 3. Çalışanın Statüsünü giriniz (işletme,yazılım,gıda,diğer):")
    
    calisan1 = Calisan("53627859481", "Sıla", "Ceylan", 28, "kadın", "Türk", statu1, 3, 15000)
    calisan2 = Calisan("24354625347", "Oğuz", "Çelik", 35, "erkek", "Türk", statu2, 6, 20000)
    calisan3 = Calisan("76859037584", "Ece", "Akbaş", 42, "erkek", "Türk", statu3, 9, 25000)
    print()
    print("Çalışan Bilgileri:")
    print(calisan1)
    print(calisan2)
    print(calisan3)
    print()
    print()


    # MaviYaka sınıfı için 3 nesne oluşturuldu
    
    
    maviyaka1 = MaviYaka("63728564719", "Arda", "Demir", 28, "erkek", "Türk", 3, 19000, 5)
    maviyaka2 = MaviYaka("35467182930", "Gizem", "Üzel", 35, "kadın", "Türk", 6, 21000, 8)
    maviyaka3 = MaviYaka("29200304265", "Josefıne", "Frida", 42, "kadın", "Norveçli", 9, 23000, 6)
    print("Mavi Yaka Bilgileri:")
    print(maviyaka1)
    print(maviyaka2)
    print(maviyaka3)
    print()


# BeyazYaka sınıfı için 3 nesne oluşturuldu

    beyazyaka1 = BeyazYaka("45678901234", "Selmin", "Tanyeri", 30, "kadın", "Türk", 3, 13000, 1000)
    beyazyaka2 = BeyazYaka("12345678924", "Sıla", "Ceylan", 35, "Kadın", "Türk", 5, 15000, 1300)
    beyazyaka3 = BeyazYaka("74659012354", "Ersin", "Albayrak", 28, "Erkek", "Türk", 2, 11000, 1200)
    print("Beyaz Yaka Bilgileri:")
    print(beyazyaka1)
    print(beyazyaka2)
    print(beyazyaka3)
    print()
    
    
    