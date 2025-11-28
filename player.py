from PyQt6.QtWidgets import QGraphicsPixmapItem
from PyQt6.QtGui import QPixmap, QColor
from PyQt6.QtCore import Qt

class Player:
    def __init__(self, name, icon=None, color="red", cell_size=50):
        self.name = name
        self.color = color
        self.cell_size = cell_size
        self.index = 0
        self.path = []

        self.token = self._create_token(icon)

    def _create_token(self, icon):
        pix = QPixmap(icon)
        pix = pix.scaled(int(self.cell_size*0.7), int(self.cell_size*0.7), Qt.AspectRatioMode.KeepAspectRatio)
        return QGraphicsPixmapItem(pix)

    def set_path(self, path):
        self.path = path
        self.new_position()

    def new_position(self):
        if not self.path:
            return
        x, y = self.path[self.index]
        offset = self.cell_size * 0.15
        self.token.setPos(x*self.cell_size + offset, y*self.cell_size + offset)

    def move(self, steps):
        if not self.path:
            return
        self.index = (self.index + steps) % len(self.path)
        self.new_position()
