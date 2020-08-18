import sys
#from PyQt5.QtWidgets import (QApplication, QWidget, QLineEdit, QTextBrowser, QPushButton, QVBoxLayout, QHBoxLayout, Qfont)
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from yeonhap_class import yeonhapNews
import threading
from time import sleep

class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.fontSize=10
        self.initUI()

    def initUI(self):
        self.tb1=QTextBrowser()
        self.tb1.setAcceptRichText(True)
        self.tb1.setOpenExternalLinks(True)

        self.tb1.setStyleSheet("background-color: #05B8CC")
        self.tb1.setCurrentFont(QFont("맑은고딕",20,QFont.Bold))
        self.tb1.setTextColor(QColor(0,0,255))

        self.tb2=QTextBrowser()
        self.tb2.setAcceptRichText(True)
        self.tb2.setOpenExternalLinks(True)
        hbox=QHBoxLayout()
        hbox.addWidget(self.tb1,1)
        hbox.addWidget(self.tb2,2)
        self.setLayout(hbox)
        self.setWindowTitle('QTextBrowser')
        self.setGeometry(0,0,1800,900)
        self.show()
    
    def append_tb1(self,text):
        #self.tb1.setFontPointSize(self.fontSize + 5)
        #self.tb1.setStyleSheet("background-color: blue;")
        self.tb1.append(text)
        #self.tb1.resize(300,300)

    def append_tb2(self,text):
        # 배경색 실패
        #p = self.palette()
        #p.setColor(self.backgroundRole(), QColor(255,0,0))
        #self.tb2.setPalette(p) 
        self.tb2.append(text)

    def clear_text(self):
        self.tb1.clear()
        self.tb2.clear()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    news = yeonhapNews()
  #  while True:
    top = news.topNews()
    for i in top:
        ex.append_tb1("■ " + i + "\n")
    #sleep(3)
    #ex.clear_text()

  #  body = news.bodyNews(3)
   # for j in body:
    #    ex.append_tb2("■ " + j + "\n")

    sys.exit(app.exec_()) # 안주면 프로그램 종료 됨


