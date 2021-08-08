#String Sederhana
print("Hallo apa kabar?")
print('Hai aku baik')

#Jika ingin membuat percakapan (gunakan kompilasi)
print('"Swandewi berkata, bahwa ia akan terus belajar hal baru"')
print("It does'nt matter")

#Cara lain jika malas
print('Have a g\'day') #maksudnya good day

#Doube backslash untuk hal tertentu
print("C:\\user\\Swandewi") #jadi \ didepan membuat \ dibelakangan menjadi sebuah string biasa

# Tab (\t)
print("Social Distancing")
print("Social\tDistancing")

# Backspace (\b)
print("Bersama kami")
print("Bersama \bkami") #Ini jadi backspace

# Newline (\n)
print("Yuk Ikut \nKami")

# New Line
print("Kalimat Pertama.\nKalimat Kedua.") # LF -> line feed -> unix, macos, linux
print("Kalimat Pertama.\rKalimat Kedua.") # CR -> carriage return -> commodore, acorn, lisp 
print("Kalimat Pertama.\r\nKalimat Kedua.") # CRLF -> line feed carriage return -> dipakai oleh windows

# Special Case
print("C:\new folder")
print("C:\\new folder") #solusi 1
print(r"C:\new folder") #solusi 2 (menggunakan raw string)

# Multiline Literal String
print("""
Nama : Ni Putu Mas Swandewi
Jurusan : Software Engineering
Cita-cita : Programmer (or etc field in IT) then be a CEO and build my own business
Age : 19 years old (July, 13th 2002)
""")


########## PART 2 ##########

# Operasi & Manipulasi

# 1) Menyambungkan string (concatenate)
nama_awal = "Ni Putu"
nama_akhir = "Mas Swandewi"

nama_lengkap = nama_awal + " " + nama_akhir
print(nama_lengkap)

# 2) Menghitung panjang string
panjang = len(nama_lengkap)
print("Panjang dari " + nama_lengkap + "=", str(panjang))

# 3) Operator Untuk String
Cek = "swandewi" #tapi ini sangat dipengaruhi upper dan lower case
Status = Cek in nama_lengkap
print (Cek + " ada ga di" + nama_lengkap + " : " + str(Status))

# 4) Mengulang string
print(10*"wk")

# 5) Mengambil data (Indexing)
print("Index ke-0 : " + nama_lengkap[0])
print("Index ke-(-1) : " + nama_lengkap[-1]) #Jadi (-1) ambil dari paling belakang
print("Index ke-(0 sampai 6) : " + nama_lengkap[0:7]) #(:) artinya sampai, dan kenapa angka 7 bukan 6 karena 7 nanti tidak dihitung alias dihitung sampai sebelum 7
print("Index ke-(0 sampai akhir) : " + nama_lengkap[0:])
print("Index ke-(0,2,4 dst 19) : " + nama_lengkap[0:19:2])

#Item Paling
print("Paling Kecil : " + min(nama_lengkap))
print("Paling Besar : " + max(nama_lengkap))

#ASCII CODE
AsciiCode = ord(" ")
print("ASCII Code untuk spasi adalah : " + str(AsciiCode)) #Karena sebelumnya angka jadi ubah dulu ke string

angka = 124
print("Karakter untuk ASCII (" + str(angka) + ") adalah : " + chr(angka))

# Operator dalam bentuk Method
data = "Saya adalah seorang mahasiswi Universitas Prasetiya Mulya"
jumlah = data.count('a') #data itu : object sedangkan count : method
print("jumlah huruf a pada " + data + " = " + str(jumlah))