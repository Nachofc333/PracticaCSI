# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'InicioW.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_login(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(339, 451)
        MainWindow.setMinimumSize(QtCore.QSize(339, 451))
        MainWindow.setMaximumSize(QtCore.QSize(339, 451))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 341, 61))
        self.label.setAutoFillBackground(False)
        self.label.setStyleSheet("background-color: rgb(0, 170, 255);\n"
"font: 700 14pt \"Arial\";")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(0, 60, 341, 16))
        self.label_2.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(-2, 65, 351, 351))
        self.label_3.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0.489, y1:0, x2:0.506, y2:1, stop:0 rgba(0, 142, 202, 255), stop:0.846591 rgba(255, 255, 255, 255));")
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(60, 130, 221, 141))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_4 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_4.setAutoFillBackground(False)
        self.label_4.setStyleSheet("font: 14pt \"Arial\";")
        self.label_4.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.label_4)
        self.txt_user = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.txt_user.setObjectName("txt_user")
        self.verticalLayout.addWidget(self.txt_user)
        self.label_5 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_5.setStyleSheet("font: 14pt \"Arial\";")
        self.label_5.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.label_5.setObjectName("label_5")
        self.verticalLayout.addWidget(self.label_5)
        self.txt_password = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.txt_password.setInputMethodHints(QtCore.Qt.ImhHiddenText|QtCore.Qt.ImhNoAutoUppercase|QtCore.Qt.ImhNoPredictiveText|QtCore.Qt.ImhSensitiveData)
        self.txt_password.setText("")
        self.txt_password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.txt_password.setReadOnly(False)
        self.txt_password.setObjectName("txt_password")
        self.verticalLayout.addWidget(self.txt_password)
        self.btnIniciarSesion = QtWidgets.QPushButton(self.centralwidget)
        self.btnIniciarSesion.setGeometry(QtCore.QRect(60, 300, 101, 41))
        self.btnIniciarSesion.setObjectName("btnIniciarSesion")
        self.btnRegistrar = QtWidgets.QPushButton(self.centralwidget)
        self.btnRegistrar.setGeometry(QtCore.QRect(180, 300, 101, 41))
        self.btnRegistrar.setObjectName("btnRegistrar")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 339, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Inicio de Sesión"))
        self.label_4.setText(_translate("MainWindow", "-Usuario:"))
        self.txt_user.setPlaceholderText(_translate("MainWindow", "Introduce el usuario."))
        self.label_5.setText(_translate("MainWindow", "-Contraseña:"))
        self.txt_password.setPlaceholderText(_translate("MainWindow", "Introduce la contraseña."))
        self.btnIniciarSesion.setText(_translate("MainWindow", "Iniciar sesión"))
        self.btnIniciarSesion.setShortcut(_translate("MainWindow", "Return"))
        self.btnRegistrar.setText(_translate("MainWindow", "Registrar usuario"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_login()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
