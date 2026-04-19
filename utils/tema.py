TEMA_ATUAL = "claro"

def salvar_tema():
    # Salva o tema atual em um arquivo de texto
    with open("tema.txt", "w") as f:
        f.write(TEMA_ATUAL)
        
def carregar_tema():
    # Carrega o tema atual de um arquivo de texto
    # salvo na variável global TEMA_ATUAL 
    global TEMA_ATUAL
    try:
        with open("tema.txt", "r") as f:
            TEMA_ATUAL = f.read().strip()
            # tenta ler o tema do arquivo e remove espaços em branco
    except FileNotFoundError:
        TEMA_ATUAL = "claro"  # Define o tema padrão como claro se o arquivo não existir

from PyQt6.QtWidgets import QApplication

def aplicar_estilo(widget=None):
    app = QApplication.instance()

    if TEMA_ATUAL == "dark":
        estilo = """
            QWidget {
                background-color: #2b2b2b;
                color: white;
                font-size: 14px;
            }

            QPushButton {
                background-color: #3c3f41;
                border-radius: 15px;
                padding: 12px;
                font-weight: bold;
            }

            QPushButton:hover {
                background-color: #505354;
            }

            QLineEdit {
                background-color: #3c3f41;
                border: 1px solid #555;
                padding: 6px;
                color: white;
            }

            QRadioButton {
                spacing: 10px;
            }

            QRadioButton::indicator {
                width: 16px;
                height: 16px;
            }

            QRadioButton::indicator:unchecked {
                border: 2px solid #aaa;
                border-radius: 8px;
                background: transparent;
            }

            QRadioButton::indicator:checked {
                background-color: #00e676;
                border: 2px solid #00c853;
                border-radius: 8px;
            }
        """
    else:
        estilo = """
            QWidget {
                background-color: #f5f5f5;
                color: black;
                font-size: 14px;
            }

            QPushButton {
                background-color: #e0e0e0;
                border-radius: 15px;
                padding: 12px;
                font-weight: bold;
            }

            QPushButton:hover {
                background-color: #d6d6d6;
            }

            QLineEdit {
                background-color: white;
                border: 1px solid #ccc;
                padding: 6px;
            }

            QRadioButton {
                spacing: 10px;
            }

            QRadioButton::indicator {
                width: 16px;
                height: 16px;
            }

            QRadioButton::indicator:unchecked {
                border: 2px solid #555;
                border-radius: 8px;
                background: white;
            }

            QRadioButton::indicator:checked {
                background-color: #4CAF50;
                border: 2px solid #388E3C;
                border-radius: 8px;
            }
        """

    # aplica globalmente
    app.setStyleSheet(estilo)