# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'pengadilannegeri.ui'
##
## Created by: Qt User Interface Compiler version 6.10.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFormLayout, QHeaderView, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QTableWidget,
    QTableWidgetItem, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(616, 390)
        self.formLayoutWidget = QWidget(Form)
        self.formLayoutWidget.setObjectName(u"formLayoutWidget")
        self.formLayoutWidget.setGeometry(QRect(50, 30, 501, 80))
        self.formLayout = QFormLayout(self.formLayoutWidget)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.iDPengadilanLabel = QLabel(self.formLayoutWidget)
        self.iDPengadilanLabel.setObjectName(u"iDPengadilanLabel")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.LabelRole, self.iDPengadilanLabel)

        self.editID = QLineEdit(self.formLayoutWidget)
        self.editID.setObjectName(u"editID")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.FieldRole, self.editID)

        self.namaPengadilanLabel = QLabel(self.formLayoutWidget)
        self.namaPengadilanLabel.setObjectName(u"namaPengadilanLabel")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.LabelRole, self.namaPengadilanLabel)

        self.editNama = QLineEdit(self.formLayoutWidget)
        self.editNama.setObjectName(u"editNama")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.FieldRole, self.editNama)

        self.btnSimpan = QPushButton(Form)
        self.btnSimpan.setObjectName(u"btnSimpan")
        self.btnSimpan.setGeometry(QRect(41, 130, 90, 29))
        self.btnUbah = QPushButton(Form)
        self.btnUbah.setObjectName(u"btnUbah")
        self.btnUbah.setGeometry(QRect(240, 130, 90, 29))
        self.btnHapus = QPushButton(Form)
        self.btnHapus.setObjectName(u"btnHapus")
        self.btnHapus.setGeometry(QRect(430, 130, 90, 29))
        self.tabelPengadilan = QTableWidget(Form)
        if (self.tabelPengadilan.columnCount() < 2):
            self.tabelPengadilan.setColumnCount(2)
        __qtablewidgetitem = QTableWidgetItem()
        self.tabelPengadilan.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tabelPengadilan.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        self.tabelPengadilan.setObjectName(u"tabelPengadilan")
        self.tabelPengadilan.setGeometry(QRect(50, 180, 501, 192))

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.iDPengadilanLabel.setText(QCoreApplication.translate("Form", u"ID Pengadilan", None))
        self.namaPengadilanLabel.setText(QCoreApplication.translate("Form", u"Nama Pengadilan", None))
        self.btnSimpan.setText(QCoreApplication.translate("Form", u"SIMPAN", None))
        self.btnUbah.setText(QCoreApplication.translate("Form", u"UBAH", None))
        self.btnHapus.setText(QCoreApplication.translate("Form", u"HAPUS", None))
        ___qtablewidgetitem = self.tabelPengadilan.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Form", u"ID Pengadilan", None));
        ___qtablewidgetitem1 = self.tabelPengadilan.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Form", u"Nama Pengadilan", None));
    # retranslateUi

