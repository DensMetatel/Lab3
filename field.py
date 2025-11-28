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
            ("start", "green", "Вперёд"),
            ("street", "brown", "Нагатинская улица"),
            ("street", "white", "Событие"),
            ("street", "brown", "Житная улица"),
            ("street", "white", "Событие"),
            ("street", "#81d4fa", "Первая парковая улица"),
            ("street", "#81d4fa", "Улица Огарева"),
            ("street", "#81d4fa", "Варшавское шоссе"),
            ("jail", "red", "Просто посетили / Тюрьма"),
            ("street", "#e83a96", "Улица Полянка"),
            ("street", "white", "Событие"),
            ("street", "#e83a96", "Улица Сретенка"),
            ("street", "#e83a96", "Ростовская набережная"),
            ("street", "orange", "Рязанский проспект"),
            ("street", "orange", "Улица Вавилова"),
            ("street", "orange", "Рублевское шоссе"),
            ("street", "white", "Бесплатная стоянка"),
            ("street", "red", "Тверская улица"),
            ("street", "white", "Событие"),
            ("street", "red", "Пушкинская площадь"),
            ("street", "red", "Площадь Маяковского"),
            ("street", "yellow", "Улица Грузинский Вал"),
            ("street", "yellow", "Новинский бульвар"),
            ("street", "yellow", "Смоленская площадь"),
            ("free", "blue", "Отправляйтесь в тюрьму"),
            ("street", "green", "Улица Щусева"),
            ("street", "white", "Событие"),
            ("street", "green", "Гоголевский бульвар"),
            ("street", "green", "Кутузовский проспект"),
            ("street", "white", "Событие"),
            ("street", "blue", "улица Малая Бронная"),
            ("street", "blue", "Улица Арбат")
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

