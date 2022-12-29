import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow
from PyQt5 import uic 
from asn1crypto.core import Integer

form_class = uic.loadUiType("main02.ui")[0]

class WindowClass(QMainWindow, form_class): 
    def __init__(self): 
        super().__init__() 
        self.setupUi(self)
        
        self.pb.clicked.connect(self.btnClick)

        
    def btnClick(self):
        print("버튼이 클릭되었습니다.")
        a = int(self.le.text())*2
        print(a)
        self.le.setText(str(a))
        

if __name__ == "__main__": 
    app = QApplication(sys.argv) 
    myWindow = WindowClass() 
    myWindow.show() 
    app.exec_()