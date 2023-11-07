# Tic-Tac-Toe board representation (3x3)
board = [" " for _ in range(9)]

# Function to display the Tic-Tac-Toe board
def display_board(board):
    print(f"{board[0]} | {board[1]} | {board[2]}")
    print("--+---+--")
    print(f"{board[3]} | {board[4]} | {board[5]}")
    print("--+---+--")
    print(f"{board[6]} | {board[7]} | {board[8]}")

# Function to check if the board is full
def is_board_full(board):
    return " " not in board

# Function to check if a player has won
def check_win(board, player):
    # Check rows, columns, and diagonals
    win_conditions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
        [0, 4, 8], [2, 4, 6]  # Diagonals
    ]

    for condition in win_conditions:
        if all(board[i] == player for i in condition):
            return True
    return False

# Function for the AI player to make a move
def ai_move(board):
    # Minimax function with Alpha-Beta Pruning
    def minimax(board, depth, is_maximizing_player):
        # Terminal state (leaf node)
        if check_win(board, "O"):
            return 1
        if check_win(board, "X"):
            return -1
        if is_board_full(board):
            return 0

        if is_maximizing_player:
            max_eval = -float("inf")
            for i in range(len(board)):
                if board[i] == " ":
                    board[i] = "O"
                    eval = minimax(board, depth + 1, False)
                    board[i] = " "
                    max_eval = max(max_eval, eval)
            return max_eval
        else:
            min_eval = float("inf")
            for i in range(len(board)):
                if board[i] == " ":
                    board[i] = "X"
                    eval = minimax(board, depth + 1, True)
                    board[i] = " "
                    min_eval = min(min_eval, eval)
            return min_eval

    best_move = -1
    best_eval = -float("inf")
    for i in range(len(board):
        if board[i] == " ":
            board[i] = "O"
            eval = minimax(board, 0, False)
            board[i] = " "
            if eval > best_eval:
                best_eval = eval
                best_move = i

    return best_move

# Main game loop
while True:
    display_board(board)
    if is_board_full(board):
        print("It's a draw!")
        break

    user_move = int(input("Enter your move (1-9): ")) - 1
    if 0 <= user_move < 9 and board[user_move] == " ":
        board[user_move] = "X"

        if check_win(board, "X"):
            display_board(board)
            print("You win!")
            break
        elif is_board_full(board):
            display_board(board)
            print("It's a draw!")
            break

        ai_move_index = ai_move(board)
        board[ai_move_index] = "O"

        if check_win(board, "O"):
            display_board(board)
            print("AI wins!")
            break
    else:
        print("Invalid move. Try again.")
