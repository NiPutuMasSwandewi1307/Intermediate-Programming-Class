"""
Literal : suatu nilai yg tidak punya variabel jadi langsung angka (a==4, nah 4 disebut literal & a memakan memory karena berupa variabel)

KOMPARASI PYTHON
1)Kurang dari (<)
2)Lebih dari (>)
3)Kurang dari sama dengan (<=)
4)Lebih dari sama dengan (>=)
5)Komparasi membandingkan nilai sama pada object, variabel djs (is)
6)Komparasi membandingan nilai tidak sama pada object djs (is not)
is : membandingkan object
"""

a=4
b=4
hasil = a is b
print("a is b =",hasil)


"""

"""

### BOOLEAN ###
print("=== NOT ===")
a = True
b = not a
print("Data a :",a,"\nData b :",b)

print("=== OR ===")
#Yang penting salah satu TRUE maka hasilnya TRUE
a = True
b = False
hasil = a or b
print("Hasil a or b adalah",hasil)#maksudnya (:) adalah berbanding

print("=== AND ===")
#Hanya TRUE ketika keduanya TRUE
a = True
b = False
hasil2 = a and b
print("Hasil a AND b adalah",hasil2)

print("=== XOR ===")
#Hanya TRUE ketika salah satu TRUE, hanya salah satu, jadi kalo keduanya TRUE hasilnya tetep FALSE
a = True
b = False
hasil2 = a and b
print("Hasil a AND b adalah",hasil2)