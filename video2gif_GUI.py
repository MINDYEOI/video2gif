# https://wikidocs.net/21928

from cProfile import label
import sys
import numpy as np
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
        self.labels = []

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

        self.fileNames = QFileDialog.getOpenFileNames(
            self, "open file", "./",
            "mp4 file(*.mp4) ;; avi file(*.avi) ;; mov file(*.mov) ;; wmv file (*.wmv) ;; mpeg-ps file (*.mpeg) ;; mkv file (*.mkv)")

        if self.fileNames[0]:
            
            files = self.fileNames[0]
            
            for i in range(len(files)):
                label = QLabel(
                    " "*75, self)
                label.setStyleSheet(
                    "border: 1px;" "border-color: #727272;" "border-style: solid;"  "background-color: white;")
                label.adjustSize()
                label.move(10, 40 * i)
                self.labels.append(label)
                
                self.labels[i].setText(
                    files[i])  # Show file location

            self.statusbar.showMessage("Converting...")  # Show status label

            QApplication.processEvents()

            # To show the loading icon
            #self.movie = QMovie("./assets/loader.gif")
            # self.loadingLabel.setMovie(self.movie)
            # self.startAnimation()
            QApplication.processEvents()

            fileExtension = self.fileNames[1][self.fileNames[1].find('.'):-1]
            print(fileExtension)
            
            for i, file in enumerate(files):
                

                outputName = file.replace(file[file.find('.'):], '')
                outputName = outputName + '.gif'
                print(outputName)
                QApplication.processEvents()

                clip = VideoFileClip(file)
            # # Want to know video's number of frame
            # frames = int(clip.fps * clip.duration)
            # print(frames)
                QApplication.processEvents()

                resized_clip = clip.resize(0.8)

                if i+1 == len(files):
                    self.statusbar.setStyleSheet("color: red;")
                    self.statusbar.showMessage("Done!")
                    QApplication.processEvents()

                
                else:
                    self.statusbar.setStyleSheet("color: red;")
                    self.statusbar.showMessage("%d/%d Converted!" %(i+1, len(files)))
                    QApplication.processEvents()

                    
                resized_clip.write_gif(outputName, fps=20, fuzz=1, opt='nq', program='ffmpeg')
                QApplication.processEvents()



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
