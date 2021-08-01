#Note : Aturan Programming itu DRY
# Don't Repeat Yourself

class Ojek() :

    def __init__(self, nama, transmisi, daerah) :
        self.nama = nama
        self.transmisi = transmisi
        self.daerah = daerah
    
    def cek_id_ojek(self) :
        print("\nNama :", self.nama,'\nMotor :', self.transmisi,'\nDaerah :', self.daerah)

class Gojek(Ojek) : #Inheritance "Jadi semua itu turunan dari class Ojek"
    pass

ojek1 = Ojek("Swandewi","Matic","Tangerang")
ojek2 = Gojek("Krisna","Manual","Bogor")

#hanya perlu memanggil saja karena sudah print diatas 'def cek id'
(ojek1.cek_id_ojek())
(ojek2.cek_id_ojek())
