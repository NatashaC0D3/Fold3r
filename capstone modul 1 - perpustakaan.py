from tabulate import tabulate 
import regex as re 
import datetime 
import json 

#MAIN DATA DICTIONARIES ----------------------------------------------------------------------
#
global data  
Data_Member = [
    {"Member": "Anna", "ID_Member": "An4128", "Kontak": "081356724128"},
    {"Member": "Benny", "ID_Member": "Be5343", "Kontak": "081597435343"},
    {"Member": "Chinta", "ID_Member": "Ch1176", "Kontak": "085811981176"}
]

Data_Buku = [
    {"Rek":"0", "Buku": "Don Quixote", "ID_Buku": "DE11", "Status": "ADA", "Member": "-", "ID_Member": "-", "Kembali": "-"}, 
    {"Rek":"1", "Buku": "Tale of Two Cities", "ID_Buku": "TS19", "Status": "sedang dipinjam", "Member": "Anna", "ID_Member": "An4128", "Kembali": "28/02/2024"}, 
    {"Rek":"0", "Buku": "Lord of the Rings", "ID_Buku": "LS18", "Status": "ADA", "Member": "-", "ID_Member": "-", "Kembali": "-"}, 
    {"Rek":"0", "Buku": "Book of Mormon", "ID_Buku": "BN14", "Status": "ADA", "Member": "-", "ID_Member": "-", "Kembali": "-"}, 
    {"Rek":"1", "Buku": "Little Prince", "ID_Buku": "LE13", "Status": "sedang dipinjam", "Member": "Anna", "ID_Member": "An4128", "Kembali": "01/03/2024"}, 
    {"Rek":"0", "Buku": "Harry Potter", "ID_Buku": "HR12", "Status": "sedang dipinjam", "Member": "Benny", "ID_Member": "Be5343", "Kembali": "01/03/2024"}, 
    {"Rek":"1", "Buku": "Alice in Wonderland", "ID_Buku": "AD19", "Status": "sedang dipinjam", "Member": "Benny", "ID_Member": "Be5343", "Kembali": "01/03/2024"},   
    {"Rek":"0", "Buku": "Dream of the Red Chamber", "ID_Buku": "DR24", "Status": "sedang dipinjam", "Member": "Benny", "ID_Member": "Be5343", "Kembali": "05/03/2024"}, 
    {"Rek":"0", "Buku": "Narnia", "ID_Buku": "NA6", "Status": "ADA", "Member": "-", "ID_Member": "-", "Kembali": "-"}, 
    {"Rek":"0", "Buku": "Goosebumps", "ID_Buku": "GS10", "Status": "ADA", "Member": "-", "ID_Member": "-", "Kembali": "-"}    
]

#PUBLIC POINT------------------------------------------------------------------------------------
#
#--- MP(Main Page): Selamat datang, list rekomendasi
#~~~~~~
def HeadMainPage():
    today = datetime.date.today()
    print(f'''
        ##### Selamat Datang di Perpustakaan #####
                    ~~~ TanTan ~~~
Jangan Lupa Cek Buku Rekomendasi Kita Hari Ini {today}:''')

def ListRekomendasi():
    RekomendasiBuku = [book for book in Data_Buku if book["Rek"] == "1"]
    return [[book["Buku"], book["ID_Buku"], book["Status"], book["Kembali"]] for book in RekomendasiBuku]

def Flow(): 
    while True: 
        pilih = input("Masukan Pilihan Menu: ")
        if pilih == '0':
            CariBuku()
        elif pilih == '1':
            Member_PG()
        elif pilih == '2':
            Admin_PG()
        elif pilih == '3':
            print('Keluar Dari Program...')
            break
        else: 
            print("Pilihan Yang Kamu Masukan Salah. Silahkan Coba Lagi")
#~~~~~~
def MainPage():
    HeadMainPage()
    Tabulate_RekomendasiBuku = ListRekomendasi()
    print(tabulate(Tabulate_RekomendasiBuku, headers=["Buku", "ID Buku", "Status", "Kembali"], tablefmt="pretty"))
    print('''
    Pilih Menu:
    0 => Cari Buku
    1 => Log In Member
    2 => Log In Admin
    3 => Exit''')
    Flow()


