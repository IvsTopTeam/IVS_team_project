import os
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLineEdit
from PyQt5 import uic


class GUI(QWidget):
    def __init__(self):
        super(GUI, self).__init__()
        directory = os.path.dirname(os.path.abspath(__file__))  # its retarded :( I have to calculate and pass the
        guipath = os.path.join(directory, 'gui.ui')  # absolute path to gui.ui file
        uic.loadUi(guipath, self)

        button = self.findChild(QPushButton, 'pushButton_0')
        button.clicked.connect(self.clicked_0)
        button = self.findChild(QPushButton, 'pushButton_1')
        button.clicked.connect(self.clicked_1)
        button = self.findChild(QPushButton, 'pushButton_2')
        button.clicked.connect(self.clicked_2)
        button = self.findChild(QPushButton, 'pushButton_3')
        button.clicked.connect(self.clicked_3)
        button = self.findChild(QPushButton, 'pushButton_4')
        button.clicked.connect(self.clicked_4)
        button = self.findChild(QPushButton, 'pushButton_5')
        button.clicked.connect(self.clicked_5)
        button = self.findChild(QPushButton, 'pushButton_6')
        button.clicked.connect(self.clicked_6)
        button = self.findChild(QPushButton, 'pushButton_7')
        button.clicked.connect(self.clicked_7)
        button = self.findChild(QPushButton, 'pushButton_8')
        button.clicked.connect(self.clicked_8)
        button = self.findChild(QPushButton, 'pushButton_9')
        button.clicked.connect(self.clicked_9)
        button = self.findChild(QPushButton, 'pushButton_dot')
        button.clicked.connect(self.clicked_dot)
        button = self.findChild(QPushButton, 'pushButton_eq')
        button.clicked.connect(self.clicked_eq)
        button = self.findChild(QPushButton, 'pushButton_add')
        button.clicked.connect(self.clicked_add)
        button = self.findChild(QPushButton, 'pushButton_sub')
        button.clicked.connect(self.clicked_sub)
        button = self.findChild(QPushButton, 'pushButton_mul')
        button.clicked.connect(self.clicked_mul)
        button = self.findChild(QPushButton, 'pushButton_div')
        button.clicked.connect(self.clicked_div)
        button = self.findChild(QPushButton, 'pushButton_pow')
        button.clicked.connect(self.clicked_pow)
        button = self.findChild(QPushButton, 'pushButton_root')
        button.clicked.connect(self.clicked_root)
        button = self.findChild(QPushButton, 'pushButton_fact')
        button.clicked.connect(self.clicked_fact)
        button = self.findChild(QPushButton, 'pushButton_abs')
        button.clicked.connect(self.clicked_abs)
        button = self.findChild(QPushButton, 'pushButton_delete')
        button.clicked.connect(self.clicked_delete)
        button = self.findChild(QPushButton, 'pushButton_clear')
        button.clicked.connect(self.clicked_clear)

    def clicked_0(self):
        print("0")

    def clicked_1(self):
        print("1")

    def clicked_2(self):
        print("2")

    def clicked_3(self):
        print("3")

    def clicked_4(self):
        print("4")

    def clicked_5(self):
        print("5")

    def clicked_6(self):
        print("6")

    def clicked_7(self):
        print("7")

    def clicked_8(self):
        print("8")

    def clicked_9(self):
        print("9")

    def clicked_dot(self):
        print("dot")

    def clicked_eq(self):
        print("eq")

    def clicked_add(self):
        print("add")

    def clicked_sub(self):
        print("sub")

    def clicked_mul(self):
        print("mul")

    def clicked_div(self):
        print("div")

    def clicked_pow(self):
        print("pow")

    def clicked_root(self):
        print("root")

    def clicked_fact(self):
        print("fact")

    def clicked_abs(self):
        print("abs")

    def clicked_delete(self):
        print("delete")

    def clicked_clear(self):
        print("clear")

    def keyPressEvent(self, key):
        if key.text() == "0":
            print("0")
        elif key.text() == "1":
            print("1")
        elif key.text() == "2":
            print("2")
        elif key.text() == "3":
            print("3")
        elif key.text() == "4":
            print("4")
        elif key.text() == "5":
            print("5")
        elif key.text() == "6":
            print("6")
        elif key.text() == "7":
            print("7")
        elif key.text() == "8":
            print("8")
        elif key.text() == "9":
            print("9")
        elif key.text() == ".":
            print("dot")
        elif key.text() == "=":
            print("eq")
        elif key.text() == "+":
            print("add")
        elif key.text() == "-":
            print("sub")
        elif key.text() == "*":
            print("mul")
        elif key.text() == "/":
            print("div")
        elif key.text() == "!":
            print("fact")
        elif key.text() == "|":
            print("abs")
        elif key.text() == "^":
            print("pow")
        elif key.text() == "r":
            print("root")
        elif key.text() == "c":
            print("clear")
        elif key.key() == 16777223 or key.key() == 16777219:
            print("delete")
