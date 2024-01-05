import sqlite3

koneksi = sqlite3.connect('database_fauna.db')

kursor = koneksi.cursor()

#ubah berdasarkan ID Pegawai
id_fauna = 4

#Gunakan Query UPDATE SET
kursor.execute(f"UPDATE FAUNA SET asal = 'Kalimantan Timur' WHERE id_fauna = {id_fauna}")
koneksi.commit()

#Cek apakah data berhasil diubah atau belum
if kursor.rowcount > 0: #cek berdasarkan adanya baris atau tidak
    print(f"Data dengan ID {id_fauna} Berhasil Diubah!")
else:
    print(f"Tidak ada data fauna dengan ID {id_fauna}!")

# Putuskan koneksi 
koneksi.close()