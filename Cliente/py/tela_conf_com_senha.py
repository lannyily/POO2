# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tela_conf_com_senha.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_tela_conf_com_senha(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(655, 186)
        MainWindow.setStyleSheet("background-color: rgb(223, 223, 223);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 10, 511, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(170, 50, 361, 31))
        self.lineEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton_exckuir = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_exckuir.setGeometry(QtCore.QRect(350, 90, 93, 41))
        self.pushButton_exckuir.setStyleSheet("QPushButton {\n"
"    \n"
"    background-color: rgb(255, 0, 0);\n"
"           border: none;\n"
"           padding: 10px 20px;\n"
"           text-align: center;\n"
"           text-decoration: none;\n"
"           display: inline-block;\n"
"color: white;\n"
"           font-size: 15px;\n"
"           margin: 4px 2px;\n"
"           cursor: pointer;\n"
"           border-radius: 8px;\n"
"        }\n"
"        QPushButton:hover {\n"
"          \n"
"    \n"
"    \n"
"    background-color: rgb(190, 16, 16);\n"
"        }")
        self.pushButton_exckuir.setObjectName("pushButton_exckuir")
        self.pushButton_voltar = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_voltar.setGeometry(QtCore.QRect(240, 90, 91, 41))
        self.pushButton_voltar.setStyleSheet("QPushButton {\n"
"           \n"
"    \n"
"    \n"
"    background-color: rgb(238, 255, 254);\n"
"           border: none;\n"
"           padding: 10px 20px;\n"
"           text-align: center;\n"
"           text-decoration: none;\n"
"           display: inline-block;\n"
"           font-size: 15px;\n"
"           margin: 4px 2px;\n"
"           cursor: pointer;\n"
"           border-radius: 8px;\n"
"        }\n"
"        QPushButton:hover {\n"
"          \n"
"    \n"
"    background-color: rgb(255, 255, 255);\n"
"        }")
        self.pushButton_voltar.setObjectName("pushButton_voltar")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 655, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "É Necessário informar a senha para realizar essa operação: "))
        self.pushButton_exckuir.setText(_translate("MainWindow", "Excluir"))
        self.pushButton_voltar.setText(_translate("MainWindow", "Voltar"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_tela_conf_com_senha()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
