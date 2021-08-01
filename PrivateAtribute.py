### CLASS ###
class mahasiswa():
    #Dikasi (__) agar bersifat private
    __nilai = 0 #private : default
    jurusan = "Software Engineering"
    
    def __init__(self, input_nama, input_nim) : 
        self.nama = input_nama #public
        self.nim = input_nim #public

    def uts(self, input_nilai) :
        self.__nilai += input_nilai
    
    def uas(self, input_nilai) :
        self.__nilai += input_nilai

    def check_status(self) :
        if self.__nilai <= 50 :
            print(self.nama, "Kamu tidak LULUS")
        else :
            print(self.nama, "SELAMAT KAMU LULUS")


### MAIN PROGRAM ###
swandewi=mahasiswa("Ni Putu Mas Swandewi", 23502010009)
valen=mahasiswa("Valen Meicella Ishen", 23502010003)

swandewi.uts(40)
swandewi.uas(45)

swandewi.check_status()

valen.uts(10)
valen.uas(35)
valen.check_status()

###KESIMPULAN###
# Private Atrbute yakni atribut yang hanya bisa dirubah di dalam kelas saja
