def main():
    # Inisialisasi daftar untuk menyimpan data mahasiswa
    mahasiswa = []

    while True:
        # Memasukkan NIM dan Nama Mahasiswa
        nim = input("Masukkan NIM: ")
        nama = input("Masukkan Nama: ")

        # Menambahkan data mahasiswa ke dalam daftar
        mahasiswa.append({"NIM": nim, "Nama": nama})

        # Menanyakan apakah ingin menambah data lagi
        tambah_lagi = input("Ingin tambah lagi? (ya/tidak): ").strip().lower()

        if tambah_lagi == 'tidak':
            # Jika tidak, tampilkan data mahasiswa dan keluar dari loop
            print("\nData Mahasiswa:")
            for data in mahasiswa:
                print(f"NIM: {data['NIM']}, Nama: {data['Nama']}")
            break

    print("Program selesai. Terima kasih.")

if __name__ == "__main__":
    main()