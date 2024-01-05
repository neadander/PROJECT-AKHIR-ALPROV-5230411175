import sqlite3

koneksi = sqlite3.connect('database_fauna.db')

kursor = koneksi.cursor()

kursor.execute("SELECT SUM (JUMLAH) FROM FAUNA")
rata_rata_fauna = kursor.fetchone()[0]
print(f"Total Populasi Hewan Langka Saat ini : {rata_rata_fauna}")

koneksi.close()