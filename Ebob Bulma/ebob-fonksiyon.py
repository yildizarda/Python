# Kullanıcıdan 2 tane sayı alarak bu sayıların en büyük ortak bölenini (EBOB) dönen bir tane fonksiyon yazın.




def ebob_bulma(sayı1,sayı2):
    
    i = 1
    ebob = 1
    while (i <= sayı1 and i <= sayı2 ):
 
        if ( not (sayı1 % i) and not (sayı2 % i)):
            ebob = i
        i += 1
    return ebob
sayı1 = int(input("Sayı-1:")) 
sayı2 = int(input("Sayı-2:")) 
 
print("Ebob:",ebob_bulma(sayı1,sayı2))









# def ebob_bulma(sayı1,sayı2): # sayı1 ve sayı2'nin en büyük ortak bölenini bulan foksiyon tanımla
 
#     i = 1 #i'nin varsayılan değeri 1'dir
#     ebob = 1 # ebob varsayılan değeri 1'dir
    
#     while (i <= sayı1 and i <= sayı2 ): #i'nin değeri, sayı1 VE sayı2'den küçük eşit olduğu sürece işlem devam etsin.
 
#         if ( not (sayı1 % i) and not (sayı2 % i)): # sayı1 VE sayı2'nin bölümünden kalan False DEĞİLSE, yani True ise
#             ebob = i #obeb değerinin i değerine eşitle
#         i += 1 # i'nin değerini 1 artır, yeni değer bu olsun.
#     return ebob # fonksiyon çalışıp nihayete erince ebob değerini hafızada tut/döndür. 
 
# sayı1 = int(input("Sayı-1:")) #sayı1 stringini girin, sayı değerine (integer) çevirin
# sayı2 = int(input("Sayı-2:")) #sayı2 stringini girin, sayı değerine (integer) çevirin
 
# print("Ebob:",ebob_bulma(sayı1,sayı2)) # "Ebob:" yaz bir boşluk bırak, girilen sayı1 ve sayı2 değerlerini ebob_bulma fonksiyonunda işlet ve sonucun ekrana yaz. 
 
# # anlaşılması en zor kısım şurası sanıyorum;
# if ( not (sayı1 % i) and not (sayı2 % i)):
# # (sayı1 % i) ifadesi; "sayı1'in, i değerine bölümünden kalan" değer demektir. (True veya False olarak çıktı verir. Kalan sıfır ise (yani kalansız bölünüyorsa) False anlamına gelir)
# # not (sayı1 % i) ifadesi ise; sayı1'in i değerine bölümünden kalan değerin tersi demektir. (True veya False olarak çıktı verir)     
# #Python'da sıfır (0) ve boş değer (""), False olarak kabul edilir. Geri kalan tüm değerler True olarak kabul edilir.
# # not ibaresi, sonucun tersini al, ters çevir demektir. True ise False yap, False ise True yap.
 
# if ( not (sayı1 % i) and not (sayı2 % i)):
# #bu kod ile şunu yapmak istiyoruz;
#     # sayı1'in VE sayı2'nin,  i'ye bölümünden kalan sıfır olsun, yani kalansız bölünürse, aşağıdaki kodları çalıştır.
 
# #eğer (tersini al (sayı1'in i'ye bölümünden kalan değer) VE tersini al (sayı2'in i'ye bölümünden kalan değer)):    
# #eğer ((sayı1'in i'ye bölümünden kalan True ise) VE (sayı1'in i'ye bölümünden kalan True ise)):
 
# #eğer (True VE True) ise:                                                           
# #yani sayı1 VE sayı2, i değerine kalansız bölünüyorsa
                                                           
 
# if ( not (sayı1 % i) and not (sayı2 % i)): #Bu kodu aşağıdaki gibi yazmak belki daha anlaşılır olmasını sağlar.
# if ((sayı1 % i) == False and (sayı2 % i) == False):