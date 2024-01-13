# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tela_inicial_adm.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_tela_inicial_adm(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(362, 502)
        MainWindow.setStyleSheet("background-color: rgb(223, 223, 223);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(10, 10, 331, 81))
        self.widget.setStyleSheet("background-color: rgb(0, 85, 0);")
        self.widget.setObjectName("widget")
        self.pushButton_sair = QtWidgets.QPushButton(self.widget)
        self.pushButton_sair.setGeometry(QtCore.QRect(220, 20, 93, 41))
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
        self.pushButton_redefinir_senha = QtWidgets.QPushButton(self.widget)
        self.pushButton_redefinir_senha.setGeometry(QtCore.QRect(20, 20, 161, 41))
        self.pushButton_redefinir_senha.setStyleSheet("QPushButton {\n"
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
        self.pushButton_redefinir_senha.setObjectName("pushButton_redefinir_senha")
        self.splitter = QtWidgets.QSplitter(self.centralwidget)
        self.splitter.setGeometry(QtCore.QRect(70, 120, 211, 321))
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setObjectName("splitter")
        self.layoutWidget = QtWidgets.QWidget(self.splitter)
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.pushButton_usuarios = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_usuarios.setStyleSheet("QPushButton {\n"
"           background-color: #4CAF50;\n"
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
"           background-color: #45a049;\n"
"        }")
        self.pushButton_usuarios.setObjectName("pushButton_usuarios")
        self.verticalLayout.addWidget(self.pushButton_usuarios)
        self.pushButton_hoteis_2 = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_hoteis_2.setStyleSheet("QPushButton {\n"
"           background-color: #4CAF50;\n"
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
"           background-color: #45a049;\n"
"        }")
        self.pushButton_hoteis_2.setObjectName("pushButton_hoteis_2")
        self.verticalLayout.addWidget(self.pushButton_hoteis_2)
        self.pushButton_restaurantes = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_restaurantes.setStyleSheet("QPushButton {\n"
"           background-color: #4CAF50;\n"
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
"           background-color: #45a049;\n"
"        }")
        self.pushButton_restaurantes.setObjectName("pushButton_restaurantes")
        self.verticalLayout.addWidget(self.pushButton_restaurantes)
        self.pushButton_monumentos = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_monumentos.setStyleSheet("QPushButton {\n"
"           background-color: #4CAF50;\n"
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
"           background-color: #45a049;\n"
"        }")
        self.pushButton_monumentos.setObjectName("pushButton_monumentos")
        self.verticalLayout.addWidget(self.pushButton_monumentos)
        self.pushButton_excussoes = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_excussoes.setStyleSheet("QPushButton {\n"
"           background-color: #4CAF50;\n"
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
"           background-color: #45a049;\n"
"        }")
        self.pushButton_excussoes.setObjectName("pushButton_excussoes")
        self.verticalLayout.addWidget(self.pushButton_excussoes)
        self.pushButton_ingressos = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_ingressos.setStyleSheet("QPushButton {\n"
"           background-color: #4CAF50;\n"
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
"           background-color: #45a049;\n"
"        }")
        self.pushButton_ingressos.setObjectName("pushButton_ingressos")
        self.verticalLayout.addWidget(self.pushButton_ingressos)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 362, 26))
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
        self.pushButton_redefinir_senha.setText(_translate("MainWindow", "Redefinir senha"))
        self.pushButton_usuarios.setText(_translate("MainWindow", "Usuários"))
        self.pushButton_hoteis_2.setText(_translate("MainWindow", "Hotéis "))
        self.pushButton_restaurantes.setText(_translate("MainWindow", "Restaurantes "))
        self.pushButton_monumentos.setText(_translate("MainWindow", "Monumentos"))
        self.pushButton_excussoes.setText(_translate("MainWindow", "Excussões "))
        self.pushButton_ingressos.setText(_translate("MainWindow", "Ingressos"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_tela_inicial_adm()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
