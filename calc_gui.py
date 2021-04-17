import math
import os
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLineEdit
from PyQt5 import uic
import calc_engine as eng
import our_library as lib


class GUI(QWidget):
    result = float(0)
    first = True
    last_operation = "none"

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
        display_main = self.findChild(QLineEdit, 'lineEdit_main')
        display_top = self.findChild(QLineEdit, 'lineEdit_top')

    def clicked_0(self):
        self.lineEdit_main.setText(eng.clicked_number(self.lineEdit_main.text(), "0"))

    def clicked_1(self):
        self.lineEdit_main.setText(eng.clicked_number(self.lineEdit_main.text(), "1"))

    def clicked_2(self):
        self.lineEdit_main.setText(eng.clicked_number(self.lineEdit_main.text(), "2"))

    def clicked_3(self):
        self.lineEdit_main.setText(eng.clicked_number(self.lineEdit_main.text(), "3"))

    def clicked_4(self):
        self.lineEdit_main.setText(eng.clicked_number(self.lineEdit_main.text(), "4"))

    def clicked_5(self):
        self.lineEdit_main.setText(eng.clicked_number(self.lineEdit_main.text(), "5"))

    def clicked_6(self):
        self.lineEdit_main.setText(eng.clicked_number(self.lineEdit_main.text(), "6"))

    def clicked_7(self):
        self.lineEdit_main.setText(eng.clicked_number(self.lineEdit_main.text(), "7"))

    def clicked_8(self):
        self.lineEdit_main.setText(eng.clicked_number(self.lineEdit_main.text(), "8"))

    def clicked_9(self):
        self.lineEdit_main.setText(eng.clicked_number(self.lineEdit_main.text(), "9"))

    def clicked_dot(self):
        self.lineEdit_main.setText(eng.clicked_number(self.lineEdit_main.text(), "."))

    def clicked_eq(self):
        if self.first:
            self.result = float(self.lineEdit_main.text())
            self.lineEdit_top.setText(" ")

        else:
            self.result = eng.eval(self.result, self.lineEdit_main.text(), self.last_operation)
            self.last_operation = "none"
            self.lineEdit_main.setText(str(round(self.result, 2)))
            self.lineEdit_top.setText(" ")
            self.first = True

    def clicked_add(self):
        self.operation("+")

    def clicked_sub(self):
        self.operation("-")

    def clicked_mul(self):
        self.operation("×")

    def clicked_div(self):
        self.operation("÷")

    def clicked_pow(self):
        self.operation("ⁿ")

    def clicked_root(self):
        self.operation("√")

    def clicked_fact(self):
        if self.first:
            self.result = float(self.lineEdit_main.text())
        # int check
        if not self.result.is_integer():
            print("s")
        self.result = float(lib.our_fact(int(self.result)))
        self.lineEdit_top.setText(" ")
        self.lineEdit_main.setText(str(round(self.result, 2)))
        self.first = False
        self.last_operation = "none"

    def clicked_abs(self):
        if self.first:
            self.result = float(self.lineEdit_main.text())
            self.first = False
        self.result = lib.our_abs(self.result)
        self.lineEdit_top.setText(" ")
        self.lineEdit_main.setText(str(round(self.result, 2)))
        self.last_operation = "none"

    def clicked_delete(self):
        self.lineEdit_main.setText(eng.clicked_delete(self.lineEdit_main.text()))

    def clicked_clear(self):
        print("clear")

    def keyPressEvent(self, key):
        if key.text() == "0":
            self.clicked_0()
        elif key.text() == "1":
            self.clicked_1()
        elif key.text() == "2":
            self.clicked_2()
        elif key.text() == "3":
            self.clicked_3()
        elif key.text() == "4":
            self.clicked_4()
        elif key.text() == "5":
            self.clicked_5()
        elif key.text() == "6":
            self.clicked_6()
        elif key.text() == "7":
            self.clicked_7()
        elif key.text() == "8":
            self.clicked_8()
        elif key.text() == "9":
            self.clicked_9()
        elif key.text() == ".":
            self.clicked_dot()
        elif key.text() == "=" or key.key() == 16777220 or key.key() == 16777221:  # enters (normal an numpad)
            self.clicked_eq()
        elif key.text() == "+":
            self.clicked_add()
        elif key.text() == "-":
            self.clicked_sub()
        elif key.text() == "*":
            self.clicked_mul()
        elif key.text() == "/":
            self.clicked_div()
        elif key.text() == "!":
            self.clicked_fact()
        elif key.text() == "|":
            self.clicked_abs()
        elif key.text() == "^":
            self.clicked_pow()
        elif key.text() == "r":
            self.clicked_root()
        elif key.text() == "c":
            self.clicked_clear()
        elif key.key() == 16777223 or key.key() == 16777219:  # backspace and delete
            self.clicked_delete()
        # else:
            # print(key.key())

    def operation(self, which):
        self.last_operation = which
        if self.first:
            self.first = False
            self.result = float(self.lineEdit_main.text())
            self.lineEdit_top.setText(str(round(self.result, 2)) + " " + which)
            self.lineEdit_main.setText("0")
        else:
            self.result = eng.eval(self.result, self.lineEdit_main.text(), which)
            self.lineEdit_top.setText(str(round(self.result, 2)) + " " + which)
            self.lineEdit_main.setText("0")
