# Program to simulate a 3x3 tic-tac-toe game and check for a winner

board = [[' ' for _ in range(3)] for _ in range(3)]

def print_board():
    for row in board:
        print('|'.join(row))
        print('-' * 5)

def check_winner():
    # Check rows and columns for a winner
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != ' ':
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] != ' ':
            return board[0][i]

    # Check diagonals for a winner
    if board[0][0] == board[1][1] == board[2][2] != ' ':
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != ' ':
        return board[0][2]

    return None

def is_board_full():
    for row in board:
        if ' ' in row:
            return False
    return True



def tic_tac_toe():
    current_player = 'X'

    while True:
        print_board()
        print(f"Player {current_player}, it's your turn.")
        row = int(input("Enter row (0, 1, or 2): "))
        col = int(input("Enter column (0, 1, or 2): "))

        if board[row][col] == ' ':
            board[row][col] = current_player
        else:
            print("That spot is already taken. Try again.")
            continue

        winner = check_winner()
        if winner:
            print_board()
            print(f"\nWinner: {winner}")
            break

        if is_board_full():
            print_board()
            print("\nIt's a draw!")
            break

        current_player = 'O' if current_player == 'X' else 'X'

tic_tac_toe()
