from tabulate import  tabulate 
import datetime 
import sys

#Data buku di perpustakaan dan status 
Data_Buku = [
    {"Rek":"0", "Buku": "Don Quixote", "ID_Buku": "DE11", "Status": "ADA", "ID_Member": "-", "Kembali": "-"}, 
    {"Rek":"1", "Buku": "Tale of Two Cities", "ID_Buku": "TS19", "Status": "sedang dipinjam", "ID_Member": "An4128", "Kembali": "28/02/2024"}, 
    {"Rek":"0", "Buku": "Lord of the Rings", "ID_Buku": "LS18", "Status": "ADA", "ID_Member": "-", "Kembali": "-"}, 
    {"Rek":"0", "Buku": "Book of Mormon", "ID_Buku": "BN14", "Status": "ADA", "ID_Member": "-", "Kembali": "-"}, 
    {"Rek":"1", "Buku": "Little Prince", "ID_Buku": "LE13", "Status": "sedang dipinjam", "ID_Member": "An4128", "Kembali": "01/03/2024"}, 
    {"Rek":"0", "Buku": "Harry Potter", "ID_Buku": "HR12", "Status": "sedang dipinjam", "ID_Member": "Be5343", "Kembali": "01/03/2024"}, 
    {"Rek":"1", "Buku": "Alice in Wonderland", "ID_Buku": "AD19", "Status": "sedang dipinjam", "ID_Member": "Be5343", "Kembali": "01/03/2024"},   
    {"Rek":"0", "Buku": "Dream of the Red Chamber", "ID_Buku": "DR24", "Status": "sedang dipinjam", "ID_Member": "Be5343", "Kembali": "05/03/2024"}, 
    {"Rek":"0", "Buku": "Narnia", "ID_Buku": "NA6", "Status": "ADA", "ID_Member": "-", "Kembali": "-"}, 
    {"Rek":"0", "Buku": "Goosebumps", "ID_Buku": "GS10", "Status": "ADA", "ID_Member": "-", "Kembali": "-"}    
]

# data log in member dan peminjama buku
Data_Member = [
    {"Member": "Anna", "ID_Member": "An4128", "Kontak": "081356724128"},
    {"Member": "Benny", "ID_Member": "Be5343", "Kontak": "081597435343"},
    {"Member": "Chinta", "ID_Member": "Ch1176", "Kontak": "085811981176"}
]

# data log in staf dan data edit
Data_Admin = {
    "ID_Admin": "Ad2024",
    "Pass_Admin": "13579"
}

# variasi global 
username = "" #untuk log in

#tampilan print untuk hasil pencarian buku maupun member
def read_data_buku_tampilan_member():
    headers=['Buku', 'ID_Buku', 'Status', 'Kembali']
    display = [{key: book[key] for key in headers} for book in Data_Buku]
    print(tabulate(display, headers="keys", tablefmt="pretty"))   

def read_data_buku_tampilan_admin():
    print(tabulate(Data_Buku, headers="keys", tablefmt="pretty"))

def read_data_member():
    print(tabulate(Data_Member, headers="keys", tablefmt="pretty"))

def read_data_peminjaman_member(username):
    list_pinjam = [pinjam for pinjam in Data_Buku if pinjam["ID_Member"].lower() == username.lower() and pinjam["Status"].lower() == "sedang dipinjam"]
    jumlah = len(list_pinjam)
    print(f"status: ada peminjaman sebanyak {jumlah} buku")

    if jumlah >0:
        headers = ['Buku', 'ID_Buku', 'Kembali']
        rows = [[pinjam["Buku"], pinjam['ID_Buku'], pinjam['Kembali']] for pinjam in list_pinjam]
        print(tabulate(rows, headers=headers, tablefmt="pretty"))
        print("Mau pinjam buku lagi? Silahkan hubungi admin")
        Log_In_Member()

    else:
        print("tidak ada peminjaman. Mau pinjam buku? Silahkan hubungi admin")
        Log_In_Member()

