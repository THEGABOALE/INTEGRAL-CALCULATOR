from PyQt5.QtWidgets import (
    QWidget, QLabel, QLineEdit, QPushButton, QBoxLayout,
    QHBoxLayout, QTextEdit, QComboBox
)
from PyQt5.QtCore import Qt

class IntegralView(QWidget):
    def __init__(self):
        super().__init__()
        self.windowTitle("Integral Calculator") 