import random

class CasinoGame:
    def __init__(self, initial_balance):
        self.balance = initial_balance
        self.slots = list(range(1, 11))

    def place_bet(self, slot, amount):
        if amount > self.balance:
            print("Недостаточно средств для ставки.")
            return False
        if slot not in self.slots:
            print("Неверный слот. Выберите число от 1 до 10.")
            return False
        self.balance -= amount
        return True

    def play_game(self, bet_slot, bet_amount):
        winning_slot = random.choice(self.slots)
        if bet_slot == winning_slot:
            self.balance += bet_amount * 2
            return True, winning_slot
        else:
            return False, winning_slot

class WinLogic:
    def __init__(self):
        pass

    @staticmethod
    def determine_win(bet_slot, winning_slot):
        if bet_slot == winning_slot:
            return "Вы выиграли!"
        else:
            return "Вы проиграли."