def read_data_peminjaman_admin():
    list_pinjam = [pinjam for pinjam in Data_Buku if pinjam["Status"].lower() == "sedang dipinjam"]
    jumlah = len(list_pinjam)
    print(f"status: ada peminjaman sebanyak {jumlah} buku")

    if jumlah >0:
        headers = ['Buku', 'ID_Buku', 'Status', 'ID_Member', 'Kembali']
        rows = [[pinjam["Buku"], pinjam['ID_Buku'], pinjam['Status'], pinjam['ID_Member'], pinjam['Kembali']] for pinjam in list_pinjam]
        print(tabulate(rows, headers=headers, tablefmt="pretty"))
    else:
        print("tidak ada peminjaman")

def read_data_rekomendasi(): 
    rekomendasi = [book for book in Data_Buku if book["Rek"] == "1"]
    headers = ['Buku', 'ID_Buku', 'Status', 'Kembali']
    rows = [[book["Buku"], book["ID_Buku"], book['Status'], book['Kembali']] for book in rekomendasi]
    print(tabulate(rows, headers=headers, tablefmt="pretty"))

#search buku, member
def member_search_buku():
    Cari_Judul = input ('judul atau ID buku yang dicari: ').strip()
    filtered_CariJudul = [item for item in Data_Buku if item.get('Buku').lower() == Cari_Judul.lower() or item.get('ID_Buku').lower() == Cari_Judul.lower()]
    if filtered_CariJudul:
        headers = ['Buku', 'ID_Buku', 'Status', 'Kembali']
        rows = [[item["Buku"], item['ID_Buku'], item['Status'], item['Kembali']] for item in filtered_CariJudul]
        print(tabulate(rows, headers=headers, tablefmt="pretty"))
    
        konfirmasi = input("pilih:\n (1) lanjut Cari Buku\n (tombol lainnya) Kembali")
        if konfirmasi == "1":
            member_search_buku()
        else: 
            Log_In_Member()

    else:
        print("buku tidak terdaftar. silahkan coba lagi")
        konfirmasi = int(input("pilih:\n (1) lanjut Cari Buku\n (tombol lainnya) Kembali"))
        if konfirmasi == 1:
            member_search_buku()
        else: 
            Log_In_Member()

def admin_search_buku():
    Cari_Judul = input ('judul atau ID buku yang dicari: ').strip()
    filtered_CariJudul = [item for item in Data_Buku if item.get('Buku').lower() == Cari_Judul.lower() or item.get('ID_Buku').lower() == Cari_Judul.lower()]
    if filtered_CariJudul:
        headers = ['Rek', 'Buku', 'ID_Buku', 'Status', 'ID_Member', 'Kembali']
        rows = [[item["Rek"], item["Buku"], item['ID_Buku'], item['Status'], item["ID_Member"], item['Kembali']] for item in filtered_CariJudul]
        print(tabulate(rows, headers=headers, tablefmt="pretty"))
        konfirmasi = input("pilih:\n (1) lanjut Cari Buku\n (tombol lainnya) Kembali")
        if konfirmasi == "1":
            admin_search_buku()
        else: 
            Halaman_Log_In_Admin()    
    
    else:
        print("buku yang kamu cari tidak ada. silahkan coba lagi")
        konfirmasi = input("pilih:\n (1) lanjut Cari Buku\n (tombol lainnya) Kembali")
        if konfirmasi == "1":
            admin_search_buku()
        else: 
            Halaman_Log_In_Admin() 

def admin_search_member(): 
    Cari_Member = input('nama atau ID member yang dicari: ').strip()
    filtered_CariMember = [member for member in Data_Member if member.get('Member').lower() == Cari_Member.lower() or member.get('ID_Member').lower() == Cari_Member.lower()]
    if filtered_CariMember:
        headers = ['Member', 'ID_Member', 'Kontak']
        rows = [[item["Member"], item['ID_Member'], item['Kontak']] for item in filtered_CariMember]
        print(tabulate(rows, headers=headers, tablefmt="pretty"))
        
        konfirmasi = input("pilih:\n (1) lanjut Cari Member\n (tombol lainnya) Kembali")
        if konfirmasi == "1":
            admin_search_member()
        else: 
            Halaman_Log_In_Admin()

    else: 
        print("Member tidak terdaftar. silahkan coba lagi")
        konfirmasi = input("pilih:\n (1) lanjut Cari Member\n (tombol lainnya) Kembali")
        if konfirmasi == "1":
            admin_search_member()
        else: 
            Halaman_Log_In_Admin()

