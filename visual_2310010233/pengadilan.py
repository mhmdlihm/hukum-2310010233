# This Python file uses the following encoding: utf-8
import sys

from PySide6.QtWidgets import QApplication, QWidget, QMessageBox, QTableWidgetItem
from PySide6.QtCore import QFile
from PySide6.QtUiTools import QUiLoader
from databasequery import crud

class pengadilan(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        filenya=QFile("pengadilan.ui")
        filenya.open(QFile.ReadOnly)

        unggahfile=QUiLoader()
        self.halamanPengadilan=unggahfile.load(filenya,self)
        #self.resize(self.halamanAnggota.size())
        self.aksi=crud()
        self.tampilPengadilan()
        self.halamanPengadilan.btnHapus.clicked.connect(self.doHapusPengadilan)
        self.halamanPengadilan.btnUbah.clicked.connect(self.doUbahPengadilan)
        self.halamanPengadilan.btnSimpan.clicked.connect(self.doSimpanPengadilan)

    def doSimpanPengadilan(self):
        if not self.halamanPengadilan.editID.text().strip():
            QMessageBox.information(None,"Informasi","ID Pengadilan Belum di isi")
            self.halamanPengadilan.editID.setFocus()
        elif not self.halamanPengadilan.editNama.text().strip():
            QMessageBox.information(None,"Informasi","Nama Pengadilan Belum di isi")
            self.halamanPengadilan.editNama.setFocus()
        else:
            validasi=QMessageBox.information(None,"Informasi","Apakah anda yakin menyimpan data ini?",
            QMessageBox.Yes | QMessageBox.No)

            if validasi==QMessageBox.Yes:

                tempID=self.halamanPengadilan.editID.text()
                tempNama=self.halamanPengadilan.editNama.text()
                self.aksi.doSimpanPengadilan(tempID, tempNama)
                QMessageBox.information(None,"Informasi","Data Berhasil di simpan")
                self.tampilPengadilan()

            else:
                pass

    def doUbahPengadilan(self):
        tempID=self.halamanPengadilan.editID.text()
        tempNama=self.halamanPengadilan.editNama.text()
        self.aksi.doUbahPengadilan(tempID, tempNama)
        QMessageBox.information(None,"Informasi","Data Berhasil di ubah")
        self.tampilPengadilan()

    def doHapusPengadilan(self):
        tempID=self.halamanPengadilan.editID.text()
        self.aksi.doHapusPengadilan(tempID)
        QMessageBox.information(None,"Informasi","Data Berhasil di Hapus")
        self.tampilPengadilan()


    def tampilPengadilan(self):
        self.halamanPengadilan.tabelPengadilan.setRowCount(0)
        data=self.aksi.dataPengadilan()
        for i, r in enumerate(data):
            self.halamanPengadilan.tabelPengadilan.insertRow(i)
            self.halamanPengadilan.tabelPengadilan.setItem(i, 0, QTableWidgetItem(str(r["id_pengadilan"])))
            self.halamanPengadilan.tabelPengadilan.setItem(i, 1, QTableWidgetItem(str(r["nama_pengadilan"])))

