from PyQt6.QtWidgets import QPushButton, QWidget, QLabel
from PyQt6.QtCore import Qt

class Interface(QWidget):
    def __init__(self, parent, game_logic, button_pos=(0,0), status_pos=(50,250)):
        super().__init__(parent)
        self.game = game_logic

        self.button = QPushButton("Бросить кубики", self)
        self.button.move(*button_pos)
        self.button.clicked.connect(self.on_roll_clicked)
        self.button.show()

        self.status = QLabel("Готово", self)
        self.status.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.status.move(*status_pos)
        self.status.resize(400, 50)
        self.status.show()

        width = max(button_pos[0]+self.button.width(), status_pos[0]+self.status.width())
        height = max(button_pos[1]+self.button.height(), status_pos[1]+self.status.height())
        self.setFixedSize(width, height)
        self.show()

    def on_roll_clicked(self):
        result = self.game.roll_and_move()
        name = result['player_name']
        steps = result['steps']
        d1 = result['d1']
        d2 = result['d2']
        money = result['player_money']
        cell = result['new_cell']

        if d1 is None and d2 is None:
            msg = f"{name} → ход: {steps}, Деньги: ${money}\nНа клетке: {cell.name}"
        else:
            msg = f"{name} → {d1} + {d2} = {steps}, Деньги: ${money}\nНа клетке: {cell.name}"

        self.status.setText(msg)
