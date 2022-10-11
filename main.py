from dataclasses import dataclass

from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *

from functools import partial
import sys

from logic import *


class Button:
    def __init__(self, text, function, arg, place):  # arg will be symbol ("1", "+", "/", ...), or fully expression
        super().__init__()
        self.symbols = [
            ["8", "9", "+", "-"],
            ["4", "5", "6", "*", "/"],
            ["1", "2", "3", "sqr", "√"],
            ["CE", "0", "=", "(", ")"]
        ]
        self.button = QPushButton(text)
        self.button.clicked.connect(partial(function, arg, place))





class Buttons:
    def __init__(self, place):
        self.buttons: list[Button]
        self.buttons = [
            [Button("7", symbol_add, "7", place).button, Button("8", symbol_add, "8", place).button,
             Button("9", symbol_add, "9", place).button, Button("+", symbol_add, "+", place).button,
             Button("7", symbol_add, "7", place).button],

            [Button("4", symbol_add, "4", place).button, Button("5", symbol_add, "5", place).button,
             Button("6", symbol_add, "6", place).button, Button("*", symbol_add, "*", place).button,
             Button("/", symbol_add, "/", place).button],

            [Button("1", symbol_add, "1", place).button, Button("2", symbol_add, "2", place).button,
             Button("3", symbol_add, "3", place).button, Button("x²", symbol_add, "sqr()", place).button,
             Button("√", symbol_add, "√()", place).button],

            [NotImplemented, Button("0", symbol_add, "0", place).button,
             NotImplemented, Button("(", symbol_add, "(", place).button,
             Button(")", symbol_add, ")", place).button],

        ]


class Window(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.entry = QLineEdit("", self)
        self.entry.setText("")
        self.entry.show()

        self.grid = QGridLayout(self)

        self.buttons = Buttons(self.entry).buttons

        for i, m in enumerate(self.buttons):
            for k, d in enumerate(m):
                if (i + 1, k + 1) == (4, 1):
                    self.btn1 = QPushButton("CE")
                    self.btn1.clicked.connect(partial(break_expression, self.entry))
                    self.grid.addWidget(self.btn1, i + 1, k + 1)
                elif (i + 1, k + 1) == (4, 3):
                    self.btn2 = QPushButton("=")
                    self.btn2.clicked.connect(partial(execution, self.entry))
                    self.grid.addWidget(self.btn2, i + 1, k + 1)
                else:
                    self.grid.addWidget(d, i+1, k+1)

        self.show()

    def execution(self):
        expression = self.entry.text()
        print(expression)



if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    app.exec()
