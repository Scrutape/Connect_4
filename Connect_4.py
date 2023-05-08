class Connect_4:

  col_count = 7
  row_count = 6

# Creates the 2D list to represent each spot on the 7x6 board
  def create_board(self):
    return [[' ' for i in range(Connect_4.col_count)]
            for j in range(Connect_4.row_count)]
# Uses ASCII to visually represent the game board and the pieces in play
  def print_board(self):
    result = ''
    result = '  1   2   3   4   5   6   7' + '\n'
    for i in self.board:
      result += '+---' * Connect_4.col_count + '+' + '\n'
      for j in i:
        result += f'| {j} '
      result += '|\n'
    result += '+---' * Connect_4.col_count + '+' + '\n'
    print(result)

# Makes sure the col value entered by the user meets some basic criteria before proceeding
  def is_valid_move(self, col):
    if col <= 0 or col > Connect_4.col_count or isinstance(col, int) == False:
      return False
    return True
'''
 drop_piece():
 Places a piece in the lowest possible spot on the board. This is how it works: starting with the user input that passes
 the 'is_valid_move' check, it first subtracts 1 that input to provide an accurate index number to be used.
 
 Second: the code uses a 'for' loop to iterate through a range representing the number of rows on a Connect 4 board (6), starting at
 the last (aka highest index value) list and stepping backwards to the first (aka lowest index value) list. The variable holding the
 iterations is 'row'.
 
 Immediately after, it uses the 'row' value, plus the 'col' value input by the player, to check if the list values are ' ' (blank)
 in that respective column, starting with the "bottom" (or highest index value) row and moving down the 'row' index each time the corresponding 'row'
 iteration decreases. The moment it finds a blank space ' ' it writes to the nested list index whatever symbol represents the currently assigned
 player, and returns a True value (indicating a piece was placed), and the row & col values at the index the symbol was placed at.
 
''' 
 
  def drop_piece(self, player, col):
    col -= 1
    for row in range(Connect_4.row_count - 1, -1, -1):
      if self.board[row][col] == ' ':
        self.board[row][col] = 'X' if player == 1 else 'O'
        return True, row, col
    return False, None, None

'''
is_winning_move() does the following:
It's fed the current position of the piece/symbol "dropped" from the 'drop_piece()' function, and the entire 2D list that contains all the symbols
representing the players, and the symbol representing the player at play currently.
It iterates through a list of tuples, each tuple representing a direction on the gameboard that Connect 4 wins could be (up, up-right, right, and up-left)
and iterates through each pair. Then a second FOR loop introduces a tuple that is used to house forward and backward stepping in the direction dictated
by the 'directions' tuple from earlier. Each time it steps in a direction, it adds 1 to the count variable and advances through each direction until it finds four
player symbols in a specific direction, so when the count hits 4 (or greater, in case of game situations where a single piece connects two strips of three pieces each)
it returns True, indicating a winning move has been found. If it doesn't find 4 of the same players symbols in a row, it returns False, indicating a winning move has
NOT been found in a given direction.

'''
  
  def is_winning_move(self, board, row, col, player):
    directions = [(1, 0), (1, 1), (0, 1), (-1, 1)]
    for dr, dc in directions:
      count = 1
      for d in (1, -1):
        r, c = row + dr * d, col + dc * d
        while 0 <= r < 6 and 0 <= c < 7 and board[r][c] == player:
          count += 1
          r, c = r + dr * d, c + dc * d
        if count >= 4:
          return True
    return False
  
'''
main():
the "engine" which runs the game. Establishes the 2D list, sets player to 1, keeps the game open with a 'while True' conditional,
then prints the board, informs the players who's turn it is, requests a column number, checks if that column entry is valid, drop_piece into that column,
if piece is successfully placed then it checks if there's a winning string of pieces in any given direction, if yes then it prints the game board and who wins
and ends the function, otherwise switches to player 2 and starts at the 'while True' portion of the code. Also there is code to translate player 1 or 2 to their
correct symbol, announce when a valid column pick cannot be executed because a column is full, and announce when an input is invalid.

'''
  
  
  def main(self):
    self.board = self.create_board()
    player = 1
    while True:
      try:
        self.print_board()
        print(f"Player {player}'s turn")
        col = int(input("Enter a column (1-7): "))
        if self.is_valid_move(col):
          success, row, col = self.drop_piece(player, col)
          if success:
            player_symbol = 'X' if player == 1 else 'O'
            if self.is_winning_move(self.board, row, col, player_symbol):
              self.print_board()
              print(f"Player {player} wins!")
              break
            player = 3 - player
          else:
            print("Can't drop piece, choose another column.")
        else:
          print("Invalid move. Please try again.")
      except ValueError:
        print("Invalid input. Please try again.")



if __name__ == "__main__":
  game = Connect_4()
  game.main()

#game1 = Connect_4()
