import sys

from PySide6.QtGui import QIcon, QMovie
from PySide6.QtWidgets import QApplication, QWidget, QLabel


class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.setGeometry(800, 800, 480, 480)
        self.setWindowTitle("Python GUI Window")
        self.setWindowIcon(QIcon('erro.gif'))
        self.falar()

    def falar(self):
        label = QLabel(self)
        movie = QMovie('falando.gif')
        movie.setSpeed(500)
        label.setMovie(movie)
        movie.start()

    def dorme(self):
        label = QLabel(self)
        movie = QMovie('dormindo.gif')
        movie.setSpeed(500)
        label.setMovie(movie)
        movie.start()

    def choque(self):
        label = QLabel(self)
        movie = QMovie('chocado.gif')
        movie.setSpeed(500)
        label.setMovie(movie)
        movie.start()

    def olhos(self):
        label = QLabel(self)
        movie = QMovie('espremendoolho.gif')
        movie.setSpeed(500)
        label.setMovie(movie)
        movie.start()

    def pisca(self):
        label = QLabel(self)
        movie = QMovie('piscando.gif')
        movie.setSpeed(500)
        label.setMovie(movie)
        movie.start()

    def error(self):
        label = QLabel(self)
        movie = QMovie('erro.gif')
        movie.setSpeed(500)
        label.setMovie(movie)
        movie.start()


app = QApplication([])
window = Window()
window.show()
sys.exit(app.exec())
