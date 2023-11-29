daftar_angka=(123,456,789,234)
print("daftar_angka:")
for angka in daftar_angka:
    print(angka)
nomor_pengguna=int(input("masukan tiga digit angka:"))
if nomor_pengguna in daftar_angka:
    posisi = daftar_angka.index(nomor_pengguna) + 1
    print(f"nomor {nomor_pengguna} ditemukan di posisi {posisi} dalam daftar")
else:
    print('nomor tersebut tidak ada dalam daftar')