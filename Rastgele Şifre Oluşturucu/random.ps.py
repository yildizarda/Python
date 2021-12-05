import random 

print('Şifre nelerden oluş oluşsun ? :')
print('1. Sadece Küçük Harfler')
print('2 Küçük ve Büyük Harfler')
print('3. Küçük-Büyük Harf ve Rakam')
print('4. Küçük-Büyük Harfler, Rakam ve Özel karakterler')

option = int(input('Tercih : '))
length = int(input('Girilecek Şifre Uzunuluğu : '))

option1 = "abcdefghijklmnopqrstuvwxyz"
option2 = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
option3 = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ"
option4 = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"

if(option == 1):
    password =  "".join(random.sample(option1,length ))
elif(option == 2):
    password =  "".join(random.sample(option2,length ))
elif(option == 3):
    password =  "".join(random.sample(option3,length ))
elif(option == 4):
    password =  "".join(random.sample(option4,length ))

print ("Oluşturulan Şifreniz: {0}".format(password))