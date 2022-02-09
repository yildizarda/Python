class otopark():
    def __init__(self,marka,plaka,renk,kalacak_sure):
        self.marka = marka
        self.plaka = plaka
        self.renk = renk
        self.kalacak_sure = int(kalacak_sure / 60) 

    def arac_bilgi(self):
        print(""""
         
        Park halindeki araç bilgileri

        Araç Markası : {}

        Plaka : {}

        Renk : {}

        Kalacak Süre : {} saat
                
        """.format(self.marka,self.plaka,self.renk,self.kalacak_sure))

    def sure_ekle(self,eksure):

        self.kalacak_sure += int(eksure)
        print('Ek süreniz Eklenmiştir')
        print(f'Kalan süreniz {self.kalacak_sure}')

arac1 = otopark("Honda-Civic","05 LD 408","Beyaz",120)

arac1.arac_bilgi()
arac1.sure_ekle(5)



        