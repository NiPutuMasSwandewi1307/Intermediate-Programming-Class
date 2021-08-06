#SOAL 1
InputUser = int(input("Masukan angka kurang dari 5\natau \nLebih dari 10 : "))

#Check MANUAL
# isKurangDari = InputUser < 5
# print(isKurangDari)

# isLebihDari = InputUser > 10
# print(isLebihDari)

#Check Simple jadi satu
isCorrect = InputUser<5 or InputUser>10
print("Angka ",InputUser,":",isCorrect)

#SOAL 2
InputUser2 = int(input("Masukan angka lebih besar dari 5\nDAN \nKurang dari 10 : "))
isCorrect2 = InputUser2>5 and InputUser2<10
print("Angka kedua kamu ",InputUser2,":",isCorrect2)