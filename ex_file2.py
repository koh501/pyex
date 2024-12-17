## Ex 5-12. QPixmap.

import sys, filetype
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout
from PyQt5.QtWidgets import QMainWindow, QAction
from PyQt5.QtGui import QPixmap, QMovie, QIcon
from PyQt5.QtCore import Qt, QSize
from PyQt5.QtWidgets import QFrame, QHBoxLayout, QFileDialog, QMessageBox


class MyWidget(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.height = 500 
        self.h_layout = QHBoxLayout()
        """
        hbox = QHBoxLayout()
  
        self.add_image('1.jpg', hbox)
        self.add_image('2.jpg', hbox)
        self.add_image('3.jpg', hbox)
        self.setLayout(hbox)
        """
        self.setLayout(self.h_layout)
        #self.setWindowTitle('QPixmap')
        #self.move(300, 300)
        self.show()

    def add_image(self, image, h_layout):
        frame = QFrame()
        frame.setFrameShape(QFrame.Panel | QFrame.Sunken)
        layout  = QHBoxLayout()
        frame.setLayout(layout)

        pixmap = QPixmap(image)
        pixmap = pixmap.scaledToHeight(self.height)
        label = QLabel()
        label.setPixmap(pixmap)
        layout.addWidget(label)
        h_layout.addWidget(frame)

    def add_moive(self, img, h_layout):
        frame = QFrame()
        layout = QHBoxLayout()
        pixmap = QPixmap(img)
        pixmap = pixmap.scaledToHeight(self.height)

        movie = QMovie(img)
        movie.setScaledSize(QSize(pixmap.width(), pixmap.height()))

        label = QLabel()
        label.setMovie(movie)

        layout.addWidget(label)
        frame.setLayout(layout)
        h_layout.addWidget(frame)
        movie.start()

class MyMainWindow(QMainWindow):
 def __init__(self):
    super().__init__()
    self.initUI()

 def initUI(self):
    openFile = QAction( QIcon('open.png'), 'Open', self)
    openFile.setShortcut('Ctrl+O')
    openFile.setStatusTip('Open New File')
    
    openFile.triggered.connect(self.showDialog)

    menubar = self.menuBar()
    menubar.setNativeMenuBar(False)
    fileMenu = menubar.addMenu('&File')
    fileMenu.addAction(openFile)

    self.wg = MyWidget()
    self.setCentralWidget(self.wg)
    self.resize(300,300)
    self.show()

 def showDialog(self):
    file,check = QFileDialog.getOpenFileName(self, 'Open File', './','All File(*.*);;Image(*.jpg *.png *.bmp)')

    #file_type = imghdr.what(file)
    file_type = filetype.guess(file)

    if(file_type):
       if(file_type.extension == 'gif'):
        self.wg.add_moive(file, self.wg.h_layout)
       else :
        self.wg.add_image(file, self.wg.h_layout)
    else:
       QMessageBox.critical(self, '경고', '이미지 화일을 선택하세요', QMessageBox.Yes)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyMainWindow()
    sys.exit(app.exec_())
