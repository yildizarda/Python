# Bankamatik uygulaması

ArdaHesap = {

    'ad': 'Arda Yıldız',
    'hesapNo': '123456789',
    'bakiye': 3000,
    'ekHesap': 2000

}

#Kedim :)

RoziHesap = {

    'ad': 'Rozi Yıldız',
    'hesapNo': '123456756',
    'bakiye': 2000,
    'ekHesap': 1000

}

def paraCek(hesap, miktar):
    print(f"Merhaba {hesap['ad']}")

    if (hesap['bakiye'] >= miktar):
        hesap['bakiye'] -= miktar
        print('Paranızı alabilrsiniz. ')
        bakiyeSorgula(hesap)
    else:
        toplam = hesap['bakiye'] + hesap['ekHesap']

        if (toplam >= miktar):
            ekHesapKullanimi = input('Ek hesap kullanılsın mı (e/h) ')

            if ekHesapKullanimi == 'e':
                bakiye = hesap ['bakiye']

                ekhesapKullanilacakMiktar = miktar - hesap['bakiye']
                hesap['bakiye']= 0 
                hesap['ekHesap'] -= ekhesapKullanilacakMiktar

                print('Paranızı alabilirsiniz.')
                bakiyeSorgula(hesap)
                
            else:
                print(f"{hesap['hesapNo']}') nolu hesabınızda {hesap['bakiye']} bulunmaktadır. ")
        else:
            print('Üzgünüz bakiye yetersiz.')
            bakiyeSorgula(hesap)

def bakiyeSorgula(hesap):
    print(f"{hesap['hesapNo']} nolu hesabınızda {hesap['bakiye']} TL bulunmaktadır. Ek hesap limitiniz ise {hesap['ekHesap']} TL bulunmaktadır.")



paraCek(ArdaHesap, 3000)
bakiyeSorgula(ArdaHesap)

print("------------------------------")

paraCek(ArdaHesap, 2000)
bakiyeSorgula(ArdaHesap)