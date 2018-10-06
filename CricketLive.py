# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'CricketLive.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
from LiveScore import Ui_liveScoreDisplay
import urllib.request
from bs4 import BeautifulSoup
import threading
import sys
import time

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_mainWindow(object):


    def setupUi(self, mainWindow):
        mainWindow.setObjectName(_fromUtf8("mainWindow"))
        mainWindow.resize(209, 162)
        self.centralwidget = QtGui.QWidget(mainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))

        self.team1 = QtGui.QLabel(self.centralwidget)
        self.team1.setGeometry(QtCore.QRect(0, 20, 91, 20))
        self.team1.setObjectName(_fromUtf8("team1"))

        self.team2 = QtGui.QLabel(self.centralwidget)
        self.team2.setGeometry(QtCore.QRect(20, 60, 41, 20))
        self.team2.setObjectName(_fromUtf8("team2"))

        self.comboBox = QtGui.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(110, 20, 85, 21))
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        self.comboBox.addItem('india')
        self.comboBox.addItem('pakistan')
        self.comboBox.addItem('bangladesh')
        self.comboBox.addItem('australia')
        self.comboBox.addItem('sri-lanka')
        self.comboBox.addItem('england')
        self.comboBox.addItem('windies')
        self.comboBox.addItem('south-africa')
        self.comboBox.addItem('zimbabwe')
        self.comboBox.addItem('new-zealand')
        self.comboBox.addItem('ireland')
        self.comboBox.addItem('afghanistan')
        #self.comboBox.activated[str].connect(self.getLiveScore)

        self.comboBox_2 = QtGui.QComboBox(self.centralwidget)
        self.comboBox_2.setGeometry(QtCore.QRect(110, 60, 85, 21))
        self.comboBox_2.setObjectName(_fromUtf8("comboBox_2"))
        self.comboBox_2.addItem('india')
        self.comboBox_2.addItem('pakistan')
        self.comboBox_2.addItem('bangladesh')
        self.comboBox_2.addItem('australia')
        self.comboBox_2.addItem('sri-lanka')
        self.comboBox_2.addItem('england')
        self.comboBox_2.addItem('windies')
        self.comboBox_2.addItem('south-africa')
        self.comboBox_2.addItem('zimbabwe')
        self.comboBox_2.addItem('new-zealand')
        self.comboBox_2.addItem('ireland')
        self.comboBox_2.addItem('afghanistan')
        #self.comboBox_2.activated[str].connect(self.getLiveScore)


        self.getScore = QtGui.QPushButton(self.centralwidget)
        self.getScore.setGeometry(QtCore.QRect(60, 90, 75, 23))
        self.getScore.setObjectName(_fromUtf8("getScore"))
        self.getScore.clicked.connect(mainWindow.close)
        self.getScore.clicked.connect(self.viewScore)



        mainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(mainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 209, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        mainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(mainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        mainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(mainWindow)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)


    def retranslateUi(self, mainWindow):
        mainWindow.setWindowTitle(_translate("mainWindow", "Cricket Live", None))
        self.team1.setText(_translate("mainWindow", "       Team 1", None))
        self.team2.setText(_translate("mainWindow", "Team 2", None))
        self.getScore.setText(_translate("mainWindow", "Get Live Score!", None))

    def viewScore(self):
        self.window = QtGui.QMainWindow()
        self.ui = Ui_liveScoreDisplay()
        self.window.show()
        while True:
            liveScore=self.getLiveScore()
            self.ui.setupUi(self.window, liveScore)
            time.sleep(1.0)




    def getLiveScore(self):
        while True:
            team1 = self.comboBox.currentText()
            team2 = self.comboBox_2.currentText()
            team_code = {'india':2, 'pakistan':3, 'bangladesh':6, 'australia':4, 'south-africa':11,
                     'sri-lanka':5, 'zimbabwe':12, 'new-zealand':13, 'afghanistan':96, 'ireland':27,
                     'england':9, 'windies':10}
            url = 'https://www.cricbuzz.com//cricket-team//'+ team1 + '//' + str(team_code[team1])
            html = urllib.request.urlopen(url).read()

            soup = BeautifulSoup(html, features='html5lib')

            element = soup.find('div', {"id": 'scag_live'})
            a_tag = element.find_all('a')
            match_url = "https://www.cricbuzz.com"+a_tag[0]['href']

            match_html = urllib.request.urlopen(match_url).read()

            match_soup = BeautifulSoup(match_html, features="html5lib")
            score = match_soup.find_all('div', class_='cb-col-100 cb-col cb-col-scores')
            if len(score)==0:
                liveScore =  "Match has ended "
            else:
                for score in score:
                    liveScore = score.text
            time.sleep(1.0)
            return liveScore







if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    mainWindow = QtGui.QMainWindow()
    ui = Ui_mainWindow()
    ui.setupUi(mainWindow)
    mainWindow.show()
    sys.exit(app.exec_())

