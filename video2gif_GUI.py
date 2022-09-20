# https://wikidocs.net/21928

from cProfile import label
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from moviepy.editor import *
import argparse


class MyApp(QMainWindow):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        # Geometry
        self.setWindowTitle('Video2GIF')
        self.resize(400, 200)
        self.center()

        # self.bFileName = False

        # Load data button
        self.pushButton = QPushButton('Open File', self)
        self.pushButton.move(290, 35)
        self.pushButton.clicked.connect(self.pushButtonClicked)

        # statusbar (status bar)
        self.statusbar = QStatusBar(self)          # QStatusBar 객체 생성
        self.setStatusBar(self.statusbar)          # 위젯 배치
        self.statusbar.showMessage("READY")

        # Label
        self.label = QLabel(
            " "*75, self)
        self.label.setStyleSheet(
            "border: 1px;" "border-color: #727272;" "border-style: solid;"  "background-color: white;")
        self.label.adjustSize()
        self.label.move(10, 40)

        # Label (Loading icon)
        #self.loadingLabel = QLabel("For Loading")
        # adding label to status bar
        # self.statusBar().addPermanentWidget(self.loadingLabel)

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def startAnimation(self):
        self.movie.start()

    def stopAnimation(self):
        self.movie.stop()

    def pushButtonClicked(self):

        self.fileName = QFileDialog.getOpenFileName(
            self, "open file", "./",
            "mp4 file(*.mp4) ;; avi file(*.avi) ;; mov file(*.mov) ;; wmv file (*.wmv) ;; mpeg-ps file (*.mpeg) ;; mkv file (*.mkv)")

        if self.fileName[0]:

            self.label.setText(
                self.fileName[0])  # Show file location

            self.statusbar.showMessage("Converting...")  # Show status label

            QApplication.processEvents()

            # To show the loading icon
            #self.movie = QMovie("./assets/loader.gif")
            # self.loadingLabel.setMovie(self.movie)
            # self.startAnimation()
            QApplication.processEvents()

            fileExtension = self.fileName[1][self.fileName[1].find('.'):-1]
            print(fileExtension)
            inputName = self.fileName[0]
            QApplication.processEvents()

            outputName = inputName.replace(fileExtension, '')
            outputName = outputName + '.gif'
            print(outputName)
            QApplication.processEvents()

            videoClip = VideoFileClip(inputName)
            # Want to know video's number of frame
            frames = int(videoClip.fps * videoClip.duration)
            # print(frames)
            QApplication.processEvents()

            videoClip.write_gif(outputName)
            QApplication.processEvents()

            self.statusbar.setStyleSheet("color: red;")
            self.statusbar.showMessage("Converted!")

        else:
            self.label.setText("")

            self.statusbar.setStyleSheet("color: blue;")
            self.statusbar.showMessage("No file selected")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    # print(str(ex.label.isVisible()))
    ex.show()
    sys.exit(app.exec_())
