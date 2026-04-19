from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QTableWidget,
    QTableWidgetItem, QLabel, QLineEdit,
    QPushButton, QHBoxLayout
)
from banco import listar_alunos
from utils.tema import aplicar_estilo


class TelaListar(QWidget):
    def __init__(self):
        super().__init__()

        aplicar_estilo(self)

        self.setWindowTitle("Lista de Alunos")
        self.resize(700, 400)

        layout = QVBoxLayout()

        # CAMPO DE BUSCA + BOTÃO LIMPAR
        self.busca = QLineEdit()
        self.busca.setPlaceholderText("Buscar por nome, CPF ou ID...")
        self.busca.textChanged.connect(self.filtrar_tabela)

        btn_limpar = QPushButton("Limpar")
        btn_limpar.clicked.connect(self.limpar_busca)

        busca_layout = QHBoxLayout()
        busca_layout.addWidget(self.busca)
        busca_layout.addWidget(btn_limpar)

        # TÍTULO
        titulo = QLabel("Alunos cadastrados")
        titulo.setStyleSheet("font-size: 18px; font-weight: bold;")

        # TABELA
        self.tabela = QTableWidget()
        self.tabela.setColumnCount(6)
        self.tabela.setHorizontalHeaderLabels([
            "ID", "Nome", "CPF", "Nascimento", "Matrícula", "Pagamento"
        ])

        self.tabela.setSortingEnabled(True)

        # ADICIONANDO NO LAYOUT
        layout.addLayout(busca_layout) 
        layout.addWidget(titulo)
        layout.addWidget(self.tabela)

        self.setLayout(layout)

        self.carregar_dados()

    def carregar_dados(self):
        alunos = listar_alunos()

        self.tabela.setRowCount(len(alunos))

        for linha, aluno in enumerate(alunos):
            for coluna, valor in enumerate(aluno):

                if coluna == 2: #CPF
                    from utils.validacoes import mascarar_cpf
                    valor = mascarar_cpf(valor)

                self.tabela.setItem(linha, coluna, QTableWidgetItem(str(valor)))

    def filtrar_tabela(self):
        texto = self.busca.text().lower()

        for linha in range(self.tabela.rowCount()):
            mostrar = False

            for coluna in range(self.tabela.columnCount()):
                item = self.tabela.item(linha, coluna)

                if item and texto in item.text().lower():
                    mostrar = True
                    break

            self.tabela.setRowHidden(linha, not mostrar)

    def limpar_busca(self):
        self.busca.clear()

        for linha in range(self.tabela.rowCount()):
            self.tabela.setRowHidden(linha, False)