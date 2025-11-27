from PyQt6.QtWidgets import QGraphicsPixmapItem
from PyQt6.QtGui import QPixmap

class Player:
    def __init__(self, name, icon=None, color="red", cell_size=50, start_index=0):

        self.name = name
        self.icon = icon
        self.color = color
        self.cell_size = cell_size
        self.index = start_index

        pix_image = QPixmap(icon)
        pix_image = pix_image.scaled(int(cell_size * 0.7), int(cell_size * 0.7))
        self.token = QGraphicsPixmapItem(pix_image)

    def set_path(self, path):
        self.path = path
        self.new_position()

    def new_position(self):
        x, y = self.path[self.index]
        offset = self.cell_size * 0.15
        self.token.setPos(x * self.cell_size + offset, y * self.cell_size + offset)

    def move(self, steps):
        self.index = (self.index + steps) % len(self.path)
        self.new_position()
