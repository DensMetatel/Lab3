from PyQt6.QtWidgets import QGraphicsScene
from PyQt6.QtGui import QPen
from PyQt6.QtCore import Qt

class FieldMonopoly(QGraphicsScene):
    def __init__(self):
        super().__init__()
        self.cell_size = 50
        self.draw_field()

    def draw_field(self):
        pen = QPen(Qt.GlobalColor.black)
        for i in range(9):
            self.addRect(i * self.cell_size, 0, self.cell_size, self.cell_size, pen)
            self.addRect(i * self.cell_size, 8 * self.cell_size, self.cell_size, self.cell_size, pen)
            self.addRect(0, i * self.cell_size, self.cell_size, self.cell_size, pen)
            self.addRect(8 * self.cell_size, i * self.cell_size, self.cell_size, self.cell_size, pen)