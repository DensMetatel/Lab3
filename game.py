from random import randint

class Game:
    def __init__(self, players, field):
        self.players = players
        self.field = field
        self.cells = field.cells
        self.current_player_index = 0

        for p in self.players:
            p.set_path(self.cells)

    def current_player(self):
        return self.players[self.current_player_index]

    def roll_and_move(self):
        player = self.current_player()

        d1, d2 = randint(1,6), randint(1,6)
        steps = d1 + d2
        player.move_steps(steps)
        cell = self.cells[player.position]

        await_purchase = False
        if cell.cell_type == "street" and cell.owner is None and cell.price > 0:
            await_purchase = True
        elif cell.cell_type == "street" and cell.owner is not None and cell.owner != player:
            rent = max(1, cell.price // 5)
            player.money -= rent
            cell.owner.money += rent

        return {
            'player': player,
            'steps': steps,
            'new_cell': cell,
            'await_purchase': await_purchase
        }

    def next_player(self):
        n = len(self.players)
        self.current_player_index = (self.current_player_index + 1) % n
        return self.current_player()
