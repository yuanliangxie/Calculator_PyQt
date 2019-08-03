import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow
from calculator import Ui_Form
from firstUi import Ui_Form as Ui_Form2


class mainwindow(QWidget, Ui_Form):
    def __init__(self,f):
        super(mainwindow, self).__init__()
        self.setupUi(self)
        self.bts_connect()
        #self.show()

    def ps_bt(self):
        self.textBrowser.clear()

    def ps_bt1(self):
        self.lineEdit.insert('/')

    def ps_bt2(self):
        self.lineEdit.insert('*')

    def ps_bt3(self):
        self.lineEdit.insert('+')

    def ps_bt4(self):
        self.lineEdit.insert('-')

    def ps_bt5(self):
        #self.lineEdit.insert('=')
        self.calculate()

    def ps_bt6(self):
        self.lineEdit.insert('.')

    def ps_bt7(self):
        self.lineEdit.insert('0')

    def ps_bt8(self):
        self.lineEdit.insert('1')

    def ps_bt9(self):
        self.lineEdit.insert('2')

    def ps_bt10(self):
        self.lineEdit.insert('3')

    def ps_bt11(self):
        self.lineEdit.insert('4')

    def ps_bt12(self):
        self.lineEdit.insert('5')

    def ps_bt13(self):
        self.lineEdit.insert('6')

    def ps_bt14(self):
        self.lineEdit.insert('7')

    def ps_bt15(self):
        self.lineEdit.insert('8')

    def ps_bt16(self):
        self.lineEdit.insert('9')

    def ps_bt17(self):
        self.lineEdit.backspace()

    def ps_bt18(self):
        self.lineEdit.clear()

    def ps_bt19(self):
        #self.close()
        f.show()
        # self.setupUi1(self)
        # self.show()
    def ps_bt20(self):
        self.setupUi(self)
        self.show()
    def ps_bt21(self):
        self.close()

    def lineEdit_clear(self):
        self.lineEdit.clear()

    def calculate(self):
        # text = self.lineEdit.text()
        # self.lineEdit.setText('%s= %.2f' % (text, eval(text)))
        text = self.lineEdit.text()
        str1 = '%s=%.2f' % (text, eval(text))
        #str2 = str(eval(text))
        #text1='wo ai ni'

        self.textBrowser.append(str1)
        self.lineEdit_clear()
    def bts_connect(self):
        self.pushButton.clicked.connect(self.ps_bt8)
        # w.pushButton_1.clicked.connect(w.ps_bt1)
        self.pushButton_2.clicked.connect(self.ps_bt18)
        self.pushButton_3.clicked.connect(self.ps_bt9)
        self.pushButton_4.clicked.connect(self.ps_bt10)
        self.pushButton_5.clicked.connect(self.ps_bt13)
        self.pushButton_6.clicked.connect(self.ps_bt12)
        self.pushButton_7.clicked.connect(self.ps_bt11)
        self.pushButton_8.clicked.connect(self.ps_bt14)
        self.pushButton_9.clicked.connect(self.ps_bt15)
        self.pushButton_10.clicked.connect(self.ps_bt16)
        # w.pushButton_11.clicked.connect(w.ps_bt11)
        # w.pushButton_12.clicked.connect(w.ps_bt12)
        self.pushButton_13.clicked.connect(self.ps_bt4)
        self.pushButton_14.clicked.connect(self.ps_bt3)
        self.pushButton_15.clicked.connect(self.ps_bt2)
        self.pushButton_16.clicked.connect(self.ps_bt1)
        # w.pushButton_17.clicked.connect(w.ps_bt17)
        self.pushButton_18.clicked.connect(self.ps_bt19)
        self.pushButton_19.clicked.connect(self.ps_bt17)
        self.pushButton_20.clicked.connect(self.ps_bt)
        self.pushButton_21.clicked.connect(self.ps_bt5)
        self.pushButton_22.clicked.connect(self.ps_bt7)
        # self.pushButton_23.clicked.connect(self.ps_bt21)
        # self.pushButton_24.clicked.connect(self.ps_bt20)

class secondwindow(QWidget, Ui_Form2):
    def __init__(self, w = None):
        super(secondwindow, self).__init__()
        self.setupUi(self)
        self.bts_connect()
    def ps_bt1(self):
        self.close()
        w.close()
    def ps_bt2(self):
        if w != None:
            self.close()
            w.show()
    def bts_connect(self):
        self.pushButton.clicked.connect(self.ps_bt1)
        self.pushButton_2.clicked.connect(self.ps_bt2)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    f = secondwindow()
    w = mainwindow(f)
    f = secondwindow(w)
    w.show()
    sys.exit(app.exec_())