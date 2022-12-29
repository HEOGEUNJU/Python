import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow
from PyQt5 import uic 
from random import random

form_class = uic.loadUiType("main07.ui")[0]

class WindowClass(QMainWindow, form_class): 
    def __init__(self): 
        super().__init__() 
        self.setupUi(self)
        
        self.pb.clicked.connect(self.btnClick)
        self.leMine.returnPressed.connect(self.btnClick)

        
    def btnClick(self):
        me = self.leMine.text()
        com1 = ""
        rnd = random()
        com = ""
        result = ""
        if rnd >0.6:
            com = "가위"
        elif rnd >0.3:
            com = "바위"    
        else :
            com = "보"     
        self.leCom.setText(com)
                
        if me == com:
            result="비김"
        elif me=="가위" and com=="바위" or me=="바위" and com=="보" or me=="보"  and com=="가위" :
            result="컴퓨터 승리"
        else: 
            result="플레이어 승리"   
        self.leResult.setText(result)        
        
        
        

if __name__ == "__main__": 
    app = QApplication(sys.argv) 
    myWindow = WindowClass() 
    myWindow.show() 
    app.exec_()