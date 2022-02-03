import pafy
import shutil
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, main_window):
        main_window.setObjectName("MainWindow")
        main_window.resize(662, 291)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Barbaris.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(main_window)
        self.centralwidget.setObjectName("centralwidget")
        self.yt_link_textbox = QtWidgets.QLineEdit(self.centralwidget)
        self.yt_link_textbox.setGeometry(QtCore.QRect(20, 60, 621, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.yt_link_textbox.setFont(font)
        self.yt_link_textbox.setObjectName("yt_link_textbox")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 10, 181, 51))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.save_path_textbox = QtWidgets.QLineEdit(self.centralwidget)
        self.save_path_textbox.setGeometry(QtCore.QRect(20, 150, 621, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.save_path_textbox.setFont(font)
        self.save_path_textbox.setObjectName("save_path_textbox")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 100, 221, 51))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(20, 210, 171, 61))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.status_textbox = QtWidgets.QLabel(self.centralwidget)
        self.status_textbox.setGeometry(QtCore.QRect(200, 210, 221, 51))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.status_textbox.setFont(font)
        self.status_textbox.setText("")
        self.status_textbox.setObjectName("status_textbox")
        main_window.setCentralWidget(self.centralwidget)

        self.pushButton.clicked.connect(self.downloading)

        self.retranslateUi(main_window)
        QtCore.QMetaObject.connectSlotsByName(main_window)

    def retranslateUi(self, main_window):
        _translate = QtCore.QCoreApplication.translate
        main_window.setWindowTitle(_translate("MainWindow", "Barbaris YT Video Downloader"))
        self.label.setText(_translate("MainWindow", "YT Video Link:"))
        self.label_2.setText(_translate("MainWindow", "Saving on PC path:"))
        self.pushButton.setText(_translate("MainWindow", "Download"))

    def downloading(self):
        self.status_textbox.setText("")
        url = self.yt_link_textbox.text()
        video = pafy.new(url)

        best_resolution = video.getbest()
        print(best_resolution.resolution, best_resolution.extension)

        name = video.title
        ext = best_resolution.extension
        best_resolution.download()

        shutil.move(name + "." + ext, self.save_path_textbox.text())
        self.status_textbox.setText("Downloaded")


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
