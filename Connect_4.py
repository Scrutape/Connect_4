class Connect_4:

  col_count = 7
  row_count = 6

  def create_board(self):
    return [[' ' for i in range(Connect_4.col_count)]
            for j in range(Connect_4.row_count)]

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

  def is_valid_move(self, col):
    if col <= 0 or col > Connect_4.col_count or isinstance(col, int) == False:
      return False
    return True

  def drop_piece(self, player, col):
    col -= 1
    for row in range(Connect_4.row_count - 1, -1, -1):
      if self.board[row][col] == ' ':
        self.board[row][col] = 'X' if player == 1 else 'O'
        return True, row, col
    return False, None, None

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
