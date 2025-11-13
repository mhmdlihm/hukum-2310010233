# This Python file uses the following encoding: utf-8
import sys

from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtCore import QFile
from PySide6.QtUiTools import QUiLoader
from pengadilan import pengadilan
from tahapan import tahapan




class main(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        filenya=QFile("main.ui")
        filenya.open(QFile.ReadOnly)

        unggahfile=QUiLoader()
        self.halamanUtama=unggahfile.load(filenya,self)
        self.setMenuBar(self.halamanUtama.menuBar())
        self.resize(self.halamanUtama.size())
        self.halamanUtama.actionPengadilan.triggered.connect(self.bukaPengadilan)
        self.halamanUtama.actionTahapan.triggered.connect(self.bukaTahapan)


    def bukaPengadilan(self):
        self.formPengadilan=pengadilan()
        self.formPengadilan.show()

    def bukaTahapan(self):
        self.formTahapan=tahapan()
        self.formTahapan.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    aplikasi = main()
    aplikasi.show()
    sys.exit(app.exec())










