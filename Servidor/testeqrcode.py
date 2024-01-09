from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget
from PyQt5.QtGui import QPixmap
import mysql.connector
from io import BytesIO
import base64

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout(self.central_widget)
        self.label_imagem = QLabel(self)
        self.layout.addWidget(self.label_imagem)

        # Conecta ao banco de dados MySQL
        self.conexao = mysql.connector.connect(
            host='localhost', database='turismo', user='root', passwd='amor2004'
        )
        self.cursor = self.conexao.cursor()

        # Carrega a imagem do banco de dados
        self.carregar_imagem()

    def carregar_imagem(self):
        try:
            # Recupera a imagem do banco de dados
            self.cursor.execute("SELECT imagem FROM qrcodes WHERE id = 1")  # Substitua 1 pelo ID desejado
            imagem_bytes = self.cursor.fetchone()[0]

            # Converte os bytes da imagem para QPixmap
            pixmap = QPixmap()
            pixmap.loadFromData(imagem_bytes)

            # Exibe a imagem no QLabel
            self.label_imagem.setPixmap(pixmap)
            self.label_imagem.show()

        except Exception as e:
            print(f"Erro ao carregar a imagem: {e}")

if __name__ == '__main__':
    app = QApplication([])
    main_window = MainWindow()
    main_window.show()
    app.exec_()
