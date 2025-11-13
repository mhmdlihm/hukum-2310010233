# This Python file uses the following encoding: utf-8
import sys

from PySide6.QtWidgets import QApplication, QWidget, QMessageBox, QTableWidgetItem
from PySide6.QtCore import QFile
from PySide6.QtUiTools import QUiLoader
from databasequery import crud

class tahapan(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        filenya=QFile("tahapan.ui")
        filenya.open(QFile.ReadOnly)

        unggahfile=QUiLoader()
        self.halamanTahapan=unggahfile.load(filenya,self)
        #self.resize(self.halamanAnggota.size())
        self.aksi=crud()
        self.tampilTahapan()
        self.halamanTahapan.btnHapus.clicked.connect(self.doHapusTahapan)
        self.halamanTahapan.btnUbah.clicked.connect(self.doUbahTahapan)
        self.halamanTahapan.btnSimpan.clicked.connect(self.doSimpanTahapan)

    def doSimpanTahapan(self):
        if not self.halamanTahapan.editID.text().strip():
            QMessageBox.information(None,"Informasi","ID Tahapan Belum di isi")
            self.halamanTahapan.editID.setFocus()
        elif not self.halamanTahapan.editNama.text().strip():
            QMessageBox.information(None,"Informasi","Nama Tahapan Belum di isi")
            self.halamanTahapan.editNama.setFocus()
        else:
            validasi=QMessageBox.information(None,"Informasi","Apakah anda yakin menyimpan data ini?",
            QMessageBox.Yes | QMessageBox.No)

            if validasi==QMessageBox.Yes:

                tempID=self.halamanTahapan.editID.text()
                tempNama=self.halamanTahapan.editNama.text()
                self.aksi.doSimpanTahapan(tempID, tempNama)
                QMessageBox.information(None,"Informasi","Data Berhasil di simpan")
                self.tampilTahapan()

            else:
                pass

    def doUbahTahapan(self):
        tempID=self.halamanTahapan.editID.text()
        tempNama=self.halamanTahapan.editNama.text()
        self.aksi.doUbahTahapan(tempID, tempNama)
        QMessageBox.information(None,"Informasi","Data Berhasil di ubah")
        self.tampilTahapan()

    def doHapusTahapan(self):
        tempID=self.halamanTahapan.editID.text()
        self.aksi.doHapusTahapan(tempID)
        QMessageBox.information(None,"Informasi","Data Berhasil di Hapus")
        self.tampilTahapan()


    def tampilTahapan(self):
        self.halamanTahapan.tabelTahapan.setRowCount(0)
        data=self.aksi.dataTahapan()
        for i, r in enumerate(data):
            self.halamanTahapan.tabelTahapan.insertRow(i)
            self.halamanTahapan.tabelTahapan.setItem(i, 0, QTableWidgetItem(str(r["id_tahapan"])))
            self.halamanTahapan.tabelTahapan.setItem(i, 1, QTableWidgetItem(str(r["nama_tahapan"])))

