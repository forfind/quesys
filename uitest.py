import sys
from PyQt5.QtWidgets import QApplication,QWidget,QLabel,QPushButton
from PyQt5.QtGui import QPixmap

class MyClass(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("刘金玉编程")
        self.setGeometry(300,100,400,300)
        self.lbl=QLabel("图片",self)
        self.pm=QPixmap("帮助.png")
        print(self.pm)
        self.lbl.setPixmap(self.pm)
        self.lbl.resize(300,200)
        self.lbl.setScaledContents(True)

        #移除按钮
        btn1=QPushButton("移除图片",self)
        btn1.clicked.connect(self.myRemovePic)
        btn1.move(0,220)
        #增加按钮
        btn2=QPushButton("增加图片",self)
        btn2.clicked.connect(self.myAddPic)
        btn2.move(0,250)
        self.show()
    def myRemovePic(self):
        self.lbl.setPixmap(QPixmap(""))
    def myAddPic(self):
        self.lbl.setPixmap(self.pm)
if __name__=="__main__":
    app=QApplication(sys.argv)
    mc=MyClass()
    app.exec_()