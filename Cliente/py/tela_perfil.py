# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tela_perfil.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_tela_perfil(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1174, 690)
        MainWindow.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(10, 10, 1151, 141))
        self.widget.setStyleSheet("background-color: rgb(255, 222, 124);")
        self.widget.setObjectName("widget")
        self.layoutWidget = QtWidgets.QWidget(self.widget)
        self.layoutWidget.setGeometry(QtCore.QRect(990, 32, 141, 103))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.pushButton_sair = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_sair.setStyleSheet("QPushButton {\n"
"           \n"
"    background-color: rgb(111, 125, 255);\n"
"           border: none;\n"
"           color: white;\n"
"           padding: 10px 20px;\n"
"           text-align: center;\n"
"           text-decoration: none;\n"
"           display: inline-block;\n"
"           font-size: 16px;\n"
"           margin: 4px 2px;\n"
"           cursor: pointer;\n"
"           border-radius: 8px;\n"
"        }\n"
"        QPushButton:hover {\n"
"           background-color: rgb(85, 170, 255); \n"
"        }")
        self.pushButton_sair.setObjectName("pushButton_sair")
        self.verticalLayout_3.addWidget(self.pushButton_sair)
        self.pushButton_voltar = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_voltar.setStyleSheet("QPushButton {\n"
"           \n"
"    background-color: rgb(111, 125, 255);\n"
"           border: none;\n"
"           color: white;\n"
"           padding: 10px 20px;\n"
"           text-align: center;\n"
"           text-decoration: none;\n"
"           display: inline-block;\n"
"           font-size: 16px;\n"
"           margin: 4px 2px;\n"
"           cursor: pointer;\n"
"           border-radius: 8px;\n"
"        }\n"
"        QPushButton:hover {\n"
"           background-color: rgb(85, 170, 255); \n"
"        }")
        self.pushButton_voltar.setObjectName("pushButton_voltar")
        self.verticalLayout_3.addWidget(self.pushButton_voltar)
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setGeometry(QtCore.QRect(-10, -10, 341, 151))
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap("../imagens/logo.png"))
        self.label_3.setScaledContents(True)
        self.label_3.setObjectName("label_3")
        self.foto13 = QtWidgets.QLabel(self.centralwidget)
        self.foto13.setGeometry(QtCore.QRect(10, 160, 641, 471))
        self.foto13.setText("")
        self.foto13.setPixmap(QtGui.QPixmap("../imagens/foto13.jpg"))
        self.foto13.setObjectName("foto13")
        self.lineEdit_nome = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_nome.setGeometry(QtCore.QRect(90, 180, 511, 41))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_nome.setFont(font)
        self.lineEdit_nome.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit_nome.setText("")
        self.lineEdit_nome.setReadOnly(True)
        self.lineEdit_nome.setObjectName("lineEdit_nome")
        self.lineEdit_email = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_email.setGeometry(QtCore.QRect(40, 230, 391, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.lineEdit_email.setFont(font)
        self.lineEdit_email.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit_email.setReadOnly(True)
        self.lineEdit_email.setObjectName("lineEdit_email")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(510, 230, 631, 391))
        self.tableWidget.setStyleSheet("background-color: rgb(229, 240, 255);")
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(720, 180, 261, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("background-color: rgb(92, 160, 212);\n"
"color: rgb(255, 255, 255);")
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(40, 180, 51, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit.setFont(font)
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton_excluir_conta = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_excluir_conta.setGeometry(QtCore.QRect(1000, 160, 141, 41))
        self.pushButton_excluir_conta.setStyleSheet("QPushButton {\n"
"           \n"
"    \n"
"    \n"
"    \n"
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
        self.pushButton_excluir_conta.setObjectName("pushButton_excluir_conta")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1174, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
        self.label_3.setPixmap(QtGui.QPixmap("Cliente/imagens/logo.png"))
        self.foto13.setPixmap(QtGui.QPixmap("Cliente/imagens/foto13.jpg"))

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_sair.setText(_translate("MainWindow", "SAIR"))
        self.pushButton_voltar.setText(_translate("MainWindow", "Voltar"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Código"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Tipo"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Data"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Horario"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Valor"))
        self.label.setText(_translate("MainWindow", " Histórico de compras"))
        self.lineEdit.setText(_translate("MainWindow", "Olá,"))
        self.pushButton_excluir_conta.setText(_translate("MainWindow", "Excluir conta "))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_tela_perfil()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
