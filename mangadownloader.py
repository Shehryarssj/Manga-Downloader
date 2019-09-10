# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'manga.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from requests import get
from PyQt5.QtCore import QThread, pyqtSignal
import bs4
import os

global stopit
stopit = False

class MyThread(QThread):

    StatusLabelText = pyqtSignal(str)
    progressvalue = pyqtSignal(int)
    def GetImageLinks(self, link):
        re = get(link)
        imagesoup = bs4.BeautifulSoup(re.text, features='lxml').select('#vungdoc img')
        imglinks = []
        for x in imagesoup:
            imglinks.append(x.get('src'))
        self.downloader(imglinks)

    def run(self):
        self.StatusLabelText.emit("Status: Starting")
        for each in soup.select('.row span a'):
            if each.get('title') == ui.GetCurrentComboBoxText():
                self.GetImageLinks(each.get('href'))

    def MainFolderMaker(self):
        numanganame = ui.GetCurrentComboBoxText().split('Chapter')[0]
        if ':' in numanganame:
            manganame = numanganame.replace(":", "-")
        else:
            manganame = numanganame
        global path
        path = os.getcwd() + "\\Manga Downloader\\"+ manganame.strip()
        if os.path.exists(path) == False:
            os.makedirs(path)

    def ChapterFolderMaker(self):
        Chapter = ui.GetCurrentComboBoxText().split('Chapter')[1].strip('?')
        if ':' in Chapter:
            global ChapterNumber
            ChapterNumber = "Chapter " + Chapter.replace(":", "-")
        else:
            ChapterNumber = "Chapter " + Chapter
        os.chdir(path)
        chapterpath = os.getcwd() + "\\" + ChapterNumber
        if os.path.exists(chapterpath) == False:
            os.makedirs(chapterpath)
        os.chdir(chapterpath)


    def downloader(self, links):
        self.progressvalue.emit(0)
        global stopit
        self.MainFolderMaker()
        self.ChapterFolderMaker()
        imgcount = 1
        self.StatusLabelText.emit("Status: Downloading...")
        eachpercentprogress = 100/len(links)
        progress = eachpercentprogress
        for y in links:
            if stopit == False:
                res = get(y)
            elif stopit == True:
                break

            with open(str(imgcount) +".jpg", 'wb') as img:
                for chunk in res.iter_content(1000):
                    img.write(chunk)
            self.progressvalue.emit(progress)
            progress += eachpercentprogress
            imgcount+=1
        if stopit != True:
            if progress != 100:
                self.progressvalue.emit(100)
            self.StatusLabelText.emit("Status: Done")
        else:
            self.StatusLabelText.emit("Status: Cancelled!")
            stopit = False
        os.chdir('..\\')
        os.chdir('..\\')
        os.chdir('..\\')


