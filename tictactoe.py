import re

class Player:
    def __init__(self, player_number):
        self.player_number = player_number

class Board:
    def __init__(self, size):
        self.size = size
        self.board = [[None] * size for _ in range(size)]

    def is_move_valid(self, x, y):
        if self.board[x][y] == None:
            return True
        else:
            return False

    def play(self, x, y, player):
        self.board[x][y] = str(player.player_number)

    def print_board(self):
        for row in self.board:
            for item in row:
                if item == None:
                    print(".", end=" ")
                else:
                    print(item, end=" ")
            print()

    def check_winner(self, player):
        player = str(player.player_number)

        # case where all cells of a row are the same
        for row in self.board:
            if all(cell == player for cell in row):
                return True

        # case where all cells of a col are the same
        for col in range(self.size):
            if all(self.board[row][col] == player for row in range(self.size)):
                return True

        # case where all cells in a diag are the same
        if all(self.board[i][i] == player for i in range(self.size)):
            return True

        return False

    def check_tie(self):
        for row in self.board:
            if None in row:
                return False
        return True

def start_game():
    board_size = 3
    board = Board(board_size)
    players = [Player(0), Player(1)]
    player_turn = 0 # 0 always goes first

    player_input = input(f"Player's {players[player_turn].player_number} turn:")

    # game loop, runs until a player either yields, win or tie
    while player_input != "yield":

        if is_input_valid(player_input, board_size):
            x, y = convert_string_to_int(player_input)

            if board.is_move_valid(x, y):
                board.play(x, y, players[player_turn])
                board.print_board()

                if board.check_winner(players[player_turn]):
                    print(f"Player {players[player_turn].player_number} wins!")
                    break

                if board.check_tie():
                    print(f"This is a tie. Everyone wins. ♡")
                    break

                player_turn = (player_turn + 1) % 2 # this is the end of the turn, iterates to next player

            # if move is not valid the same player will play again
            else:
                print('This move is not valid because the space is occupied. Try a different move.')
                player_input = input(f"Player's {players[player_turn].player_number} turn:")
                continue

        else:
            print('Invalid pattern, please use the format "X Y". X and Y have to be integers between (0 and 2).\n')
            player_input = input(f"Player's {players[player_turn].player_number} turn:")
            continue

        player_input = input(f"Player's {players[player_turn].player_number} turn:") # grabs next player's input to be evaluated in next loop iteration

# util functions
def convert_string_to_int(input):
    return [int(num) for num in input.split()]

def is_input_valid(input, board_size):
    pattern = r'^\s*-?\d+\s*\s\s*-?\d+\s*$'
    if re.match(pattern, input):
        input_nums = convert_string_to_int(input)
        return all(0 <= num < board_size for num in input_nums)
    return input == 'yield'

if __name__ == "__main__":
    start_game()
