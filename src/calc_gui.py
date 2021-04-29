##
# @file calc_gui.py
# @author David Novak
# @date 27.4. 2020
# @brief Module with class GUI
#

from PyQt5.QtWidgets import QWidget, QPushButton, QLineEdit, QApplication
from PyQt5 import uic
import calc_engine as eng
import our_library as lib
import os


##
# @brief GUI class includes all methods to interact with GUI of calculator
#
class GUI(QWidget):
    result = float(0)           # stores intermediate result
    first = True                # if I am entering first or second operand
    last_operation = "none"     # remembers last clicked operation

    ##
    # @brief Constructor of method GUI
    #
    def __init__(self):
        super(GUI, self).__init__()
        directory = os.path.dirname(os.path.abspath(__file__))  # its retarded and cant load the ui file, it has to
        gui_path = os.path.join(directory, 'gui.ui')            # calculate and pass the absolute path to gui.ui file
        uic.loadUi("gui_path", self)

        # makes buttons to work
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
        self.findChild(QLineEdit, 'lineEdit_main')
        self.findChild(QLineEdit, 'lineEdit_top')

    ##
    # @brief Method that handles button "0" click
    #
    def clicked_0(self):
        self.lineEdit_main.setText(eng.clicked_number(self.lineEdit_main.text(), "0"))

    ##
    # @brief Method that handles button "1" click
    #
    def clicked_1(self):
        self.lineEdit_main.setText(eng.clicked_number(self.lineEdit_main.text(), "1"))

    ##
    # @brief Method that handles button "2" click
    #
    def clicked_2(self):
        self.lineEdit_main.setText(eng.clicked_number(self.lineEdit_main.text(), "2"))

    ##
    # @brief Method that handles button "3" click
    #
    def clicked_3(self):
        self.lineEdit_main.setText(eng.clicked_number(self.lineEdit_main.text(), "3"))

    ##
    # @brief Method that handles button "4" click
    #
    def clicked_4(self):
        self.lineEdit_main.setText(eng.clicked_number(self.lineEdit_main.text(), "4"))

    ##
    # @brief Method that handles button "5" click
    #
    def clicked_5(self):
        self.lineEdit_main.setText(eng.clicked_number(self.lineEdit_main.text(), "5"))

    ##
    # @brief Method that handles button "6" click
    #
    def clicked_6(self):
        self.lineEdit_main.setText(eng.clicked_number(self.lineEdit_main.text(), "6"))

    ##
    # @brief Method that handles button "7" click
    #
    def clicked_7(self):
        self.lineEdit_main.setText(eng.clicked_number(self.lineEdit_main.text(), "7"))

    ##
    # @brief Method that handles button "8" click
    #
    def clicked_8(self):
        self.lineEdit_main.setText(eng.clicked_number(self.lineEdit_main.text(), "8"))

    ##
    # @brief Method that handles button "9" click
    #
    def clicked_9(self):
        self.lineEdit_main.setText(eng.clicked_number(self.lineEdit_main.text(), "9"))

    ##
    # @brief Method that handles button "." click
    #
    def clicked_dot(self):
        self.lineEdit_main.setText(eng.clicked_number(self.lineEdit_main.text(), "."))

    ##
    # @brief Method that handles button "=" click
    #
    def clicked_eq(self):
        if self.first:
            if eng.isfloat(self.lineEdit_main.text()):
                self.result = float(self.lineEdit_main.text())
            else:
                self.result = 0.0
        else:
            error, self.result = eng.evaluation(self.result, self.lineEdit_main.text(), self.last_operation)
            if error == "Math Error":
                self.clicked_clear()
                self.lineEdit_main.setText("Math Error")
                return
            if eng.display_num(self.result) == "Too large!":
                self.clicked_clear()
                self.lineEdit_main.setText("Too large!")
                return
            self.lineEdit_main.setText(eng.display_num(self.result))
            self.first = True
        self.lineEdit_top.setText(" ")

    ##
    # @brief Method that handles button "+" click
    #
    def clicked_add(self):
        self.operation("+")

    ##
    # @brief Method that handles button "-" click
    #
    def clicked_sub(self):
        if self.lineEdit_main.text() == "0" or self.lineEdit_main.text() == "-":
            self.lineEdit_main.setText("-")
        else:
            self.operation("-")

    ##
    # @brief Method that handles button "×" click
    #
    def clicked_mul(self):
        self.operation("×")

    ##
    # @brief Method that handles button "÷" click
    #
    def clicked_div(self):
        self.operation("÷")

    ##
    # @brief Method that handles button "ⁿ" click
    #
    def clicked_pow(self):
        self.operation("ⁿ")

    ##
    # @brief Method that handles button "√" click
    #
    def clicked_root(self):
        self.operation("√")

    ##
    # @brief Method that handles button "x!" click
    #
    def clicked_fact(self):
        # implementation maximum value the calculator can compute factorial from
        # from large number it takes long to compute and the display is too small for displaying that long numbers
        max_fact = 20
        if self.first:
            if eng.isfloat(self.lineEdit_main.text()):
                self.result = float(self.lineEdit_main.text())
            else:
                self.result = 0.0
        # int check
        if not self.result.is_integer() or self.result < 0:
            self.clicked_clear()
            self.lineEdit_main.setText("Math Error")
            return
        if self.result > max_fact:
            self.clicked_clear()
            self.lineEdit_main.setText("Too large!")
            return
        self.result = float(lib.our_fact(int(self.result)))
        self.lineEdit_top.setText(" ")
        if eng.display_num(self.result) == "Too large!":
            self.clicked_clear()
            self.lineEdit_main.setText("Too large!")
            return
        self.lineEdit_main.setText(eng.display_num(self.result))
        self.first = True
        self.last_operation = "none"

    ##
    # @brief Method that handles button "|x|" click
    #
    def clicked_abs(self):
        if self.first:                                          # if this is first operation
            self.result = float(self.lineEdit_main.text())      # sets the number into result
            # self.first = False
        self.result = lib.our_abs(self.result)                  # call abs function on result
        self.first = True
        self.last_operation = "none"
        self.lineEdit_top.setText(" ")                              # resets top display text
        if eng.display_num(self.result) == "Too large!":
            self.clicked_clear()
            self.lineEdit_main.setText("Too large!")
            return
        self.lineEdit_main.setText(eng.display_num(self.result))    # displays result on main display

    ##
    # @brief Method that handles button "delete" click
    #
    def clicked_delete(self):
        tmp_str = eng.clicked_delete(self.lineEdit_main.text())
        self.lineEdit_main.setText(tmp_str)
        if tmp_str == "-":
            self.result = 0

    ##
    # @brief Method that handles button "clear" click
    #
    def clicked_clear(self):
        self.result = float(0)
        self.first = True
        self.last_operation = "none"
        self.lineEdit_top.setText(" ")
        self.lineEdit_main.setText("0")

    ##
    # @brief Method that redirects button clicks from keyboards to their proper button functions
    #
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
        elif key.text() == "=" or key.key() == 16777220 or key.key() == 16777221:  # Enter (normal an numpad)
            self.clicked_eq()
        elif key.text() == "+":
            self.clicked_add()
        elif key.text() == "-" or key.text() == "s":
            self.clicked_sub()
        elif key.text() == "*" or key.text() == "m":
            self.clicked_mul()
        elif key.text() == "/" or key.text() == "d":
            self.clicked_div()
        elif key.text() == "!" or key.text() == "f":
            self.clicked_fact()
        elif key.text() == "|" or key.text() == "a":
            self.clicked_abs()
        elif key.text() == "^" or key.text() == "p":
            self.clicked_pow()
        elif key.text() == "r":
            self.clicked_root()
        elif key.text() == "c":
            self.clicked_clear()
        elif key.key() == 16777223 or key.key() == 16777219:  # backspace and delete
            self.clicked_delete()
        # else:
            # print(key.key())

    ##
    # @brief Method that is called by clicked_operation methods and coordinates entering operands and operations
    #
    def operation(self, which):
        if self.first:                                                              # if this operation is first
            self.last_operation = which
            self.first = False
            if not eng.isfloat(self.lineEdit_main.text()):
                self.lineEdit_main.setText("0")
            self.result = float(self.lineEdit_main.text())                          # sets the result to main_display
        else:
            error, self.result = eng.evaluation(self.result, self.lineEdit_main.text(), self.last_operation)
            self.last_operation = which
            if error == "Math Error":
                self.clicked_clear()
                self.lineEdit_main.setText("Math Error")
                return
            if eng.display_num(self.result) == "Too large!":
                self.clicked_clear()
                self.lineEdit_main.setText("Too large!")
                return

        self.lineEdit_top.setText(eng.display_num(self.result) + " " + which)  # sets the top with temporary result

        self.lineEdit_main.setText("0")  # sets main display to "0" to start entering new number
