from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3
import os
try:
    os.mkdir(".\Data")
except:
    pass
from hata import Ui_Form_hata
from ana import Ui_Form_ana

baglanti = sqlite3.connect(".\Data\stok.db")
islem = baglanti.cursor()
islem.execute("CREATE TABLE IF NOT EXISTS login (adı TEXT , sifre TEXT)")
islem.execute("CREATE TABLE IF NOT EXISTS giris (giris TEXT)")
islem.execute("CREATE TABLE IF NOT EXISTS ses (konum TEXT , kullanıcı TEXT , stok TEXT)")
islem.execute("CREATE TABLE IF NOT EXISTS mail (mail TEXT , konum TEXT , kullanıcı TEXT , stok TEXT)")
islem.execute("CREATE TABLE IF NOT EXISTS ana (tarih TEXT , stokk TEXT , stoka TEXT ,birim TEXT ,adet TEXT , gurubu TEXT , arag TEXT,marka TEXT , cinsi TEXT , model TEXT , aciklama TEXT)")
islem.execute("CREATE TABLE IF NOT EXISTS a (gurubu TEXT)")
islem.execute("CREATE TABLE IF NOT EXISTS b (aragurubu TEXT)")
islem.execute("CREATE TABLE IF NOT EXISTS c (marka TEXT)")
islem.execute("CREATE TABLE IF NOT EXISTS d (ürüncinsi TEXT)")
islem.execute("CREATE TABLE IF NOT EXISTS e (model TEXT)")
islem.execute("CREATE TABLE IF NOT EXISTS f (birim TEXT)")
islem.execute("CREATE TABLE IF NOT EXISTS stokk (stokk İNT)")
baglanti.commit()

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(793, 595)
        Form.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        Form.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(80, 20, 641, 521))
        self.widget.setStyleSheet("QPushButton#pushButton{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(11, 131, 120, 219), stop:1 rgba(85, 98, 112, 226));\n"
"    color:rgba(255, 255, 255, 210);\n"
"    border-radius:5px;\n"
"}\n"
"\n"
"QPushButton#pushButton:hover{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(150, 123, 111, 219), stop:1 rgba(85, 81, 84, 226));\n"
"}\n"
"\n"
"QPushButton#pushButton:pressed{\n"
"    padding-left:5px;\n"
"    padding-top:5px;\n"
"    background-color:rgba(150, 123, 111, 255);\n"
"}\n"
"\n"
"QPushButton#pushButton_2, #pushButton_3, #pushButton_4, #pushButton_5{\n"
"    background-color: rgba(0, 0, 0, 0);\n"
"    color:rgba(85, 98, 112, 255);\n"
"}\n"
"\n"
"QPushButton#pushButton_2:hover, #pushButton_3:hover, #pushButton_4:hover, #pushButton_5:hover{\n"
"    color: rgba(131, 96, 53, 255);\n"
"}\n"
"\n"
"QPushButton#pushButton_2:pressed, #pushButton_3:pressed, #pushButton_4:pressed, #pushButton_5:pressed{\n"
"    padding-left:5px;\n"
"    padding-top:5px;\n"
"    color:rgba(91, 88, 53, 255);\n"
"}\n"
"\n"
"")
        self.widget.setObjectName("widget")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setGeometry(QtCore.QRect(9, 30, 311, 441))
        self.label.setStyleSheet("border-image: url(:/images/istockphoto-1325240511-612x612.jpg);\n"
"border-top-left-radius: 50px;")
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setGeometry(QtCore.QRect(10, 30, 271, 441))
        self.label_2.setStyleSheet("background-color:rgba(0, 0, 0, 80);\n"
"border-top-left-radius: 50px;")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setGeometry(QtCore.QRect(280, 30, 321, 441))
        self.label_3.setStyleSheet("background-color:rgba(255, 255, 255, 255);\n"
"border-bottom-right-radius: 50px;")
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.widget)
        self.label_4.setGeometry(QtCore.QRect(360, 80, 151, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color:rgba(0, 0, 0, 200);")
        self.label_4.setObjectName("label_4")
        self.lineEdit = QtWidgets.QLineEdit(self.widget)
        self.lineEdit.setGeometry(QtCore.QRect(320, 150, 211, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet("background-color:rgba(0, 0, 0, 0);\n"
"border:none;\n"
"border-bottom:2px solid rgba(46, 82, 101, 200);\n"
"color:rgba(0, 0, 0, 240);\n"
"padding-bottom:7px;")
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_2.setGeometry(QtCore.QRect(320, 210, 211, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setStyleSheet("background-color:rgba(0, 0, 0, 0);\n"
"border:none;\n"
"border-bottom:2px solid rgba(46, 82, 101, 200);\n"
"color:rgba(0, 0, 0, 240);\n"
"padding-bottom:7px;")
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushButton = QtWidgets.QPushButton(self.widget)
        self.pushButton.setGeometry(QtCore.QRect(320, 290, 211, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.sorgu)
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.widget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(340, 380, 181, 32))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_2 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_2.setMaximumSize(QtCore.QSize(30, 30))
        font = QtGui.QFont()
        font.setFamily("Social Media Circled")
        font.setPointSize(15)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout.addWidget(self.pushButton_2)
        self.pushButton_3 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_3.setMaximumSize(QtCore.QSize(30, 30))
        font = QtGui.QFont()
        font.setFamily("Social Media Circled")
        font.setPointSize(15)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout.addWidget(self.pushButton_3)
        self.pushButton_4 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_4.setMaximumSize(QtCore.QSize(30, 30))
        font = QtGui.QFont()
        font.setFamily("Social Media Circled")
        font.setPointSize(15)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setObjectName("pushButton_4")
        self.horizontalLayout.addWidget(self.pushButton_4)
        self.pushButton_5 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_5.setMaximumSize(QtCore.QSize(30, 30))
        font = QtGui.QFont()
        font.setFamily("Social Media Circled")
        font.setPointSize(15)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setObjectName("pushButton_5")
        self.horizontalLayout.addWidget(self.pushButton_5)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_4.setText(_translate("Form", "Log In"))
        self.lineEdit.setPlaceholderText(_translate("Form", "Kullanıcı"))
        self.lineEdit_2.setPlaceholderText(_translate("Form", "Şifre"))
        self.pushButton.setText(_translate("Form", "Giriş Yap"))
        self.pushButton_2.setText(_translate("Form", "E"))
        self.pushButton_3.setText(_translate("Form", "D"))
        self.pushButton_4.setText(_translate("Form", "M"))
        self.pushButton_5.setText(_translate("Form", "C"))
        islem.execute("select * from mail")
        self.sorgu = islem.fetchall()
        if len(self.sorgu) == 0:
            islem.execute("Insert into giris Values('sistem')")
            islem.execute("Insert into ses Values('kapalı','kapalı','kapalı')")
            islem.execute("Insert into mail Values('mert.findikli33@gmail.com','kapalı','kapalı','kapalı')")
            islem.execute("Insert into login Values('sistem','mert123')")
        islem.execute("select * from stokk")
        self.stok = islem.fetchall()
        if len(self.stok) == 0:
            islem.execute("Insert into stokk Values('10000')")
        islem.execute("select * from e")
        self.sorgu1 = islem.fetchall()
        if len(self.sorgu1) == 0:
            islem.execute("Insert into e Values('Model Seçiniz')")
        islem.execute("select * from c")
        self.sorgu2 = islem.fetchall()
        if len(self.sorgu2) == 0:
            islem.execute("Insert into c Values('Marka Seçiniz')")
        islem.execute("select * from b")
        self.sorgu3 = islem.fetchall()
        if len(self.sorgu3) == 0:
            islem.execute("Insert into b Values('Ara Gurubunu Seçiniz')")
        islem.execute("select * from f")
        self.sorgu4 = islem.fetchall()
        if len(self.sorgu4) == 0:
            islem.execute("Insert into f Values('Birim Seçiniz')")
        islem.execute("select * from a")
        self.sorgu5 = islem.fetchall()
        if len(self.sorgu5) == 0:
            islem.execute("Insert into a Values('Gurup Seçiniz')")
        islem.execute("select * from d")
        self.sorgu6 = islem.fetchall()
        if len(self.sorgu6) == 0:
            islem.execute("Insert into d Values('Ürün Seçiniz')")
        baglanti.commit()
    def sorgu(self):
        self.kullanici = self.lineEdit.text()
        self.sifre = self.lineEdit_2.text()
        islem.execute("Select adı From login")
        self.islem = islem.fetchall()
        islem.execute("Select sifre From login")
        self.w = islem.fetchall()
        for i in self.islem:
            for e in self.w:
                if self.kullanici == i[0] and self.sifre == e[0]:
                    islem.execute("UPDATE giris SET giris='{}'".format(self.kullanici))
                    baglanti.commit()
                    self.anaekran()
                else:
                    self.hata()
    def hata(self):
        self.hata_pencere = QtWidgets.QMainWindow()
        self.ui1 = Ui_Form_hata()
        self.ui1.setupUi(self.hata_pencere)
        self.hata_pencere.show()
    def anaekran(self):
        self.ana_pencere = QtWidgets.QMainWindow()
        self.ui = Ui_Form_ana()
        self.ui.setupUi_ana(self.ana_pencere)
        self.ana_pencere.show()
        pencere.hide()
import resim_rc
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    pencere = QtWidgets.QMainWindow()
    ui = Ui_Form()
    ui.setupUi(pencere)
    pencere.show()
    sys.exit(app.exec_())