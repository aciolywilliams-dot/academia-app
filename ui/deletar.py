from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QLabel,
    QLineEdit, QPushButton
)

import utils.tema as tema


class TelaDeletar(QWidget):
    def __init__(self):
        super().__init__()

        tema.aplicar_estilo()

        self.setWindowTitle("Deletar Aluno")
        self.resize(400, 300)

        layout = QVBoxLayout()

        # Título
        titulo = QLabel("Deletar Aluno por ID")
        titulo.setStyleSheet("font-size: 18px; font-weight: bold;")

        # Campo ID
        self.input_id = QLineEdit()
        self.input_id.setPlaceholderText("Digite o ID do aluno")

        # Botão buscar
        self.btn_buscar = QPushButton("Buscar")

        # Área de resultado
        self.resultado = QLabel("")
        self.resultado.setStyleSheet("margin-top: 10px;")

        # Botão deletar (inativo no começo)
        self.btn_deletar = QPushButton("Deletar")
        self.btn_deletar.setEnabled(False)

        # Adicionando ao layout
        layout.addWidget(titulo)
        layout.addWidget(self.input_id)
        layout.addWidget(self.btn_buscar)
        layout.addWidget(self.resultado)
        layout.addWidget(self.btn_deletar)

        self.setLayout(layout)