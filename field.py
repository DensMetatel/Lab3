from PyQt6.QtWidgets import QGraphicsScene
from PyQt6.QtGui import QPen, QBrush, QColor

class FieldMonopoly(QGraphicsScene):
    def __init__(self, cell_size=50):
        super().__init__()
        self.cell_size = 50
        self.setSceneRect(0, 0, 9 * cell_size, 9 * cell_size)
        self.draw_field()

    def draw_field(self):
        pen = QPen(QColor(212, 175, 55))
        pen.setWidth(2)
        brush = QBrush(QColor("black"))

        for i in range(9):
            self.addRect(i * self.cell_size, 0, self.cell_size, self.cell_size, pen, brush)
            self.addRect(i * self.cell_size, 8 * self.cell_size, self.cell_size, self.cell_size, pen, brush)
            self.addRect(0, i * self.cell_size, self.cell_size, self.cell_size, pen, brush)
            self.addRect(8 * self.cell_size, i * self.cell_size, self.cell_size, self.cell_size, pen, brush)
