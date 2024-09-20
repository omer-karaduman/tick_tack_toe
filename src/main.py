from game import Game
def main():
    game = Game()
    game.start_game()
    game.win.wait_for_close()
main()