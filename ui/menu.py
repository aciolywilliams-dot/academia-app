# Importando elementos da interface
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QPushButton, QHBoxLayout

# Importando módulo do tema corretamente
import utils.tema as tema

from utils.toggle import ToggleSwitch
from ui.cadastro import TelaCadastro
from ui.listar import TelaListar
from ui.atualizar import TelaAtualizar


class Menu(QWidget):
    def __init__(self):
        super().__init__()

        tema.aplicar_estilo()

        self.setWindowTitle("Sistema Academia")
        self.resize(400, 300)

        layout = QVBoxLayout()

        # Layout do topo (toggle de tema)
        topo = QHBoxLayout()

        self.btn_dark = ToggleSwitch()
        self.btn_dark.clicked.connect(self.alterar_tema)

        # Estado inicial do toggle
        if tema.TEMA_ATUAL == "dark":
            self.btn_dark.setChecked(True)

        topo.addWidget(self.btn_dark)
        topo.addStretch()

        layout.addLayout(topo)

        # Botões principais
        btn_cadastrar = QPushButton("Cadastrar Aluno")
        btn_listar = QPushButton("Listar Alunos")
        btn_atualizar = QPushButton("Atualizar Aluno")
        btn_deletar = QPushButton("Deletar Aluno")
        btn_sair = QPushButton("Sair")

        layout.addWidget(btn_cadastrar)
        layout.addWidget(btn_listar)
        layout.addWidget(btn_atualizar)
        layout.addWidget(btn_deletar)
        layout.addWidget(btn_sair)

        # Eventos
        btn_cadastrar.clicked.connect(self.abrir_cadastro)
        btn_listar.clicked.connect(self.abrir_listar)
        btn_atualizar.clicked.connect(self.abrir_atualizar)
        btn_deletar.clicked.connect(self.abrir_deletar)
        btn_sair.clicked.connect(self.close)

        self.setLayout(layout)

    def alterar_tema(self):
        # Atualiza o tema corretamente no módulo
        if self.btn_dark.isChecked():
            tema.TEMA_ATUAL = "dark"
        else:
            tema.TEMA_ATUAL = "claro"

        tema.aplicar_estilo()
        tema.salvar_tema()

    def abrir_cadastro(self):
        self.tela = TelaCadastro()
        self.tela.show()

    def abrir_listar(self):
        self.tela = TelaListar()
        self.tela.show()

    def abrir_atualizar(self):
        self.tela = TelaAtualizar()
        self.tela.show()

    def abrir_deletar(self):
        print("Deletar funcionando")