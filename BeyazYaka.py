#BeyazYaka.py 

from Calisan import Calisan

class BeyazYaka(Calisan):
    
    def __init__(self, tc_no, ad, soyad, yas, cinsiyet, uyruk, sektor="", tecrube=0, maas=0, tesvik_primi=0):
        super().__init__(tc_no, ad, soyad, yas, cinsiyet, uyruk, sektor, tecrube, maas)
        self.tesvik_primi = tesvik_primi

   
   
    def get_tesvik_primi(self):
        return self.tesvik_primi

    def set_tesvik_primi(self, tesvik_primi):
        self.tesvik_primi = tesvik_primi

#zam hakkını hesaplayan metod

    def zam_hakki(self):
        try:
            maaş = self.get_maas()
            tecrube = self.get_tecrube()

            if tecrube < 2:
                zam_miktari = self.tesvik_primi
            elif 2 <= tecrube <= 4 and maaş < 15000:
                zam_miktari = (maaş % tecrube) * 5 + self.tesvik_primi
            elif tecrube > 4 and maaş < 25000:
                zam_miktari = (maaş % tecrube) * 4 + self.tesvik_primi
            else:
                zam_miktari = 0

            yeni_maas = maaş + zam_miktari

            return yeni_maas if yeni_maas != maaş else maaş

        except Exception as e:
            print("Hata:", str(e))
            return None

    def __str__(self):
        try:
            ad = self.get_ad()
            soyad = self.get_soyad()
            tecrube = self.get_tecrube()
            yeni_maas = self.zam_hakki()

            return f"BEYAZ YAKA-\nAd: {ad}\nSoyad: {soyad}\nTecrübe: {tecrube}\nYeni Maaş: {yeni_maas}"

        except Exception as e:
            print("Hata:", str(e))
            return None
