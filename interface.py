from PyQt6.QtWidgets import QWidget, QPushButton, QMessageBox

class Interface(QWidget):
    def __init__(self, parent=None, game_logic=None):
        super().__init__(parent)
        self.game = game_logic
        self.parent_window = parent
        self.waiting_for_purchase = False

        self.button = QPushButton("Бросить кубики", self)
        self.button.move(0, 0)
        self.button.clicked.connect(self.on_roll)
        self.button.show()

        self.setFixedSize(150, 50)
        self.show()

    def on_roll(self):
        if self.waiting_for_purchase:
            return

        result = self.game.roll_and_move()
        player = result['player']
        cell = result['new_cell']

        if result['await_purchase']:
            self.waiting_for_purchase = True
            self.ask_purchase(player, cell)
        else:
            self.game.next_player()

        self.update_status()

    def ask_purchase(self, player, cell):
        msg_box = QMessageBox(self)
        msg_box.setWindowTitle("Покупка")
        msg_box.setText(f"Хотите купить {cell.name} за ${cell.price}?")
        msg_box.setStandardButtons(QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)

        def handle_reply(button):
            if msg_box.standardButton(button) == QMessageBox.StandardButton.Yes:
                if player.money >= cell.price:
                    player.money -= cell.price
                    cell.owner = player
            self.waiting_for_purchase = False
            self.game.next_player()
            self.update_status()
            msg_box.deleteLater()

        msg_box.buttonClicked.connect(handle_reply)
        msg_box.show()

    def update_status(self):
        if self.parent_window:
            self.parent_window.update_status_bar()