#tambah buku, member
def create_data_buku():
    judul = input('judul buku (tanpa perlu dimasukan bagian "A" atau "The" apabila tersemat pada awal judul): ')

    judul1 = judul[0].upper()
    judul2 = judul[-1].upper()
    num = len(judul)
    id_buku = f"{judul1}{judul2}{num}"

    BukuKetemu = False #untuk check apakah buku sudah pernah terdaftar atau belum

    for book in Data_Buku:
        if book['ID_Buku'].lower() == id_buku.lower(): 
            print('buku sudah pernah didaftar')
            read_data_buku_tampilan_admin()
            BukuKetemu = True
            break

    if not BukuKetemu: 
        rek = "1"
        buku = judul
        status = "ADA"
        id_member = "-"
        kembali = "-"
        Data_Buku.append({"Rek":rek, "Buku": buku, "ID_Buku": id_buku, "Status": status, "ID_Member": id_member, "Kembali": kembali})
        read_data_buku_tampilan_admin()
        print('buku sudah terdaftarkan')     
        
        konfirmasi = input("pilih:\n (1) lanjut pendaftaran\n (tombol lainnya) Kembali")
        if konfirmasi == "1":
            create_data_buku()
        else: 
            Halaman_Log_In_Admin()
            
    else: 
        konfirmasi = input("pilih:\n (1) lanjut pendaftaran\n (tombol lainnya) Kembali")
        if konfirmasi == "1":
            create_data_buku()
        else: 
            Halaman_Log_In_Admin()
        
def create_data_member():    
    nama = input('nama member (cukup nama panggilan atau 1 kata saja)')
    kontak = input('nomor kontak yang dapat dihubungi')

    if nama.isalpha() and kontak.isdigit(): 
        huruf1 = nama[:2].capitalize()
        num = kontak[8:]
        id_member = f"{huruf1}{num}"
        MemberKetemu = False #untuk check apakah member sudah pernah terdaftar atau belum
    
        for member in Data_Member:
            if member['ID_Member'] == id_member: 
                print('member sudah pernah terdaftar')
                read_data_member()
                MemberKetemu = True
                break
              
        if not MemberKetemu: 
                NamaMember = nama
                IDMember = id_member
                Telp = kontak
                Data_Member.append({"Member":NamaMember, "ID_Member": IDMember, "Kontak": Telp})
                read_data_member()
                print('member baru sudah terdaftarkan')
                
                konfirmasi = input("pilih:\n (1) lanjut pendaftaran\n (tombol lainnya) Kembali")
                if konfirmasi == "1":
                    create_data_member()
                else:
                    Halaman_Log_In_Admin()
              
        else:
            konfirmasi = input("pilih: \n (1) lanjut pendaftaran\n (tombol lainnya) Kembali")
            if konfirmasi == "1":
                create_data_member()
            else: 
                Halaman_Log_In_Admin()

    else: 
            print('Salah Input')
            konfirmasi = input("pilih: \n (1) lanjut pendaftaran\n (tombol lainnya) Kembali")
            if konfirmasi == "1":
                create_data_member()
            else: 
                Halaman_Log_In_Admin()
 
