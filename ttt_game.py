# code by Oliver Den, 2023-10-29, Toronto, ON

# create a board function
def my_board(board):
    # Display the current board state
    for row in board:
        print(" | ".join(row))
        print("-" * 9)


# create a function to identify winners
def identify_winners(board, player):
    # Check for a player's win in rows, columns, and diagonals
    for row in board:
        if all(cell == player for cell in row):
            return True

    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True

    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True

    return False

# create the game logic
def game_logic():
    # Initialize the game board and the starting player
    board = [[" " for _ in range(3)] for _ in range(3)]
    player = "X"

    for move in range(9):  # There are 9 total moves in Tic-Tac-Toe
        my_board(board)  # Display the current board

        while True:
            try:
                # Ask the player to enter a row
                row = int(input(f"Player {player}, enter row (1, 2, or 3): "))
                if row < 1 or row > 3:
                    raise ValueError("Value should be between 1 and 3.")

                # Ask the player to enter a column
                col = int(input(f"Player {player}, enter column (1, 2, or 3): "))
                if col < 1 or col > 3:
                    raise ValueError("Value should be between 1 and 3.")

                if board[row - 1][col - 1] == " ":
                    # If the selected square is empty, place the player's mark
                    board[row - 1][col - 1] = player
                    break
                else:
                    print("This square is already occupied. Try again.")
            except ValueError:
                # Handle invalid input and ask the player to try again
                print("Invalid input. Enter an integer between 1 and 3.")

        if identify_winners(board, player):
            # Check if the current player has won
            my_board(board)
            print(f"Player {player} wins!")
            break
        else:
            # Switch to the other player's turn
            player = "O" if player == "X" else "X"
    else:
        # If all squares are filled and no winner, it's a draw
        my_board(board)
        print("It's a draw!")

# play the game

if __name__ == "__main__":
    # Start the game
    game_logic()
