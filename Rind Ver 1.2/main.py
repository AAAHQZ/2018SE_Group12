import sys
import os
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui, QtWidgets
<<<<<<< HEAD
from big import Big
from line import Line
from top_actor import TopActor
from top_movie import TopMovie
from view import View
from login import Login
from search import Search
from choice import Choice
from sign import sign_up,log_in
from crawler import Crawler

=======
from SE12_GUI import *
>>>>>>> Huangquanzhe

'''class MyMainWindow(QMainWindow, Ui_MainWindow):
	def __init__(self, parent = None):
		super(MyMainWindow, self).__init__(parent)
		self.setupUi(self)'''
# 游客标志
Travel_tip = 0

class View(QDialog,View):
	def __init__(self, parent = None):
		super(View, self).__init__(parent)
		self.setupUi(self)

class Line(QDialog,Line):
	def __init__(self, parent = None):
		super(Line, self).__init__(parent)
		self.setupUi(self)

class Crawler(QDialog,Crawler):
	def __init__(self, parent = None):
		super(Crawler, self).__init__(parent)
		self.setupUi(self)

class TopMovie(QDialog,TopMovie):
	def __init__(self, parent = None):
		super(TopMovie, self).__init__(parent)
		self.setupUi(self)

class Big(QDialog,Big):
	def __init__(self, parent = None):
		super(Big, self).__init__(parent)
		self.setupUi(self)

class Login(QDialog,Login):
	def __init__(self, parent = None):
		super(Login, self).__init__(parent)
		self.setupUi(self)

class TopActor(QDialog,TopActor):
	def __init__(self, parent = None):
		super(TopActor, self).__init__(parent)
		self.setupUi(self)

class Search(QDialog,Search):
	def __init__(self, parent = None):
		super(Search, self).__init__(parent)
		self.setupUi(self)

class Choice(QDialog,Choice):
	def __init__(self, parent = None):
		super(Choice, self).__init__(parent)
		self.setupUi(self)


def login_clicked():
	if log_in(login.lineEdit_login_account.text(),login.lineEdit_login_password.text())==0:
		global Travel_tip
		Travel_tip = 1
		choice.show()
		login.close()
	elif log_in(login.lineEdit_login_account.text(),login.lineEdit_login_password.text())==2:
		login.Tip_Login.setText("账号不存在")
	elif log_in(login.lineEdit_login_account.text(),login.lineEdit_login_password.text())==1:
		login.Tip_Login.setText("密码错误")

def sign_clicked():
	if sign_up(login.lineEdit_sign_account.text(),login.lineEdit_sign_password.text())==0:
		login.Tip_Signup.setText("账号已存在")
	elif sign_up(login.lineEdit_sign_account.text(),login.lineEdit_sign_password.text())==3:
		login.Tip_Signup.setText("账号不能为空")
	elif sign_up(login.lineEdit_sign_account.text(),login.lineEdit_sign_password.text())==2:
		login.Tip_Signup.setText("密码不能为空")

	else:
		login.Tip_Signup.setText("注册成功")

def view_clicked():
	if(Travel_tip == 0):
		choice.label_text2.setText("请登录后再使用本功能")
		choice.label_text1.setText("")
	else:
		view.show()
		choice.close()

def crawler_clicked():
	if(Travel_tip == 0):
		choice.label_text1.setText("请登录后再使用本功能")
		choice.label_text2.setText("")
	else:
		crawler.show()
		choice.close()
	
def logout():
	login.show()
	global Travel_tip
	Travel_tip = 0
	choice.label_text1.setText("")
	choice.label_text2.setText("")
	choice.close()

def view_close_click():
	view.label_tip.setText('')
	choice.show()

def crawler_close_click():
	crawler.label_tip.setText('')
	choice.show()

if __name__ == "__main__":
	try:
		os.remove('report.docx')
	except Exception:
		print('file do not exist')
	else:
		print('file has been removed')
	app = QApplication(sys.argv)
	view=  View()
	line= Line()
	top_movie=TopMovie()
	crawler = Crawler()
	big=Big()
	top_actor=TopActor()
	login=Login()
	search=Search()
	choice=Choice()
	login.show()


	login.pushButton_login.clicked.connect(login_clicked)
	login.pushButton_sign.clicked.connect(sign_clicked)
		#else :

	login.pushButton_traveller.clicked.connect(choice.show)


	choice.pushButton_search.clicked.connect(search.show)
	choice.pushButton_crawler.clicked.connect(crawler_clicked)
	choice.pushButton_view.clicked.connect(view_clicked)
	choice.pushButton.clicked.connect(logout)
	
	view.closeWinBtn.clicked.connect(view_close_click)
	search.closeWinBtn.clicked.connect(choice.show)
	crawler.closeWinBtn.clicked.connect(crawler_close_click)

	view.pushButton_Actor.clicked.connect(top_actor.show)
	view.pushButton_TopMovie.clicked.connect(top_movie.show)
	view.pushButton_piaofang.clicked.connect(big.show)
	view.pushButton_line.clicked.connect(line.show)

    
	line.closeWinBtn.clicked.connect(view.show)
	top_actor.closeWinBtn.clicked.connect(view.show)
	big.closeWinBtn.clicked.connect(view.show)
	top_movie.closeWinBtn.clicked.connect(view.show)

	sys.exit(app.exec_())