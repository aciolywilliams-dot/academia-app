import sys
from PyQt6.QtWidgets import QApplication
from ui.menu import Menu
from utils.tema import carregar_tema, aplicar_estilo

if __name__ == "__main__":
    # Carrega o tema atual antes de iniciar a aplicação
    carregar_tema()

    app = QApplication(sys.argv)

    aplicar_estilo()  # Aplica o estilo globalmente

    janela = Menu()
    janela.show()

    sys.exit(app.exec())