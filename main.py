from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *

import sys


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(200, 200, 200, 200)
        self.label = QLabel(self)
        self.label.setText("123")
        self.label.show()

        self.grid = QGridLayout(self)
        #self.setLayout(self.grig)
        names = ['Cls', 'Bck', '', 'Close',
                 '7', '8', '9', '/',
                 '4', '5', '6', '*',
                 '1', '2', '3', '-',
                 '0', '.', '=', '+']

        positions = [(i, j) for i in range(5) for j in range(4)]

        for position, name in zip(positions, names):

            if name == '':
                continue
            button = QPushButton(name)
            self.grid.addWidget(button, *position)
        self.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    app.exec()
