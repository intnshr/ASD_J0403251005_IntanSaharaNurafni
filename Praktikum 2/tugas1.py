# ==========================================================
# TUGAS HANDS-ON MODUL 1
# Studi Kasus: Sistem Stok Barang Kantin (Berbasis File .txt)
#
# Nama : Intan Sahara Nurafni
# NIM : J0403251005
# Kelas : TPL A2
# ==========================================================

# -------------------------------
# Konstanta nama file
# -------------------------------
NAMA_FILE = "stok_barang.txt"

# -------------------------------
# Fungsi: Membaca data dari file
# -------------------------------
def baca_stok(nama_file):
    """
    Membaca data stok dari file teks.
    Format per baris: KodeBarang,NamaBarang,Stok
    Output:
    - stok_dict (dictionary)
    key = kode_barang
    value = {"Nama Barang": nama_barang, "Stok Barang": stok_int}
    """
    stok_dict = {} #inisialisasi stok dictionary
    with open(nama_file, "r", encoding="utf-8") as file:
        for baris in file:
            baris = baris.strip() #ambil stok per baris dan hilangkan new line
            if baris:
                kode_barang, nama_barang, stok = baris.split(",") #ambil data per item data
                stok_dict[kode_barang] = {"Nama Barang": nama_barang, "Stok Barang": int(stok)} #masukkan dalam dictionary
    return stok_dict

# -------------------------------
# Fungsi: Menyimpan data ke file
# -------------------------------
def simpan_stok(nama_file, stok_dict):
    """
    Menyimpan seluruh data stok ke file teks.
    Format per baris: KodeBarang,NamaBarang,Stok
    """
    with open(nama_file, "w", encoding="utf-8") as file:
        for KodeBarang in sorted(stok_dict.keys()):       
            NamaBarang = stok_dict[KodeBarang]["Nama Barang"] #ambil barang per item barang
            Stok = stok_dict[KodeBarang]["Stok Barang"] #ambil stok per item stok
            file.write(f"{KodeBarang},{NamaBarang},{Stok}\n") #masukkan dalam dictionary

# -------------------------------
# Fungsi: Menampilkan semua data
# -------------------------------
def tampilkan_semua(stok_dict):
    """
    Menampilkan semua barang di stok_dict dengan format rapi.
    Jika stok kosong, tampilkan pesan stok kosong.
    """
    if not stok_dict:
        print("\n===STOK KOSONG===")
        return
    
    print("\n===DAFTAR BARANG===")
    #header tabel
    print(f"{'KODE BARANG' : <10} | {'NAMA BARANG': <12} | {'STOK': >5}")
    #garis pemisah supaya tampilan rapi
    print("-" * 35)

    for KodeBarang in sorted(stok_dict.keys()):
        NamaBarang = stok_dict[KodeBarang]["Nama Barang"]
        Stok = stok_dict[KodeBarang]["Stok Barang"]
        print(f"{KodeBarang: <10} | {NamaBarang: <12} | {int(Stok): >5}")
#tampilkan_semua(buka_stok)  #memanggil fungsi untuk menampilkan data        

# -------------------------------
# Fungsi: Cari barang berdasarkan kode
# -------------------------------
def cari_barang(stok_dict):
    """
    Mencari barang berdasarkan kode barang.
    """
    #pencarian barang berdasarkan kode barang sebagai key dictionary
    #membuat input kode barang yang akan dicari
    kode = input("Masukkan kode barang: ").strip()
    
    if kode in stok_dict:
        NamaBarang = stok_dict[kode]["Nama Barang"]
        Stok = stok_dict[kode]["Stok Barang"]

        print("\n===DATA BARANG DITEMUKAN===")
        print(f"KODE BARANG   : {kode}")
        print(f"NAMA BARANG   : {NamaBarang}")
        print(f"STOK          : {Stok}")
    else:
        print("\nBarang tidak ditemukan. Pastikan kode yang dimasukkan benar.")

#memanggil fungsi cari barang
# cari_barang(buka_stok)        

# -------------------------------
# Fungsi: Tambah barang baru
# -------------------------------
def tambah_barang(stok_dict):
    """
    Menambah barang baru ke stok_dict.
    Validasi kode tidak boleh duplikat.
    """
    #awali dulu dengan input kode barang baru
    kode = input("\nMasukkan kode barang baru: ").strip()
    
    if kode in stok_dict:
        print("Kode sudah digunakan. Gunakan kode lain.")
        return
    
    nama = input("Masukkan nama barang: ").strip()
    
    try:
        stok_awal = int(input("Masukkan stok awal: ").strip())
        stok_dict[kode] = {"Nama Barang": nama, "Stok Barang": stok_awal}
        print("Barang berhasil ditambahkan.")
    except ValueError:
        print("Error: Stok harus berupa angka!")

#memanggil fungsi tambah barang
#tambah_barang(buka_stok)        

# -------------------------------
# Fungsi: Update stok barang
# -------------------------------
def update_stok(stok_dict):
    """
    Mengupdate stok barang di stok_dict.
    """
    #awali dulu dengan input kode barang yang ingin di update
    kode = input("\nMasukkan kode barang yang akan diupdate: ").strip()
    
    if kode not in stok_dict:
        print("Kode barang tidak ditemukan.")
        return
    
    print(f"Barang saat ini: {stok_dict[kode]['Nama Barang']}")
    print(f"Stok saat ini  : {stok_dict[kode]['Stok Barang']}")
    
    try:
        stok_baru = int(input("Masukkan stok baru: ").strip())
        stok_dict[kode]["Stok Barang"] = stok_baru
        print("Stok berhasil diupdate.")
    except ValueError:
        print("Error: Stok harus berupa angka!")

#memanggil fungsi update stok
#update_stok(buka_stok)

# =========================================================
# MENU UTAMA
# =========================================================
def menu_utama():
    #load data dari file
    """
    Menu utama untuk sistem stok barang kantin.
    """
    buka_data = baca_stok(NAMA_FILE)
    
    tampilkan_semua(buka_data)
    
    while True:
        #opsi yang tersedia di menu utama
        print("\n=== MENU STOK KANTIN ===")
        print("1. Tampilkan semua barang")
        print("2. Cari barang berdasarkan kode")
        print("3. Tambah barang baru")
        print("4. Update stok barang")
        print("5. Simpan ke file")
        print("0. Keluar")
        pilihan = input("Pilih menu: ").strip()
        
        if pilihan == "1":
            tampilkan_semua(buka_data) #memanggil fungsi tampilkan semua
        elif pilihan == "2":
            cari_barang(buka_data) #memanggil fungsi cari barang
        elif pilihan == "3":
            tambah_barang(buka_data) #memanggil fungsi tambah barang
        elif pilihan == "4":
            update_stok(buka_data) #memanggil fungsi update stok
        elif pilihan == "5":
            simpan_stok(NAMA_FILE, buka_data) #memanggil fungsi simpan ke file
            print("Data berhasil disimpan.")
        elif pilihan == "0":
            print("Program telah ditutup. Terima kasih!")   #keluar dari program
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.") #validasi input menu

# Jalankan program
if __name__ == "__main__":
    menu_utama()