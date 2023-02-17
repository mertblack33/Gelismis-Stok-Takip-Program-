import smtplib
import ssl
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from playsound import playsound
from PyQt5 import QtCore, QtGui, QtWidgets
from datetime import datetime
import sqlite3
baglanti = sqlite3.connect(".\Data\stok.db")
islem = baglanti.cursor()
class Ui_Form_stokekle(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(993, 660)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/self/Stok/warehouse.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Form.setWindowIcon(icon)
        Form.setStyleSheet("#widget{\n"
" background-color: #3DD1E7;}")
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(0, 0, 1001, 671))
        self.widget.setStyleSheet("#widget{\n"
"QPushButton{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(11, 131, 120, 219), stop:1 rgba(85, 98, 112, 226));\n"
"    color:rgba(255, 255, 255, 210);\n"
"    border-radius:5px;\n"
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
"}")
        self.widget.setObjectName("widget")
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setGeometry(QtCore.QRect(10, 20, 391, 631))
        self.label_3.setStyleSheet("\n"
"background-color: rgb(121, 238, 238);\n"
"border-bottom-right-radius: 50px;\n"
"border-top-left-radius: 50px;")
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_4.setGeometry(QtCore.QRect(40, 80, 281, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_4.setFont(font)
        self.lineEdit_4.setStyleSheet("background-color:rgba(0, 0, 0, 0);\n"
"border:none;\n"
"border-bottom:2px solid rgba(46, 82, 101, 200);\n"
"color:rgba(0, 0, 0, 240);\n"
"padding-bottom:7px;")
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.comboBox = QtWidgets.QComboBox(self.widget)
        self.comboBox.setGeometry(QtCore.QRect(40, 150, 281, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.comboBox.setFont(font)
        self.comboBox.setStyleSheet("background-color:rgba(0, 0, 0, 0);\n"
"border:none;\n"
"border-bottom:2px solid rgba(46, 82, 101, 200);\n"
"color:rgba(0, 0, 0, 240);\n"
"padding-bottom:7px;")
        self.comboBox.setObjectName("comboBox")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_5.setGeometry(QtCore.QRect(40, 220, 281, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_5.setFont(font)
        self.lineEdit_5.setStyleSheet("background-color:rgba(0, 0, 0, 0);\n"
"border:none;\n"
"border-bottom:2px solid rgba(46, 82, 101, 200);\n"
"color:rgba(0, 0, 0, 240);\n"
"padding-bottom:7px;")
        self.lineEdit_5.setText("")
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.comboBox_2 = QtWidgets.QComboBox(self.widget)
        self.comboBox_2.setGeometry(QtCore.QRect(40, 290, 281, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.comboBox_2.setFont(font)
        self.comboBox_2.setStyleSheet("background-color:rgba(0, 0, 0, 0);\n"
"border:none;\n"
"border-bottom:2px solid rgba(46, 82, 101, 200);\n"
"color:rgba(0, 0, 0, 240);\n"
"padding-bottom:7px;")
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_3 = QtWidgets.QComboBox(self.widget)
        self.comboBox_3.setGeometry(QtCore.QRect(40, 360, 281, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.comboBox_3.setFont(font)
        self.comboBox_3.setStyleSheet("background-color:rgba(0, 0, 0, 0);\n"
"border:none;\n"
"border-bottom:2px solid rgba(46, 82, 101, 200);\n"
"color:rgba(0, 0, 0, 240);\n"
"padding-bottom:7px;")
        self.comboBox_3.setObjectName("comboBox_3")
        self.comboBox_4 = QtWidgets.QComboBox(self.widget)
        self.comboBox_4.setGeometry(QtCore.QRect(40, 430, 281, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.comboBox_4.setFont(font)
        self.comboBox_4.setStyleSheet("background-color:rgba(0, 0, 0, 0);\n"
"border:none;\n"
"border-bottom:2px solid rgba(46, 82, 101, 200);\n"
"color:rgba(0, 0, 0, 240);\n"
"padding-bottom:7px;")
        self.comboBox_4.setObjectName("comboBox_4")
        self.comboBox_5 = QtWidgets.QComboBox(self.widget)
        self.comboBox_5.setGeometry(QtCore.QRect(40, 500, 281, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.comboBox_5.setFont(font)
        self.comboBox_5.setStyleSheet("background-color:rgba(0, 0, 0, 0);\n"
"border:none;\n"
"border-bottom:2px solid rgba(46, 82, 101, 200);\n"
"color:rgba(0, 0, 0, 240);\n"
"padding-bottom:7px;")
        self.comboBox_5.setObjectName("comboBox_5")
        self.comboBox_6 = QtWidgets.QComboBox(self.widget)
        self.comboBox_6.setGeometry(QtCore.QRect(40, 570, 281, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.comboBox_6.setFont(font)
        self.comboBox_6.setStyleSheet("background-color:rgba(0, 0, 0, 0);\n"
"border:none;\n"
"border-bottom:2px solid rgba(46, 82, 101, 200);\n"
"color:rgba(0, 0, 0, 240);\n"
"padding-bottom:7px;")
        self.comboBox_6.setObjectName("comboBox_6")
        self.label_4 = QtWidgets.QLabel(self.widget)
        self.label_4.setGeometry(QtCore.QRect(400, 20, 431, 511))
        self.label_4.setStyleSheet("background-color: rgb(151, 255, 255);\n"
"border-bottom-right-radius: 50px;\n"
"")
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.textEdit = QtWidgets.QTextEdit(self.widget)
        self.textEdit.setGeometry(QtCore.QRect(430, 70, 381, 351))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.textEdit.setFont(font)
        self.textEdit.setStyleSheet("background-color:rgba(0, 0, 0, 0);\n"
"border:none;\n"
"border-bottom:2px solid rgba(46, 82, 101, 200);\n"
"color:rgba(0, 0, 0, 240);\n"
"padding-bottom:7px;")
        self.textEdit.setObjectName("textEdit")
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setGeometry(QtCore.QRect(830, 100, 141, 151))
        self.label_2.setStyleSheet("background-color:rgba(0, 0, 0, 80);\n"
"border-bottom-right-radius: 50px;\n"
"border-top-right-radius: 50px;\n"
"")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.pushButton_8 = QtWidgets.QPushButton(self.widget)
        self.pushButton_8.setGeometry(QtCore.QRect(830, 100, 141, 61))
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
        self.pushButton_8.clicked.connect(self.veriekle)
        self.pushButton_9 = QtWidgets.QPushButton(self.widget)
        self.pushButton_9.setGeometry(QtCore.QRect(830, 190, 141, 61))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_9.setFont(font)
        self.pushButton_9.setStyleSheet("QPushButton{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(11, 131, 120, 219), stop:1 rgba(85, 98, 112, 226));\n"
"    color:rgba(255, 255, 255, 210);\n"
"    border-bottom-right-radius: 50px;\n"
"border-bottom-right-radius: 50px;\n"
"\n"
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
        icon2.addPixmap(QtGui.QPixmap(":/self/Stok/exit.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_9.setIcon(icon2)
        self.pushButton_9.setIconSize(QtCore.QSize(25, 25))
        self.pushButton_9.setObjectName("pushButton_9")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setGeometry(QtCore.QRect(840, 270, 121, 41))
        self.label.setObjectName("label")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "STOK EKLE"))
        self.lineEdit_4.setPlaceholderText(_translate("Form", "Stok Adı Giriniz."))
        self.lineEdit_5.setPlaceholderText(_translate("Form", "Adet Giriniz."))
        self.textEdit.setPlaceholderText(_translate("Form", "AÇIKLAMA GİRİNİZ..."))
        self.pushButton_8.setText(_translate("Form", "KAYDET"))
        self.pushButton_9.setText(_translate("Form", "KAPAT"))
        # Comboxlar
        islem.execute("Select * From f")
        self.f = islem.fetchall()
        for i in self.f:
            self.comboBox.addItem(i[0])
        islem.execute("Select * From a")
        self.a = islem.fetchall()
        for ia in self.a:
            self.comboBox_2.addItem(ia[0])
        islem.execute("Select * From b")
        self.b = islem.fetchall()
        for ib in self.b:
            self.comboBox_3.addItem(ib[0])
        islem.execute("Select * From c")
        self.c = islem.fetchall()
        for ic in self.c:
            self.comboBox_4.addItem(ic[0])
        islem.execute("Select * From d")
        self.d = islem.fetchall()
        for id in self.d:
            self.comboBox_5.addItem(id[0])
        islem.execute("Select * From e")
        self.e = islem.fetchall()
        for ie in self.e:
            self.comboBox_6.addItem(ie[0])
        self.tarih = datetime.now()
        islem.execute("Select * From stokk")
        self.stokk = islem.fetchall()
        for i in self.stokk:
            self.stokkodu = i[0]
    def veriekle(self):
        self.stok_adi = self.lineEdit_4.text()
        self.birim = self.comboBox.currentText()
        self.adet = self.lineEdit_5.text()
        self.gurubu = self.comboBox_2.currentText()
        self.aragurubu = self.comboBox_3.currentText()
        self.marka = self.comboBox_4.currentText()
        self.uruncinsi = self.comboBox_5.currentText()
        self.model = self.comboBox_6.currentText()
        self.aciklama = self.textEdit.toPlainText()
        islem.execute("Insert into ana Values('{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}')"
                      .format(self.tarih.date(),str(self.stokkodu),self.stok_adi,self.birim,self.adet,self.gurubu,
                              self.aragurubu,self.marka,self.uruncinsi,self.model,self.aciklama))
        islem.execute("UPDATE stokk SET stokk=stokk+1 WHERE stokk")
        baglanti.commit()
        self.lineEdit_4.clear()
        self.lineEdit_5.clear()
        self.textEdit.clear()
        islem.execute("Select konum From ses")
        self.sest = islem.fetchall()
        for i in self.sest:
            if i[0] == "açık":
                islem.execute("Select stok From ses")
                self.sest1 = islem.fetchall()
                for i in self.sest1:
                    if i[0] == "açık":
                        playsound("stoksesi.mp3")
        islem.execute("Select konum From mail")
        self.konum = islem.fetchall()
        for i in self.konum:
            if i[0] == "açık":
                islem.execute("Select stok From mail")
                self.stok = islem.fetchall()
                for e in self.stok:
                    if e[0] == "açık":
                        self.mail()
        self.label.setText("Kayıt Başarılı .....")
    def mail(self):
        islem.execute("Select mail From mail")
        self.mail1 = islem.fetchall()
        for i in self.mail1:
            pass
        self.konu = "Yeni Stok Girişi Yapıldı ...."
        self.ileti = "Tarih = {} Stok Ekleme Yapılmıştır.\n \n Stok Kodu = {}    Stok Adı = {} \n \n Birim = {}     Adet ={} \n \n Gurubu = {}     Ara Gurubu = {} \n \n Marka = {}     Urun Cinsi = {}    Model = {} \n \n \n \n  Açıklama = {}".format(self.tarih.date(),str(self.stokkodu),self.stok_adi,self.birim,self.adet,self.gurubu,
                              self.aragurubu,self.marka,self.uruncinsi,self.model,self.aciklama)
        self.gonderenMail = "mertblack33@yandex.com"
        self.gonderilenMail = "{}".format(i[0])
        self.sifre = "6101331mert"
        self.message = MIMEMultipart()
        self.message["From"] = self.gonderenMail
        self.message["To"] = self.gonderilenMail
        self.message["Subject"] = self.konu
        self.message["Bcc"] = self.gonderilenMail
        self.message.attach(MIMEText(self.ileti, "plain"))
        self.yazi = self.message.as_string()
        self.context = ssl.create_default_context()
        with smtplib.SMTP_SSL("smtp.yandex.com", 465, context=self.context) as server:
            server.login(self.gonderenMail, self.sifre)
            server.sendmail(self.gonderenMail, self.gonderilenMail, self.yazi)
import resim1_rc
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    stok_pencere = QtWidgets.QMainWindow()
    ui = Ui_Form_stokekle()
    ui.setupUi(stok_pencere)
    stok_pencere.show()
    app.exec_()