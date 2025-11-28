import os
from PyQt6.QtWidgets import QGraphicsPixmapItem
from PyQt6.QtGui import QPixmap, QColor
from PyQt6.QtCore import Qt

class Player:
    def __init__(self, name, icon=None, color="red", cell_size=50):
        self.name = name
        self.icon = icon
        self.color = color
        self.cell_size = cell_size
        self.position = 0
        self.path = []
        self.money = 1500
        self.skip_turns = 0
        self.token = self._create_token(icon)

    def _create_token(self, icon):
        size = max(1, int(self.cell_size * 0.7))
        pix = QPixmap(size, size)
        pix.fill(QColor(self.color))
        try:
            if icon and os.path.exists(icon):
                tmp = QPixmap(icon)
                if not tmp.isNull():
                    pix = tmp.scaled(size, size,
                                     Qt.AspectRatioMode.KeepAspectRatio,
                                     Qt.TransformationMode.SmoothTransformation)
        except Exception as e:
            print("Ошибка загрузки иконки:", icon, e)
        return QGraphicsPixmapItem(pix)

    def set_path(self, path):
        self.path = path
        self.new_position()

    def new_position(self):
        if not self.path:
            return
        cell = self.path[self.position]
        x = cell.pos().x()
        y = cell.pos().y()
        offset = self.cell_size * 0.15
        self.token.setPos(x + offset, y + offset)

    def move_steps(self, steps):
        if not self.path:
            return
        self.position = (self.position + steps) % len(self.path)
        self.new_position()

    def move(self, steps):
        self.move_steps(steps)
