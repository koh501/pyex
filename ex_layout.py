import sys
from PySide6 import QtCore, QtWidgets
from Custom_Widgets.QCustomFlowLayout import QCustomFlowLayout
from PySide6.QtWidgets import  QFrame, QVBoxLayout,  QLabel
from PySide6.QtCore import QSize
from PySide6.QtGui import QPixmap, QMovie
 

class MainWindow(QtWidgets.QMainWindow):

    def  add_image(self,  img, layout):        
        pixmap = QPixmap(img)
        pixmap = pixmap.scaledToHeight(self.height)
        label = QLabel()
        label.setFrameStyle(QFrame.Panel | QFrame.Raised)
        label.setPixmap(pixmap) 
        layout.addWidget(label)

    def add_movie(self, img, layout):
        pixmap = QPixmap(img)
        pixmap = pixmap.scaledToHeight(self.height)
        movie = QMovie(img)
        movie.setScaledSize(QSize(pixmap.width(), pixmap.height())); 
        label = QLabel()
        label.setFrameStyle(QFrame.Panel | QFrame.Raised)
        label.setMovie(movie)
        layout.addWidget(label)
        movie.start()    

    def __init__(self):
        super().__init__()
        self.height = 500
        self.setWindowTitle("QCustomFlowLayout Example")
        self.central_widget = QtWidgets.QWidget()
        self.setCentralWidget(self.central_widget)
        self.flow_layout = QCustomFlowLayout(parent=self.central_widget, margin=10, spacing=5)

        self.add_image('1.jpg', self.flow_layout)
        self.add_image('2.jpg', self.flow_layout)
        self.add_image('3.jpg', self.flow_layout)
        self.add_movie('1.gif', self.flow_layout)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.resize(800, 800)
    window.show()
    sys.exit(app.exec())
