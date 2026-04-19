from PyQt6.QtWidgets import QPushButton
from PyQt6.QtCore import QPropertyAnimation, QRect


class ToggleSwitch(QPushButton):
    def __init__(self):
        super().__init__()

        self.setFixedSize(60, 30)
        self.setCheckable(True)

        # círculo interno
        self.circle = QPushButton(self)
        self.circle.setFixedSize(26, 26)
        self.circle.move(2, 2)

        self.circle.setStyleSheet("""
            background-color: white;
            border-radius: 13px;
        """)

        self.anim = QPropertyAnimation(self.circle, b"geometry")
        self.anim.setDuration(200)

        self.update_style()

        self.clicked.connect(self.toggle)

    def toggle(self):
        if self.isChecked():
            self.anim.setStartValue(QRect(2, 2, 26, 26))
            self.anim.setEndValue(QRect(32, 2, 26, 26))
        else:
            self.anim.setStartValue(QRect(32, 2, 26, 26))
            self.anim.setEndValue(QRect(2, 2, 26, 26))

        self.anim.start()
        self.update_style()

    def update_style(self):
        if self.isChecked():
            self.setStyleSheet("""
                background-color: #00c853;
                border-radius: 15px;
            """)
        else:
            self.setStyleSheet("""
                background-color: #ccc;
                border-radius: 15px;
            """)