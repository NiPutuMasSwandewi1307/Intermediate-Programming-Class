# TRY & EXCEPTION itu merupakan error handling
#Tujuannya ketika ada error program tidak berhenti atau malah keluar otomatis tapi program itu menghiraukan error itu
# a = 1/0

# try:
#     a = 1/0
# except:
#     print("error pembagi nol")

# print("ini akhir dari program")

### Mengecek input itu angka atau string ###
print("Ini adalah program pembagian sederhana")

# 1/0

while True : 
    try:
        penyebut = int(input("Masukan angka penyebut : "))
        pembilang = int(input("Masukan angka pembilang : "))
        hasil = penyebut/pembilang
        break
    ## Bagus untuk di bugging
    except Exception as Error:
        print(Error)
    """
    except ValueError:
        print("Yang kamu masukan bukan berupa angka") #value error artinya value yg dimasukan tidak sesuai aturan alias berupa simbol atau huruf
    except ZeroDivisionError:
        print("Pembilang yang kamu masukan yakni angka 0, sebaiknya pilih angka lain yaaa...")
    """

    ### CATATAN ###
    """
    1. except : tujuan untuk menerima saja, tanpa tau error nya apa
    2. except dengan mengambil flag (contoh Value Error, Zero, Exception as Error) : jaid lebih spesifik
        ValueError
        Division by Zero or ZeroDvisionError 
    3. IOError : untuk input output. Kalo misal kita masukin/ngebuka file gitu kalo misalnya ada corrupted file
    4. ImportError : Kalo bisa kita import modul tapi di kita ga ada
    5. KeyboardInterupted :
    6. EOError : 
    """
        
print("Yeay, hasil pembagiannya",penyebut,":",pembilang,"=",hasil)
