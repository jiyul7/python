import sys
#from PyQt5.QtWidgets import (QApplication, QWidget, QLineEdit, QTextBrowser, QPushButton, QVBoxLayout, QHBoxLayout, Qfont)
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtTest import QTest
from yeonhap_class import yeonhapNews


class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.fontSize=10
        self.initUI()

    def initUI(self):
        self.tb1=QTextBrowser()
        self.tb1.setAcceptRichText(True)
        self.tb1.setOpenExternalLinks(True)
        self.tb1.setStyleSheet("background-color: #F4FCDF;")
        #self.tb1.setFontPointSize(self.fontSize + 5)
        self.tb1.setCurrentFont(QFont("맑은고딕", 30, QFont.Bold))
        self.tb1.setTextColor(QColor(0,0,255))

        self.tb2=QTextBrowser()
        self.tb2.setAcceptRichText(True)
        self.tb2.setOpenExternalLinks(True)
        self.tb2.setStyleSheet("background-color: #FBEFDA;")
        self.tb2.setCurrentFont(QFont("맑은고딕", 20, QFont.Bold))
        self.tb2.setTextColor(QColor(0,0,255))
        
        hbox=QHBoxLayout()
        hbox.addWidget(self.tb1,1)
        hbox.addWidget(self.tb2,2)
        self.setLayout(hbox)
        self.setWindowTitle('연합뉴스 속보')
        self.setGeometry(100,100,1800,900)
        self.show()
    
    def append_tb1(self,text):
        self.tb1.append(text)
        #self.tb1.resize(300,300)

    def reapint(self):
        self.update()    
        self.repaint()

    def append_tb2(self,text):
        self.tb2.append(text)

    def clear_text(self):
        self.tb1.clear()
        self.tb2.clear()
    
    def sleep(self, secs):
        QTest.qWait(secs)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    news = yeonhapNews()
    while True:
        top = news.topNews()
        for i in top:
            ex.append_tb1("■ " + i + "\n")
            print(i)

        body = news.bodyNews(2)
        for j in body:
            ex.append_tb2("■ " + j + "\n")

        ex.sleep(30000)
        print("ok")
        ex.clear_text()
        #ex.sleep(1000)

sys.exit(app.exec_()) # 안주면 프로그램 종료 됨


