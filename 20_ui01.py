import sys
from PyQt5.QtWidgets import QApplication, QWidget


class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('My First Application')
        # self.move(300, 300)
        self.resize(400, 200)
        self.show()

# 모듈명을 담은 내장 변수 : __name__  (ex> ModuleA.py 면 ModuleA)
# 코드를 직접 실행한거면 __main__이 됨
if __name__ == '__main__':
   app = QApplication(sys.argv)
   ex = MyApp()
   sys.exit(app.exec_())