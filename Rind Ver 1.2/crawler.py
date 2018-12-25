from PyQt5 import QtCore, QtGui, QtWidgets
from SE12_Crawler import *
#import time

class Crawler(object):
    def setupUi(self, dialog):
        dialog.setObjectName("dialog")
        dialog.resize(454, 277)
        self.closeWinBtn = QtWidgets.QPushButton(dialog)
        self.closeWinBtn.setGeometry(QtCore.QRect(160, 230, 131, 31))
        self.closeWinBtn.setObjectName("closeWinBtn")
        self.label_picture = QtWidgets.QLabel(dialog)
        self.label_picture.setGeometry(QtCore.QRect(-160, -10, 1150, 850))
        self.label_picture.setStyleSheet("image: url(:/new/background.jpg);")
        self.label_picture.setText("")
        self.label_picture.setObjectName("label_picture")
        self.pushButton = QtWidgets.QPushButton(dialog)
        self.pushButton.setGeometry(QtCore.QRect(320, 90, 111, 28))
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(dialog)
        self.label.setGeometry(QtCore.QRect(10, 60, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.spinBox_year1 = QtWidgets.QSpinBox(dialog)
        self.spinBox_year1.setGeometry(QtCore.QRect(100, 65, 61, 22))
        self.spinBox_year1.setMinimum(2015)
        self.spinBox_year1.setMaximum(2020)
        self.spinBox_year1.setObjectName("spinBox_year1")
        self.spinBox_month1 = QtWidgets.QSpinBox(dialog)
        self.spinBox_month1.setGeometry(QtCore.QRect(200, 65, 46, 22))
        self.spinBox_month1.setMinimum(1)
        self.spinBox_month1.setMaximum(12)
        self.spinBox_month1.setObjectName("spinBox_month1")
        self.label_2 = QtWidgets.QLabel(dialog)
        self.label_2.setGeometry(QtCore.QRect(170, 60, 21, 31))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.spinBox_month2 = QtWidgets.QSpinBox(dialog)
        self.spinBox_month2.setGeometry(QtCore.QRect(200, 115, 46, 22))
        self.spinBox_month2.setMinimum(1)
        self.spinBox_month2.setMaximum(12)
        self.spinBox_month2.setObjectName("spinBox_month2")
        self.spinBox_year2 = QtWidgets.QSpinBox(dialog)
        self.spinBox_year2.setGeometry(QtCore.QRect(100, 115, 61, 22))
        self.spinBox_year2.setMinimum(2015)
        self.spinBox_year2.setMaximum(2020)
        self.spinBox_year2.setObjectName("spinBox_year2")
        self.label_4 = QtWidgets.QLabel(dialog)
        self.label_4.setGeometry(QtCore.QRect(170, 110, 21, 31))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(dialog)
        self.label_5.setGeometry(QtCore.QRect(10, 110, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(dialog)
        self.label_6.setGeometry(QtCore.QRect(250, 60, 41, 31))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(12)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(dialog)
        self.label_7.setGeometry(QtCore.QRect(250, 110, 41, 31))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(12)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.label_tip = QtWidgets.QLabel(dialog)
        self.label_tip.setGeometry(QtCore.QRect(180, 160, 91, 41))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(11)
        self.label_tip.setFont(font)
        self.label_tip.setStyleSheet("color: rgb(255, 0, 0);")
        self.label_tip.setText("")
        self.label_tip.setObjectName("label_tip")
        self.label_picture.raise_()
        self.closeWinBtn.raise_()
        self.pushButton.raise_()
        self.label.raise_()
        self.spinBox_year1.raise_()
        self.spinBox_month1.raise_()
        self.label_2.raise_()
        self.spinBox_month2.raise_()
        self.spinBox_year2.raise_()
        self.label_4.raise_()
        self.label_5.raise_()
        self.label_6.raise_()
        self.label_7.raise_()
        self.label_tip.raise_()

        self.retranslateUi(dialog)
        self.closeWinBtn.clicked.connect(dialog.close)

        self.pushButton.clicked.connect(self.on_click)

        QtCore.QMetaObject.connectSlotsByName(dialog)

    def on_click(self, dialog):
        self.label_tip.setText('')
        if(self.spinBox_year1.value() > self.spinBox_year2.value()):
            self.label_tip.setText('年份有误')
            #self.label_tip.setText('')
        elif(self.spinBox_year1.value() == self.spinBox_year2.value() and self.spinBox_month1.value() > self.spinBox_month2.value()):
            self.label_tip.setText('月份有误')
            #self.label_tip.setText('')
        else:
            self.label_tip.setText('爬取中……')
            self.open_crawler(dialog)
        '''
        if (MovieCrawler(self.spinBox_year1.value(),self.spinBox_month1.value(), self.spinBox_year2.value(), self.spinBox_month2.value())  == 1):
            #self.label_tip.setText('')
            self.label_tip.setText('爬取成功!')
        '''

    def open_crawler(self, dialog):
        self.label_tip.setText('爬取中……')
        if (MovieCrawler(self.spinBox_year1.value(),self.spinBox_month1.value(), self.spinBox_year2.value(), self.spinBox_month2.value())  == 1):
            #self.label_tip.setText('')
            self.label_tip.setText('爬取成功!')

    def retranslateUi(self, dialog):
        _translate = QtCore.QCoreApplication.translate
        dialog.setWindowTitle(_translate("dialog", "爬虫功能"))
        self.closeWinBtn.setText(_translate("dialog", "返回上一级"))
        self.pushButton.setText(_translate("dialog", "开始爬取数据"))
        self.label.setText(_translate("dialog", "起始时间"))
        self.label_2.setText(_translate("dialog", "年"))
        self.label_4.setText(_translate("dialog", "年"))
        self.label_5.setText(_translate("dialog", "终止时间"))
        self.label_6.setText(_translate("dialog", "月"))
        self.label_7.setText(_translate("dialog", "月"))

import pictures
