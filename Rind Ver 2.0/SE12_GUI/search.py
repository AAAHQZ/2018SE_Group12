from PyQt5 import QtCore, QtGui, QtWidgets
import sys
sys.path.append("..")
from SE12_Crawler import SearchSQL 

class Search(object):
    def setupUi(self, Dialog):


        Dialog.setObjectName("Dialog")
        Dialog.resize(531, 682)
        self.label_logo = QtWidgets.QLabel(Dialog)
        self.label_logo.setGeometry(QtCore.QRect(-180, -20, 911, 271))
        self.label_logo.setStyleSheet("image: url(:/new/logo4.jpg);")
        self.label_logo.setText("")
        self.label_logo.setObjectName("label_logo")
        self.lineEdit_name = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_name.setGeometry(QtCore.QRect(20, 270, 351, 51))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(12)
        self.lineEdit_name.setFont(font)
        self.lineEdit_name.setObjectName("lineEdit_name")
        self.pushButton_search = QtWidgets.QPushButton(Dialog)
        self.pushButton_search.setGeometry(QtCore.QRect(410, 270, 91, 51))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(12)
        self.pushButton_search.setFont(font)
        self.pushButton_search.setObjectName("pushButton_search")
        self.listWidget = QtWidgets.QListWidget(Dialog)
        self.listWidget.setGeometry(QtCore.QRect(20, 340, 481, 291))
        self.listWidget.setObjectName("listWidget")
        self.closeWinBtn = QtWidgets.QPushButton(Dialog)
        self.closeWinBtn.setGeometry(QtCore.QRect(410, 640, 93, 28))
        self.closeWinBtn.setObjectName("closeWinBtn")

        self.retranslateUi(Dialog)

        self.closeWinBtn.clicked.connect(Dialog.close)
        self.pushButton_search.clicked.connect(self.on_click)
        
        QtCore.QMetaObject.connectSlotsByName(Dialog)
    
    def on_click(self, dialog):
        self.listWidget.clear()
        if(self.lineEdit_name.text() != ''):
            lst = SearchSQL(self.lineEdit_name.text())
            for list in lst :
                #print(list)
                for item in list: 
                    #print(item)
                    self.listWidget.addItem(item)
                self.listWidget.addItem('')

    #def on_printAction1_triggered():


    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "搜索功能"))
        self.lineEdit_name.setPlaceholderText("请输入电影名称或关键词")
        self.pushButton_search.setText(_translate("Dialog", "搜索"))
        self.closeWinBtn.setText(_translate("Dialog", "返回上一级"))

import pictures