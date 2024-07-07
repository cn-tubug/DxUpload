#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
ZetCode PyQt5 tutorial 

In this example, we position two push
buttons in the bottom-right corner 
of the window. 

Author: Jan Bodnar
Website: zetcode.com 
Last edited: August 2017
"""

import requests
import sys
from PyQt5.QtCore import QCoreApplication
from PyQt5.QtWidgets import (QWidget, QPushButton, 
    QHBoxLayout, QVBoxLayout, QApplication, QLabel)


class Confirm(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):

        lbl1 = QLabel('Do you want to upload：', self)
        lbl1.move(15, 10)
        
        self.label = QLabel(self)

        okButton = QPushButton("OK", self)
        okButton.clicked.connect(self.upload_file)

        cancelButton = QPushButton("Cancel")
        cancelButton.clicked.connect(QCoreApplication.instance().quit)
        
        hbox = QHBoxLayout()

        hbox.addStretch(1)
        hbox.addWidget(okButton)
        hbox.addWidget(cancelButton)

        vbox = QVBoxLayout()
        vbox.addWidget(lbl1)
        vbox.addWidget(self.label)
        vbox.addStretch(1)
        vbox.addLayout(hbox)

        self.setLayout(vbox)    

        self.setGeometry(300, 300, 300, 150)
        self.setWindowTitle('Upload files') 
    def setText(self, text: str):
        self.label.setText(text)

    def upload_file(self):
        try:
            file_name = sys.argv[1]
        except Exception:
            file_name = sys.argv[0]
        with open(file_name, 'rb') as f:
            # 上传文件
            response = requests.post('http://127.0.0.1:5000/upload', files={'file': f})

            if response.status_code == 200:
                print(f'文件上传成功！服务器响应：{response.text}')
                self.label.setText(f'文件上传成功！')
            else:
                print(f'文件上传失败！错误代码：{response.status_code}')

if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Confirm()
    try:
        ex.setText(sys.argv[1])
    except Exception:
        ex.setText(sys.argv[0])
    ex.show()
    sys.exit(app.exec_())