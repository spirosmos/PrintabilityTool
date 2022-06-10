
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication
import sys
import source_GUI

class ExampleApp(QtWidgets.QMainWindow, source_GUI.Ui_MainWindow):
    def __init__(self, parent=None):
        super(ExampleApp, self).__init__(parent)
        self.setupUi(self)

def main():
    app = QApplication(sys.argv) 
    app.setFont(QtGui.QFont('Arial',9))
    app.setStyle('Fusion')
    form = ExampleApp()
    form.show()
    app.exec_()

if __name__ == '__main__':
    main()
