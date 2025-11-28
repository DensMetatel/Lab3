from random import randint, choice

class Game:
    def __init__(self, players, field, parent_window=None):
        self.players = players
        self.field = field
        self.cells = field.cells
        self.current_player_index = 0
        self.parent_window = parent_window
        self.game_over = False

        for p in self.players:
            p.set_path(self.cells)

    def current_player(self):
        return self.players[self.current_player_index]

    def roll_and_move(self):
        if self.game_over:
            return None

        player = self.current_player()
        d1, d2 = randint(1, 6), randint(1, 6)
        steps = d1 + d2
        old_pos = player.position
        player.move_steps(steps)
        cell = self.cells[player.position]

        logs = [f"{player.name} попал на {cell.name}"]

        if old_pos + steps >= len(self.cells):
            player.money += 200
            logs.append("Прошёл поле Вперёд и получил $200")

        await_purchase = False

        if cell.cell_type == "street":
            if cell.owner is None and cell.price > 0:
                await_purchase = True
            elif cell.owner is not None and cell.owner != player:
                rent = cell.price
                self.pay_or_sell(player, rent, f"платит аренду ${rent} владельцу {cell.owner.name}", logs)
                paid = min(player.money + rent, rent)
                cell.owner.money += paid

        elif cell.cell_type == "event":
            change = choice([-500, -250, 250, 500])
            if change < 0:
                self.pay_or_sell(player, -change, f"потерял ${-change} на событии", logs)
            else:
                player.money += change
                logs.append(f"получил ${change} на событии")

        elif cell.cell_type == "jail":
            player.skip_turns = 1
            logs.append("просто посетил тюрьму. Пропускает 1 ход.")

        elif cell.cell_type == "free":
            jail_cell = self.find_jail_cell()
            player.position = self.cells.index(jail_cell)
            player.new_position()
            player.skip_turns = 1
            logs.append("отправляется в тюрьму!")

        if self.parent_window:
            self.parent_window.add_log(" | ".join(logs))

        self.check_game_over()
        return {
            'player': player,
            'steps': steps,
            'new_cell': cell,
            'await_purchase': await_purchase
        }

    def pay_or_sell(self, player, amount, action_desc, logs):
        while player.money < amount:
            # ищем улицы игрока
            streets = sorted([c for c in self.field.cells if getattr(c, "owner", None) == player],
                             key=lambda x: x.price)
            if not streets:
                break
            street = streets[0]
            player.money += street.price
            street.owner = None
            logs.append(f"{player.name} продал {street.name} за ${street.price}, чтобы попытаться заплатить долг")

        if player.money >= amount:
            player.money -= amount
            logs.append(action_desc)
        else:
            logs.append(f"{player.name} не смог заплатить и банкрот!")
            player.money = 0

    def find_jail_cell(self):
        for c in self.cells:
            if c.cell_type == "jail":
                return c
        return self.cells[0]

    def next_player(self):
        if self.game_over:
            return None

        n = len(self.players)
        while True:
            self.current_player_index = (self.current_player_index + 1) % n
            player = self.players[self.current_player_index]
            if player.skip_turns > 0:
                player.skip_turns -= 1
            else:
                break

        if self.parent_window:
            self.parent_window.update_status_bar()
        return self.current_player()

    def check_game_over(self):
        active_players = [p for p in self.players if self.has_assets(p)]
        if len(active_players) <= 1:
            self.game_over = True
            winner = max(self.players, key=lambda p: p.money)
            if self.parent_window:
                self.parent_window.add_log(f"Игра окончена! Побеждает {winner.name} с ${winner.money}!")
            return True
        return False

    def has_assets(self, player):
        streets = [c for c in self.field.cells if getattr(c, "owner", None) == player]
        return player.money > 0 or len(streets) > 0
