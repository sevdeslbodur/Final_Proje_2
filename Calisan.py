#Calisan.py
from Insan import Insan

class Calisan(Insan):
    def __init__(self, tc_no, ad, soyad, yas, cinsiyet, uyruk, sektor, tecrube, maas):
        super().__init__(tc_no, ad, soyad, yas, cinsiyet, uyruk)
        self.sektor = self.sektor_kontrol(sektor)
        self.tecrube = tecrube
        self.maas = maas

    def get_sektor(self):
        return self.sektor

    def set_sektor(self, sektor):
        self.sektor = self.sektor_kontrol(sektor)

    def get_tecrube(self):
        return self.tecrube

    def set_tecrube(self, tecrube):
        self.tecrube = tecrube

    def get_maas(self):
        return self.maas

    def set_maas(self, maas):
        self.maas = maas
        
        
        #Sektor değeri bulunamazsa "diğer" şeceneği seçiliyor
        
    def sektor_kontrol(self, sektor):
        sektorler = ["teknoloji", "muhasebe", "inşaat", "diğer"]
        sektor = sektor.lower()

        if sektor in sektorler:
            return sektor
        else:
            return "diğer"  
        
        
        
        #Zam oranını belirliyor
        
    def zam_hakki(self):
        try:
            tecrube = self.get_tecrube()
            maas = self.get_maas()

            if tecrube < 2:
                zam_orani = 0
            elif 2 <= tecrube <= 4 and maas < 15000:
                zam_orani = maas * tecrube / 100
            elif tecrube > 4 and maas < 25000:
                zam_orani = maas * tecrube / 200
            else:
                zam_orani = 0

            yeni_maas = maas + zam_orani

            if yeni_maas == maas:
                return maas
            else:
                return yeni_maas

        except Exception as e:
            print("Hata:", str(e))
            return None

    def __str__(self):
        return f"Ad: {self.get_ad()}, Soyad: {self.get_soyad()}, Sektör: {self.get_sektor()}, Tecrübe: {self.get_tecrube()}, Maaş: {self.get_maas()}, Yeni Maaş: {self.zam_hakki()}"