#hapus buku, member
def delete_data_buku(): 
    HapusBuku = input("Masukkan ID Buku: ")
    KetemuBuku = None

    for book in Data_Buku:
        if book['ID_Buku'].lower() == HapusBuku.lower():
            KetemuBuku = book
            break 
     
    if KetemuBuku is None: 
        print('buku tidak diketemukan. Silahkan check dan coba lagi')
        konfirmasi1 = input("pilih:\n (1) lanjut penghapusan\n (tombol lainnya) Kembali")
        if konfirmasi1 == "1":
            delete_data_buku()
        else: 
            Halaman_Log_In_Admin()
    
    else: 
        konfirmasi = input(f"apakah kamu yakin mau menghapus buku {KetemuBuku['Buku']}? (y/n)")
        if konfirmasi == "y":
            if KetemuBuku['Status'].lower() == "sedang dipinjam": 
                print(f"buku {KetemuBuku['Buku']} {HapusBuku} tidak bisa dihapus karena sedang dipinjam oleh {KetemuBuku['ID_Member']} sampai dengan {KetemuBuku['Kembali']}")
                konfirmasi1 = input("pilih:\n (1) lanjut penghapusan\n (tombol lainnya) Kembali")
                if konfirmasi1 == "1":
                    delete_data_buku()
                else: 
                    Halaman_Log_In_Admin()
            
            else: 
                Data_Buku.remove(KetemuBuku)
                read_data_buku_tampilan_admin()
                print("Data berhasil dihapus")
                konfirmasi1 = input("pilih:\n (1) lanjut penghapusan\n (tombol lainnya) Kembali")
                if konfirmasi1 == "1":
                    delete_data_buku()
                else: 
                    Halaman_Log_In_Admin()

        elif konfirmasi == "n": 
            print("proses penghapusan dibatalkan")
            konfirmasi1 = input("pilih:\n (1) lanjut penghapusan\n (tombol lainnya) Kembali")
            if konfirmasi1 == "1":
                delete_data_buku()
            else: 
                Halaman_Log_In_Admin()

def delete_data_member(): 
    HapusMember = input("Masukkan ID Member: ")
    KetemuMember = None
    PinjamMember = None

    for member in Data_Member:
        if member['ID_Member'].lower() == HapusMember.lower():
            KetemuMember = member
            break 
     
    for pinjam in Data_Buku: 
        if pinjam['ID_Member'].lower() == HapusMember.lower() and pinjam['Status'].lower() == "sedang dipinjam": 
            PinjamMember = pinjam
            break 
     
    if KetemuMember is None: 
        print('member tidak diketemukan. Silahkan check dan coba lagi')
        konfirmasi1 = input("pilih:\n (1) lanjut penghapusan\n (tombol lainnya) Kembali")
        if konfirmasi1 == "1":
            delete_data_member()
        else: 
            Halaman_Log_In_Admin() 
    
    else: 
        konfirmasi = input(f"apakah kamu yakin mau menghapus member {KetemuMember['Member']}? (y/n)")
        if konfirmasi == "y":
            if PinjamMember is not None: 
                print(f"member {KetemuMember['Member']} {HapusMember} tidak bisa dihapus karena sedang ada transaksi peminjaman")
                konfirmasi1 = input("pilih:\n (1) lanjut penghapusan\n (tombol lainnya) Kembali")
                if konfirmasi1 == "1":
                    delete_data_member()
                else: 
                    Halaman_Log_In_Admin()    
            
            else: 
                Data_Member.remove(KetemuMember)
                read_data_member()
                print("Data berhasil dihapus")
                konfirmasi1 = input("pilih:\n (1) lanjut penghapusan\n (tombol lainnya) Kembali")
                if konfirmasi1 == "1":
                    delete_data_member()
                else: 
                    Halaman_Log_In_Admin()

        elif konfirmasi == "n": 
            print("proses penghapusan dibatalkan")
            konfirmasi1 = input("pilih:\n (1) lanjut penghapusan\n (tombol lainnya) Kembali")
            if konfirmasi1 == "1":
                delete_data_member()
            else: 
                Halaman_Log_In_Admin()

