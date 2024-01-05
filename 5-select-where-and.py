import sqlite3

koneksi = sqlite3.connect('database_fauna.db')

kursor = koneksi.cursor()

kursor.execute("SELECT *FROM FAUNA WHERE JENIS = 'Mamalia' AND ASAL = 'Sulawesi' ")

baris_tabel = kursor.fetchall()

print("Data Fauna")
print("="*150)
print("{:<20} {:<20} {:<20} {:<20} {:<20} {:<20}".format("ID FAUNA", "NAMA FAUNA", "JENIS", "ASAL", "JUMLAH SAAT INI", "TAHUN TERAKHIR DITEMUKAN"))
print("="*150)

for baris in baris_tabel:
    print("{:<20} {:<20} {:<20} {:<20} {:<20} {:<20}".format(baris[0], baris[1], baris[2], baris[3], baris[4], baris[5]))

koneksi.close()