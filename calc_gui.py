import os
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLineEdit
from PyQt5 import uic
import calc_engine

num1 = "0"
num2 = " "
operator = "none"

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

    def clicked_0(self, event):
        calc_engine.clicked_number("0")

    def clicked_1(self):
        calc_engine.clicked_number("1")

    def clicked_2(self):
        calc_engine.clicked_number("2")

    def clicked_3(self):
        calc_engine.clicked_number("3")

    def clicked_4(self):
        calc_engine.clicked_number("4")

    def clicked_5(self):
        calc_engine.clicked_number("5")

    def clicked_6(self):
        calc_engine.clicked_number("6")

    def clicked_7(self):
        calc_engine.clicked_number("7")

    def clicked_8(self):
        calc_engine.clicked_number("8")

    def clicked_9(self):
        calc_engine.clicked_number("9")

    def clicked_dot(self):
        calc_engine.clicked_number(".")

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
        calc_engine.clicked_delete()

    def clicked_clear(self):
        print("clear")

    def keyPressEvent(self, key):
        if key.text() == "0":
            calc_engine.clicked_number("0")
        elif key.text() == "1":
            calc_engine.clicked_number("1")
        elif key.text() == "2":
            calc_engine.clicked_number("2")
        elif key.text() == "3":
            calc_engine.clicked_number("3")
        elif key.text() == "4":
            calc_engine.clicked_number("4")
        elif key.text() == "5":
            calc_engine.clicked_number("5")
        elif key.text() == "6":
            calc_engine.clicked_number("6")
        elif key.text() == "7":
            calc_engine.clicked_number("7")
        elif key.text() == "8":
            calc_engine.clicked_number("8")
        elif key.text() == "9":
            calc_engine.clicked_number("9")
        elif key.text() == ".":
            calc_engine.clicked_number(".")
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
            calc_engine.clicked_delete()
