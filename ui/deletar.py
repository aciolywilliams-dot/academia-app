from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QLabel,
    QLineEdit, QPushButton
)
from banco import buscar_por_id
from banco import deletar_aluno
from PyQt6.QtWidgets import QMessageBox
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
        self.btn_buscar.clicked.connect(self.buscar_aluno)

        # Área de resultado
        self.resultado = QLabel("")
        self.resultado.setStyleSheet("margin-top: 10px;")

        # Botão deletar (inativo no começo)
        self.btn_deletar = QPushButton("Deletar")
        self.btn_deletar.setEnabled(False)
        self.btn_deletar.clicked.connect(self.confirmar_delete)

        # Adicionando ao layout
        layout.addWidget(titulo)
        layout.addWidget(self.input_id)
        layout.addWidget(self.btn_buscar)
        layout.addWidget(self.resultado)
        layout.addWidget(self.btn_deletar)

        self.setLayout(layout)

    def buscar_aluno(self):
        id_texto = self.input_id.text()

        if not id_texto.isdigit():
            self.resultado.setText("ID inválido")
            self.btn_deletar.setEnabled(False)
            return

        aluno = buscar_por_id(int(id_texto))

        if aluno:
            # aluno = (id, nome, cpf, nascimento, matricula, pagamento)
            texto = f"""
        ID: {aluno[0]}
        Nome: {aluno[1]}
        CPF: {aluno[2]}
        Nascimento: {aluno[3]}
        Matrícula: {aluno[4]}
        Pagamento: {aluno[5]}
        """
            self.resultado.setText(texto)
            self.btn_deletar.setEnabled(True)

            # guarda o id para deletar depois
            self.id_encontrado = aluno[0]

        else:
            self.resultado.setText("Aluno não encontrado")
            self.btn_deletar.setEnabled(False)

    def confirmar_delete(self):
        resposta = QMessageBox.question(
            self,
            "Confirmação",
            "Tem certeza que deseja deletar este aluno?",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
        )

        if resposta == QMessageBox.StandardButton.Yes:
            self.deletar_aluno()

    def deletar_aluno(self):
        sucesso = deletar_aluno(self.id_encontrado)

        if sucesso:
            QMessageBox.information(self, "Sucesso", "Aluno deletado com sucesso")

            self.resultado.setText("")
            self.input_id.clear()
            self.btn_deletar.setEnabled(False)

        else:
            QMessageBox.warning(self, "Erro", "Erro ao deletar aluno")