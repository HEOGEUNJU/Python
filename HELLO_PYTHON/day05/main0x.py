import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow
from PyQt5 import uic 
from asn1crypto.core import Integer
from PyQt5.Qt import QMessageBox
from random import random, randrange

form_class = uic.loadUiType("main0x.ui")[0]

class WindowClass(QMainWindow, form_class): 
 
    def __init__(self): 
        super().__init__() 
        self.setupUi(self)
        
        self.pb.clicked.connect(self.btnClick)
        
        

        
        
    def btnClick(self):
        com = list(range(1,10))
        count =0;
        strike = 0;
        ball = 0;
        result ="";
              
        for i in range(10000):
            rnd = int(random()*9)              
            a=com[0]
            b=com[rnd]
            com[0]=b
            com[rnd]=a
        print(str(com))
            
        inputNum = self.le.text()
        
        user =[]
              
        user.append(inputNum[0:1])
        user.append(inputNum[1:2])
        user.append(inputNum[2:3])
        
        print(user)
        
        for i in range(0,3):
            for j in range(0,3):
                if com[i]==user[j]:
                    if(i==j):
                        strike += 1
                        
                    else:
                        ball += 1
                        
                    
       
        print(ball)
            
     
       
        
        # self.te.setText("{}".format(com1)) 
    
  
   

if __name__ == "__main__": 
    app = QApplication(sys.argv) 
    myWindow = WindowClass() 
    myWindow.show() 
    app.exec_()