import random

def get_empty_cells(board):
    # Returns a list of coordinates (i, j) of empty cells on the board
    empty_cells = []
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                empty_cells.append((i, j))
    return empty_cells

def get_random_tile():
    # Returns a randomly selected tile (either 2 or 4) with a 90% probability for 2 and a 10% probability for 4
    return random.choices([2, 4], [0.9, 0.1])[0]

def add_random_tile(board):
    # Adds a randomly generated tile to an empty cell on the board
    empty_cells = get_empty_cells(board)
    if empty_cells:
        i, j = random.choice(empty_cells)
        tile = get_random_tile()
        board[i][j] = tile

def initialize_board(size):
    # Creates and returns a new game board of the specified size (size x size)
    board = [[0] * size for _ in range(size)]
    add_random_tile(board)
    add_random_tile(board)
    return board

def transpose(board):
    # Transposes the board (rows become columns and vice versa)
    return [list(row) for row in zip(*board)]

def reverse(board):
    # Reverses the order of elements in each row of the board
    return [row[::-1] for row in board]

def slide(row):
    # Slides the tiles in a row to the left, merging adjacent tiles if they have the same value
    new_row = [val for val in row if val != 0]
    for i in range(len(new_row) - 1):
        if new_row[i] == new_row[i + 1]:
            new_row[i] *= 2
            new_row[i + 1] = 0
    new_row = [val for val in new_row if val != 0] + [0] * row.count(0)
    return new_row

def perform_move(board, direction):
    # Performs a move in the specified direction (left, right, up, or down)
    size = len(board)
    if direction == 'left':
        board = [slide(row) for row in board]
    elif direction == 'right':
        board = reverse([slide(row) for row in reverse(board)])
    elif direction == 'up':
        board = transpose([slide(row) for row in transpose(board)])
    elif direction == 'down':
        board = transpose(reverse([slide(row) for row in reverse(transpose(board))]))
    return board

def get_best_move(board):
    # Returns the best move (direction) to make based on the maximum tile value after performing each possible move
    moves = ['left', 'right', 'up', 'down']
    max_tile = 0
    best_move = None
    for move in moves:
        new_board = perform_move(board, move)
        max_val = max([max(row) for row in new_board])
        if max_val > max_tile:
            max_tile = max_val
            best_move = move
    return best_move

def is_game_over(board):
    # Checks if the game is over (no available moves)
    for move in ['left', 'right', 'up', 'down']:
        new_board = perform_move(board, move)
        if new_board != board:
            return False
    return True

def play_game():
    # Plays a game of 2048 until the game is over or the maximum tile value reaches 2048
    size = 4  # Size of the game board
    board = initialize_board(size)
    while True:
        print_board(board)
        if is_game_over(board) or max([max(row) for row in board]) == 2048:
            break
        move = get_best_move(board)
        board = perform_move(board, move)
        add_random_tile(board)
    print_board(board)
    if max([max(row) for row in board]) == 2048:
        print("Congratulations! You won!")
    else:
        print("Game over!")

def print_board(board):
    # Prints the game board
    for row in board:
        print(row)
    print()

# Play the ga