#--- MP.Cari Buku: List lengkap (flow: LI.Member, LI.Admin, MP) 
#~~~~~
def CariJudul(Data_Buku, keys=['Buku', 'ID_Buku', 'Status', 'Kembali']): 
    Cari_Judul = input ('Masukan Judul Buku Yang Ingin Dicari: ').strip()
    filtered_CariJudul = [item for item in Data_Buku if item.get('Buku').lower() == Cari_Judul.lower()]
    if filtered_CariJudul:
        headers = keys
        rows = [[book[key] for key in keys] for book in filtered_CariJudul]
        print(tabulate(rows, headers=headers, tablefmt="pretty"))
    else:
        print("Buku Yang Kamu Cari Tidak Ada. Silahkan Coba Lagi")

def HeadCariBuku():
    now = datetime.datetime.now ()
    Bulan_Ini = now.strftime("%m-%Y")
    print(f'''\n Berikut List Lengkap Koleksi Kita per Bulan {Bulan_Ini}:''')

def FullCollection(Data_Buku, keys=['Buku', 'ID_Buku', 'Status', 'Kembali']):  
    extracted_FullCollection = [{key: item.get(key) for key in keys} for item in Data_Buku]
    return extracted_FullCollection

def FlowCariBuku(): 
    HeadCariBuku()
    print(tabulate([[book[key] for key in ['Buku', 'ID_Buku', 'Status', 'Kembali']] for book in Data_Buku], headers=['Buku', 'ID_Buku', 'Status', 'Kembali'], tablefmt="pretty")) 
    while True: 
        pilih = input("Masukan Pilihan Menu: ")
        if pilih == '0':
            CariJudul(Data_Buku)
        elif pilih == '1':
            Member_PG()
        elif pilih == '2':
            Admin_PG()
        elif pilih == '3':
            MainPage()
            break
        else: 
            print("Pilihan Yang Kamu Masukan Salah. Silahkan Coba Lagi")
    FullCollection() 
#~~~~~~
def CariBuku(Data_Buku): 
    print('''
    Pilih Menu:
    0 => Cari Judul 
    1 => Log In Member
    2 => Log In Admin
    3 => Main Page''') 
    FlowCariBuku() 
     


#MEMBER POINT------------------------------------------------------------------------------------
#--- Member.PG: Log In Member
def FlowLogMember ():
    while True: 
        pilih = input("Masukan Pilihan Menu: ")
        if pilih == '0':
            PassMember_Input = input("Masukan ID Member: ").strip()

            if any(member['ID_Member'].lower() == PassMember_Input.lower() for member in Data_Member):
                M_HeadMember(PassMember_Input)
                break
            else:
                print("ID_Member Salah")
                pilih_salah = input("Apakah kamu Mau: \n1) Mencoba Lagi, atau \n2) Membuat ID Member Baru").strip()

                if pilih_salah == '2':
                    print("Mau Menjadi Member? Silahkan Hubungi Admin Untuk Memproses ID Member Bar")
                    break
        elif pilih == '1':
            MainPage()
            break
        else: 
            print("Pilihan Yang Kamu Masukan Salah. Silahkan Coba Lagi")

def Member_PG(): 
    print('''
    Pilih Menu:
    0 => Log In Member (berhasil -> M_Member; gagal -> coba lagi atau main page)
    1 => Main Page''') 
    FlowLogMember()   



#--- M_Member: Selamat datang, status pinjam buku berapa banyak apa aja sampai kapan
#~~~~~~
def M_HeadMember(PassMember_Input):
    NamaMember = next((item['Member'] for item in Data_Member if item['ID_Member'].lower() == PassMember_Input.lower()), None)
    print(f'Selamat Datang, {NamaMember}!\n')
    return NamaMember

def M_ListBukuDipinjam(PassMember_Input): #filter
    NamaMember = next((item['Member'] for item in Data_Member if item['ID_Member'].lower() == PassMember_Input.lower()), None)  # Re-fetch the name based on ID
    AdaPeminjaman = [HitungBuku for HitungBuku in Data_Buku if HitungBuku['Member'] == NamaMember and HitungBuku['Status'].lower() == "sedang dipinjam"]
    JumlahBuku = len(AdaPeminjaman)       

    print(f'Status: Ada Peminjaman Sebanyak {JumlahBuku} Buku')

    if JumlahBuku > 0:
        headers = ['Buku', 'Kembali']
        rows = [[HitungBuku['Buku'], HitungBuku['Kembali']] for HitungBuku in AdaPeminjaman]
        print(tabulate(rows, headers=headers, tablefmt="pretty"))
    else: 
        print("Tidak ada Peminjaman yang Sedang Berlangsung. Mau Pinjam Buku? Silahkan Hubungi Admin Untuk Memproses Peminjaman Buku")

