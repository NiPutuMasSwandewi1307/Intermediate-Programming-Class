#Operator bitwise, operasi biner, dan binary

a = 9
b = 5

# bitwise OR (|)
c = a|b
print("\n===== OR =====")
print("Nilai :",a,"Biner :", format(a,'08b'))
print("Nilai :",b,"Biner :", format(b,'08b'))
#HASIL
print("Nilai :",c,"Biner :", format(c,'08b'))

# bitwise AND (&)
c = a&b
print("\n===== AND ======")
print("Nilai :",a,"Biner :", format(a,'08b'))
print("Nilai :",b,"Biner :", format(b,'08b'))
#HASIL
print("Nilai :",c,"Biner :", format(c,'08b'))

# bitwise XOR (^) note : hanya true ketika salah satu 1 (true)  kalo keduanya true maka akan menjadi false 
c = a^b
print("\n===== XOR ======")
print("Nilai :",a,"Biner :", format(a,'08b'))
print("Nilai :",b,"Biner :", format(b,'08b'))
#HASIL
print("Nilai :",c,"Biner :", format(c,'08b'))

# bitwise NOT (~)
c = ~a
print("\n===== NOT ======")
print("Nilai :",a,"Biner :", format(a,'08b'))
print("Nilai :",c,"Biner :", format(c,'08b'))

#shifting

#shifting right (>>)
c = a>>1
print("\n===== >> ======")
print("Nilai :",a,"Biner :", format(a,'08b'))
print("Nilai :",c,"Biner :", format(c,'08b'))

#shifting left (<<)
c = a<<2
print("\n===== << ======")
print("Nilai :",a,"Biner :", format(a,'08b'))
print("Nilai :",c,"Biner :", format(c,'08b'))

