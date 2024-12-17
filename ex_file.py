## Ex 6-4. QFileDialog.

import sys,  imghdr
from PyQt5.QtWidgets import QApplication, QMainWindow, QTextEdit, QAction, QFileDialog
from PyQt5.QtGui import QIcon, QPixmap, QMovie
from PyQt5.QtWidgets import  QWidget, QLabel, QVBoxLayout, QHBoxLayout, QFrame, QSplitter
from PyQt5.QtWidgets  import QMessageBox
from PyQt5.QtCore import Qt, QSize


class MyWidget(QWidget ):
    def __init__(self):
        super().__init__()
        self.height = 500
        self.h_layout = QHBoxLayout()
        self.setLayout( self.h_layout)
        self.show()

    def  add_image(self,  img, layout):        
        frame = QFrame()
        in_layout = QVBoxLayout()
        pixmap = QPixmap(img)
        pixmap = pixmap.scaledToHeight(self.height)
        label = QLabel()
        label.setPixmap(pixmap) 
        in_layout.addWidget(label)
        frame.setLayout( in_layout)
        layout.addWidget(frame)

    def add_movie(self, img, layout):
        frame = QFrame()
        in_layout = QVBoxLayout()
        pixmap = QPixmap(img)
        pixmap = pixmap.scaledToHeight(self.height)
 
        movie = QMovie(img)
        movie.setScaledSize(QSize(pixmap.width(), pixmap.height())); 
        label = QLabel()
        label.setMovie(movie)
        in_layout.addWidget(label)
        frame.setLayout(in_layout)
        layout.addWidget(frame)
        movie.start()

class MyMainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        openFile = QAction(QIcon('open.png'), 'Open', self)
        openFile.setShortcut('Ctrl+O')
        openFile.setStatusTip('Open New File')
        openFile.triggered.connect(self.showDialog)

        menubar = self.menuBar()
        menubar.setNativeMenuBar(False)
        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(openFile)
 
        self.wg=MyWidget()
        self.setCentralWidget(self.wg)
        self.resize(300,300)
        self.show()

    def showDialog(self):
        file, check = QFileDialog.getOpenFileName(self, 'Open file', './',  "All Files (*.*);;Image (*.jpg *.png *.bmp)")

        file_type = imghdr.what(file)

        if(file_type) :
            if(file_type == 'gif'):
                self.wg.add_movie(file, self.wg.h_layout)
            else :
                self.wg.add_image(file, self.wg.h_layout)
            print (file_type)
        else :
            QMessageBox.critical(  self, '경고', "이미지 화일을 선택하세요",  QMessageBox.Yes )
            
"""
        ext =  file.split('.')

        if(ext[1] =='jpg') :
            self.wg.add_image(file, self.wg.h_layout)
        else :
            QMessageBox.critical(  self, '이미지 파일 선택', "이미지 화일이 아님니다",  QMessageBox.Yes )
        
        if check:
            print (check)

        fname = QFileDialog.getOpenFileName(self, 'Open file', './',  "All Files (*.*);;Image (*.jpg *.png *.bmp)")

        if fname[0]:
            self.wg.add_image(fname[0], self.wg.h_layout)

        if fname[0]:
            f = open(fname[0], 'r')
            print (fname[0])
             
            with f:
                data = f.read()
                #self.textEdit.setText(data)        

    def initUI2(self):
        self.textEdit = QTextEdit()
        self.setCentralWidget(self.textEdit)
        self.statusBar()

        openFile = QAction(QIcon('open.png'), 'Open', self)
        openFile.setShortcut('Ctrl+O')
        openFile.setStatusTip('Open New File')
        openFile.triggered.connect(self.showDialog)

        menubar = self.menuBar()
        menubar.setNativeMenuBar(False)
        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(openFile)

        self.setWindowTitle('File Dialog')
        self.setGeometry(300, 300, 300, 200)
        self.show()

    def showDialog(self):
        fname = QFileDialog.getOpenFileName(self, 'Open file', './')

        if fname[0]:
            f = open(fname[0], 'r')

            with f:
                data = f.read()
                self.textEdit.setText(data)
"""

if __name__ == '__main__':
    app = QApplication(sys.argv)
    #ex = MyApp()
 #   ex = MyWidget()
    ex2= MyMainWindow()
    sys.exit(app.exec_())
