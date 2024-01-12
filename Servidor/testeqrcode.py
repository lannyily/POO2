from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget
from PyQt5.QtGui import QPixmap
import mysql.connector
from io import BytesIO
import base64
import qrcode
import random

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

        # Gera e armazena a imagem no banco de dados
        self.gerar_e_armazenar_qr_code()

        # Carrega a imagem do banco de dados
        self.carregar_imagem()

    def gerar_e_armazenar_qr_code(self):
        try:
            # Gera um número aleatório de 8 dígitos
            numero_aleatorio = random.randint(10000000, 99999999)
            print(f"Número aleatório: {numero_aleatorio}")
            # Cria um QR code a partir do número aleatório
            qr = qrcode.QRCode(
                version=1,
                error_correction=qrcode.constants.ERROR_CORRECT_L,
                box_size=10,
                border=4,
            )
            qr.add_data(str(numero_aleatorio))
            qr.make(fit=True)

            # Cria uma imagem do QR code
            img = qr.make_image(fill_color="black", back_color="white")

            # Converte a imagem para bytes
            buffer = BytesIO()
            img.save(buffer)
            imagem_bytes = buffer.getvalue()

            # Armazena a imagem no banco de dados
            self.cursor.execute("INSERT INTO qrcodes (imagem) VALUES (%s)", (imagem_bytes,))
            self.conexao.commit()

        except Exception as e:
            print(f"Erro ao gerar e armazenar o QR code: {e}")

    def carregar_imagem(self):
        try:
            # Recupera a imagem do banco de dados
            self.cursor.execute("SELECT imagem FROM qrcodes ORDER BY id DESC LIMIT 1")
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
