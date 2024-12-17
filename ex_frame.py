import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QHBoxLayout, QFrame, QSplitter
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt


class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.height = 500
        h_layout = QHBoxLayout()
 
        self.add_image('1.jpg'  , h_layout)
        self.add_image('2.jpg'  , h_layout)
        self.add_image('3.jpg'  , h_layout)
        self.setLayout( h_layout)
        self.show()

    def  add_image(self,  img, layout):        
        frame = QFrame()
        frame.setFrameShape(QFrame.Panel | QFrame.Sunken)
        in_layout = QVBoxLayout()
        pixmap = QPixmap(img)
        pixmap = pixmap.scaledToHeight(self.height)
        label = QLabel()
        label.setPixmap(pixmap) 
        in_layout.addWidget(label)
        frame.setLayout( in_layout)
        layout.addWidget(frame)
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())