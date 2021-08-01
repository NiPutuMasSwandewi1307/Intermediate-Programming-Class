#input output file

#ATURAN
"""
w = write mode / mode menulis dan menghapus atau menimpa file lama. Jika file tidak ada maka akan buat baru
r = read only mode 
a = appending mode / menambahkan data di akhir baris
r+ = read & write mode
"""
### MEMBUAT FILE TEXT ###
#Tentu harus membuat lembaran baru (maksudnya file baru)/atau ceking data ini akan dimasukan ke file mana
file = open ("Data.txt", "w")

file.write("Aku sedang semangat belajar")
file.write("\nIni baris kedua")

file.close()

### MEMBACA FILE TEXT ###
file2 = open ("Data.txt", "r")
#print(file2.read(10)) artinya baca 10 kata
print(file2.read())
print(file2.readline()) #baca satu baris

file2.close()

### APPENDING MODE
file3 = open("Data.txt", "a")

file3.write("\nBaris ini dibuat dengan mode append")

file.close()

