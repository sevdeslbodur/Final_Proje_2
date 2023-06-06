#Insan.py
class Insan:
    def __init__(self, tc_no, ad, soyad, yas, cinsiyet, uyruk):
        self.tc_no = tc_no
        self.ad = ad
        self.soyad = soyad
        self.yas = yas
        self.cinsiyet = cinsiyet
        self.uyruk = uyruk

    def get_tc_no(self):
        return self.tc_no

    def set_tc_no(self, tc_no):
        self.tc_no = tc_no

    def get_ad(self):
        return self.ad

    def set_ad(self, ad):
        self.ad = ad

    def get_soyad(self):
        return self.soyad

    def set_soyad(self, soyad):
        self.soyad = soyad

    def get_yas(self):
        return self.yas

    def set_yas(self, yas):
        self.__yas = yas

    def get_cinsiyet(self):
        return self.cinsiyet

    def set_cinsiyet(self, cinsiyet):
        self.cinsiyet = cinsiyet

    def get_uyruk(self):
        return self.uyruk

    def set_uyruk(self, uyruk):
        self.uyruk = uyruk

    def __str__(self):
        return f"TC No: {self.__tc_no}\nAd: {self.__ad}\nSoyad: {self.__soyad}\nYaş: {self.__yas}\nCinsiyet: {self.__cinsiyet}\nUyruk: {self.__uyruk}"