#peminjaman dan pengembalian buku
def checkout_buku(): 
    JudulBuku = input('Masukan ID Buku: ').strip()
    Ketemu_JudulBuku = None
    Ketemu_MemberNama = None
    
    for book in Data_Buku:
        if book["ID_Buku"].lower() == JudulBuku.lower(): 
            Ketemu_JudulBuku = book
            break

    if Ketemu_JudulBuku is None: 
        print('judul buku tidak terdaftar. Silahkan coba lagi')
        konfirmasi = input("pilih:\n (1) lanjut check out\n (tombol lainnya) Kembali")
        if konfirmasi == "1":
            checkout_buku()
        else: 
            Halaman_Log_In_Admin()

    elif Ketemu_JudulBuku["Status"].lower() == "sedang dipinjam":
        print(f"saat ini buku {Ketemu_JudulBuku['Buku']} {JudulBuku} sedang dipinjam oleh: {Ketemu_JudulBuku['ID_Member']} sampai dengan {Ketemu_JudulBuku['Kembali']}")
        konfirmasi = input("pilih:\n (1) lanjut check out\n (tombol lainnya) Kembali")
        if konfirmasi == "1":
            checkout_buku()
        else: 
            Halaman_Log_In_Admin()
    
    else:
        IDMember = input('Masukan ID Member Peminjam: ').strip()
        
        for name in Data_Member:
            if name["ID_Member"].lower() == IDMember.lower(): 
                Ketemu_MemberNama = name
                break

        if Ketemu_MemberNama is None: 
            print("Member Tidak Terdaftar. Silahkan Check Dan Coba Kembali")
            konfirmasi = input("pilih:\n (1) lanjut check out\n (tombol lainnya) Kembali")
            if konfirmasi == "1":
                checkout_buku()
            else: 
                Halaman_Log_In_Admin()
            
        else: 
            tglKembali = input("Masukan tanggal pengembalian yang adalah 2 minggu dari tanggal peminjaman (DD/MM/YYYY): ").strip()
            book["Status"] = "sedang dipinjam"
            book["ID_Member"] = IDMember
            book["Kembali"] = tglKembali 

            headers = Ketemu_JudulBuku.keys()
            book_details = [Ketemu_JudulBuku.values()]
            print(tabulate(book_details, headers=headers, tablefmt="Pretty"))

            print(f"buku {Ketemu_JudulBuku['Buku']} {JudulBuku} telah berhasil check out oleh {IDMember}. Mohon untuk dikembalikan dalamn keadaan baik sebelum tenggat waktu {tglKembali}\n Terima kasih dan selamat membaca!")
            konfirmasi = input("pilih:\n (1) lanjut check out\n (tombol lainnya) Kembali")
            if konfirmasi == "1":
                checkout_buku()
            else: 
                Halaman_Log_In_Admin()    

def return_buku(): 
    JudulBuku = input('masukan ID buku: ').strip()
    Ketemu_JudulBuku = None

    for book in Data_Buku:
        if book["ID_Buku"].lower() == JudulBuku.lower(): 
            Ketemu_JudulBuku = book
            break
    
    if Ketemu_JudulBuku is None: 
        print('judul buku tidak terdaftar. silahkan coba lagi')
        konfirmasi = input("pilih:\n (1) lanjut check out\n (tombol lainnya) Kembali")
        if konfirmasi == "1":
            return_buku()
        else: 
            Halaman_Log_In_Admin()

    elif Ketemu_JudulBuku["Status"].lower() == "ADA":
        print(f"buku {Ketemu_JudulBuku['Buku']} {JudulBuku} tidak pernah check out. silahkah check kembali")
        konfirmasi = input("pilih:\n (1) lanjut check out\n (tombol lainnya) Kembali")
        if konfirmasi == "1":
            return_buku()
        else: 
            Halaman_Log_In_Admin()
    
    else: 
        Ketemu_JudulBuku["Status"] = "ADA"
        Ketemu_JudulBuku["ID_Member"] = "-"
        Ketemu_JudulBuku["Kembali"] = "-" 

        headers = Ketemu_JudulBuku.keys()
        book_details = [Ketemu_JudulBuku.values()]
        print(tabulate(book_details, headers=headers, tablefmt="Pretty"))

        print(f'''buku {Ketemu_JudulBuku['Buku']} {JudulBuku} telah berhasil dikembalikan. Terima kasih!''')
        konfirmasi = input("pilih:\n (1) lanjut check out\n (tombol lainnya) Kembali")
        if konfirmasi == "1":
            return_buku()
        else: 
            Halaman_Log_In_Admin()  
       
