#MaviYaka.py

from Calisan import Calisan

class MaviYaka(Calisan):
    def __init__(self, tc_no, ad, soyad, yas, cinsiyet, uyruk, tecrube, maas, yipranma_payi, sektor=""):
        super().__init__(tc_no, ad, soyad, yas, cinsiyet, uyruk, sektor, tecrube, maas)
        self.yipranma_payi = yipranma_payi

    def get_yipranma_payi(self):
        return self.yipranma_payi

    def set_yipranma_payi(self, yipranma_payi):
        self.yipranma_payi = yipranma_payi


 #zam hakkını hesaplayan yöntem
 
    def zam_hakki(self):
        try:
            maas = self.get_maas()
            tecrube = self.get_tecrube()

            if tecrube < 2:
                zam_orani = self.__yipranma_payi * 10
            elif 2 <= tecrube <= 4 and maas < 15000:
                zam_orani = (maas % tecrube) / 2 + self.yipranma_payi * 10
            elif tecrube > 4 and maas < 25000:
                zam_orani = (maas % tecrube) / 3 + self.yipranma_payi * 10
            else:
                zam_orani = 0

            yeni_maas = maas + (maas * zam_orani / 100)

            return yeni_maas if yeni_maas != maas else maas

        except Exception as e:
            print("Hata:", str(e))
            return None

    def __str__(self):
        try:
            ad = self.get_ad()
            soyad = self.get_soyad()
            tecrube = self.get_tecrube()
            yeni_maas = self.zam_hakki()

            return f"Mavi Yaka - \nAd: {ad}\nSoyad: {soyad}\nTecrübe: {tecrube} yıl\nYeni Maaş: {yeni_maas}"

        except Exception as e:
            print("Hata:", str(e))
            return None
