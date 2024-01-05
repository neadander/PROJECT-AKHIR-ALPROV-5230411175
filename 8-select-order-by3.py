import sqlite3

koneksi = sqlite3.connect('database_fauna.db')

kursor = koneksi.cursor()

#ngurutin dari yang terkecil hingga terbesar (ASCENDING = ASC)
#ngurutin dari yang terbesar hingga terkecil (DESCENDING = DESC)
kursor.execute("SELECT *FROM FAUNA ORDER BY tahun ASC ")

baris_tabel = kursor.fetchall()

print("Data Fauna Saat Ini")
print("="*150)
print("{:<5} {:<20} {:<20} {:<20} {:<20}".format("ID FAUNA", "NAMA FAUNA", "JENIS", "ASAL", "JUMLAH", "TAHUN TERAKHIR DITEMUKAN"))
print("="*150)

for baris in baris_tabel:
    print("{:<5} {:<20} {:<20} {:<20} {:<20}".format(baris[0], baris[1], baris[2], baris[3], baris[4], baris[5]))

koneksi.close()