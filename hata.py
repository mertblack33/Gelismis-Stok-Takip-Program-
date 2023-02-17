

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form_hata(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(386, 338)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/newPrefix/Stok/work-process.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Form.setWindowIcon(icon)
        Form.setStyleSheet("background-color: #3DD1E7;\n"
"")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(110, 10, 161, 141))
        self.label.setStyleSheet("border-image: url(:/self/Stok/man (1).png);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(110, 150, 201, 91))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(160, 210, 71, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(100, 260, 201, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "HATA !"))
        self.label_2.setText(_translate("Form", "KULLANICI ADI"))
        self.label_3.setText(_translate("Form", "Veya"))
        self.label_4.setText(_translate("Form", "ŞİFRE YANLIŞTIR."))
import resim1_rc
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    hata_pencere = QtWidgets.QMainWindow()
    ui = Ui_Form_hata()
    ui.setupUi(hata_pencere)
    hata_pencere.show()
    sys.exit(app.exec_())