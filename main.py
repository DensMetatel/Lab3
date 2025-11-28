import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QGraphicsView, QInputDialog, QStatusBar
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

if __name__ == "__main__":
    app = QApplication([])

    class GameWindow(QMainWindow):
        def __init__(self):
            super().__init__()

            self.cell_size = 50
            self.setMinimumSize(600, 600)
            self.setWindowTitle("Монополия")

            # количество игроков
            self.num_players, ok = QInputDialog.getInt(
                self, "Количество игроков", "Введите число игроков (2–4):", 2, 2, 4
            )
            if not ok:
                self.num_players = 2

            # поле
            self.field = FieldMonopoly(cell_size=self.cell_size)
            self.view = QGraphicsView(self.field, self)
            self.setCentralWidget(self.view)

            # игроки
            self.players = [
                Player(PLAYER_DATA[i][0], PLAYER_DATA[i][1], PLAYER_DATA[i][2], self.cell_size)
                for i in range(self.num_players)
            ]
            for p in self.players:
                self.field.addItem(p.token)

            # игра
            self.game = Game(self.players, self.field)

            # интерфейс
            self.controls = Interface(self, self.game)
            self.controls.move(self.cell_size*9 + 10, 20)

            # статус-бар
            self.status_bar = QStatusBar()
            self.setStatusBar(self.status_bar)
            self.update_status_bar()

            self.init_menu()

        def update_status_bar(self):
            text = " | ".join([f"{p.name}: ${p.money}" for p in self.players])
            current = self.game.current_player()
            text += f"  ← Текущий ход: {current.name}"
            self.status_bar.showMessage(text)

        def init_menu(self):
            menu_bar = self.menuBar()
            settings_menu = menu_bar.addMenu("Настройки")
            resize_action = QAction("Изменить размер окна", self)
            resize_action.triggered.connect(self.change_window_size)
            settings_menu.addAction(resize_action)

        def change_window_size(self):
            text, ok = QInputDialog.getText(
                self, "Настройка окна", "Введите размеры (ширина x высота):",
                text=f"{self.width()}x{self.height()}"
            )
            if ok and "x" in text:
                try:
                    width_str, height_str = text.lower().split("x")
                    width = int(width_str.strip())
                    height = int(height_str.strip())
                    self.setGeometry(self.x(), self.y(), width, height)
                except ValueError:
                    pass

    window = GameWindow()
    window.show()
    sys.exit(app.exec())
