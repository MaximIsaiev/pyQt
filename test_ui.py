import sys
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow
from PyQt5 import uic

class Ui_Window(QMainWindow):

    def __init__(self):
        super().__init__()
        uic.loadUi('window.ui', self)
    def abobus(self):
        print('hello')
    def colorChanged(self, color):
        if (color == u"Red"):
            self.setStyleSheet(u"background-color: rgb(255, 0, 0);")
        elif (color == u"Green"):
            self.setStyleSheet(u"background-color: rgb(0, 255, 0);")
        elif (color == u"Blue"):
            self.setStyleSheet(u"background-color: rgb(0, 0, 255);")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Ui_Window()
    ex.show()
    app.exec()