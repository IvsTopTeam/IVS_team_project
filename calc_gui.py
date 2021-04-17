import os
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLineEdit
from PyQt5 import uic


class GUI(QWidget):
    def __init__(self):
        super(GUI, self).__init__()
        directory = os.path.dirname(os.path.abspath(__file__))  # its retarded :( I have to calculate and pass the
        guipath = os.path.join(directory, 'gui.ui')  # absolute path to gui.ui file
        uic.loadUi(guipath, self)


