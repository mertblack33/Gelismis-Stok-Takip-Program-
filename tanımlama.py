from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3
baglanti = sqlite3.connect(".\Data\stok.db")
islem = baglanti.cursor()

class Ui_Form_tanimlama(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(670, 417)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/self/Stok/warehouse (1).png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Form.setWindowIcon(icon)
        Form.setStyleSheet("background-color:rgba(0, 0, 0, 80);")
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(0, -20, 831, 481))
        self.widget.setStyleSheet(" background-color: #3DD1E7;")
        self.widget.setObjectName("widget")
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setGeometry(QtCore.QRect(10, 60, 301, 351))
        self.label_3.setStyleSheet("\n"
"background-color: rgb(121, 238, 238);\n"
"border-top-right-radius: 50px;\n"
"border-top-left-radius: 50px;\n"
"border-bottom-left-radius: 50px;")
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.widget)
        self.label_4.setGeometry(QtCore.QRect(310, 120, 351, 291))
        self.label_4.setStyleSheet("background-color: rgb(151, 255, 255);\n"
"border-bottom-right-radius: 50px;\n"
"border-top-right-radius: 50px;")
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.comboBox = QtWidgets.QComboBox(self.widget)
        self.comboBox.setGeometry(QtCore.QRect(20, 150, 281, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.comboBox.setFont(font)
        self.comboBox.setStyleSheet("background-color:rgba(0, 0, 0, 0);\n"
"border:none;\n"
"border-bottom:2px solid rgba(46, 82, 101, 200);\n"
"color:rgba(0, 0, 0, 240);\n"
"padding-bottom:7px;")
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_4.setGeometry(QtCore.QRect(20, 210, 281, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_4.setFont(font)
        self.lineEdit_4.setStyleSheet("background-color:rgba(0, 0, 0, 0);\n"
"border:none;\n"
"border-bottom:2px solid rgba(46, 82, 101, 200);\n"
"color:rgba(0, 0, 0, 240);\n"
"padding-bottom:7px;")
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.pushButton_8 = QtWidgets.QPushButton(self.widget)
        self.pushButton_8.setGeometry(QtCore.QRect(200, 60, 111, 61))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_8.setFont(font)
        self.pushButton_8.setStyleSheet("QPushButton{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(11, 131, 120, 219), stop:1 rgba(85, 98, 112, 226));\n"
"    color:rgba(255, 255, 255, 210);\n"
"    border-top-right-radius: 50px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(150, 123, 111, 219), stop:1 rgba(85, 81, 84, 226));\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    padding-left:5px;\n"
"    padding-top:5px;\n"
"    background-color:rgba(150, 123, 111, 255);\n"
"}\n"
"\n"
"\n"
"\n"
"border-left-radius: 25px;")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/self/Stok/in-stock (1).png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_8.setIcon(icon1)
        self.pushButton_8.setIconSize(QtCore.QSize(25, 25))
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_8.clicked.connect(self.islem)
        self.pushButton_9 = QtWidgets.QPushButton(self.widget)
        self.pushButton_9.setGeometry(QtCore.QRect(550, 120, 111, 61))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_9.setFont(font)
        self.pushButton_9.setStyleSheet("QPushButton{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(11, 131, 120, 219), stop:1 rgba(85, 98, 112, 226));\n"
"    color:rgba(255, 255, 255, 210);\n"
"    border-top-right-radius: 50px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(150, 123, 111, 219), stop:1 rgba(85, 81, 84, 226));\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    padding-left:5px;\n"
"    padding-top:5px;\n"
"    background-color:rgba(150, 123, 111, 255);\n"
"}\n"
"\n"
"\n"
"\n"
"border-left-radius: 25px;")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/newPrefix/Stok/trash.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_9.setIcon(icon2)
        self.pushButton_9.setIconSize(QtCore.QSize(25, 25))
        self.pushButton_9.setObjectName("pushButton_9")
        self.pushButton_9.clicked.connect(self.sil)
        self.comboBox_2 = QtWidgets.QComboBox(self.widget)
        self.comboBox_2.setGeometry(QtCore.QRect(340, 220, 281, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.comboBox_2.setFont(font)
        self.comboBox_2.setStyleSheet("background-color:rgba(0, 0, 0, 0);\n"
"border:none;\n"
"border-bottom:2px solid rgba(46, 82, 101, 200);\n"
"color:rgba(0, 0, 0, 240);\n"
"padding-bottom:7px;")
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.pushButton_10 = QtWidgets.QPushButton(self.widget)
        self.pushButton_10.setGeometry(QtCore.QRect(550, 350, 111, 61))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_10.setFont(font)
        self.pushButton_10.setStyleSheet("QPushButton{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(11, 131, 120, 219), stop:1 rgba(85, 98, 112, 226));\n"
"    color:rgba(255, 255, 255, 210);\n"
"    border-BOTTOM-right-radius: 50px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(150, 123, 111, 219), stop:1 rgba(85, 81, 84, 226));\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    padding-left:5px;\n"
"    padding-top:5px;\n"
"    background-color:rgba(150, 123, 111, 255);\n"
"}\n"
"\n"
"\n"
"\n"
"border-left-radius: 25px;")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/self/Stok/exit.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_10.setIcon(icon3)
        self.pushButton_10.setIconSize(QtCore.QSize(25, 25))
        self.pushButton_10.setObjectName("pushButton_10")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setGeometry(QtCore.QRect(340, 80, 121, 31))
        self.label.setObjectName("label")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "TANIMLAMA"))
        self.comboBox.setItemText(0, _translate("Form", "Birim Ekleme"))
        self.comboBox.addItem("Gurup Ekleme")
        self.comboBox.addItem("Ara Gurubu Ekleme")
        self.comboBox.addItem("Marka Ekleme")
        self.comboBox.addItem("Ürün Ekleme")
        self.comboBox.addItem("Model Ekleme")
        self.lineEdit_4.setPlaceholderText(_translate("Form", " Adı Giriniz."))
        self.pushButton_8.setText(_translate("Form", "EKLE"))
        self.pushButton_9.setText(_translate("Form", "SİL"))
        self.comboBox_2.setItemText(0, _translate("Form", " Seçiniz"))
        islem.execute("Select * From f ")
        self.f = islem.fetchall()
        for i in self.f:
                self.comboBox_2.addItem(i[0])
        islem.execute("Select * From a ")
        self.a = islem.fetchall()
        for ia in self.a:
                self.comboBox_2.addItem(ia[0])
        islem.execute("Select * From b ")
        self.b = islem.fetchall()
        for ib in self.b:
                self.comboBox_2.addItem(ib[0])
        islem.execute("Select * From c ")
        self.c = islem.fetchall()
        for ic in self.c:
                self.comboBox_2.addItem(ic[0])
        islem.execute("Select * From d ")
        self.d = islem.fetchall()
        for id in self.d:
                self.comboBox_2.addItem(id[0])
        islem.execute("Select * From e ")
        self.e = islem.fetchall()
        for ie in self.e:
                self.comboBox_2.addItem(ie[0])
        self.pushButton_10.setText(_translate("Form", "KAPAT"))
    def islem(self):
        self.secim = self.comboBox.currentText()
        self.ekle = self.lineEdit_4.text().capitalize()

        if self.secim == "Birim Ekleme":
            islem.execute("Insert into f Values('{}')".format(self.ekle))
            self.label.setText("Ekleme Başarılı.")
        elif self.secim == "Gurup Ekleme":
            islem.execute("Insert into a Values('{}')".format(self.ekle))
            self.label.setText("Ekleme Başarılı.")
        elif self.secim == "Ara Gurubu Ekleme":
            islem.execute("Insert into b Values('{}')".format(self.ekle))
            self.label.setText("Ekleme Başarılı.")
        elif self.secim == "Marka Ekleme":
            islem.execute("Insert into c Values('{}')".format(self.ekle))
            self.label.setText("Ekleme Başarılı.")
        elif self.secim == "Ürün Ekleme":
            islem.execute("Insert into d Values('{}')".format(self.ekle))
            self.label.setText("Ekleme Başarılı.")
        elif self.secim == "Model Ekleme":
            islem.execute("Insert into e Values('{}')".format(self.ekle))
            self.label.setText("Ekleme Başarılı.")
        else:
            self.label.setText("Yanlış Deger Girdiniz.")
        baglanti.commit()
    def sil(self):
        self.birim = []
        self.gurup = []
        self.ara = []
        self.marka = []
        self.urun = []
        self.model = []
        islem.execute("Select * From f ")
        self.f = islem.fetchall()
        for i in self.f:
            self.birim.append(i[0])
        islem.execute("Select * From a ")

        self.a = islem.fetchall()
        for ia in self.a:
            self.gurup.append(ia[0])
        islem.execute("Select * From b ")

        self.b = islem.fetchall()
        for ib in self.b:
            self.ara.append(ib[0])
        islem.execute("Select * From c ")

        self.c = islem.fetchall()
        for ic in self.c:
            self.marka.append(ic[0])
        islem.execute("Select * From d ")

        self.d = islem.fetchall()
        for id in self.d:
            self.urun.append(id[0])
        islem.execute("Select * From e ")

        self.e = islem.fetchall()
        for ie in self.e:
            self.model.append(ie[0])
        self.silme = self.comboBox_2.currentText()
        if self.silme == "Birim Seçiniz" and self.silme == "Gurup Seçiniz" and self.silme == "Ara Gurubunu Seçiniz" and self.silme == "Marka Seçiniz" and self.silme == "Ürün Seçiniz" and self.silme == "Model Seçiniz":
            self.label.setText("Silme Başarısız.")

        else:
            for f in self.birim:
                if f == self.silme:
                    islem.execute("DELETE FROM f WHERE birim='{}'".format(self.silme))
                    self.label.setText("Silme Başarılı.")
            for a in self.gurup:
                if a == self.silme:
                    islem.execute("DELETE FROM a WHERE gurubu='{}'".format(self.silme))
                    self.label.setText("Silme Başarılı.")
            for b in self.ara:
                if b == self.silme:
                    islem.execute("DELETE FROM b WHERE aragurubu='{}'".format(self.silme))
                    self.label.setText("Silme Başarılı.")
            for c in self.marka:
                if c == self.silme:
                    islem.execute("DELETE FROM c WHERE marka='{}'".format(self.silme))
                    self.label.setText("Silme Başarılı.")
            for d in self.urun:
                if d == self.silme:
                    islem.execute("DELETE FROM d WHERE ürüncinsi='{}'".format(self.silme))
                    self.label.setText("Silme Başarılı.")
            for e in self.model:
                if e == self.silme:
                    islem.execute("DELETE FROM e WHERE model='{}'".format(self.silme))
                    self.label.setText("Silme Başarılı.")
        baglanti.commit()

import resim1_rc

if __name__ == "__main__":
    import sys
    ayarlar = QtWidgets.QApplication(sys.argv)
    tanimlama_pencere = QtWidgets.QMainWindow()
    ui = Ui_Form_tanimlama()
    ui.setupUi(tanimlama_pencere)
    tanimlama_pencere.show()
    ayarlar.exec_()
