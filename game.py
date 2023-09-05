def print_board(board):
    for row in board:
        print(' '.join(row))
    print()

def is_valid_move(board, from_pos, to_pos):
    if not (0 <= from_pos[0] < 8 and 0 <= from_pos[1] < 8 and 0 <= to_pos[0] < 8 and 0 <= to_pos[1] < 8):
        return False

    from_piece = board[from_pos[0]][from_pos[1]]
    to_piece = board[to_pos[0]][to_pos[1]]

    if from_piece == ' ':
        return False

    # You can add more rules for valid moves here
    return True

def move_piece(board, from_pos, to_pos):
    piece = board[from_pos[0]][from_pos[1]]
    board[from_pos[0]][from_pos[1]] = ' '
    board[to_pos[0]][to_pos[1]] = piece


chessboard = [
    ['♜','♞','♝','♛','♚','♝','♞','♜'],
    ['♟','♟','♟','♟','♟','♟','♟','♟'],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    ['♙', '♙', '♙', '♙', '♙', '♙', '♙', '♙'],
    ['♖', '♘', '♗', '♕', '♔', '♗', '♘', '♖']
]


while True:
    print_board(chessboard)
    from_square = input("Enter the starting square:")
    to_square = input("Enter the target square:")

    from_pos = (int(from_square[1]) - 1, ord(from_square[0]) - ord('a'))
    to_pos = (int(to_square[1]) - 1, ord(to_square[0]) - ord('a'))

    if is_valid_move(chessboard, from_pos, to_pos):
        move_piece(chessboard, from_pos, to_pos)
    else:
        print("Invalid move!")