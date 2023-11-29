try:
    daftar_angka=[123,456,789,160]
    while daftar_angka==[123,456,789.160]:
        for i in daftar_angka:
            print(i)
        pilihan_nomor=int(input('input nomor anda!'))
        if pilihan_nomor in daftar_angka:
            posisi=daftar_angka.index(pilihan_nomor)
            print(f'angka {pilihan_nomor} di temukan di posisi {posisi+1} dalam daftar!')
            break
        else:
            print('nomor tidak terdaftar!')
except:
    print('input hanya nomor!')