class Ui_Window(object):
    def setupUi(self, Window):
        Window.setObjectName("Window")
        Window.resize(869, 726)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        Window.setFont(font)
        self.centralwidget = QtWidgets.QWidget(Window)
        self.centralwidget.setObjectName("centralwidget")
        self.UrlLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.UrlLineEdit.setGeometry(QtCore.QRect(60, 70, 701, 31))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.UrlLineEdit.setFont(font)
        self.UrlLineEdit.setClearButtonEnabled(True)
        self.UrlLineEdit.setObjectName("UrlLineEdit")
        self.UrlLabel = QtWidgets.QLabel(self.centralwidget)
        self.UrlLabel.setGeometry(QtCore.QRect(10, 70, 41, 31))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.UrlLabel.setFont(font)
        self.UrlLabel.setObjectName("UrlLabel")
        self.GoPushButton = QtWidgets.QPushButton(self.centralwidget)
        self.GoPushButton.setGeometry(QtCore.QRect(760, 70, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.GoPushButton.setFont(font)
        self.GoPushButton.setObjectName("GoPushButton")
        self.Step1Label = QtWidgets.QLabel(self.centralwidget)
        self.Step1Label.setGeometry(QtCore.QRect(10, 20, 341, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Step1Label.setFont(font)
        self.Step1Label.setObjectName("Step1Label")
        self.Step2Label = QtWidgets.QLabel(self.centralwidget)
        self.Step2Label.setGeometry(QtCore.QRect(10, 170, 201, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Step2Label.setFont(font)
        self.Step2Label.setObjectName("Step2Label")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(50, 220, 651, 41))
        self.comboBox.setEditable(True)
        self.comboBox.setObjectName("comboBox")
        self.InfoLabel = QtWidgets.QLabel(self.centralwidget)
        self.InfoLabel.setGeometry(QtCore.QRect(10, 640, 781, 51))
        self.InfoLabel.setObjectName("InfoLabel")
        self.StatusLabel = QtWidgets.QLabel(self.centralwidget)
        self.StatusLabel.setGeometry(QtCore.QRect(610, 480, 150, 150))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.StatusLabel.setFont(font)
        self.StatusLabel.setObjectName("StatusLabel")
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(200, 520, 331, 31))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.StatusInfoLabel = QtWidgets.QLabel(self.centralwidget)
        self.StatusInfoLabel.setGeometry(QtCore.QRect(680, 500, 181, 121))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.StatusInfoLabel.setFont(font)
        self.StatusInfoLabel.setText("")
        self.StatusInfoLabel.setObjectName("StatusInfoLabel")
        font = QtGui.QFont()
        font.setPointSize(12)
        self.DownloadPushButton = QtWidgets.QPushButton(self.centralwidget)
        self.DownloadPushButton.setGeometry(QtCore.QRect(280, 420, 161, 41))
        self.DownloadPushButton.setObjectName("DownloadPushButton")
        self.StopPushButton = QtWidgets.QPushButton(self.centralwidget)
        self.StopPushButton.setGeometry(QtCore.QRect(20, 520, 101, 31))
        self.StopPushButton.setObjectName("StopPushButton")
        self.Step3Label = QtWidgets.QLabel(self.centralwidget)
        self.Step3Label.setGeometry(QtCore.QRect(20, 350, 201, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Step3Label.setFont(font)
        self.Step3Label.setObjectName("Step3Label")
        Window.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Window)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 869, 21))
        self.menubar.setObjectName("menubar")
        Window.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Window)
        self.statusbar.setObjectName("statusbar")
        Window.setStatusBar(self.statusbar)

        self.retranslateUi(Window)
        QtCore.QMetaObject.connectSlotsByName(Window)

        self.GoPushButton.clicked.connect(self.Checker)

        self.DownloadPushButton.clicked.connect(self.StartThread)

        self.StopPushButton.clicked.connect(self.stopper)

    def retranslateUi(self, Window):
        _translate = QtCore.QCoreApplication.translate
        Window.setWindowTitle(_translate("Window", "MainWindow"))
        self.UrlLineEdit.setPlaceholderText(_translate("Window", "eg,   https://manganelo.com/manga/boruto_naruto_next_generations"))
        self.UrlLabel.setText(_translate("Window", "URL"))
        self.GoPushButton.setText(_translate("Window", "Go"))
        self.Step1Label.setText(_translate("Window", "Step1: Enter Url to the main manga page"))
        self.Step2Label.setText(_translate("Window", "Step2: Choose Chapter"))
        #self.comboBox.setItemText(0, _translate("Window", "Indivial Chapter"))
        self.InfoLabel.setText(_translate("Window", "Info: This app downloads manga only from www.manganelo.com. This app downloads manga to the same folder where this app is located. "))
        self.StatusLabel.setText(_translate("Window", ""))
        self.DownloadPushButton.setText(_translate("Window", "Download"))
        self.StopPushButton.setText(_translate("Window", "Cancel"))
        self.Step3Label.setText(_translate("Window", "Step3: Download"))

    def GetUrl(self):
        return self.UrlLineEdit.text().strip()

    def Checker(self):
        try:
            r = get(self.GetUrl())
            soup = bs4.BeautifulSoup(r.text, features='lxml')
            chapters = soup.select('.row span a')
            if chapters == []:
                raise Exception
            if self.comboBox.currentText() != "":
                self.comboBox.clear()
            self.GetTotalChapters()

        except Exception as a:
            msg = QtWidgets.QMessageBox()
            msg.setWindowTitle("Error!")
            msg.setText('Enter a Valid URL')
            x = msg.exec_()

    def GetTotalChapters(self):
        r = get(self.GetUrl())
        global soup
        soup = bs4.BeautifulSoup(r.text, features='lxml')
        listofchaptertags = soup.select('.row span a')
        for each in listofchaptertags:
            self.comboBox.addItem(each.get('title'))

    def StartThread(self):
        if ui.GetCurrentComboBoxText() != "":
            self.thread = MyThread()
            self.thread.StatusLabelText.connect(self.StatusLabelTextSetter)
            self.thread.progressvalue.connect(self.progresser)
            self.thread.start()

    def StatusLabelTextSetter(self, text):
        self.StatusLabel.setText(text)

    def GetCurrentComboBoxText(self):
        return self.comboBox.currentText()

    def progresser(self, val):
        self.progressBar.setValue(val)

    def stopper(self):
        global stopit
        stopit = True
        self.StatusLabel.setText("Stopping...")

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Window = QtWidgets.QMainWindow()
    ui = Ui_Window()
    ui.setupUi(Window)
    Window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Window = QtWidgets.QMainWindow()
    ui = Ui_Window()
    ui.setupUi(Window)
    Window.show()
    sys.exit(app.exec_())
