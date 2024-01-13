# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tela_excluir_conta.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_tela_excluir_conta(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(553, 274)
        MainWindow.setStyleSheet("background-color: rgb(223, 223, 223);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 30, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(20, 70, 511, 131))
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
        self.pushButton_voltar = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_voltar.setGeometry(QtCore.QRect(440, 20, 93, 41))
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
        self.pushButton_redefinir_senha = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_redefinir_senha.setGeometry(QtCore.QRect(270, 20, 161, 41))
        self.pushButton_redefinir_senha.setStyleSheet("QPushButton {\n"
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
        self.pushButton_redefinir_senha.setObjectName("pushButton_redefinir_senha")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 553, 26))
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
        self.label.setText(_translate("MainWindow", "Usuário"))
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
        self.pushButton_voltar.setText(_translate("MainWindow", "Voltar"))
        self.pushButton_redefinir_senha.setText(_translate("MainWindow", "Excluir conta"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_tela_excluir_conta()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
