# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import pymysql
from PyQt5.QtWidgets import *
from datetime import datetime
from datetime import timedelta
class Ui_MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(QtWidgets.QMainWindow,self).__init__()
        self.setupUi(self)
        self.retranslateUi(self)

        self.textBrowser_tendays.setText(print_thing_tendays())
        self.textBrowser_today.setText(print_thing_today())
        self.textBrowser_tomorrow.setText(print_thing_tomorrow())

    def findit(self):
        if self.lineEdit.textChanged and self.lineEdit_2.textChanged and self.lineEdit_3.textChanged:
            str1 = self.lineEdit.text()
            str2 = self.lineEdit_2.text()
            str3 = self.lineEdit_3.text()
            p = add_thing(str1, str2, str3)

            if p==1:
                self.showsdialog()
                self.lineEdit.clear()
                self.lineEdit_2.clear()
                self.lineEdit_3.clear()
            elif p==0:
                self.showfdialog()
                self.lineEdit.clear()
                self.lineEdit_2.clear()
                self.lineEdit_3.clear()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(640, 480)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.textBrowser_today = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_today.setGeometry(QtCore.QRect(0, 20, 641, 41))
        self.textBrowser_today.setObjectName("textBrowser_today")
        self.label_today = QtWidgets.QLabel(self.centralwidget)
        self.label_today.setGeometry(QtCore.QRect(0, 0, 111, 16))
        self.label_today.setObjectName("label_today")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(440, 370, 177, 29))
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.pushButton.setMouseTracking(False)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("333.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setCheckable(False)
        self.pushButton.setAutoDefault(False)
        self.pushButton.setDefault(False)
        self.pushButton.setFlat(False)
        self.pushButton.setObjectName("pushButton")
        self.label_tomorrow = QtWidgets.QLabel(self.centralwidget)
        self.label_tomorrow.setGeometry(QtCore.QRect(0, 60, 111, 16))
        self.label_tomorrow.setObjectName("label_tomorrow")
        self.textBrowser_tomorrow = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_tomorrow.setGeometry(QtCore.QRect(0, 80, 641, 51))
        self.textBrowser_tomorrow.setObjectName("textBrowser_tomorrow")
        self.label_tendays = QtWidgets.QLabel(self.centralwidget)
        self.label_tendays.setGeometry(QtCore.QRect(0, 140, 111, 16))
        self.label_tendays.setObjectName("label_tendays")
        self.textBrowser_tendays = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_tendays.setGeometry(QtCore.QRect(0, 160, 641, 101))
        self.textBrowser_tendays.setObjectName("textBrowser_tendays")
        self.layoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget_2.setGeometry(QtCore.QRect(0, 330, 623, 23))
        self.layoutWidget_2.setObjectName("layoutWidget_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget_2)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.lineEdit = QtWidgets.QLineEdit(self.layoutWidget_2)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout.addWidget(self.lineEdit)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.layoutWidget_2)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.horizontalLayout.addWidget(self.lineEdit_2)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.layoutWidget_2)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.horizontalLayout.addWidget(self.lineEdit_3)
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(1, 300, 657, 22))
        self.widget.setObjectName("widget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        spacerItem2 = QtWidgets.QSpacerItem(180, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        spacerItem3 = QtWidgets.QSpacerItem(168, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem3)
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_2.addWidget(self.label_3)
        spacerItem4 = QtWidgets.QSpacerItem(158, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem4)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.pushButton.clicked.connect(self.findit)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "^_^备忘录^_^"))
        self.textBrowser_today.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:600; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-weight:400;\"><br /></p></body></html>"))
        self.label_today.setText(_translate("MainWindow", "今日待办事件："))
        self.pushButton.setText(_translate("MainWindow", "添加"))
        self.pushButton.setShortcut(_translate("MainWindow", "Ctrl+R"))
        self.label_tomorrow.setText(_translate("MainWindow", "明日待办事件："))
        self.textBrowser_tomorrow.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:600; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-weight:400;\"><br /></p></body></html>"))
        self.label_tendays.setText(_translate("MainWindow", "十天内待办事件："))
        self.textBrowser_tendays.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:600; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-weight:400;\"><br /></p></body></html>"))
        self.label.setText(_translate("MainWindow", "日期"))
        self.label_2.setText(_translate("MainWindow", "地点"))
        self.label_3.setText(_translate("MainWindow", "事件"))

    def showsdialog(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setWindowTitle("MessageBox demo")
        msg.setText("数据添加成功！")

        msg.exec()

    def showfdialog(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setWindowTitle("MessageBox demo")
        msg.setText("数据添加失败")

        msg.exec()

def print_thing_today():
    list=[]
    db=pymysql.connect(host='localhost',user='root',password='*****',db='mydatabase',charset='gbk')
    today=datetime.today().date()
    taday=str(today)
    # SQL ��ѯ���
    cursor=db.cursor()
    sql = "SELECT * FROM information WHERE date = '%s'" % (today)
    try:
        # ִ��SQL���
        t=cursor.execute(sql)
        results = cursor.fetchall()

        if t==0:
            list.append('今天没有待办事件.....')
        else:
            for row in results:
                fname = row[0]
                lname = row[1]
                age = row[2]
                list.append("%s,%s,%s" % (fname, lname, age))
    except:
        print("Error: unable to fecth data")
    st='\n'.join(list)
    return st
def print_thing_tomorrow():
    list=[]
    db=pymysql.connect(host='localhost',user='root',password='****',db='mydatabase',charset='gbk')
    a=timedelta(days=1)
    today=datetime.today().date()
    tomorrow=today+a
    cursor=db.cursor()
    tomorrow=str(tomorrow)

    sqll="select * from information where date='%s'"%(tomorrow)
    try:
        # ִ��SQL���
        t=cursor.execute(sqll)
        results = cursor.fetchall()

        if t==0:
            list.append('明天没有待办事件')
        else:
            for row in results:
                fname = row[0]
                lname = row[1]
                age = row[2]

                list.append("{},{},{}".format(fname, lname, age))
    except:
        print("Error: unable to fecth data")
    st='\n'.join(list)

    return st
def print_thing_tendays():
    list = []
    db = pymysql.connect(host='localhost', user='root', password='**', db='mydatabase', charset='gbk')
    a = timedelta(days=1)
    today = datetime.today().date()
    tomorrow = today + a
    cursor = db.cursor()
    tomorrow = str(tomorrow)
    b=timedelta(days=10)
    ddate=today+b
    ddate=str(ddate)
    sql="select * from information  where date<'%s'and date >'%s'"%(ddate,tomorrow)
    try:
        t=cursor.execute(sql)
        results=cursor.fetchall()
        if t==0:
            list.append('十天内没有待办事件。。。。')
        else:
            for it in results:
                date=it[0]
                address=it[1]
                thing=it[2]
                list.append("{},{},{}".format(date,address,thing))
    except:
        print("Error: unable to fectch data")
    db.close()
    st='\n'.join(list)
    return st
def add_thing(date,address,thing):
    db = pymysql.connect(host='localhost', user='root', password='***', db='mydatabase', charset='gbk')
    cursor = db.cursor()
    try:
        pp=cursor.execute('insert into information (date, address,thing) values (%s, %s,%s)',[date, address,thing])
        db.commit()
    except:
        pp=0
    db.close()

    return pp


if  __name__=='__main__':
    app=QApplication(sys.argv)
    window=Ui_MainWindow()
    window.show()
    sys.exit(app.exec_())
