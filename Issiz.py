#Issiz.py

from Insan import Insan

class Issiz(Insan):
    def __init__(self, tc_no, ad, soyad, yas, cinsiyet, uyruk, tecrubeler):
        super().__init__(tc_no, ad, soyad, yas, cinsiyet, uyruk)
        self.tecrubeler = tecrubeler
        self.statu = self.statu_bul()
        
        
 #tecrübeye göre statü bulan yöntem 
 
    def __statu_bul(self):
        try:
            mavi_yaka = self.tecrubeler.get("mavi yaka", 0)
            beyaz_yaka = self.tecrubeler.get("beyaz yaka", 0)
            yonetici = self.tecrubeler.get("yönetici", 0)
            
            mavi_yaka_etkisi = mavi_yaka * 0.20
            beyaz_yaka_etkisi = beyaz_yaka * 0.35
            yonetici_etkisi = yonetici * 0.45
            
            max_etki = max(mavi_yaka_etkisi, beyaz_yaka_etkisi, yonetici_etkisi)
            
            if max_etki == mavi_yaka_etkisi:
                return "mavi yaka"
            elif max_etki == beyaz_yaka_etkisi:
                return "beyaz yaka"
            else:
                return "yonetici"
            
        except Exception as e:
            print("Hata:", str(e))
            return None

    def __str__(self):
        return f"Ad: {self.get_ad()}\nSoyad: {self.get_soyad()}\nUygun Statü: {self.statu}"

    def get_tecrubeler(self):
        return self.tecrubeler

    def set_tecrubeler(self, tecrubeler):
        self.tecrubeler = tecrubeler

    def get_statu(self):
        return self.statu
