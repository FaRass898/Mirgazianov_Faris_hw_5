import configparser
from casino_game import CasinoGame, WinLogic



def main():
    config = configparser.ConfigParser()
    config.read('settings.ini')
    initial_balance = int(config['DEFAULT']['MY_MONEY'])

    game = CasinoGame(initial_balance)
    while True:
        print(f"Ваш баланс: {game.balance}")
        slot = int(input("Выберите слот (от 1 до 10): "))
        amount = int(input("Введите сумму ставки: "))

        if game.place_bet(slot, amount):
            win, winning_slot = game.play_game(slot, amount)
            print(f"Выпавший слот: {winning_slot}")
            print(WinLogic.determine_win(slot, winning_slot))
            print(f"Ваш баланс: {game.balance}")

        play_again = input("Хотите сыграть еще раз? (да/нет): ").lower()
        if play_again != 'да':
            print(f"Итоговый баланс: {game.balance}")
            if game.balance > initial_balance:
                print("Вы в выигрыше!")
            elif game.balance < initial_balance:
                print("Вы в проигрыше!")
            else:
                print("Вы закончили игру с тем же балансом, что и в начале.")
            break


if __name__ == "__main__":
    main()

