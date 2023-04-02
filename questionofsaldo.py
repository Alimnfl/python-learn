saldo_awal = 5000
deposit = input('Berapa mau depositnya: ')

saldo_total = saldo_awal + int(deposit)

hutang = 50_000

if saldo_total >= hutang:
    print('Kamu bisa deposit ya, lalu hutangmu akan terpotong dengan deposit ini hehehe...')
elif saldo_total <= hutang:
    print('Maaf kamu tidak bisa deposit...Karena hutangmu terlalu banyak :)')





# Soal
#user bisa bayar hutang jika saldo dia cukup atau lebih untuk membayar
#user tidak akan bisa bayar hutang jika saldonya kurang