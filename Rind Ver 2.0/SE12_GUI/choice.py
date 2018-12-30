# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys

class Choice(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(598, 309)
        self.pushButton_search = QtWidgets.QPushButton(Dialog)
        self.pushButton_search.setGeometry(QtCore.QRect(80, 250, 93, 28))
        self.pushButton_search.setObjectName("pushButton_search")
        self.pushButton_view = QtWidgets.QPushButton(Dialog)
        self.pushButton_view.setGeometry(QtCore.QRect(410, 250, 93, 28))
        self.pushButton_view.setObjectName("pushButton_view")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(-10, -160, 621, 631))
        self.label.setStyleSheet("image: url(:/new/logo4.jpg);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.pushButton_crawler = QtWidgets.QPushButton(Dialog)
        self.pushButton_crawler.setGeometry(QtCore.QRect(250, 250, 93, 28))
        self.pushButton_crawler.setObjectName("pushButton_crawler")
        self.label_text1 = QtWidgets.QLabel(Dialog)
        self.label_text1.setGeometry(QtCore.QRect(210, 280, 181, 21))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(11)
        self.label_text1.setFont(font)
        self.label_text1.setStyleSheet("color: rgb(0, 85, 255);")
        self.label_text1.setText("")
        self.label_text1.setObjectName("label_text1")
        self.label_text2 = QtWidgets.QLabel(Dialog)
        self.label_text2.setGeometry(QtCore.QRect(370, 280, 181, 21))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(11)
        self.label_text2.setFont(font)
        self.label_text2.setStyleSheet("color: rgb(0, 85, 255);")
        self.label_text2.setText("")
        self.label_text2.setObjectName("label_text2")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(532, 20, 41, 28))
        self.pushButton.setObjectName("pushButton")
        self.label.raise_()
        self.pushButton_search.raise_()
        self.pushButton_view.raise_()
        self.pushButton_crawler.raise_()
        self.label_text1.raise_()
        self.label_text2.raise_()
        self.pushButton.raise_()

        self.retranslateUi(Dialog)

        #self.pushButton_view.clicked.connect(Dialog.close)
        self.pushButton_search.clicked.connect(Dialog.close)
        #self.pushButton_crawler.clicked.connect(Dialog.close)
        
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "功能选择"))
        self.pushButton_search.setText(_translate("Dialog", "搜索"))
        self.pushButton_view.setText(_translate("Dialog", "可视化"))
        self.pushButton_crawler.setText(_translate("Dialog", "爬虫"))
        self.pushButton.setText(_translate("Dialog", "注销"))

import pictures
