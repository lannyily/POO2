# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tela_novo_hotel.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_tela_novo_hotel(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(791, 600)
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
        self.widget_2 = QtWidgets.QWidget(self.widget)
        self.widget_2.setGeometry(QtCore.QRect(0, 0, 761, 80))
        self.widget_2.setStyleSheet("background-color: rgb(0, 85, 0);")
        self.widget_2.setObjectName("widget_2")
        self.pushButton_sair_2 = QtWidgets.QPushButton(self.widget_2)
        self.pushButton_sair_2.setGeometry(QtCore.QRect(650, 20, 93, 41))
        self.pushButton_sair_2.setStyleSheet("QPushButton {\n"
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
        self.pushButton_sair_2.setObjectName("pushButton_sair_2")
        self.pushButton_voltar_2 = QtWidgets.QPushButton(self.widget_2)
        self.pushButton_voltar_2.setGeometry(QtCore.QRect(540, 20, 93, 41))
        self.pushButton_voltar_2.setStyleSheet("QPushButton {\n"
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
        self.pushButton_voltar_2.setObjectName("pushButton_voltar_2")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 110, 251, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(30, 150, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(30, 210, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(30, 380, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.lineEdit_nome = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_nome.setGeometry(QtCore.QRect(30, 180, 631, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_nome.setFont(font)
        self.lineEdit_nome.setObjectName("lineEdit_nome")
        self.lineEdit_endereco = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_endereco.setGeometry(QtCore.QRect(30, 240, 631, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_endereco.setFont(font)
        self.lineEdit_endereco.setObjectName("lineEdit_endereco")
        self.lineEdit_endereco_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_endereco_2.setGeometry(QtCore.QRect(30, 420, 641, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_endereco_2.setFont(font)
        self.lineEdit_endereco_2.setObjectName("lineEdit_endereco_2")
        self.pushButton_add_hotel = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_add_hotel.setGeometry(QtCore.QRect(310, 480, 201, 51))
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
        self.widget1 = QtWidgets.QWidget(self.centralwidget)
        self.widget1.setGeometry(QtCore.QRect(30, 270, 131, 91))
        self.widget1.setObjectName("widget1")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget1)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_4 = QtWidgets.QLabel(self.widget1)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.label_4)
        self.radioButton_esta_sim = QtWidgets.QRadioButton(self.widget1)
        self.radioButton_esta_sim.setObjectName("radioButton_esta_sim")
        self.verticalLayout.addWidget(self.radioButton_esta_sim)
        self.radioButton_esta_nao = QtWidgets.QRadioButton(self.widget1)
        self.radioButton_esta_nao.setObjectName("radioButton_esta_nao")
        self.verticalLayout.addWidget(self.radioButton_esta_nao)
        self.widget2 = QtWidgets.QWidget(self.centralwidget)
        self.widget2.setGeometry(QtCore.QRect(260, 270, 121, 91))
        self.widget2.setObjectName("widget2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_5 = QtWidgets.QLabel(self.widget2)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_2.addWidget(self.label_5)
        self.radioButton_piscina_sim = QtWidgets.QRadioButton(self.widget2)
        self.radioButton_piscina_sim.setObjectName("radioButton_piscina_sim")
        self.verticalLayout_2.addWidget(self.radioButton_piscina_sim)
        self.radioButton_piscina_nao = QtWidgets.QRadioButton(self.widget2)
        self.radioButton_piscina_nao.setObjectName("radioButton_piscina_nao")
        self.verticalLayout_2.addWidget(self.radioButton_piscina_nao)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 791, 26))
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
        self.pushButton_sair_2.setText(_translate("MainWindow", "Sair"))
        self.pushButton_voltar_2.setText(_translate("MainWindow", "Voltar"))
        self.label.setText(_translate("MainWindow", "Cadastro de novo hotel"))
        self.label_2.setText(_translate("MainWindow", "Nome do hotel:"))
        self.label_3.setText(_translate("MainWindow", "Endereço:"))
        self.label_6.setText(_translate("MainWindow", "Link do Instagram:"))
        self.pushButton_add_hotel.setText(_translate("MainWindow", "Cadastrar"))
        self.label_4.setText(_translate("MainWindow", "Estacionamento:"))
        self.radioButton_esta_sim.setText(_translate("MainWindow", "SIM"))
        self.radioButton_esta_nao.setText(_translate("MainWindow", "NÃO"))
        self.label_5.setText(_translate("MainWindow", "Piscina:"))
        self.radioButton_piscina_sim.setText(_translate("MainWindow", "SIM"))
        self.radioButton_piscina_nao.setText(_translate("MainWindow", "NÃO"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_tela_novo_hotel()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())