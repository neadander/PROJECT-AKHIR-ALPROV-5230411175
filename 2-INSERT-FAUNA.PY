import sqlite3

# koneksi database
koneksi = sqlite3.connect('database_fauna.db')

#insert data tabel 

koneksi.execute(f'''
                INSERT INTO FAUNA (nama_fauna, jenis, asal, jumlah, tahun)
                VALUES('Harimau Jawa', 'Mamalia', 'Jawa', '40', '2019')
                ''')
koneksi.execute(f'''
                INSERT INTO FAUNA (nama_fauna, jenis, asal, jumlah, tahun)
                VALUES('Kuskus Beruang', 'Mamalia', 'Sulawesi', '30', '2021')
                ''')
koneksi.execute(f'''
                INSERT INTO FAUNA (nama_fauna, jenis, asal, jumlah, tahun)
                VALUES('Beruang Madu', 'Mamalia', 'Sumatra', '1000', '2020')
                ''')
koneksi.execute(f'''
                INSERT INTO FAUNA (nama_fauna, jenis, asal, jumlah, tahun)
                VALUES('Pesut Mahakam', 'Mamalia', 'Kalimantan', '100', '2021')
                ''')
koneksi.execute(f'''
                INSERT INTO FAUNA (nama_fauna, jenis, asal, jumlah, tahun)
                VALUES('Burung Maleo', 'Burung', 'Sulawesi', '7000', '2023')
                ''')
koneksi.execute(f'''
                INSERT INTO FAUNA (nama_fauna, jenis, asal, jumlah, tahun)
                VALUES('Macan Dahan', 'Mamalia', 'Sumatra', '400', '2020')
                ''')
koneksi.execute(f'''
                INSERT INTO FAUNA (nama_fauna, jenis, asal, jumlah, tahun)
                VALUES('Kancil', 'Mamalia', 'Jawa', '60', '2022')
                ''')
koneksi.execute(f'''
                INSERT INTO FAUNA (nama_fauna, jenis, asal, jumlah, tahun)
                VALUES('Gajah Kalimantan', 'Mamalia', 'Kalimantan', '1500', '2021')
                ''')
koneksi.execute(f'''
                INSERT INTO FAUNA (nama_fauna, jenis, asal, jumlah, tahun)
                VALUES('Elang Jawa', 'Burung', 'Jawa', '200', '2021')
                ''')
koneksi.execute(f'''
                INSERT INTO FAUNA (nama_fauna, jenis, asal, jumlah, tahun)
                VALUES('Katak Borneo', 'Amfibi', 'Kalimantan', '2000', '2023')
                ''')
koneksi.commit()
koneksi.close()