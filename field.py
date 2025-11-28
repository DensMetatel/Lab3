from PyQt6.QtWidgets import QGraphicsScene, QGraphicsPixmapItem
from PyQt6.QtGui import QPixmap
from cell import Cell
from PyQt6.QtCore import Qt

class FieldMonopoly(QGraphicsScene):
    def __init__(self, cell_size=50):
        super().__init__()
        self.cell_size = cell_size
        self.cells = []
        self.grid_size = 9
        self.setSceneRect(0, 0, self.grid_size*cell_size, self.grid_size*cell_size)
        self.draw_field()
        self.add_monopoly_logo()  # добавляем картинку в центр

    def draw_field(self):
        cells_info = [
            ("start", "green", "Вперёд", 0),
            ("street", "brown", "Нагатинская улица", 60),
            ("street", "white", "Событие", 0),
            ("street", "brown", "Житная улица", 60),
            ("street", "white", "Событие", 0),
            ("street", "#81d4fa", "Первая парковая улица", 100),
            ("street", "#81d4fa", "Улица Огарева", 100),
            ("street", "#81d4fa", "Варшавское шоссе", 100),
            ("jail", "red", "Просто посетили / Тюрьма", 0),
            ("street", "#e83a96", "Улица Полянка", 140),
            ("street", "white", "Событие", 0),
            ("street", "#e83a96", "Улица Сретенка", 140),
            ("street", "#e83a96", "Ростовская набережная", 140),
            ("street", "orange", "Рязанский проспект", 160),
            ("street", "orange", "Улица Вавилова", 160),
            ("street", "orange", "Рублевское шоссе", 160),
            ("street", "white", "Бесплатная стоянка", 0),
            ("street", "red", "Тверская улица", 180),
            ("street", "white", "Событие", 0),
            ("street", "red", "Пушкинская площадь", 180),
            ("street", "red", "Площадь Маяковского", 180),
            ("street", "yellow", "Улица Грузинский Вал", 200),
            ("street", "yellow", "Новинский бульвар", 200),
            ("street", "yellow", "Смоленская площадь", 200),
            ("free", "blue", "Отправляйтесь в тюрьму", 0),
            ("street", "green", "Улица Щусева", 260),
            ("street", "white", "Событие", 0),
            ("street", "green", "Гоголевский бульвар", 260),
            ("street", "green", "Кутузовский проспект", 260),
            ("street", "white", "Событие", 0),
            ("street", "blue", "Улица Малая Бронная", 320),
            ("street", "blue", "Улица Арбат", 350)
        ]

        perim = 4 * self.grid_size - 4
        for i in range(min(len(cells_info), perim)):
            cell_type, color, name, price = cells_info[i]
            x, y = self.index_to_coord(i)
            px, py = x*self.cell_size, y*self.cell_size
            cell = Cell(px, py, self.cell_size, name=name, cell_type=cell_type, color=color, price=price)
            self.addItem(cell)
            self.cells.append(cell)

    def index_to_coord(self, i):
        size = self.grid_size
        perim = 4*size - 4
        i = i % perim
        if i < size:
            return i, 0
        elif i < size + size - 1:
            return size-1, i-(size-1)
        elif i < 3*size-2:
            return 3*size-3-i, size-1
        else:
            return 0, 4*size-4-i

    def add_monopoly_logo(self):
        pixmap = QPixmap("pictures/Monopoly-Emblem.png")

        max_width = int(self.grid_size * self.cell_size * 0.8)
        max_height = int(self.grid_size * self.cell_size * 0.8)
        pixmap = pixmap.scaled(max_width, max_height,
                               Qt.AspectRatioMode.KeepAspectRatio,
                               Qt.TransformationMode.SmoothTransformation)

        item = QGraphicsPixmapItem(pixmap)

        scene_rect = self.sceneRect()
        x = scene_rect.width() / 2 - pixmap.width() / 2
        y = scene_rect.height() / 2 - pixmap.height() / 2
        item.setPos(x, y)
        self.addItem(item)
