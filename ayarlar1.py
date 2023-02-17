import sqlite3
from PyQt5 import QtCore, QtGui, QtWidgets
baglanti = sqlite3.connect(".\Data\stok.db")
islem = baglanti.cursor()
baglanti.commit()

class Ui_Form_ayar(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(824, 453)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/newPrefix/Stok/work-process.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Form.setWindowIcon(icon)
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(-10, -10, 921, 501))
        self.widget.setStyleSheet(" background-color: #3DD1E7;")
        self.widget.setObjectName("widget")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setGeometry(QtCore.QRect(0, 40, 861, 411))
        self.label.setStyleSheet(" background-color: #3DD1E7;\n"
"border-radius: 180px;")
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_4 = QtWidgets.QLabel(self.widget)
        self.label_4.setGeometry(QtCore.QRect(300, 10, 211, 71))
        font = QtGui.QFont()
        font.setFamily("Ink Free")
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setGeometry(QtCore.QRect(60, 380, 141, 41))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("")
        self.label_2.setObjectName("label_2")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_4.setGeometry(QtCore.QRect(190, 380, 281, 41))
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
        self.pushButton_8.setGeometry(QtCore.QRect(670, 410, 161, 51))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_8.setFont(font)
        self.pushButton_8.setStyleSheet("QPushButton{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(11, 131, 120, 219), stop:1 rgba(85, 98, 112, 226));\n"
"    color:rgba(255, 255, 255, 210);\n"
"    border-radius: 10px;\n"
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
        self.pushButton_8.clicked.connect(self.veri)
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setGeometry(QtCore.QRect(40, 110, 261, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.pushButton_10 = QtWidgets.QPushButton(self.widget)
        self.pushButton_10.setGeometry(QtCore.QRect(80, 150, 161, 51))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_10.setFont(font)
        self.pushButton_10.setStyleSheet("QPushButton{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(11, 131, 120, 219), stop:1 rgba(85, 98, 112, 226));\n"
"    color:rgba(255, 255, 255, 210);\n"
"    border-radius: 10px;\n"
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
        icon2.addPixmap(QtGui.QPixmap(":/newPrefix/Stok/mail.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_10.setIcon(icon2)
        self.pushButton_10.setIconSize(QtCore.QSize(27, 27))
        self.pushButton_10.setObjectName("pushButton_10")
        self.pushButton_10.clicked.connect(self.mail)
        self.label_5 = QtWidgets.QLabel(self.widget)
        self.label_5.setGeometry(QtCore.QRect(540, 110, 261, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.pushButton_11 = QtWidgets.QPushButton(self.widget)
        self.pushButton_11.setGeometry(QtCore.QRect(570, 150, 161, 51))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_11.setFont(font)
        self.pushButton_11.setStyleSheet("QPushButton{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(11, 131, 120, 219), stop:1 rgba(85, 98, 112, 226));\n"
"    color:rgba(255, 255, 255, 210);\n"
"    border-radius: 10px;\n"
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
        icon3.addPixmap(QtGui.QPixmap(":/newPrefix/Stok/speaker.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_11.setIcon(icon3)
        self.pushButton_11.setIconSize(QtCore.QSize(27, 27))
        self.pushButton_11.setObjectName("pushButton_11")
        self.pushButton_11.clicked.connect(self.ses)
        self.groupBox = QtWidgets.QGroupBox(self.widget)
        self.groupBox.setGeometry(QtCore.QRect(70, 210, 291, 101))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")
        self.checkBox = QtWidgets.QCheckBox(self.groupBox)
        self.checkBox.setGeometry(QtCore.QRect(20, 20, 261, 31))
        self.checkBox.setObjectName("checkBox")
        self.checkBox_2 = QtWidgets.QCheckBox(self.groupBox)
        self.checkBox_2.setGeometry(QtCore.QRect(20, 60, 261, 31))
        self.checkBox_2.setObjectName("checkBox_2")
        self.groupBox_2 = QtWidgets.QGroupBox(self.widget)
        self.groupBox_2.setGeometry(QtCore.QRect(500, 210, 291, 101))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setObjectName("groupBox_2")
        self.checkBox_3 = QtWidgets.QCheckBox(self.groupBox_2)
        self.checkBox_3.setGeometry(QtCore.QRect(20, 20, 261, 31))
        self.checkBox_3.setObjectName("checkBox_3")
        self.checkBox_4 = QtWidgets.QCheckBox(self.groupBox_2)
        self.checkBox_4.setGeometry(QtCore.QRect(20, 60, 261, 31))
        self.checkBox_4.setObjectName("checkBox_4")
        self.label_6 = QtWidgets.QLabel(self.widget)
        self.label_6.setGeometry(QtCore.QRect(509, 430, 151, 31))
        self.label_6.setObjectName("label_6")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "AYARLAR"))
        self.label_4.setText(_translate("Form", "AYARLAR"))
        self.label_2.setText(_translate("Form", "MAİL ADRESİ :"))
        islem.execute("select mail from mail")
        mail = islem.fetchall()
        for i in mail:
            self.lineEdit_4.setText(_translate("Form", "{}".format(i[0])))
        self.lineEdit_4.setPlaceholderText(_translate("Form", "Stok Adı Giriniz."))
        self.pushButton_8.setText(_translate("Form", "AYARLARI KAYDET"))
        islem.execute("select konum from mail")
        stok = islem.fetchall()
        for i in stok:
                if i[0] == "kapalı":
                        self.label_3.setText(_translate("Form", "MAİL GÖNDERME KAPALIDIR."))
                if i[0] == "açık":
                        self.label_3.setText(_translate("Form", "MAİL GÖNDERME AÇIKTIR."))
        self.pushButton_10.setText(_translate("Form", "AÇIK KAPALI"))
        islem.execute("select konum from ses")
        stok = islem.fetchall()
        for i in stok:
            if i[0] == "kapalı":
                self.label_5.setText(_translate("Form", "SES KOMUTU KAPALIDIR."))
            if i[0] == "açık":
                self.label_5.setText(_translate("Form", "SES KOMUTU AÇIKTIR."))
        self.pushButton_11.setText(_translate("Form", "AÇIK KAPALI"))
        self.groupBox.setTitle(_translate("Form", "MAİL YÖNETİMİ"))
        self.checkBox.setText(_translate("Form", "KULLANICI EKLEDİGİNDE"))
        self.checkBox_2.setText(_translate("Form", "STOK EKLENDİGİNDE"))
        self.groupBox_2.setTitle(_translate("Form", "SES YÖNETİMİ"))
        self.checkBox_3.setText(_translate("Form", "GİRİŞ YAPILDIGINDA"))
        self.checkBox_4.setText(_translate("Form", "STOK EKLENDİGİNDE"))
    def mail(self):
        if self.label_3.text() == "MAİL GÖNDERME KAPALIDIR.":
                self.label_3.setText("MAİL GÖNDERME AÇIKTIR.")
        elif self.label_3.text() == "MAİL GÖNDERME AÇIKTIR.":
                self.label_3.setText("MAİL GÖNDERME KAPALIDIR.")
    def ses(self):
        if self.label_5.text() == "SES KOMUTU KAPALIDIR.":
                self.label_5.setText("SES KOMUTU AÇIKTIR.")
        elif self.label_5.text() == "SES KOMUTU AÇIKTIR.":
                self.label_5.setText("SES KOMUTU KAPALIDIR.")
    def veri(self):
        self.mail = self.lineEdit_4.text()
        islem.execute("UPDATE mail SET mail='{}'".format(self.mail))
        if self.label_3.text() == "MAİL GÖNDERME KAPALIDIR.":
            islem.execute("UPDATE mail SET stok='kapalı' Where stok='açık'")
            islem.execute("UPDATE mail SET kullanıcı='kapalı' Where kullanıcı='açık'")
            islem.execute("UPDATE mail SET konum='kapalı' Where konum='açık'")
        if self.label_3.text() == "MAİL GÖNDERME KAPALIDIR." and self.label_5.text() == "SES KOMUTU KAPALIDIR.":
            islem.execute("UPDATE mail SET stok='kapalı' Where stok='açık'")
            islem.execute("UPDATE mail SET kullanıcı='kapalı' Where kullanıcı='açık'")
            islem.execute("UPDATE mail SET konum='kapalı' Where konum='açık'")
            islem.execute("UPDATE ses SET stok='kapalı' Where stok='açık'")
            islem.execute("UPDATE ses SET kullanıcı='kapalı' Where kullanıcı='açık'")
            islem.execute("UPDATE ses SET konum='kapalı' Where konum='açık'")
        if self.label_3.text() == "MAİL GÖNDERME AÇIKTIR.":
            if self.checkBox.isChecked():
                islem.execute("UPDATE mail SET kullanıcı='açık' Where kullanıcı='kapalı'")
                islem.execute("UPDATE mail SET konum='açık' Where konum='kapalı'")
            if self.checkBox_2.isChecked():
                islem.execute("UPDATE mail SET stok='açık' Where stok='kapalı'")
                islem.execute("UPDATE mail SET konum='açık' Where konum='kapalı'")
            if self.checkBox.isChecked() and self.checkBox_2.isChecked():
                islem.execute("UPDATE mail SET stok='açık' Where stok='kapalı'")
                islem.execute("UPDATE mail SET kullanıcı='açık' Where kullanıcı='kapalı'")
                islem.execute("UPDATE mail SET konum='açık' Where konum='kapalı'")
        if self.label_5.text() == "SES KOMUTU AÇIKTIR.":
             if self.checkBox_3.isChecked():
                islem.execute("UPDATE ses SET kullanıcı='açık' Where kullanıcı='kapalı'")
                islem.execute("UPDATE ses SET konum='açık' Where konum='kapalı'")
             if self.checkBox_4.isChecked():
                islem.execute("UPDATE ses SET stok='açık' Where stok='kapalı'")
                islem.execute("UPDATE ses SET konum='açık' Where konum='kapalı'")
             if self.checkBox_3.isChecked() and self.checkBox_4.isChecked():
                islem.execute("UPDATE ses SET stok='açık' Where stok='kapalı'")
                islem.execute("UPDATE ses SET kullanıcı='açık' Where kullanıcı='kapalı'")
                islem.execute("UPDATE ses SET konum='açık' Where konum='kapalı'")
        if self.label_5.text() == "SES KOMUTU KAPALIDIR.":
             islem.execute("UPDATE ses SET stok='kapalı' Where stok='açık'")
             islem.execute("UPDATE ses SET kullanıcı='kapalı' Where kullanıcı='açık'")
             islem.execute("UPDATE ses SET konum='kapalı' Where konum='açık'")
        if self.label_5.text() == "SES KOMUTU AÇIKTIR." and self.label_3.text() == "MAİL GÖNDERME AÇIKTIR.":
            if self.checkBox_3.isChecked():
                islem.execute("UPDATE ses SET kullanıcı='açık' Where kullanıcı='kapalı'")
                islem.execute("UPDATE ses SET konum='açık' Where konum='kapalı'")
            if self.checkBox_4.isChecked():
                islem.execute("UPDATE ses SET stok='açık' Where stok='kapalı'")
                islem.execute("UPDATE ses SET konum='açık' Where konum='kapalı'")
            if self.checkBox.isChecked():
                islem.execute("UPDATE mail SET kullanıcı='açık' Where kullanıcı='kapalı'")
                islem.execute("UPDATE mail SET konum='açık' Where konum='kapalı'")
            if self.checkBox_2.isChecked():
                islem.execute("UPDATE mail SET stok='açık' Where stok='kapalı'")
                islem.execute("UPDATE mail SET konum='açık' Where konum='kapalı'")
            if self.checkBox.isChecked() and self.checkBox_2.isChecked():
                islem.execute("UPDATE mail SET stok='açık' Where stok='kapalı'")
                islem.execute("UPDATE mail SET kullanıcı='açık' Where kullanıcı='kapalı'")
                islem.execute("UPDATE mail SET konum='açık' Where konum='kapalı'")
            if self.checkBox_3.isChecked() and self.checkBox_4.isChecked():
                islem.execute("UPDATE ses SET stok='açık' Where stok='kapalı'")
                islem.execute("UPDATE ses SET kullanıcı='açık' Where kullanıcı='kapalı'")
                islem.execute("UPDATE ses SET konum='açık' Where konum='kapalı'")
            if self.checkBox.isChecked() and self.checkBox_3.isChecked():
                islem.execute("UPDATE ses SET kullanıcı='açık' Where kullanıcı='kapalı'")
                islem.execute("UPDATE ses SET konum='açık' Where konum='kapalı'")
                islem.execute("UPDATE mail SET kullanıcı='açık' Where kullanıcı='kapalı'")
                islem.execute("UPDATE mail SET konum='açık' Where konum='kapalı'")
            if self.checkBox_2.isChecked() and self.checkBox_4.isChecked():
                islem.execute("UPDATE ses SET stok='açık' Where stok='kapalı'")
                islem.execute("UPDATE ses SET konum='açık' Where konum='kapalı'")
                islem.execute("UPDATE mail SET stok='açık' Where stok='kapalı'")
                islem.execute("UPDATE mail SET konum='açık' Where konum='kapalı'")
            if self.checkBox.isChecked() and self.checkBox_4.isChecked():
                islem.execute("UPDATE mail SET kullanıcı='açık' Where kullanıcı='kapalı'")
                islem.execute("UPDATE mail SET konum='açık' Where konum='kapalı'")
                islem.execute("UPDATE ses SET stok='açık' Where stok='kapalı'")
                islem.execute("UPDATE ses SET konum='açık' Where konum='kapalı'")
            if self.checkBox_2.isChecked() and self.checkBox_3.isChecked():
                islem.execute("UPDATE mail SET stok='açık' Where stok='kapalı'")
                islem.execute("UPDATE mail SET konum='açık' Where konum='kapalı'")
                islem.execute("UPDATE ses SET kullanıcı='açık' Where kullanıcı='kapalı'")
                islem.execute("UPDATE ses SET konum='açık' Where konum='kapalı'")
            if self.checkBox_2.isChecked() and self.checkBox_3.isChecked() and self.checkBox_4.isChecked():
                islem.execute("UPDATE mail SET stok='açık' Where stok='kapalı'")
                islem.execute("UPDATE mail SET konum='açık' Where konum='kapalı'")
                islem.execute("UPDATE ses SET kullanıcı='açık' Where kullanıcı='kapalı'")
                islem.execute("UPDATE ses SET konum='açık' Where konum='kapalı'")
                islem.execute("UPDATE ses SET stok='açık' Where stok='kapalı'")
                islem.execute("UPDATE ses SET konum='açık' Where konum='kapalı'")
            if self.checkBox.isChecked() and self.checkBox_3.isChecked() and self.checkBox_4.isChecked():
                islem.execute("UPDATE ses SET kullanıcı='açık' Where kullanıcı='kapalı'")
                islem.execute("UPDATE ses SET konum='açık' Where konum='kapalı'")
                islem.execute("UPDATE ses SET stok='açık' Where stok='kapalı'")
                islem.execute("UPDATE ses SET konum='açık' Where konum='kapalı'")
                islem.execute("UPDATE mail SET kullanıcı='açık' Where kullanıcı='kapalı'")
                islem.execute("UPDATE mail SET konum='açık' Where konum='kapalı'")
            if self.checkBox.isChecked() and self.checkBox_2.isChecked() and self.checkBox_4.isChecked():
                islem.execute("UPDATE mail SET kullanıcı='açık' Where kullanıcı='kapalı'")
                islem.execute("UPDATE mail SET konum='açık' Where konum='kapalı'")
                islem.execute("UPDATE ses SET stok='açık' Where stok='kapalı'")
                islem.execute("UPDATE ses SET konum='açık' Where konum='kapalı'")
                islem.execute("UPDATE mail SET stok='açık' Where stok='kapalı'")
                islem.execute("UPDATE mail SET konum='açık' Where konum='kapalı'")
            if self.checkBox.isChecked() and self.checkBox_2.isChecked() and self.checkBox_3.isChecked():
                islem.execute("UPDATE mail SET stok='açık' Where stok='kapalı'")
                islem.execute("UPDATE mail SET konum='açık' Where konum='kapalı'")
                islem.execute("UPDATE mail SET kullanıcı='açık' Where kullanıcı='kapalı'")
                islem.execute("UPDATE mail SET konum='açık' Where konum='kapalı'")
                islem.execute("UPDATE ses SET kullanıcı='açık' Where kullanıcı='kapalı'")
                islem.execute("UPDATE ses SET konum='açık' Where konum='kapalı'")
        baglanti.commit()
        exit()
import resim1_rc
if __name__ == "__main__":
    import sys
    ayarlar = QtWidgets.QApplication(sys.argv)
    ayar_pencere = QtWidgets.QMainWindow()
    ui = Ui_Form_ayar()
    ui.setupUi(ayar_pencere)
    ayar_pencere.show()
    ayarlar.exec_()