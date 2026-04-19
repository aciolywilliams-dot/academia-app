from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QLabel,
    QLineEdit, QPushButton, QMessageBox,
    QDateEdit, QRadioButton, QButtonGroup
)
from PyQt6.QtCore import QDate

from banco import buscar_por_id, atualizar_aluno
from utils.tema import aplicar_estilo


class TelaAtualizar(QWidget):
    def __init__(self):
        super().__init__()

        aplicar_estilo(self)

        self.setWindowTitle("Atualizar Aluno")
        self.resize(400, 500)

        layout = QVBoxLayout()

        # Campo de busca por ID
        self.input_id = QLineEdit()
        self.input_id.setPlaceholderText("Digite o ID do aluno")

        self.btn_buscar = QPushButton("Buscar")

        # Label de informação do aluno
        self.info_aluno = QLabel("")

        # Campo nome
        self.nome = QLineEdit()
        self.nome.setPlaceholderText("Nome")
        self.nome.setEnabled(False)

        # Campo CPF
        self.cpf = QLineEdit()
        self.cpf.setPlaceholderText("CPF")
        self.cpf.setEnabled(False)

        # Data de nascimento
        self.nasc = QDateEdit()
        self.nasc.setCalendarPopup(True)
        self.nasc.setEnabled(False)

        # Data de matrícula
        self.matricula = QDateEdit()
        self.matricula.setCalendarPopup(True)
        self.matricula.setEnabled(False)

        # Pagamento
        self.radio_sim = QRadioButton("Pagamento em dia")
        self.radio_nao = QRadioButton("Pagamento atrasado")

        self.radio_sim.setEnabled(False)
        self.radio_nao.setEnabled(False)

        self.grupo = QButtonGroup()
        self.grupo.addButton(self.radio_sim)
        self.grupo.addButton(self.radio_nao)

        # Botão salvar
        self.btn_salvar = QPushButton("Salvar alterações")
        self.btn_salvar.setEnabled(False)

        # Layout
        layout.addWidget(QLabel("Atualizar Aluno"))
        layout.addWidget(self.input_id)
        layout.addWidget(self.btn_buscar)
        layout.addWidget(self.info_aluno)
        layout.addWidget(self.nome)
        layout.addWidget(self.cpf)

        layout.addWidget(QLabel("Data de nascimento"))
        layout.addWidget(self.nasc)

        layout.addWidget(QLabel("Data de matrícula"))
        layout.addWidget(self.matricula)

        layout.addWidget(self.radio_sim)
        layout.addWidget(self.radio_nao)

        layout.addWidget(self.btn_salvar)

        self.setLayout(layout)

        # Eventos
        self.btn_buscar.clicked.connect(self.buscar)
        self.btn_salvar.clicked.connect(self.salvar)

    def buscar(self):
        id_texto = self.input_id.text()

        if not id_texto.isdigit():
            QMessageBox.warning(self, "Erro", "ID inválido")
            return

        aluno = buscar_por_id(int(id_texto))

        if not aluno:
            QMessageBox.critical(self, "Erro", "Aluno não encontrado")
            return

        # Exibe informações do aluno
        self.info_aluno.setText(f"Aluno: {aluno[1]} | CPF: {aluno[2]}")

        # Ativa campos
        self.nome.setEnabled(True)
        self.cpf.setEnabled(True)
        self.nasc.setEnabled(True)
        self.matricula.setEnabled(True)
        self.radio_sim.setEnabled(True)
        self.radio_nao.setEnabled(True)
        self.btn_salvar.setEnabled(True)

        # Preenche dados
        self.nome.setText(aluno[1])
        self.cpf.setText(aluno[2])

        # Datas (ajuste se necessário dependendo do formato salvo)
        self.nasc.setDate(QDate.fromString(aluno[3], "dd/MM/yyyy"))
        self.matricula.setDate(QDate.fromString(aluno[4], "dd/MM/yyyy"))

        if aluno[5] == "sim":
            self.radio_sim.setChecked(True)
        else:
            self.radio_nao.setChecked(True)

    def salvar(self):
        id_texto = self.input_id.text()

        if not id_texto.isdigit():
            QMessageBox.warning(self, "Erro", "ID inválido")
            return

        pagamento = "sim" if self.radio_sim.isChecked() else "não"

        atualizar_aluno(
            int(id_texto),
            self.nome.text(),
            self.cpf.text(),
            self.nasc.text(),
            self.matricula.text(),
            pagamento
        )

        QMessageBox.information(self, "Sucesso", "Aluno atualizado")
        self.close()