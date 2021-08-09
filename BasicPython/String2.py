# Upper Case
nama = "Ni Putu Mas Swandewi"
print("Normal : " + nama)
# nama = nama.upper()
print("Upper : " + nama.upper())

print("\n######\n")

# Lower Case
kata = "SEMANGAT PAGI"
print("Normal : " + kata)
# nama = nama.upper()
print("Upper : " + kata.lower())

print("\n######\n")

# Is X Method
kata = "jalan"
ApakahLower = kata.islower()
print("\'" + kata + "\'" + " apakah lower : " + str(ApakahLower))
ApakahUpper = kata.isupper()
print("\'" + kata + "\'" + " apakah upper : " + str(ApakahUpper))

"""
isaplha() : untuk ngecek semua komponen string adalah huruf
isalnum() : untuk ngecek semua komponen string adalah huruf dan angka
isdecimal() : untuk ngecek semua komponen string adalah angka saja
isspace() : untuk ngecek apakah kompenen string adalah string kosong (entah spasi, newline, tab)
istitle() : untuk ngecek semua kompenen string diawali dengan huruf besar/kapitas
"""

# Startswith & Endswith
cek = "Mas Swandewi".startswith("Mas")
print("Start : " + str(cek))
cek = "Mas Swandewi".endswith("Mas")
print("End: " + str(cek))

# Penggabungan Komponen join() split()
komponen = ['Putu','Kadek','Komang','Ketut']
gabungan = ','.join(komponen) #tanda koma (,) bisa diganti jadi apapun, entah spasi, entah titik atau apapun
print(komponen)
print(gabungan)
# print(komponen.join(',')) MAKE INI EMANG GAMAU

komponen2 = "Putu,Kadek,Komang,Ketut"
# pisah = ','.split(komponen2)
print(komponen2.split(',')) #BEGITU JUGA SEBALIKNYA

# JADI pemakaian split dan join itu strukturnya berbeda.

print("\n######\n")

#Alokasi Karakter rjust, ljust, dan centre
print(5*'#'+"Jeda"+'#'*5) #Nah ini manual

jeda = 'jeda'.rjust(10)
print("'" + jeda + "'")

spasi = 'spasi'.center(11,'-')
print(spasi)

#Kebalikan itu make strip
spasi = spasi.strip('-')
print(spasi)

print("\n######\n")

# FORMAT STRING
nama = "Swandewi"
format_string = f"Hallo {nama} !, apa kabar?"
print(format_string)

tahun = "2021"
format_string = f"Tahun berapa sekarang? \nTahun ini adalah tahun : {tahun}"
print(format_string)

angka = 15
format_string = f"Bilangan bulat = {angka:d}"
print(format_string)

angka = 15
format_string = f"Bilangan bulat = {angka:03}" #menambah angka 0 didepan jika angka belum memenuhi 3 buah
print(format_string)

uang = 5000000000
format_string = f"Uang saya sebanyak = {uang:,}"
print(format_string)

angka = 15.4321
format_string = f"Bilangan desimal = {angka:.2f}" #(.) artinya koma itu, 2 artinya 2 angka dibelakang koma, f artinya float (tipe data)
print(format_string)

#Menambahkan tanda (+) & (-)
angka1 = +15
angka2 = -10
format_string1 = f"Bilangan bulat = {angka1:+d}" # (+d)
format_string2 = f"Bilangan bulat = {angka2:+d}"
print(format_string1)
print(format_string2)

#Menambahkan tanda (%)
persentase = 99
format_persen = f"Peluang kamu lolos adalah = {persentase:.0%}"
print(format_persen)

# Format angka lain (binary, octa, hexa)
angka = 200
format_binary = f"Binary = {bin(angka)}"
format_octa = f"Octa = {oct(angka)}"
format_hexa = f"Hexa = {hex(angka)}"

print(format_binary)
print(format_octa)
print(format_hexa)

# Multiline pada format bisa menggunakan newline (\n) seperti diatas udah buat atau...
nama = "Ni Putu Mas Swandewi"
jurusan = "Software Engineering"
universitas = "Prasetiya Mulya"
asal = "Bali"
sma = "SMA Negeri Bali Mandara"
umur = 19
data_string = f"""
Nama : {nama.center(20)}
Umur : {str(umur).center(20)}
Jurusan : {jurusan.center(20)}
Universitas : {universitas.center(20)}
Provinsi Asal : {asal.center(20)}
Asal SMA : {sma.center(20)}
"""
print(data_string)