from PyQt6.QtWidgets import QGraphicsScene
from cell import Cell

class FieldMonopoly(QGraphicsScene):
    def __init__(self, cell_size=50):
        super().__init__()
        self.cell_size = cell_size
        self.cells = []
        self.grid_size = 9
        self.setSceneRect(0, 0, self.grid_size*cell_size, self.grid_size*cell_size)
        self.draw_field()

    def draw_field(self):
        cells_info = [
            ("start", "green", "Старт"),
            ("street", "white", "Улица 1"),
            ("street", "white", "Улица 2"),
            ("street", "white", "Улица 3"),
            ("street", "white", "Улица 4"),
            ("street", "white", "Улица 5"),
            ("street", "white", "Улица 6"),
            ("street", "white", "Улица 7"),
            ("jail", "red", "Тюрьма"),
            ("street", "white", "Улица 8"),
            ("street", "white", "Улица 9"),
            ("street", "white", "Улица 10"),
            ("street", "white", "Улица 11"),
            ("street", "white", "Улица 12"),
            ("street", "white", "Улица 13"),
            ("street", "white", "Улица 14"),
            ("street", "white", "Улица 15"),
            ("street", "white", "Улица 16"),
            ("street", "white", "Улица 17"),
            ("street", "white", "Улица 18"),
            ("street", "white", "Улица 19"),
            ("street", "white", "Улица 20"),
            ("street", "white", "Улица 21"),
            ("street", "white", "Улица 22"),
            ("free", "blue", "Бесплатная стоянка"),
            ("street", "white", "Улица 24"),
            ("street", "white", "Улица 24"),
            ("street", "white", "Улица 16"),
            ("street", "white", "Улица 17"),
            ("street", "white", "Улица 18"),
            ("street", "white", "Улица 19"),
            ("street", "white", "Улица 20")
        ]
        for i, (cell_type, color, name) in enumerate(cells_info):
            x, y = self.index_to_coord(i)
            cell = Cell(
                x*self.cell_size,
                y*self.cell_size,
                self.cell_size,
                name=name,
                cell_type=cell_type,
                color=color
            )
            self.addItem(cell)
            self.cells.append(cell)

    def index_to_coord(self, i):
        size = self.grid_size
        perim = 4 * size - 4
        i = i % perim

        if i < size:
            return i, 0
        elif i < size + size - 1:
            return size - 1, i - (size - 1) + 0
        elif i < 3 * size - 2:
            return (3 * size - 3 - i), size - 1
        else:
            return 0, (4 * size - 4 - i)

