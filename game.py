from dice import Dice

class Game:
    def __init__(self, players, field, grid_size=9):
        self.players = players
        self.field = field
        self.grid_size = grid_size
        self.path = self._build_path()
        self.cells = field.cells
        for p in self.players:
            p.set_path(self.path)
        self.current_player_index = 0

    def _build_path(self):
        path = []
        size = self.grid_size
        for x in range(size):
            path.append((x, 0))
        for y in range(1, size):
            path.append((size - 1, y))
        for x in reversed(range(size - 1)):
            path.append((x, size - 1))
        for y in reversed(range(1, size - 1)):
            path.append((0, y))
        return path

    def _normalize_roll_result(self, roll_result):
        if isinstance(roll_result, int):
            return roll_result, None, None
        if isinstance(roll_result, (tuple, list)):
            if len(roll_result) == 0:
                return 0, None, None
            if len(roll_result) == 1:
                return roll_result[0], None, None
            d1, d2 = roll_result[0], roll_result[1]
            return d1 + d2, d1, d2
        try:
            return int(roll_result), None, None
        except Exception:
            return 0, None, None

    def roll_and_move(self):
        raw = Dice.roll()
        steps, d1, d2 = self._normalize_roll_result(raw)

        player = self.players[self.current_player_index]
        player.move(steps)

        new_index = player.index
        new_coord = self.path[new_index]
        new_cell = self.cells[new_index]

        self.current_player_index = (self.current_player_index + 1) % len(self.players)

        return {
            'player': player,
            'player_name': player.name,
            'steps': steps,
            'd1': d1,
            'd2': d2,
            'new_index': new_index,
            'new_coord': new_coord,
            'new_cell': new_cell,
            'player_money': 1500
        }
