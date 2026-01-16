print("=== Aplikasi Bangun Datar ===")
nama = input("Masukkan Nama: ")

ulang = True

while ulang:
    print('\nProgram Menghitung Luas & Bangun Datar')
    print('......................................')
    print('[1] Luas & Keliling persegi panjang')
    print('[2] Luas & Keliling segitiga')
    print('[3] Luas & Keliling lingkaran')
    print('[4] Luas & Keliling jajar genjang')
    print('[5] keluar dari program')
    print('......................................')

    pilihan = int(input('pilih salah satu program (1-5): '))

    if pilihan == 1:
        print('\nprogram menghitung luas & keliling persegi panjang')
        print('..................................................')

        p = int(input('masukkan nilai panjang : '))
        l = int(input('masukkan nilai lebar : '))

        luas = p * l
        keliling = 2 * (p + l)

        print('\nluasnya       =', luas)
        print('kelilingnya   =', keliling)

    elif pilihan == 2:
        print('\nprogram menghitung luas & keliling segitiga')
        print('..................................................')

        a = float(input('masukkan nilai alas : '))
        t = float(input('masukkan nilai tinggi : '))

        luas = 0.5 * a * t
        keliling = a + a + a   # diasumsikan segitiga sama sisi

        print('\nluasnya       =', luas)
        print('kelilingnya   =', keliling)

    elif pilihan == 3:
        print('\nprogram menghitung luas & keliling lingkaran')
        print('..................................................')

        r = float(input('masukkan nilai jari-jari : '))

        phi = 3.14
        diameter = 2 * r

        luas = phi * r * r
        keliling = phi * diameter

        print('\nluasnya       =', "%.2f" % luas)
        print('kelilingnya   =', "%.2f" % keliling)

    elif pilihan == 4:
        print('\nprogram menghitung luas & keliling jajar genjang')
        print('..................................................')

        alas = float(input('masukkan nilai alas : '))
        tinggi = float(input('masukkan nilai tinggi : '))
        miring = float(input('masukkan sisi miring : '))

        luas = alas * tinggi
        keliling = 2 * (alas + miring)

        print('\nluasnya       =', luas)
        print('kelilingnya   =', keliling)

    elif pilihan == 5:
        print(f'\nTerima kasih telah menggunakan program ini!')
        break

    else:
        print('\nError : inputkan angka yang benar..')
        continue

    lagi = input('\nHitung lagi? (Y/T): ').lower()
    if lagi != 'y':
        ulang = False

print(f'\n--- Terima kasih ---\nProgram selesai.')
