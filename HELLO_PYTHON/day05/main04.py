import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow
from PyQt5 import uic 
from random import random

form_class = uic.loadUiType("main04.ui")[0]

class WindowClass(QMainWindow, form_class): 
    def __init__(self): 
        super().__init__() 
        self.setupUi(self)
        
        self.pb.clicked.connect(self.btnClick)

        
    def btnClick(self):
        mine = self.leMine.text()
        print(mine)
        rnd = random()
        print(rnd)
        com = ""
        result = ""
        if rnd >0.5:
            com = "홀"
        else :
            com = "짝"     
        self.leCom.setText(com)
        
        if mine == com:
            result = "플레이어 승리"
        else :
            result = "컴퓨터 승리"
            
        self.leResult.setText(result)        
        
        
        

if __name__ == "__main__": 
    app = QApplication(sys.argv) 
    myWindow = WindowClass() 
    myWindow.show() 
    app.exec_()