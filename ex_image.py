## Ex 5-12. QPixmap.

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout
from PyQt5.QtWidgets import QFrame, QHBoxLayout, QGridLayout, QWidget
from PyQt5.QtWidgets import QBoxLayout
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt


class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
     
        
        hbox = QHBoxLayout()
         
        self.add_image('1.jpg', '장예원', hbox)
        self.add_image('2.jpg', '장예원', hbox)
        self.add_image('3.jpg', '장예원', hbox)
        self.add_image('4.jpg', '장예원', hbox)
        self.add_image('5.jpg', '장예원', hbox)
        self.setLayout(hbox)
        
        #widget = QWidget(self)
        #self.add('1.jpg', 'aaa', widget)
        #self.add('2.jpg', 'bbb', widget)
        
        self.setWindowTitle('QPixmap')
        self.move(300, 300)
        self.show()

    def get_grid():
        item_count = 3

    def add(self, image, title, widget):
        vbox= QVBoxLayout()
 
        pixmap = QPixmap(image)
        lb_img = QLabel()
        lb_img.setPixmap(pixmap)
  
        lb_title = QLabel(title + 'Width: '+str(pixmap.width())+', Height: '+str(pixmap.height()))
        lb_title.setAlignment(Qt.AlignCenter)

        vbox.addWidget(lb_img)
        vbox.addWidget(lb_title)

        #vbox.setParent(widget)
        widget.setLayout(vbox)
        
    def add_image(self, image, title, layout):
        vbox= QVBoxLayout()
 
        pixmap = QPixmap(image)
        lb_img = QLabel()
        lb_img.setPixmap(pixmap)
  
        lb_title = QLabel(title + 'Width: '+str(pixmap.width())+', Height: '+str(pixmap.height()))
        lb_title.setAlignment(Qt.AlignCenter)

        vbox.addWidget(lb_img)
        vbox.addWidget(lb_title)
         
        layout.addLayout(vbox)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
