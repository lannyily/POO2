# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tela_usuarios.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_tela_usuarios(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(782, 600)
        MainWindow.setStyleSheet("background-color: rgb(223, 223, 223);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(10, 10, 761, 80))
        self.widget.setStyleSheet("background-color: rgb(0, 85, 0);")
        self.widget.setObjectName("widget")
        self.pushButton_sair = QtWidgets.QPushButton(self.widget)
        self.pushButton_sair.setGeometry(QtCore.QRect(650, 20, 93, 41))
        self.pushButton_sair.setStyleSheet("QPushButton {\n"
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
        self.pushButton_sair.setObjectName("pushButton_sair")
        self.pushButton_voltar = QtWidgets.QPushButton(self.widget)
        self.pushButton_voltar.setGeometry(QtCore.QRect(540, 20, 93, 41))
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
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(10, 140, 511, 401))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(6)
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
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 100, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(540, 180, 221, 31))
        self.lineEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit.setObjectName("lineEdit")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(540, 150, 161, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.pushButton_buscar = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_buscar.setGeometry(QtCore.QRect(600, 220, 101, 41))
        self.pushButton_buscar.setStyleSheet("QPushButton {\n"
"           background-color: #4CAF50;\n"
"           border: none;\n"
"           color: white;\n"
"           padding: 10px 20px;\n"
"           text-align: center;\n"
"           text-decoration: none;\n"
"           display: inline-block;\n"
"           font-size: 14px;\n"
"           margin: 4px 2px;\n"
"           cursor: pointer;\n"
"           border-radius: 8px;\n"
"        }\n"
"        QPushButton:hover {\n"
"           background-color: #45a049;\n"
"        }")
        self.pushButton_buscar.setObjectName("pushButton_buscar")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(540, 300, 221, 31))
        self.lineEdit_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(540, 270, 151, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.pushButton_buscar_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_buscar_2.setGeometry(QtCore.QRect(590, 350, 121, 41))
        self.pushButton_buscar_2.setStyleSheet("QPushButton {\n"
"           background-color: #4CAF50;\n"
"           border: none;\n"
"           color: white;\n"
"           padding: 10px 20px;\n"
"           text-align: center;\n"
"           text-decoration: none;\n"
"           display: inline-block;\n"
"           font-size: 14px;\n"
"           margin: 4px 2px;\n"
"           cursor: pointer;\n"
"           border-radius: 8px;\n"
"        }\n"
"        QPushButton:hover {\n"
"           background-color: #45a049;\n"
"        }")
        self.pushButton_buscar_2.setObjectName("pushButton_buscar_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 782, 26))
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
        self.pushButton_sair.setText(_translate("MainWindow", "Sair"))
        self.pushButton_voltar.setText(_translate("MainWindow", "Voltar"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "ID"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Nome"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "CPF"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Data de Nascimento"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Email"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Senha"))
        self.label.setText(_translate("MainWindow", "Usuários"))
        self.label_2.setText(_translate("MainWindow", "Buscar por email:"))
        self.pushButton_buscar.setText(_translate("MainWindow", "Buscar"))
        self.label_3.setText(_translate("MainWindow", "Usuário encontrado:"))
        self.pushButton_buscar_2.setText(_translate("MainWindow", "Ver usuário"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_tela_usuarios()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
