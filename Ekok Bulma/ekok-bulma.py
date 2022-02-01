# Kullanıcıdan 2 tane sayı alarak bu sayıların en küçük ortak katlarını (EKOK) dönen bir tane fonksiyon yazın.


def ekok(sayi1,sayi2):

    i = 2
    ekok = 1

    while True:

        if(sayi1 % i == 0 and sayi2 % i == 0):
            ekok *=i

            sayi1 //= i     # //= Tam bölümü bul ve sayıya eşitle. Yani sayıyı böldüğümüzde kesirliyse kesir kısmını yok sayar. sayı1 // = i 'in anlamı  i ile sayı1'i tam sayı olarak böl ve çıkan sonucu sayı1'e eşitle demek.
            sayi2 //= i

        elif ( sayi1 % i == 0 and sayi2 % i !=0):
            ekok *=i

            sayi1 //=i

        elif (sayi1 % i != 0 and sayi2 % i == 0 ):
            ekok *=i
            sayi2 //=i
        else:
            i +=1

        if(sayi1 ==1 and sayi2 ==1):
            break        
    return ekok

sayi1 = int(input("Sayı-1:")) 
sayi2 = int(input("Sayı-2:")) 

print("Ekok:",ekok(sayi1,sayi2))
