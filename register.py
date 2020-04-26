# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'register.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Register(object):
    def setupUi(self, Register):
        Register.setObjectName("Register")
        Register.resize(492, 240)
        self.formLayoutWidget = QtWidgets.QWidget(Register)
        self.formLayoutWidget.setGeometry(QtCore.QRect(70, 40, 341, 122))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.label_idnew_id = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_idnew_id.setObjectName("label_idnew_id")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_idnew_id)
        self.lineEdit_idnew_id = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.lineEdit_idnew_id.setObjectName("lineEdit_idnew_id")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineEdit_idnew_id)
        self.label_idnew_password = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_idnew_password.setObjectName("label_idnew_password")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_idnew_password)
        self.lineEdit_idnew_password = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.lineEdit_idnew_password.setObjectName("lineEdit_idnew_password")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lineEdit_idnew_password)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btn_idnew_confirm = QtWidgets.QPushButton(self.formLayoutWidget)
        self.btn_idnew_confirm.setObjectName("btn_idnew_confirm")
        self.horizontalLayout.addWidget(self.btn_idnew_confirm)
        self.btn_idnew_cancel = QtWidgets.QPushButton(self.formLayoutWidget)
        self.btn_idnew_cancel.setObjectName("btn_idnew_cancel")
        self.horizontalLayout.addWidget(self.btn_idnew_cancel)
        self.formLayout.setLayout(2, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout)

        self.retranslateUi(Register)
        #self.btn_idnew_confirm.clicked.connect(Register.check)
        #self.btn_idnew_cancel.clicked.connect(Register.cancel)
        QtCore.QMetaObject.connectSlotsByName(Register)

    def retranslateUi(self, Register):
        _translate = QtCore.QCoreApplication.translate
        Register.setWindowTitle(_translate("Register", "注册界面"))
        self.label_idnew_id.setText(_translate("Register", "账号："))
        self.lineEdit_idnew_id.setPlaceholderText(_translate("Register", "账号"))
        self.label_idnew_password.setText(_translate("Register", "密码："))
        self.lineEdit_idnew_password.setPlaceholderText(_translate("Register", "密码"))
        self.btn_idnew_confirm.setText(_translate("Register", "注册"))
        self.btn_idnew_cancel.setText(_translate("Register", "退出"))
