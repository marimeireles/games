import copy, re

player0_points = 0
player1_points = 0
board_size = 12


def init_board(size):
    return [[None] * size for _ in range(size)]

cur_board = init_board(board_size)
prev_board = init_board(board_size)
prev_board[0][0] = ['-']

def convert_string_to_int(input):
    return [int(num) for num in input.split()]

def is_input_valid(input):
    pattern = r'^\s*-?\d+\s*\s\s*-?\d+\s*$'

    if re.match(pattern, input):
        input_nums = convert_string_to_int(input)
        if all(0 <= num < 12 for num in input_nums):
            return True
    elif input == 'yield':
        return True
    elif input == 'pass':
        return True
    else:
        return False

def ko(cur_board, prev_board):
    return cur_board == prev_board

def update_board(x, y, player_number, cur_board, prev_board):
    prev_board = copy.deepcopy(cur_board)
    cur_board[x][y] = str(player_number)
    print(f"✨ adds {cur_board[x][y]} x {x} y {y} from player {player_number}")
    return cur_board, prev_board

def is_move_valid(x, y):
    if ko(cur_board, prev_board):
        print('its ko')
        return False
    elif cur_board[x][y] == None:
        print(f"Move valid.")
        return True
    else:
        print(f"Move not valid.")
        return False

from collections import deque

def inside(x, y):
    if 0 <= x < board_size and 0 <= y < board_size and cur_board[x][y] is not None:
        return True
    return False

def flood_fill(board, x, y, player_number):
    opponent_number = player_number + 1
    if board[x][y] == inside(x, y) or board[x][y] == -1:
        print("inside or -1")
        return
    if board[x][y] != opponent_number:
        print("isnt opponent_number")
        return

    board[x][y] = str(-1);
    print('🔥🔥🔥🔥🔥', board[x][y])

    # print_board(cur_board)
    # print('🔥🔥🔥🔥🔥')

    flood_fill(board, x+1, y, player_number)
    flood_fill(board, x-1, y, player_number)
    flood_fill(board, x, y+1, player_number)
    flood_fill(board, x, y-1, player_number)

    return


def capture_pieces(x, y, player_number):
    flood_fill(cur_board, x, y, player_number)


def play(x, y, player_number):
    update_board(x, y, player_number, cur_board, prev_board)
    capture_pieces(x, y, player_number)
    # if player_number == 0:
    #     global player0_points
    #     player0_points += captured_pieces
    #     print(f"player_number {player_number} points {player0_points}")
    # else:
    #     global player1_points
    #     player1_points += captured_pieces
    #     print(f"player_number {player_number} points {player1_points}")
    print("added number to board")

def print_board(board):
    print("  ", end="")
    for i in range(board_size):
        print(f"{i:2}", end="")
    print()
    for i, row in enumerate(board):
        print(f"{i:2}", end=" ")
        for cell in row:
            print(f"{cell or '.':2}", end="")
        print()

turn = 0
player_number = 0
print(f"Player's 0 turn:")
user_input = input()
# game loop
while user_input != "yield":
    if is_input_valid(user_input):
        if user_input != "pass":
            x, y = convert_string_to_int(user_input)
            if is_move_valid(x, y):
                print(f'player {player_number} is about to play')
                play(x, y, player_number)
                print('continues if play is true')
                print_board(cur_board)
                turn += 1
            else:
                print(f"Player's {player_number} turn:")
                user_input = input()
                print('continues if play is false')
                continue
        else:
            print(f"Player {player_number} passed its turn.")
            turn += 1
            continue

    else:
        print('Invalid pattern, please use the format "X Y". X and Y have to be integers between (0 and 12).\n')
        print(f"Player's {player_number} turn:")
        user_input = input()
        continue

    player_number = turn % 2
    print(f"Player's {player_number} turn:")
    user_input = input()
