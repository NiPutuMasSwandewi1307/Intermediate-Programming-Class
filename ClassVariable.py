class mahasiswa():
#class variable : variabel yang dimiliki oleh class
#kalo ada 'self' itu miliki instantiate kalo ga ada berarti miliki class
    jumlah_mahasiswa = 0
    #init untuk initialize, jadi bakal otomati dijalankan saat inisiasi object
    def __init__(self, input_nama, input_nim) : 
        self.nama = input_nama
        self.nim = input_nim
        mahasiswa.jumlah_mahasiswa += 1
        #class.variabel ditambahkan 1 setiap self

### MAIN PROGRAM ###
#inisiasi object
swandewi = mahasiswa("Ni Putu Mas Swandewi", 23502010009)
valen = mahasiswa("Valen Meicella Ishen", 23502010003)
catherine = mahasiswa("Catherine Candice Wijaya", 23502010001)

### print(mahasiswa.__dict__) #mengambil variabel yg dimiliki class ###
#memanggil jumlah mahasiswa
print("Jumlah mahasiswa =",mahasiswa.jumlah_mahasiswa)