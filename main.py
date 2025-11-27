from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QGraphicsView, QInputDialog
)
from PyQt6.QtGui import QAction
from field import FieldMonopoly
from player import Player
from game import Game
from interface import Interface

PLAYER_DATA = [
    ("Красная машина", "pictures/red_car.png", "red"),
    ("Зелёный вертолёт", "pictures/green_helicopter.png", "green"),
    ("Синий корабль", "pictures/blue_ship.png", "blue"),
    ("Белый самолёт", "pictures/white_plane.png", "white")
]

class GameWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.cell_size = 50
        self.num_players = 4
        self.window_width = self.cell_size * 9 + 150
        self.window_height = self.cell_size * 9 + 100

        self.setWindowTitle("Монополия")
        self.setGeometry(100, 100, self.window_width, self.window_height)
        self.num_players, ok = QInputDialog.getInt(
            self,
            "Количество игроков",
            "Введите число игроков (2–4):", 2, 2, 4)
        if not ok:
            self.num_players = 2

        self.field = FieldMonopoly(cell_size=self.cell_size)
        self.view = QGraphicsView(self.field, self)
        self.setCentralWidget(self.view)

        self.players = self.create_players()

        self.game = Game(self.players, grid_size=9)

        for p in self.players:
            self.field.addItem(p.token)

        controls_x = self.cell_size * 9 - 200
        controls_y = 20
        self.controls = Interface(
            self, self.game,
            button_pos=(0, 250),
            status_pos=(0, 300)
        )
        self.controls.move(controls_x, controls_y)

        self.init_menu()

    def create_players(self):
        return [
            Player(
                name=PLAYER_DATA[i][0],
                icon=PLAYER_DATA[i][1],
                color=PLAYER_DATA[i][2],
                cell_size=self.cell_size
            )
            for i in range(self.num_players)
        ]

    def set_window_size(self, width: int, height: int):
        self.setGeometry(self.x(), self.y(), width, height)

    def init_menu(self):
        menu_bar = self.menuBar()
        settings_menu = menu_bar.addMenu("Настройки")

        resize_action = QAction("Изменить размер окна", self)
        resize_action.triggered.connect(self.change_window_size)
        settings_menu.addAction(resize_action)

    def change_window_size(self):
        text, ok = QInputDialog.getText(
            self, "Настройка окна", "Введите размеры (ширина x высота):", text=f"{self.window_width}x{self.window_height}"
        )
        if ok and "x" in text:
            try:
                width_str, height_str = text.lower().split("x")
                width = int(width_str.strip())
                height = int(height_str.strip())
                self.set_window_size(width, height)
            except ValueError:
                pass

if __name__ == "__main__":
    app = QApplication([])
    window = GameWindow()
    window.show()
    app.exec()
