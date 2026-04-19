# Esta é a tela de cadastro, que será aberta quando o usuário clicar no botão "Cadastrar Aluno" no menu principal.
from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QLabel, QLineEdit,
    QPushButton, QRadioButton, QButtonGroup
)
from PyQt6.QtCore import QDate
from PyQt6.QtWidgets import QDateEdit, QMessageBox

from banco import inserir_aluno
from utils.tema import aplicar_estilo
from utils.validacoes import validar_cpf


class TelaCadastro(QWidget):
    def __init__(self):
        super().__init__()

        aplicar_estilo(self)

        self.setWindowTitle("Cadastro de Aluno")
        self.resize(400, 400)

        layout = QVBoxLayout()

        #Nome
        self.nome = QLineEdit() # O QLineEdit é um widget de entrada de texto, onde o usuário pode digitar o nome do aluno.
        self.nome.setPlaceholderText("Nome") # O setPlaceholderText é um método que define um texto de dica que aparece dentro do campo de entrada 
        # quando ele está vazio, indicando ao usuário o que deve ser digitado. 
        # Neste caso, o texto "Nome" aparecerá como uma dica para o usuário saber que deve digitar o nome do aluno nesse campo.

        #CPF
        self.cpf = QLineEdit()
        self.cpf.setPlaceholderText("CPF")

        self.cpf.textChanged.connect(self.formatar_cpf)


        #Data nascimento
        self.nasc = QDateEdit() # O QDateEdit é um widget de entrada de data, onde o usuário pode selecionar a data de nascimento do aluno. 
        self.nasc.setCalendarPopup(True) # O setCalendarPopup é um método que habilita um calendário pop-up para o QDateEdit, permitindo que o usuário selecione a data de forma mais fácil e visual.
        self.nasc.setDate(QDate.currentDate()) # O setDate é um método que define a data inicial do QDateEdit. Neste caso, estamos definindo a data atual como a data inicial, para facilitar o preenchimento pelo usuário.

        #Matrícula
        self.matricula = QDateEdit()
        self.matricula.setCalendarPopup(True)
        self.matricula.setDate(QDate.currentDate())

        #Pagamento
        self.radio_sim = QRadioButton("Pagamento em dia") # O QRadioButton é um widget de botão de opção, onde o usuário pode selecionar uma opção entre várias.
        self.radio_nao = QRadioButton("Pagamento atrasado")

        self.radio_sim.setChecked(True) # O setChecked é um método que define o estado do QRadioButton. Neste caso, estamos definindo o botão "Pagamento em dia" como selecionado por padrão, para facilitar o preenchimento pelo usuário.

        self.grupo = QButtonGroup()
        self.grupo.addButton(self.radio_sim)
        self.grupo.addButton(self.radio_nao)

        #Botão salvar
        btn_salvar = QPushButton("Salvar") # O QPushButton é um widget de botão, onde o usuário pode clicar para realizar uma ação. Neste caso, o botão "Salvar" será usado para salvar os dados do aluno no banco de dados.
        btn_salvar.clicked.connect(self.salvar_aluno) # O clicked é um sinal que é emitido quando o botão é clicado. 
        #O connect é um método que conecta esse sinal a uma função, para que quando o botão for clicado, a função seja executada. 
        # Neste caso, estamos conectando o sinal clicked do botão "Salvar" à função salvar_aluno, 
        # que será responsável por salvar os dados do aluno no banco de dados.

        #Layout
        titulo = QLabel("Cadastro de Aluno")
        titulo.setStyleSheet("font-size: 18px; font-weight: bold;")
        layout.addWidget(titulo)
        
        layout.addWidget(self.nome)
        layout.addWidget(self.cpf)

        layout.addWidget(QLabel("Data de nascimento"))
        layout.addWidget(self.nasc)

        layout.addWidget(QLabel("Data de matrícula"))
        layout.addWidget(self.matricula)

        layout.addWidget(self.radio_sim)
        layout.addWidget(self.radio_nao)

        layout.addWidget(btn_salvar)

        self.setLayout(layout)

    def formatar_cpf(self):
        texto = self.cpf.text()

        # remove tudo que não for número
        numeros = ''.join(filter(str.isdigit, texto))

        # limita a 11 dígitos
        numeros = numeros[:11]

        # formatação
        if len(numeros) <= 3:
            novo = numeros
        elif len(numeros) <= 6:
            novo = f"{numeros[:3]}.{numeros[3:]}"
        elif len(numeros) <= 9:
            novo = f"{numeros[:3]}.{numeros[3:6]}.{numeros[6:]}"
        else:
            novo = f"{numeros[:3]}.{numeros[3:6]}.{numeros[6:9]}-{numeros[9:]}"

        self.cpf.blockSignals(True)
        self.cpf.setText(novo)
        self.cpf.blockSignals(False)

    def salvar_aluno(self):
        pagamento = "sim" if self.radio_sim.isChecked() else "não"

        if not validar_cpf(self.cpf.text()):
            QMessageBox.warning(self, "Erro", "CPF inválido!")
            return

        try:
            inserir_aluno(
                self.nome.text(),
                self.cpf.text(),
                self.nasc.text(),
                self.matricula.text(),
                pagamento
            )

            QMessageBox.information(self, "Sucesso", "Aluno cadastrado!")
            self.close()

        except Exception as e:
            QMessageBox.critical(self, "Erro", str(e))