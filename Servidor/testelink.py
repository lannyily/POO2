from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QVBoxLayout, QWidget
from PyQt5.QtCore import Qt, QUrl
from PyQt5.QtGui import QDesktopServices

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout(self.central_widget)

        # Adicione um QLabel para exibir o texto do link
        self.label_link = QLabel(self)
        self.label_link.setText('<a href="https://www.youtube.com/watch?v=ZXjrrvsuvSs">Clique aqui para abrir o link</a>')
        self.label_link.setOpenExternalLinks(True)  # Permitir que links sejam abertos no navegador padrão
        self.layout.addWidget(self.label_link)

        # Adicione um QPushButton para simular o clique no link
        self.button_abrir_link = QPushButton('Abrir Link', self)
        self.button_abrir_link.clicked.connect(self.abrir_link)
        self.layout.addWidget(self.button_abrir_link)

    def abrir_link(self):
        # Função para abrir o navegador da web com o link
        QDesktopServices.openUrl(QUrl('https://www.exemplo.com'))

if __name__ == '__main__':
    app = QApplication([])
    main_window = MainWindow()
    main_window.show()
    app.exec_()
