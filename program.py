import sys

from PyQt6.QtWidgets import QWidget, QApplication
from PyQt6.QtGui import QColor, QPainter
from PyQt6.QtCore import QPoint, QRect
from PyQt6 import uic

from random import randrange


class CircleDrawing(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('circle.ui', self)
        self.setFixedSize(500, 800)
        self.do_paint = False

        self.draw_circle.clicked.connect(self.paint)
        self.draw_circle.setGeometry(10, 10, 60, 30)

    def paint(self):
        self.do_paint = True
        self.update()

    def paintEvent(self, a0):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            self.draw(qp)
            qp.end()
            self.do_paint = False

    def draw(self, painter):
        x, y = randrange(0, 100) + 200, randrange(0, 400) + 200
        size = randrange(0, 200)

        painter.setBrush(QColor('#FFFF00'))
        painter.drawEllipse(QRect(x, y, size, size))


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = CircleDrawing()
    form.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())