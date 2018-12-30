from PyQt5 import QtCore, QtGui, QtWidgets
import sys, os
from win32com.client import Dispatch, constants, gencache

class View(object):
    def setupUi(self, dialog):
        dialog.setObjectName("dialog")
        dialog.resize(679, 690)
        self.closeWinBtn = QtWidgets.QPushButton(dialog)
        self.closeWinBtn.setGeometry(QtCore.QRect(520, 630, 131, 31))
        self.closeWinBtn.setObjectName("closeWinBtn")
        self.label_picture = QtWidgets.QLabel(dialog)
        self.label_picture.setGeometry(QtCore.QRect(-20, -20, 721, 731))
        self.label_picture.setStyleSheet("image: url(:/new/back_logo.jpg);")
        self.label_picture.setText("")
        self.label_picture.setObjectName("label_picture")
        self.pushButton_Actor = QtWidgets.QPushButton(dialog)
        self.pushButton_Actor.setGeometry(QtCore.QRect(112, 427, 111, 41))
        self.pushButton_Actor.setObjectName("pushButton_Actor")
        self.CreatBaoBiao = QtWidgets.QPushButton(dialog)
        self.CreatBaoBiao.setGeometry(QtCore.QRect(270, 510, 121, 41))
        self.CreatBaoBiao.setObjectName("CreatBaoBiao")
        self.pushButton_TopMovie = QtWidgets.QPushButton(dialog)
        self.pushButton_TopMovie.setGeometry(QtCore.QRect(430, 427, 111, 41))
        self.pushButton_TopMovie.setObjectName("pushButton_TopMovie")
        self.pushButton_piaofang = QtWidgets.QPushButton(dialog)
        self.pushButton_piaofang.setGeometry(QtCore.QRect(112, 317, 111, 41))
        self.pushButton_piaofang.setObjectName("pushButton_piaofang")
        self.pushButton_line = QtWidgets.QPushButton(dialog)
        self.pushButton_line.setGeometry(QtCore.QRect(430, 317, 111, 41))
        self.pushButton_line.setObjectName("pushButton_line")
        self.label_tip = QtWidgets.QLabel(dialog)
        self.label_tip.setGeometry(QtCore.QRect(280, 560, 111, 21))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(11)
        self.label_tip.setFont(font)
        self.label_tip.setStyleSheet("color: rgb(255, 0, 0);")
        self.label_tip.setText("")
        self.label_tip.setObjectName("label_tip")
        self.label_picture.raise_()
        self.closeWinBtn.raise_()
        self.pushButton_Actor.raise_()
        self.CreatBaoBiao.raise_()
        self.pushButton_TopMovie.raise_()
        self.pushButton_piaofang.raise_()
        self.pushButton_line.raise_()
        self.label_tip.raise_()

        self.retranslateUi(dialog)

        self.pushButton_Actor.clicked.connect(dialog.close)
        self.pushButton_TopMovie.clicked.connect(dialog.close)
        self.pushButton_piaofang.clicked.connect(dialog.close)
        self.pushButton_line.clicked.connect(dialog.close)
        self.closeWinBtn.clicked.connect(dialog.close)
        
        QtCore.QMetaObject.connectSlotsByName(dialog)

        self.CreatBaoBiao.clicked.connect(self.Creat_report)

    def retranslateUi(self, dialog):
        _translate = QtCore.QCoreApplication.translate
        dialog.setWindowTitle(_translate("dialog", "可视化选择"))
        self.closeWinBtn.setText(_translate("dialog", "返回上一级"))
        self.pushButton_Actor.setText(_translate("dialog", "劳模演员"))
        self.CreatBaoBiao.setText(_translate("dialog", "生成数据报表"))
        self.pushButton_TopMovie.setText(_translate("dialog", "TOP电影"))
        self.pushButton_piaofang.setText(_translate("dialog", "票房份额"))
        self.pushButton_line.setText(_translate("dialog", "票房趋势"))
 
    def Creat_report(self, dialog):
        #print(len(sys.argv))
        if (len(sys.argv) == 2):
            input = sys.argv[1]
            output = os.path.splitext(input)[0]+'.pdf'
        elif (len(sys.argv) == 3):
            input = sys.argv[1]
            output = sys.argv[2]
        else:
            desktop = os.path.join(os.path.expanduser("~"), 'Desktop')
            desktop_path = desktop + './report.pdf'
            input = u'report.docx'#word文档的名称
            output = desktop_path #pdf文档的名称
            self.label_tip.setText('生成报表成功!')
        if (not os.path.isabs(input)):
            input = os.path.abspath(input)
        if (not os.path.isabs(output)):
            output = os.path.abspath(output)
        try:
            GenerateSupport()
            rc = doc2pdf(input, output)
            print('Creat report Successfully!')
            os.remove("report.docx")
        except:
            print('Creat report Fail!')

def doc2pdf(input, output):
    w = Dispatch("Word.Application")
    try:
        doc = w.Documents.Open(input, ReadOnly = 1)
        doc.ExportAsFixedFormat(output, constants.wdExportFormatPDF,\
            Item = constants.wdExportDocumentWithMarkup, CreateBookmarks = constants.wdExportCreateHeadingBookmarks)
        return 0
    except:
        return 1
    finally:
        w.Quit(constants.wdDoNotSaveChanges)

# 解决老版本word转化问题
def GenerateSupport():
    gencache.EnsureModule('{00020905-0000-0000-C000-000000000046}', 0, 8, 4)

import pictures
