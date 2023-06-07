#Issiz.py


from Insan import Insan

class Issiz(Insan):
    def __init__(self, tc_no, ad, soyad, yas, cinsiyet, uyruk, statu):
        super().__init__(tc_no, ad, soyad, yas, cinsiyet, uyruk)
        self.statu = statu
        self.tecrubeler = {}

    def __str__(self):
        return f"TC No: {self.tc_no}\nAd: {self.ad}\nSoyad: {self.soyad}\nYaş: {self.yas}\nCinsiyet: {self.cinsiyet}\nUyruk: {self.uyruk}\nStatü: {self.statu}"

    def tecrube_ekle(self, alan, tecrube):
        self.tecrubeler[alan] = tecrube

    def tecrube_sil(self, alan):
        if alan in self.tecrubeler:
            del self.tecrubeler[alan]

    def tecrube_getir(self, alan):
        if alan in self.tecrubeler:
            return self.tecrubeler[alan]
        else:
            return None

    def ortalama_tecrube(self):
        if len(self.tecrubeler) > 0:
            toplam_tecrube = sum(self.tecrubeler.values())
            ortalama = toplam_tecrube / len(self.tecrubeler)
            return ortalama
        else:
            return 0

