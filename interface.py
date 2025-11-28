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
        if result is None:
            return

        player = result['player']
        cell = result['new_cell']

        if result['await_purchase']:
            self.waiting_for_purchase = True
            self.ask_purchase(player, cell)
        else:
            self.game.next_player()

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
                    text = f"{player.name} купил {cell.name}"
                else:
                    text = f"{player.name} хотел купить {cell.name}, но не хватило денег"
            else:
                text = f"{player.name} отказался от покупки {cell.name}"

            self.waiting_for_purchase = False
            self.game.next_player()
            if self.parent_window:
                self.parent_window.add_log(text)
            msg_box.deleteLater()

        msg_box.buttonClicked.connect(handle_reply)
        msg_box.show()
