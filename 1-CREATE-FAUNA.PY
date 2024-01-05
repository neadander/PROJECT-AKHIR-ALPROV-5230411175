import sqlite3
koneksi = sqlite3.connect('database_fauna.db')

# CREATE TABLE PEGAWAI
koneksi.execute("""
                CREATE TABLE FAUNA(
                id_fauna INTEGER PRIMARY KEY AUTOINCREMENT,
                nama_fauna VARCHAR(50),
                jenis VARCHAR(50),
                asal VARCHAR(50),
                jumlah saat ini INT(10),
                tahun terakhir ditemukan INT(10)
                )
                """)

# break
koneksi.close()