

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5 import QtWidgets
import Win, MainWin
from register import Ui_Register




class My_UI(Win.Ui_Form):
    def __init__(self, Form):
        super().setupUi(Form)
        self.initUI_1()

    def initUI_1(self):
        self.label_new.setText("<a href ='#' >注册新用户 </a>")
        self.label_new.linkActivated.connect(self.ShowRegister)
        self.btn_login.clicked.connect(self.check)                  #登录检查
        self.btn_cancel.clicked.connect(self.cancel)                #退出按钮连接退出的信号


        self.lineEdit_password.setEchoMode(QLineEdit.Password)      #先给密码行不显示密码
        self.btn_check.clicked.connect(self.yanma)


    #密码隐藏
    def yanma(self):
        if self.btn_check.isChecked():
            self.lineEdit_password.setEchoMode(QLineEdit.Normal)
        else:
            self.lineEdit_password.setEchoMode(QLineEdit.Password)


    #登录时核查账号及密码是否正确
    def check(self):
        temp = False
        #self = QtWidgets.QWidget
        self.id_password = {}
        id = open("账号.txt")
        password = open("密码.txt")
        i = 0
        for line1 in id:
            m = i + 1
            for line2 in password:
                i = i + 1
                if i == m:
                    self.id_password[line1]=line2
                    break
                if i < m:
                    continue
                    #如果输入账号不在账号表文件中，则推送消息框提示
        if self.lineEdit_id.text()+"\n" not in self.id_password:
            #replay = QMessageBox.warning(self, "!", "账号或者密码输入错误", QMessageBox.Yes)
            replay = QMessageBox.warning(self, "!", "输入错误", QMessageBox.Yes)
        else:
            if self.id_password[self.lineEdit_id.text()+"\n"] == self.lineEdit_password.text()+"\n":
                Mainwindow.show()
                main.close()
            # else:
            #     replay = QMessageBox.warning(self, "!", "账号或密码输入错误！", QMessageBox.Yes)

            id.close()
            password.close()


    #退出
    def cancel(self):
        sys.exit()


    #关闭登录窗口，打开注册窗口
    def ShowRegister(self):
        main.close()
        mainwindow.show()



#注册窗口
class Register(Ui_Register):
    def __init__(self, Register):
        super().setupUi(Register)
        self.initUI_2()


    def initUI_2(self):
        self.btn_idnew_cancel.clicked.connect(self.idnew_cancel)

    #退出注册窗口，打开登录窗口
    def idnew_cancel(self):
        mainwindow.close()
        main.show()



#主界面
class my_MainWin(MainWin.Ui_MainWin):
    def __init__(self, MainWin):
        super().setupUi(MainWin)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = QtWidgets.QMainWindow()
    ui = My_UI(main)
    mainwindow = QtWidgets.QMainWindow()
    ui2 = Register(mainwindow)
    Mainwindow = QtWidgets.QMainWindow()
    ui3 = my_MainWin(Mainwindow)
    main.show()
    sys.exit(app.exec_())