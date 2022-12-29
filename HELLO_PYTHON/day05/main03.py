import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow
from PyQt5 import uic 
from random import random

form_class = uic.loadUiType("main03.ui")[0]

class WindowClass(QMainWindow, form_class): 
    def __init__(self): 
        super().__init__() 
        self.setupUi(self) 
        self.pb.clicked.connect(self.btnClick)

        
    def btnClick(self):
        
        arr45 = list(range(1,46))    
        print(arr45)
        for i in range(10000):
            rnd = int(random()*45)             
            a=arr45[0]
            b=arr45[rnd]
            arr45[0]=b
            arr45[rnd]=a
            
        print(arr45[0])
        print(arr45[1])
        
        self.le1.setText(str(arr45[0]))
        self.le2.setText(str(arr45[1]))
        self.le3.setText(str(arr45[2]))
        self.le4.setText(str(arr45[3]))
        self.le5.setText(str(arr45[4]))
        self.le6.setText(str(arr45[5]))
                                     

if __name__ == "__main__": 
    app = QApplication(sys.argv) 
    myWindow = WindowClass() 
    myWindow.show() 
    app.exec_()