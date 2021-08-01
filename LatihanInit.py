#FYI : Python itu intepreted language. Jadi harus berurutan
#Makanya Class harus diatas

### CLASS ###
class mahasiswa():
    #Inizialitation : Menjadi permulaan
    #Dijalankan saat inisialisasi objek
    def __init__(self, input_nama, input_nim) : 
        self.nama = input_nama
        self.nim = input_nim

    def belajar(self,kondisi): #method
        print(self.nama, "sedang belajar",kondisi)
    
    def main(self) :
        print(self.nama, "sedang main game")

### MAIN PROGRAM ###
#Jadi lebih praktis & tidak perku mengulang setiap atribut baru
swandewi=mahasiswa("Ni Putu Mas Swandewi", 23502010009)
# valen=mahasiswa("Valen Meicella Ishen")

print(swandewi.nama,swandewi.nim)
# print(swandewi.nim)
# print(valen.nama)
swandewi.nama = "Gusti Ayu Mas Swandewi"
print(swandewi.nama) ## mudah diubah dan diakses karena sifatnya publik

# #memanggil method
# swandewi.belajar("produktif jiwaaa")
# valen.main()
