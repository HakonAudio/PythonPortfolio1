def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_winner(board):
    for row in board:
        if row[0] == row[1] == row[2] and row[0] != " ":
            return True

    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != " ":
            return True

    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return True

    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        return True

    return False

def main():
    board = [[" " for _ in range(3)] for _ in range(3)]
    player_turn = "X"

    while not check_winner(board):
        print_board(board)
        print(f"It's {player_turn}'s turn!")

        try:
            row = int(input("Enter the row (1-3): ")) - 1
            col = int(input("Enter the column (1-3): ")) - 1
        except ValueError:
            print("Invalid input. Please enter numbers 1-3.")
            continue

        if 0 <= row < 3 and 0 <= col < 3 and board[row][col] == " ":
            board[row][col] = player_turn
            player_turn = "O" if player_turn == "X" else "X"
        else:
            print("Invalid move. Try again.")

        if len([cell for row in board for cell in row if cell == " "]) == 0:
            print_board(board)
            print("It's a draw!")
            break

    else:
        print_board(board)
        print(f"Player {player_turn} wins!")

if __name__ == "__main__":
    main()

