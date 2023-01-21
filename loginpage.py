# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\User\Documents\Python\loginpage.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1063, 569)
        MainWindow.setStyleSheet("*{\n"
"    border: none;\n"
"    background-color: transparent;\n"
"    background: transparent;\n"
"    padding: 0;\n"
"    margin: 0;\n"
"    color: #fff;\n"
"}\n"
"#centralwidget{\n"
"    background-color: ;\n"
"    background-image: url(:/images/R4spkB.png);\n"
"}\n"
"\n"
"#widget{\n"
"    background-color: rgb(9, 27, 68);\n"
"    border-radius: 20px;\n"
"}\n"
"\n"
"QLineEdit{\n"
"    background-color: rgb(9, 10, 37);\n"
"    padding: 3px 5px;\n"
"    border-radius : 5px;\n"
"}\n"
"\n"
"QPushButton{\n"
"    background-color: rgb(9, 10, 37);\n"
"    padding: 10px 5px;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"#to_login, #to_register{\n"
"    background-color: transparent;\n"
"}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("")
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setMinimumSize(QtCore.QSize(250, 450))
        self.widget.setMaximumSize(QtCore.QSize(250, 450))
        self.widget.setObjectName("widget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.stackedWidget_welcome = QtWidgets.QStackedWidget(self.widget)
        self.stackedWidget_welcome.setObjectName("stackedWidget_welcome")
        self.register_page = QtWidgets.QWidget()
        self.register_page.setObjectName("register_page")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.register_page)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label = QtWidgets.QLabel(self.register_page)
        self.label.setMinimumSize(QtCore.QSize(50, 50))
        self.label.setMaximumSize(QtCore.QSize(50, 50))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(":/icons/fugu_icon/icons/user--plus.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.verticalLayout_4.addWidget(self.label, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.label_2 = QtWidgets.QLabel(self.register_page)
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_4.addWidget(self.label_2, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.label_3 = QtWidgets.QLabel(self.register_page)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_4.addWidget(self.label_3, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem)
        self.frame = QtWidgets.QFrame(self.register_page)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.line_email_signup = QtWidgets.QLineEdit(self.frame)
        self.line_email_signup.setObjectName("line_email_signup")
        self.verticalLayout_3.addWidget(self.line_email_signup)
        self.line_pw_signup = QtWidgets.QLineEdit(self.frame)
        self.line_pw_signup.setEchoMode(QtWidgets.QLineEdit.Password)
        self.line_pw_signup.setObjectName("line_pw_signup")
        self.verticalLayout_3.addWidget(self.line_pw_signup)
        self.line_confirm_pw = QtWidgets.QLineEdit(self.frame)
        self.line_confirm_pw.setText("")
        self.line_confirm_pw.setEchoMode(QtWidgets.QLineEdit.Password)
        self.line_confirm_pw.setObjectName("line_confirm_pw")
        self.verticalLayout_3.addWidget(self.line_confirm_pw)
        self.label_confirm = QtWidgets.QLabel(self.frame)
        self.label_confirm.setText("")
        self.label_confirm.setWordWrap(True)
        self.label_confirm.setObjectName("label_confirm")
        self.verticalLayout_3.addWidget(self.label_confirm)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem1)
        self.verticalLayout_4.addWidget(self.frame)
        self.checkBox_signup = QtWidgets.QCheckBox(self.register_page)
        self.checkBox_signup.setObjectName("checkBox_signup")
        self.verticalLayout_4.addWidget(self.checkBox_signup)
        self.button_signup = QtWidgets.QPushButton(self.register_page)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.button_signup.setFont(font)
        self.button_signup.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.button_signup.setStyleSheet("QPushButton:hover{\n"
"    background-color: rgb(5, 23, 64);\n"
"}")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/fugu_icon/icons-shadowless/door-open-out.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_signup.setIcon(icon)
        self.button_signup.setIconSize(QtCore.QSize(24, 24))
        self.button_signup.setObjectName("button_signup")
        self.verticalLayout_4.addWidget(self.button_signup, 0, QtCore.Qt.AlignHCenter)
        self.to_login = QtWidgets.QPushButton(self.register_page)
        self.to_login.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.to_login.setStyleSheet("QPushButton:hover{\n"
"    background-color: rgb(4, 22, 63);\n"
"}")
        self.to_login.setObjectName("to_login")
        self.verticalLayout_4.addWidget(self.to_login, 0, QtCore.Qt.AlignHCenter)
        self.stackedWidget_welcome.addWidget(self.register_page)
        self.login_page = QtWidgets.QWidget()
        self.login_page.setObjectName("login_page")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.login_page)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.label_8 = QtWidgets.QLabel(self.login_page)
        self.label_8.setMinimumSize(QtCore.QSize(50, 50))
        self.label_8.setMaximumSize(QtCore.QSize(50, 50))
        self.label_8.setText("")
        self.label_8.setPixmap(QtGui.QPixmap(":/icons/fugu_icon/icons/user--arrow.png"))
        self.label_8.setScaledContents(True)
        self.label_8.setObjectName("label_8")
        self.verticalLayout_8.addWidget(self.label_8, 0, QtCore.Qt.AlignHCenter)
        self.label_7 = QtWidgets.QLabel(self.login_page)
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.verticalLayout_8.addWidget(self.label_7, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.label_9 = QtWidgets.QLabel(self.login_page)
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_9.setObjectName("label_9")
        self.verticalLayout_8.addWidget(self.label_9, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        spacerItem2 = QtWidgets.QSpacerItem(20, 27, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_8.addItem(spacerItem2)
        self.frame_3 = QtWidgets.QFrame(self.login_page)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.frame_3)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.line_email = QtWidgets.QLineEdit(self.frame_3)
        self.line_email.setObjectName("line_email")
        self.verticalLayout_7.addWidget(self.line_email)
        self.line_pw = QtWidgets.QLineEdit(self.frame_3)
        self.line_pw.setEchoMode(QtWidgets.QLineEdit.Password)
        self.line_pw.setObjectName("line_pw")
        self.verticalLayout_7.addWidget(self.line_pw)
        self.label_confirm2 = QtWidgets.QLabel(self.frame_3)
        self.label_confirm2.setText("")
        self.label_confirm2.setObjectName("label_confirm2")
        self.verticalLayout_7.addWidget(self.label_confirm2)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_7.addItem(spacerItem3)
        self.verticalLayout_8.addWidget(self.frame_3)
        self.checkBox_login = QtWidgets.QCheckBox(self.login_page)
        self.checkBox_login.setObjectName("checkBox_login")
        self.verticalLayout_8.addWidget(self.checkBox_login)
        self.button_login = QtWidgets.QPushButton(self.login_page)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.button_login.setFont(font)
        self.button_login.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.button_login.setStyleSheet("QPushButton:hover{\n"
"    background-color: rgb(5, 23, 64);\n"
"}")
        self.button_login.setIcon(icon)
        self.button_login.setIconSize(QtCore.QSize(24, 24))
        self.button_login.setObjectName("button_login")
        self.verticalLayout_8.addWidget(self.button_login, 0, QtCore.Qt.AlignHCenter)
        self.to_register = QtWidgets.QPushButton(self.login_page)
        self.to_register.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.to_register.setStyleSheet("QPushButton:hover{\n"
"    background-color: rgb(4, 22, 63);\n"
"}")
        self.to_register.setObjectName("to_register")
        self.verticalLayout_8.addWidget(self.to_register, 0, QtCore.Qt.AlignHCenter)
        self.stackedWidget_welcome.addWidget(self.login_page)
        self.verticalLayout_2.addWidget(self.stackedWidget_welcome)
        self.verticalLayout.addWidget(self.widget, 0, QtCore.Qt.AlignHCenter)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.stackedWidget_welcome.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_2.setText(_translate("MainWindow", "Sign Up"))
        self.label_3.setText(_translate("MainWindow", "Enter Your Information Below"))
        self.line_email_signup.setPlaceholderText(_translate("MainWindow", "Email Address"))
        self.line_pw_signup.setPlaceholderText(_translate("MainWindow", "Password"))
        self.line_confirm_pw.setPlaceholderText(_translate("MainWindow", "Confirm Password"))
        self.checkBox_signup.setText(_translate("MainWindow", "Show Password"))
        self.button_signup.setText(_translate("MainWindow", "Register"))
        self.to_login.setText(_translate("MainWindow", "Already Registered? Log in"))
        self.label_7.setText(_translate("MainWindow", "Log In"))
        self.label_9.setText(_translate("MainWindow", "Enter Your Information Below"))
        self.line_email.setPlaceholderText(_translate("MainWindow", "Email Address"))
        self.line_pw.setPlaceholderText(_translate("MainWindow", "Password"))
        self.checkBox_login.setText(_translate("MainWindow", "Show Password"))
        self.button_login.setText(_translate("MainWindow", "Log In"))
        self.to_register.setText(_translate("MainWindow", "Not Registered? Register"))
import resources_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
