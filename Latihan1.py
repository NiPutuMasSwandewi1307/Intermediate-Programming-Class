#FYI : Python itu intepreted language. Jadi harus berurutan
#Makanya Class harus diatas

### CLASS ###
class mahasiswa():
    nama = 'nama' #atribut mahasiswa

#methode : fungsi yang nempel di dalam class
#kalo fungsi aja berarti di luar class
#self : untuk mengindentifikasi object mana yang menggunakan class
    def belajar(self,kondisi): #methode
        print(self.nama, "sedang belajar",kondisi)
    
    def main(self) :
        print(self.nama, "sedang main game")

### MAIN PROGRAM ###
#1) Kita melakukan 'instantiate' dulu
swandewi=mahasiswa()
valen=mahasiswa()

swandewi.nama = "Ni Putu Mas Swandewi"
valen.nama = "Valen Meicella Ishen"

# print(swandewi.nama)
# print(valen.nama)

#memanggil method
swandewi.belajar("produktif jiwaaa")
valen.main()
