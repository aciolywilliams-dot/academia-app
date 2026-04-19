import sys
from PyQt6.QtWidgets import QApplication
from banco import criar_tabela
from ui.menu import Menu  # ← corrigido

if __name__ == "__main__":
    criar_tabela()  # garante que a tabela existe

    app = QApplication(sys.argv)
    janela = Menu()  # ← corrigido
    janela.show()
    sys.exit(app.exec())