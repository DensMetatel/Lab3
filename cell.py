from PyQt6.QtWidgets import QGraphicsRectItem
from PyQt6.QtGui import QBrush, QPen, QColor

class Cell(QGraphicsRectItem):
    def __init__(self, x, y, size, name="", cell_type="street", color="#FFFFFF", price=100):
        super().__init__(x, y, size, size)
        self.name = name
        self.cell_type = cell_type
        self.color = color
        self.price = price
        self.owner = None

        pen = QPen(QColor(0, 0, 0))
        pen.setWidth(2)
        brush = QBrush(QColor(self.color))
        self.setPen(pen)
        self.setBrush(brush)
