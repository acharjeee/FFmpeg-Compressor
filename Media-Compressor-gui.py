#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2021 arijit <arijit@linux-inspiron-5567>
#
# Distributed under terms of the MIT license.

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QProcess


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedWidth(1021)
        MainWindow.setFixedHeight(771)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.bgwidget = QtWidgets.QWidget(self.centralwidget)
        self.bgwidget.setGeometry(QtCore.QRect(0, 0, 1021, 771))
        self.bgwidget.setStyleSheet("#bgwidget{\n"
"background-color: qlineargradient(spread:pad, x1:0.253, y1:0.329545, x2:1, y2:1, stop:0 rgba(241, 63, 0, 255), stop:1 rgba(255, 255, 255, 255));}")
        self.bgwidget.setObjectName("bgwidget")
        self.p = None
        self.label = QtWidgets.QLabel(self.bgwidget)
        self.label.setGeometry(QtCore.QRect(290, 10, 391, 71))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(26)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.label.setFont(font)
        self.label.setStyleSheet("color: white")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.bgwidget)
        self.label_2.setGeometry(QtCore.QRect(270, 90, 441, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        font.setItalic(False)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: #FFFFFF")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.lineEdit = QtWidgets.QLineEdit(self.bgwidget)
        self.lineEdit.setGeometry(QtCore.QRect(20, 230, 471, 61))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setBold(False)
        font.setWeight(50)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.lineEdit.setFont(font)
        self.lineEdit.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lineEdit.setAutoFillBackground(False)
        self.lineEdit.setStyleSheet("border-radius: 10px;\n"
"background-color: rgb(186, 189, 182);\n"
"color: rgb(216, 73, 22);")
        self.lineEdit.setInputMask("")
        self.lineEdit.setText("")
        self.lineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit.setReadOnly(False)
        self.lineEdit.setCursorMoveStyle(QtCore.Qt.VisualMoveStyle)
        self.lineEdit.setClearButtonEnabled(True)
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QtWidgets.QPushButton(self.bgwidget)
        self.pushButton.setGeometry(QtCore.QRect(400, 330, 191, 61))
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pushButton.setStyleSheet("border-radius: 20px;\n"
"background-color: rgb(170, 255, 255);")
        self.pushButton.setAutoRepeat(True)
        self.pushButton.setFlat(True)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.on_click)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.bgwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(510, 230, 491, 61))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setBold(False)
        font.setWeight(50)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lineEdit_2.setAutoFillBackground(False)
        self.lineEdit_2.setStyleSheet("border-radius: 10px;\n"
"background-color: rgb(186, 189, 182);\n"
"color: rgb(216, 73, 22);")
        self.lineEdit_2.setInputMask("")
        self.lineEdit_2.setText("")
        self.lineEdit_2.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_2.setReadOnly(False)
        self.lineEdit_2.setCursorMoveStyle(QtCore.Qt.VisualMoveStyle)
        self.lineEdit_2.setClearButtonEnabled(True)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_3 = QtWidgets.QLabel(self.bgwidget)
        self.label_3.setGeometry(QtCore.QRect(180, 160, 641, 41))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_3.setFont(font)
        self.label_3.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_3.setStyleSheet("color: #00ffff;")
        self.label_3.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.bgwidget)
        self.plainTextEdit.setGeometry(QtCore.QRect(20, 420, 981, 331))
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.plainTextEdit.setFont(font)
        self.plainTextEdit.setStyleSheet("background-color: rgb(186, 189, 182);\n"
"border-radius: 15px;\n"
"color: rgb(216, 73, 22);")
        self.plainTextEdit.setFrameShadow(QtWidgets.QFrame.Plain)
        self.plainTextEdit.setReadOnly(True)
        self.plainTextEdit.setOverwriteMode(True)
        self.plainTextEdit.setObjectName("plainTextEdit")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Media Compressor"))
        self.label_2.setText(_translate("MainWindow", "An Implimentaion of FFmpeg Library"))
        self.lineEdit.setPlaceholderText(_translate("MainWindow", "provide the input file path here "))
        self.pushButton.setText(_translate("MainWindow", "Compress"))
        self.lineEdit_2.setPlaceholderText(_translate("MainWindow", "provide the output file path here "))
        self.label_3.setText(_translate("MainWindow", "Compress Video & Audio files without visible quality drop"))
        self.plainTextEdit.setPlaceholderText(_translate("MainWindow", "Results will be visible here...\nTry not to include file extension in output file path."))

    def process_finished(self):
            self.message("Compression finished.....")
            self.p = None
    def message(self, s):
            self.plainTextEdit.appendPlainText(s)
    def on_click(self):
            self.plainTextEdit.clear()

            if self.p is None:
                    self.message("Processing your request.....\nThis compression could take several minutes(depends upon your device hardware).")
                    self.p = QProcess()
                    if path.exists(self.lineEdit.text()):
                            path_input = self.lineEdit.text()
                            file_output = self.lineEdit_2.text()
                            a_codec = "libvorbis" # change the codec if you know a better one
                            v_codec = "libx265" # change the codec if you know a better one
                            video_file = (".mp4", ".mkv", ".webm", ".flv", ".vob", "ogv", ".gif", ".gifv", ".avi", ".wmv", ".mov", ".yuv", ".rm", ".m4v", ".mpv", ".3gp", ".wav")
                            audio_file = (".3gp", ".aac", ".aax", ".aiff", ".amr", ".ape", ".dvf", ".flac", ".m4a", ".webm", ".mp3", ".ogg", ".msv", ".oga", ".mogg", ".opus", ".raw", ".wav", ".wma", ".tta")
                            if path_input.endswith(video_file):
                                    path_output = f"{file_output}.mkv"
                                    try:
                                            av_command = ["-i", path_input, "-map", "0", "-c:v", v_codec, "-preset", "veryfast", "-crf", "26", "-c:a", a_codec, "-b:a", "128k", path_output]
                                            self.p.start("ffmpeg", av_command)
                                    except:
                                            v_command = ["-i", path_input, "-map", "0", "-c:v", v_codec, "-preset", "veryfast", "-crf", "26", "-an", path_output]
                                            self.p.start("ffmpeg", v_command)

                            if path_input.endswith(audio_file):
                                    path_output = f"{file_output}.ogg"
                                    a_command = ["-i", path_input, "-c:a", a_codec, "-b:a", "128k", "-vn", path_output]
                                    self.p.start("ffmpeg", a_command) 

                            self.p.finished.connect(self.process_finished)                              
                    else:
                            self.plainTextEdit.clear()
                            self.message("Error.... file not found.\nCheck again before providing the file path.")
                            self.p.close()
                            self.p = None 
        



if __name__ == "__main__":
    import sys
    from os import path
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())