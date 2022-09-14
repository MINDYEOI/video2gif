# https://wikidocs.net/21928

from cProfile import label
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon
from moviepy.editor import *
import argparse


class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        # Geometry
        self.setWindowTitle('Video2GIF')
        # self.setWindowIcon(QIcon('./assets/logo.png'))
        self.setGeometry(300, 300, 300, 200)

        # self.bFileName = False

        # Load data button
        # ref) https://newbie-developer.tistory.com/122, https://dotsnlines.tistory.com/501
        self.pushButton = QPushButton('Open File')
        self.pushButton.clicked.connect(self.pushButtonClicked)

        self.label = QLabel()

        layout = QVBoxLayout()
        layout.addWidget(self.pushButton)
        layout.addWidget(self.label)

        self.setLayout(layout)

    def pushButtonClicked(self):

        self.fileName = QFileDialog.getOpenFileName(
            self, "open file", "./", "mp4 file(*.mp4) ;; avi file(*.avi)")

        if self.fileName[0]:
            self.label.setText("Converting...")
            # self.label.repaint()
            QApplication.processEvents()
            inputName = self.fileName[0]
            QApplication.processEvents()
            outputName = inputName[:-4] + '.gif'
            QApplication.processEvents()
            # print(inputName)
            # print(outputName)
            videoClip = VideoFileClip(inputName)
            QApplication.processEvents()
            videoClip.write_gif(outputName)
            QApplication.processEvents()
            # self.label.setText(" ")
            self.label.setText("Converted!")

        else:
            self.label.setText("No file selected")

    # def convert(self, inputName):
    #     #inputName = self.fileName[0]
    #     outputName = inputName[:-4] + '.gif'
    #     print(inputName)
    #     print(outputName)
    #     videoClip = VideoFileClip(inputName)
    #     videoClip.write_gif(outputName)
    #     self.label.setText(" ")
    #     self.convertedLabel.setText("Converted!")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    # print(str(ex.label.isVisible()))
    ex.show()
    sys.exit(app.exec_())
