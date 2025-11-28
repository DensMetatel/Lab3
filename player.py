from PyQt6.QtWidgets import QGraphicsPixmapItem
from PyQt6.QtGui import QPixmap
from PyQt6.QtCore import Qt

class Player:
    def __init__(self, name, icon, color=None, cell_size=50):
        self.name = name
        self.icon = icon
        self.color = color
        self.cell_size = cell_size
        self.position = 0
        self.path = []
        self.money = 1500
        self.skip_turns = 0
        self.token = QGraphicsPixmapItem(
            QPixmap(icon).scaled(
                int(cell_size*0.7), int(cell_size*0.7),
                Qt.AspectRatioMode.KeepAspectRatio,
                Qt.TransformationMode.SmoothTransformation
            )
        )

    def set_path(self, path):
        self.path = path
        self.new_position()

    def new_position(self):
        if self.path:
            cell = self.path[self.position]
            offset = self.cell_size * 0.15
            self.token.setPos(cell.pos().x() + offset, cell.pos().y() + offset)

    def move_steps(self, steps):
        if self.path:
            self.position = (self.position + steps) % len(self.path)
            self.new_position()

    move = move_steps
