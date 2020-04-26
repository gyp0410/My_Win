# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Win.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(492, 240)
        self.formLayoutWidget = QtWidgets.QWidget(Form)
        self.formLayoutWidget.setGeometry(QtCore.QRect(70, 40, 341, 122))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.label_id = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_id.setObjectName("label_id")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_id)
        self.lineEdit_id = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.lineEdit_id.setObjectName("lineEdit_id")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineEdit_id)
        self.label_password = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_password.setObjectName("label_password")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_password)
        self.lineEdit_password = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.lineEdit_password.setObjectName("lineEdit_password")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lineEdit_password)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btn_login = QtWidgets.QPushButton(self.formLayoutWidget)
        self.btn_login.setObjectName("btn_login")
        self.horizontalLayout.addWidget(self.btn_login)
        self.btn_cancel = QtWidgets.QPushButton(self.formLayoutWidget)
        self.btn_cancel.setObjectName("btn_cancel")
        self.horizontalLayout.addWidget(self.btn_cancel)
        self.formLayout.setLayout(3, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout)
        self.label_new = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_new.setObjectName("label_new")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_new)
        self.btn_check = QtWidgets.QRadioButton(self.formLayoutWidget)
        self.btn_check.setChecked(False)
        self.btn_check.setObjectName("btn_check")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.btn_check)

        self.retranslateUi(Form)
        #self.btn_login.clicked.connect(Form.check)
        #self.btn_cancel.clicked.connect(Form.cancel)
        #self.label_new.linkActivated['QString'].connect(Form.idnew)
        QtCore.QMetaObject.connectSlotsByName(Form)


    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "登录界面"))
        self.label_id.setText(_translate("Form", "账号："))
        self.lineEdit_id.setPlaceholderText(_translate("Form", "账号"))
        self.label_password.setText(_translate("Form", "密码："))
        self.lineEdit_password.setPlaceholderText(_translate("Form", "密码"))
        self.btn_login.setText(_translate("Form", "登录"))
        self.btn_cancel.setText(_translate("Form", "退出"))
        self.label_new.setToolTip(_translate("Form", "注册账号"))
        self.label_new.setText(_translate("Form", "注册"))
        self.btn_check.setText(_translate("Form", "显示密码"))
