from PyQt6.QtWidgets import QApplication, QMainWindow, QGraphicsView
from field import FieldMonopoly
from player import Player

PLAYER_DATA = [
    ("Красная машина", "pictures/red_car.png", "red"),
    ("Зелёный вертолёт", "pictures/green_helicopter.png", "green"),
    ("Синий корабль", "pictures/blue_ship.png", "blue"),
    ("Белый самолёт", "pictures/white_plane.png", "white")
]

class GameWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Монополия")
        self.cell_size = 50
        self.setGeometry(100, 100, self.cell_size * 9 + 150, self.cell_size * 9 + 100)

        self.field = FieldMonopoly(cell_size=self.cell_size)
        self.view = QGraphicsView(self.field, self)
        self.setCentralWidget(self.view)

        start_path = [(0, 0)]

        self.players = []
        for name, icon, color in PLAYER_DATA:
            player = Player(name=name, icon=icon, cell_size=self.cell_size)
            player.set_path(start_path)
            self.players.append(player)
            self.field.addItem(player.token)

if __name__ == "__main__":
    app = QApplication([])
    window = GameWindow()
    window.show()
    app.exec()
