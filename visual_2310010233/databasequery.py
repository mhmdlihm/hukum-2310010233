import mysql.connector

class crud:
    def __init__(self):
        self.koneksiDB = mysql.connector.connect(
            host='localhost',
            user='root',
            password='',
            database='pbo2_2310010233'
        )

    # -----------------------------
    # CRUD untuk tabel pengadilan
    # -----------------------------
    def doSimpanPengadilan(self, ID, NAMA):
        alamat = self.koneksiDB.cursor()
        alamat.execute(
            "INSERT INTO tabel_pengadilan(id_pengadilan, nama_pengadilan) VALUES (%s, %s)",
            (ID, NAMA)
        )
        self.koneksiDB.commit()
        alamat.close()

    def doUbahPengadilan(self, ID, NAMA):
        alamat = self.koneksiDB.cursor()
        alamat.execute(
            "UPDATE tabel_pengadilan SET nama_pengadilan=%s WHERE id_pengadilan=%s",
            (NAMA, ID)
        )
        self.koneksiDB.commit()
        alamat.close()

    def dataPengadilan(self):
        alamat = self.koneksiDB.cursor(dictionary=True)
        alamat.execute("SELECT * FROM tabel_pengadilan ORDER BY id_pengadilan ASC")
        hasil = alamat.fetchall()
        alamat.close()
        return hasil

    def doHapusPengadilan(self, ID):
        alamat = self.koneksiDB.cursor()
        alamat.execute("DELETE FROM tabel_pengadilan WHERE id_pengadilan=%s", (ID,))
        self.koneksiDB.commit()
        alamat.close()

    # -----------------------------
    # CRUD untuk tabel tahapan
    # -----------------------------
    def doSimpanTahapan(self, ID, NAMA):
        alamat = self.koneksiDB.cursor()
        alamat.execute(
            "INSERT INTO tahapan_perkara(id_tahapan, nama_tahapan) VALUES (%s, %s)",
            (ID, NAMA)
        )
        self.koneksiDB.commit()
        alamat.close()

    def doUbahTahapan(self, ID, NAMA):
        alamat = self.koneksiDB.cursor()
        alamat.execute(
            "UPDATE tahapan_perkara SET nama_tahapan=%s WHERE id_tahapan=%s",
            (NAMA, ID)
        )
        self.koneksiDB.commit()
        alamat.close()

    def dataTahapan(self):
        alamat = self.koneksiDB.cursor(dictionary=True)
        alamat.execute("SELECT * FROM tahapan_perkara ORDER BY id_tahapan ASC")
        hasil = alamat.fetchall()
        alamat.close()
        return hasil

    def doHapusTahapan(self, ID):
        alamat = self.koneksiDB.cursor()
        alamat.execute("DELETE FROM tahapan_perkara WHERE id_tahapan=%s", (ID,))
        self.koneksiDB.commit()
        alamat.close()
