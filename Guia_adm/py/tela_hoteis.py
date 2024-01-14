# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tela_hoteis.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_tela_hoteis(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(789, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(20, 10, 761, 80))
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
        self.tableWidget.setGeometry(QtCore.QRect(30, 110, 511, 411))
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
        self.pushButton_add_hotel = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_add_hotel.setGeometry(QtCore.QRect(560, 120, 201, 51))
        self.pushButton_add_hotel.setStyleSheet("QPushButton {\n"
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
        self.pushButton_add_hotel.setObjectName("pushButton_add_hotel")
        self.pushButton_excluir_hotel = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_excluir_hotel.setGeometry(QtCore.QRect(560, 180, 201, 51))
        self.pushButton_excluir_hotel.setStyleSheet("QPushButton {\n"
"           \n"
"    background-color: rgb(255, 0, 0);\n"
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
"           \n"
"    \n"
"    background-color: rgb(195, 0, 0);\n"
"        }")
        self.pushButton_excluir_hotel.setObjectName("pushButton_excluir_hotel")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 789, 26))
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
        item.setText(_translate("MainWindow", "Endereço"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Estacionamento"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Piscina"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Link"))
        self.pushButton_add_hotel.setText(_translate("MainWindow", "Adicionar hotel"))
        self.pushButton_excluir_hotel.setText(_translate("MainWindow", "Excluir hotel"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_tela_hoteis()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
