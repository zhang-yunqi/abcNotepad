#!/usr/bin/env python
# coding=utf-8
from PyQt5.Qt import *
import sys 
from abcNotepad import Ui_Form
app = QApplication(sys.argv)

class MainPage(QWidget):
    def __init__(self):
        super().__init__()
        Ui_Form().setupUi(self)

main = MainPage()
main.show()
sys.exit(app.exec_())