def M_Flow(PassMember_Input): 
    while True: 
        pilih = input("Masukan Pilihan Menu: ")
        if pilih == '0':
            M_CariBuku(PassMember_Input)
        elif pilih == '1':
            MainPage()
            break
        else: 
            print("Pilihan Yang Kamu Masukan Salah. Silahkan Coba Lagi")
#~~~~~~
def M_Member(PassMember_Input): 
    NamaMember = M_HeadMember(PassMember_Input)
    print('''
    Pilih Menu:
    0 => Cari Buku di Full Collection
    1 => Log out (Main Page)''')
    M_ListBukuDipinjam(PassMember_Input)
    M_Flow(PassMember_Input)



#--- M_CariBuku: List lengkap (flow: M_Member) 
#~~~~~
def M_FlowCariBuku(PassMember_Input): 
    HeadCariBuku()
    print(tabulate([[book[key] for key in ['Buku', 'ID_Buku', 'Status', 'Kembali']] for book in Data_Buku], headers=['Buku', 'ID_Buku', 'Status', 'Kembali'], tablefmt="pretty")) 
    while True: 
        pilih = input("Masukan Pilihan Menu: ")
        if pilih == '0':
            CariJudul(Data_Buku)
        elif pilih == '1':
            M_Member(PassMember_Input) 
            break
        else: 
            print("Pilihan Yang Kamu Masukan Salah. Silahkan Coba Lagi")
    FullCollection() 
#~~~~~~
def M_CariBuku(PassMember_Input): 
    print('''
    Pilih Menu:
    0 => Cari Judul 
    1 => Main Member (M_Member())''') 
    M_FlowCariBuku(PassMember_Input)


#ADMIN POINT------------------------------------------------------------------------------------
#--- Admin.PG: Log In Admin
def FlowLogAdmin(): 
       while True:  
        pilih = input("Masukan Pilihan Menu: ")
        if pilih == '0':
            ID_Admin = "Ad2024"
            Pass_Admin = "13579" 
        
            print_ID = input ("masukan ID Admin: ")
            print_Pass = input ("masukan Pass Admin: ")
        
            if print_ID == ID_Admin and print_Pass == Pass_Admin:
                A_Admin()
                break
            else:
                print("ID_Member Salah")
                continue
        elif pilih == '1':
            MainPage()
            break
        else: 
            print("Pilihan Yang Kamu Masukan Salah. Silahkan Coba Lagi")

def Admin_PG(): 
    print('''
    Pilih Menu:
    0 => Log In Admin (berhasil -> M_Admin; gagal -> coba lagi atau main page)
    1 => Main Page''') 
    FlowLogAdmin()   



#--- A_Admin: Selamat datang, status buku apa dipinjam siapa sampai kapan
#~~~~~~
def A_HeadAdmin():
    today = datetime.date.today()
    print(f''' 
Selamat Datang [ADMIN]! \n 
Berikut List Buku yang Sedang Dipinjam per Hari Ini {today}: ''')
    
    BukuDipinjam = [HitungBukuDipinjam for HitungBukuDipinjam in Data_Buku if HitungBukuDipinjam['Status'].lower() == "sedang dipinjam"]
    JumlahBukuDipinjam = len(BukuDipinjam)
    print(f'Jumlah {JumlahBukuDipinjam} Buku')
    
    headers = ['Buku', 'ID_Buku', 'Status', 'ID_Member', ' Kembali']
    rows = [[HitungBukuDipinjam['Buku'], HitungBukuDipinjam['ID_Buku'], HitungBukuDipinjam['Status'], HitungBukuDipinjam['ID_Member'], HitungBukuDipinjam['TGL_Kembali']] for HitungBukuDipinjam in BukuDipinjam]
    print(tabulate(rows, headers=headers, tablefmt="pretty"))

def A_Flow(): 
   while True: 
        pilih = input("Masukan Pilihan Menu: ")
        if pilih == '0':
            CariBuku()
        elif pilih == '1':
            A_CheckBuku()
        elif pilih == '2':
            A_CheckMember()
        elif pilih == '3':
            MainPage()
            break
        else: 
            print("Pilihan Yang Kamu Masukan Salah. Silahkan Coba Lagi")
