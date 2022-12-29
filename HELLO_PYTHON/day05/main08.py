import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow
from PyQt5 import uic 
from asn1crypto.core import Integer

form_class = uic.loadUiType("main08.ui")[0]

class WindowClass(QMainWindow, form_class): 
    def __init__(self): 
        super().__init__() 
        self.setupUi(self)
        self.pb.clicked.connect(self.btnClick)

        
    def btnClick(self):
        lbf = self.le_f.text()    
        lbl = self.le_l.text() 
        ilbf=int(lbf)
        ilbl=int(lbl)
        result=""
        for i in range(ilbf,ilbl+1):
            for j in range(1,i+1):
                result += "*"
            result += "\n"    
            
                
        print(result)
        self.pte.setText(result)       

if __name__ == "__main__": 
    app = QApplication(sys.argv) 
    myWindow = WindowClass() 
    myWindow.show() 
    app.exec_()