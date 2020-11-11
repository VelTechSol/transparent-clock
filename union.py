import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import pyqtSlot, QRect
from PyQt5.QtCore import QCoreApplication, Qt,QBasicTimer, QPoint, QTimer, QTime, Qt
from PyQt5.QtGui import QIntValidator
from PyQt5 import QtCore
from ui import main
import time
from PyQt5.QtCore import QTimer, QTime, Qt

class MyActions(main.Ui_MainWindow, QtWidgets.QMainWindow):
    def __init__(self):
        super(MyActions, self).__init__()
        self.setupUi(self)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        timer = QTimer(self)
        timer.timeout.connect(self.showTime)
        timer.start(1000) # update every second
        self.showTime()
 
    def showTime(self):
        currentTime = QTime.currentTime()
        displayTxt = currentTime.toString('hh')
        self.label.setText(displayTxt)
        displayTxt2 = currentTime.toString(':mm')
        self.label_2.setText(displayTxt2)
        displayTxt3 = currentTime.toString(':ss')
        self.label_3.setText(displayTxt3)
       
    
    def mousePressEvent(self, event):
        self.oldPos = event.globalPos()

    def mouseMoveEvent(self, event):
        delta = QPoint (event.globalPos() - self.oldPos)
        #print(delta)
        self.move(self.x() + delta.x(), self.y() + delta.y())
        self.oldPos = event.globalPos()

   
if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    qt_app=MyActions()
    qt_app.show()
    app.exec_()