#Log + Main
def Log_In_Member(): 
    print('''Menu: 
    1. Cari Buku
    2. Lihat daftar pinjaman (Log In)
    3. Pinjam Buku
    (tombol Lainnya) Kembali''')

    choice = input("pilih:\n (1) Cari Buku\n (2) Lihat Daftar Pinjaman (Log In)\n (3) Pinjam Buku \n (tombol lainnya) Kembali")

    if choice == "1": #lihat koleksi
        read_data_buku_tampilan_member()
        member_search_buku()

    elif choice == "2": #lihat daftar pinjam (Log In)
        username = input("Masukan ID Member")
        MemberKetemu = None

        for member in Data_Member:
            if member["ID_Member"].lower() == username.lower():
                print(f"Log In berhasil. Selamat datang {member['Member']}")
                read_data_peminjaman_member(username)
                MemberKetemu = member
                break
        
        if not MemberKetemu: 
            print("ID tidak terdaftar. silahkan check dan coba lagi")
            Log_In_Member()
                
    elif choice == "3": #mau pinjam buku
        print("Silahkan hubungi admin untuk melanjutkan proses peminjaman buku")
        Log_In_Member()

    else: 
            Main()

def Log_In_Admin():
        adminID = input("Masukan ID Admin: ")
        adminPass = input("masukan Pass Admin: ")

        if adminID == Data_Admin["ID_Admin"] and adminPass == Data_Admin["Pass_Admin"]:
            Halaman_Log_In_Admin()
        else:    
            print("ID atau dan Pass salah") 
            konfirmasi = input("pilih:\n (1) lanjut Log In\n (tombol lainnya) Kembali")
            if konfirmasi == "1":
                Log_In_Admin()
            else: 
                Main()
            
def Halaman_Log_In_Admin():       
    choice = input("Pilih:\n (1)Cari Buku\n (2) Tambah Buku\n (3) Hapus Buku\n (4) Check Out Buku\n (5) Return Buku\n (6) Cari Member\n (7) Tambah Member\n (8) Hapus Member\n (9) Log Out")
    
    print(''' Selamat Datang Admin!
    Menu: 
            1. Cari Buku
            2. Tambah Buku
            3. Hapus Buku
            4. Check Out Buku
            5. Return Buku
            6. Cari Member
            7. Tambah Member
            8. Hapus Member
            9. Log Out''')
    read_data_peminjaman_admin()

    if choice == "1": 
        read_data_buku_tampilan_admin()
        admin_search_buku()
    elif choice == "2":
        print("proses pendaftaran buku...")
        create_data_buku()
    elif choice == "3":
        print("proses penghapusan buku...")
        delete_data_buku()
    elif choice == "4":
        print("proses check out buku...")
        checkout_buku()
    elif choice == "5":
        print("proses pengembalian buku...")
        return_buku()
    elif choice == "6":
        read_data_member()
        admin_search_member()
    elif choice == "7":
        print("proses pendaftaran member...")
        create_data_member()
    elif choice == "8": 
        print("proses penghapusan member...")
        delete_data_member()
    elif choice == "9":
        Log_Out()
    else: 
        print("Salah Input")
        Halaman_Log_In_Admin()
                
def Log_Out(): 
    global username 
    print("log out - kembali ke halaman utama")
    username = ""
    Main() 

def Main():
    today = datetime.date.today()
    print(f'''
        ##### Selamat Datang di Perpustakaan #####
                    ~~~ TanTan ~~~
Jangan Lupa Cek Buku Rekomendasi Kita Hari Ini {today}:''')
    read_data_rekomendasi()

    print('''
          Menu: 
          1. Admin
          2. Member
          3. Keluar''')
    choice = input("Pilih:\n (1) Admin\n (2) Member\n (3) Keluar")

    if choice == "1":
        Log_In_Admin()
    elif choice == "2":
        Log_In_Member()
    else:
        print("terima kasih telah berkunjung ke Perpustakaan TanTan. Sampai jumpa dilain waktu")
        sys.exit() 

Main()
