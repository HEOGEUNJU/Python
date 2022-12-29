import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow
from PyQt5 import uic 
from asn1crypto.core import Integer
from PyQt5.Qt import QMessageBox

form_class = uic.loadUiType("main09.ui")[0]

class WindowClass(QMainWindow, form_class): 
 
    def __init__(self): 
        super().__init__() 
        self.setupUi(self)
        
        self.pb1.clicked.connect(self.btnClick)
        self.pb2.clicked.connect(self.btnClick)
        self.pb3.clicked.connect(self.btnClick)
        self.pb4.clicked.connect(self.btnClick)
        self.pb5.clicked.connect(self.btnClick)
        self.pb6.clicked.connect(self.btnClick)
        self.pb7.clicked.connect(self.btnClick)
        self.pb8.clicked.connect(self.btnClick)
        self.pb9.clicked.connect(self.btnClick)
        self.pb0.clicked.connect(self.btnClick)
        self.pbCall.clicked.connect(self.btnClick11)

        
    def btnClick(self):
        str_new = self.sender().text()
        str_old = self.le.text()
        self.le.setText(str_old+str_new) 
    
    def btnClick11(self):
        str = self.le.text()
        QMessageBox.about(self,'통화중',str)
   

if __name__ == "__main__": 
    app = QApplication(sys.argv) 
    myWindow = WindowClass() 
    myWindow.show() 
    app.exec_()