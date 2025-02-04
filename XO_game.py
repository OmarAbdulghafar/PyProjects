# XO game
import os

# def clear_screen():
#     os.system("cls" if os.name =="nt" else "clear")

class Player:
    def __init__(self):
        self.name = ""
        self.symbol = ""

    def choose_name(self):
        while True:
            name = input("Enter your name ")
            if name.isalpha():
                self.name = name
                break
            print("Invalid name, pls enter letters only.")
    
    def choose_symbol(self):
        while True:
            symbol = input("Choose your symbol (a single letter) ")
            if symbol.isalpha() and len(symbol) == 1:
                self.symbol = symbol.upper()
                break
            print("Invalid symbol, pls choose a sinlge letter")


class Menu:
    def display_main_menu(self):
        print("Welcome to my XO Game")
        print("1. Start Game")
        print("2. Quit Game")
        while True:
            choice = input("Enter your chooice 1 or 2 ")
            if choice == "1" or choice == "2":
                break
            print("Invalid choice")
        return choice
    
    def display_endgame_menu(self):
        menu_text = """
        Game Over
        1. Restart game
        2. Quite game
        Enter your choice 1 or 2 """
        
        choice = input(menu_text)
        while True:
            choice = input("Enter your chooice 1 or 2 ")
            if choice == "1" or choice == "2":
                break
            print("Invalid choice")
        return choice



class Board:
    def __init__(self):
        self.board = []
        for i in range(1, 10):
            self.board.append(str(i))

    def display_board(self):
        for i in range(0, 10 ,3):
            print("|".join(self.board[i:i+3]))
            if i > 6:
                print("-" * 5)
    
    def update_board(self, choice, symbol):
        if self.is_valid_move(choice):
            self.board[choice - 1] = symbol
            return True
        return False


    def is_valid_move(self, choice):
        if self.board[choice -1].isdigit() == True:
            return True

    def reset_board(self):
        self.board = []
        for i in range(1, 10):
            self.board.append(str(i))


class Game:
    def __init__(self):
        self.players = [Player(), Player()]
        self.board = Board()
        self.menu = Menu()
        self.current_player_index = 0
    
    def start_game(self):
        choice = self.menu.display_main_menu()
        if choice == "1":
            self.setup_player()
            self.play_game()
        else:
            self.quit_game()
    

    def setup_player(self):
        for number, player in enumerate(self.players, start= 1):
            print(f'Player {number}, Enter your details ')
            player.choose_name()
            player.choose_symbol()
            print('-'*20)

    def play_game(self):
        while True:
            self.play_turn()
            if self.check_win() or self.check_draw():
                choice = self.menu.display_endgame_menu()
                if choice == "1":
                    self.restart_game()
                else:
                    self.quit_game()
                    break

    def quit_game(self):
        print("Thank you for playing!")

    def play_turn(self):
        player = self.players[self.current_player_index]
        self.board.display_board()
        print(f"{player.name}'s turn ({player.symbol})")
        while True:
            try:
                cell_choice = int(input("Choose a cell "))
                if  1<= cell_choice <= 9 and self.board.update_board(cell_choice, player.symbol):
                 break
                else:
                    print("Invalid move")
            except ValueError:
                print("Pls Enter a number between 1-9. ")
        
        self.switch_player()

    
    def switch_player(self):
        self.current_player_index = 1 - self.current_player_index

    def check_win(self):
        winning_conditions = [
            [0,1,2],[3,4,5],[6,7,8],
            [0,3,6],[1,4,7],[2,5,8],
            [0,4,8],[2,4,6]
        ]

        for combo in winning_conditions:
            if(self.board.board[combo[0]] == self.board.board[combo[1]] == self.board.board[combo[2]]):
                return True
        return False

    def check_draw(self):
         return all(not cell.isdigit() for cell in self.board.board)

    def restart_game(self):
        self.board.reset_board()
        self.current_player_index = 0
        self.play_game()


game = Game()
game.start_game()


##