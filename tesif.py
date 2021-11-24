angka_1= int(input('masukkan satu angka untuk ratusan =')) 
angka_2= int(input('masukkan satu angka untuk puluhan='))
angka_3= int(input('masukkan satu angka untuk satuan='))
             
 #menentukan apakah bilangan tersebut membesar atau tidak
if((angka_2>angka_1) and (angka_3>angka_2) and (angka_3>angka_1)):
   print('bilangan tersebut digit membesar')
   
elif ((angka_3<angka_2) and (angka_2<angka_1) and (angka_3<angka_1)):
    print('bilangan tersebut digit mengecil')
    
    
else:print('bilangan tersebut tidak beraturan')