#~~~~~~
def A_Admin(): 
    A_HeadAdmin()
    print('''
    Pilih Menu:
    0 => Cari Buku di List Buku Dipinjamkan
    1 => Check Buku
    2 => Check Member    
    3 => Log out (Main Page)''')
    A_Flow()



#--- A_CheckBuku: List lengkap (flow: Update List Buku, Update Status Buku, A_Admin) 
#~~~~~
def A_FlowCheckBuku(): 
    #Kalau pilih 0:  
    def HeadCariBuku() 
    ### logika pilih menu
    def FullCollection() 
    # otherwise, pindah halaman
#~~~~~~
def A_CheckBuku(): 
    def HeadCariBuku()
    print('''
    Pilih Menu:
    0 => Cari Judul (filter print)
    1 => Update List Buku
    2 => Update Status Buku
    3 => Main Admin (A_Admin())''') 
    def FullCollection()
    def A_FlowCheckBuku()



#--- A_CheckBuku_UpdateListBuku (Flow: Check Buku )  
#~~~~~
def A_Head_BukuBaru():
def A_Head_HapusBuku(): 
def A_Flow_UpdateListBuku(): 
    #Kalau pilih 0:  
    def A_Head_BukuBaru() 
    ### logika pilih 0 (berhasil -> Selamat; gagal -> karena judul sudah ada)
    #Kalau pilih 1:
    def A_Head_HapusBuku(): 
    ### logika pilih 1 (Berhasil -> berhasil hapus; gagal -> karena masih dipinjam, atau judul tidak ada)
    # otherwise, pindah halaman
#~~~~~~
def A_UpdateListBuku(): 
    print('''
    Pilih Menu:
    0 => Daftar Buku Baru (filter print)
    1 => Hapus Buku (filter print)
    2 => Kembali (A_CheckBuku())''') 
    def A_Flow_UpdateListBuku()
        



#--- A_CheckBuku_UpdateStatusBuku (Flow: Check Buku )  
#~~~~~
def A_Head_CheckOutBuku():
def A_Head_ReturnBuku(): 
def A_Flow_UpdateStatusBuku(): 
    #Kalau pilih 0:  
    def A_Head_CheckOutBuku() 
    ### logika pilih 0 (berhasil -> Selamat Menikmati; gagal -> karena judul sedang dipinjam member lain, atau judul tidak ada)
    #Kalau pilih 1:
    def A_Head_ReturnBuku(): 
    ### logika pilih 1 (Berhasil -> Terima Kasih; gagal -> Karena Judul Belum Check Out)
    # otherwise, pindah halaman
#~~~~~~
def A_UpdateStatusBuku(): 
    print('''
    Pilih Menu:
    0 => Check Out Buku (filter print)
    1 => Return Buku (filter print)
    2 => Kembali (A_CheckBuku())''') 
    def A_Flow_UpdateStatusBuku()



#--- A_CheckMember: List lengkap (flow: Update List Member, A_Admin) 
#~~~~~
def CariMember(): #filter 
def HeadCariMember():
def FullMember():
def A_FlowCheckMember():
    #Kalau pilih 0:  
    def HeadCariMember() 
    ### logika pilih menu
    def FullMember()
    #Otherwise, pindah Halaman 
#~~~~~~
def A_CheckMember(): 
    def HeadCariMember()
    print('''
    Pilih Menu:
    0 => Cari Member (filter print)
    1 => Update Member
    3 => Main Admin (A_Admin())''') 
    def FullMember()
    def FlowCheckMember() 



#--- A_CheckMember_UpdateListMember (Flow: Check Member )  
#~~~~~
def A_Head_MemberBaru():
def A_Head_HapusMember(): 
def A_Flow_UpdateListMember(): 
    #Kalau pilih 0:  
    def A_Head_MemberBaru() 
    ### logika pilih 0 (berhasil -> Selamat Datang; gagal -> karena nama sudah ada)
    #Kalau pilih 1:
    def A_Head_HapusMember(): 
    ### logika pilih 1 (Berhasil -> Terima Kaih; gagal -> karena masih pinjam buku, atau Nama tidak ada)
    # otherwise, pindah halaman
#~~~~~~
def A_UpdateListMember(): 
    print('''
    Pilih Menu:
    0 => Daftar Member Baru (filter print)
    1 => Hapus Member (filter print)
    2 => Kembali (A_CheckMember())''') 
    def A_Flow_UpdateListMember()
        



