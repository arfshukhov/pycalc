from dataclasses import dataclass

from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *

from functools import partial
import sys

from logic import *


class Button:
    def __init__(self, text, function, arg1, place):  # arg1 will be symbol ("1", "+", "/", ...), or fully expression
        super().__init__()
        self.button = QPushButton(text)
        self.button.clicked.connect(partial(function, arg1, place))


@dataclass
class Buttons:
    buttons: list[Button]
    symbols = ["7"]


class MainWindow(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.setGeometry(200, 200, 200, 200)
        self.entry = QLineEdit(self)
        self.entry.setText("√")
        self.entry.show()

        self.grid = QGridLayout(self)
        self.grid.addWidget(Button("1", print, "1").button, 1, 1)

        self.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    app.exec()
