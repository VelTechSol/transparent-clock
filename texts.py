import sys
from PyQt5 import QtGui, QtCore
 
 
class Example(QtGui.QMainWindow):
 
    def __init__(self):
        super(Example, self).__init__()
 
        self.initUI()
 
    def initUI(self):
 
        self.qle = QtGui.QLineEdit(self)
        self.qle.move(5, 5) # re
         
        global sometext
        sometext = self.qle.text              # <---- This line I think is the problem
 
        self.lbl = QtGui.QLabel(self)
        self.lbl.move(5, 55)
        btn = QtGui.QPushButton("Ok", self)
        btn.move(5, 30)
 
        btn.clicked.connect(self.buttonClicked)
 
        self.setGeometry(200, 200, 300, 200)
        self.show()
 
    def buttonClicked(self, sometext):
        sender = self.sender()
        self.lbl.setText(self.qle.text()) # calling .text() method to
                                            # get the text from QLineEdit
def main():
 
    app = QtGui.QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
 
if __name__ == '__main__':
    main()