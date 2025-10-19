import random

print("Welcome to Connect Four")
print("-----------------------")

possibleLetters = ["A","B","C","D","E","F","G"]
# Board is 6 rows (0-5) x 7 columns (0-6)
board = [["","","","","","",""], ["","","","","","",""], ["","","","","","",""], ["","","","","","",""], ["","","","","","",""], ["","","","","","",""]]

row = 6
col = 7

def printboard():
  print("\n      A    B    C    D    E    F    G  ", end="")
  for x in range(row):
    print("\n    +----+----+----+----+----+----+----+")
    print(x, " |", end="")
    for y in range(col):
      if(board[x][y] == "🔵"):
        print("",board[x][y], end=" |")
      elif(board[x][y] == "🔴"):
        print("", board[x][y], end=" |")
      else:
        print(" ", board[x][y], end="  |")
  print("\n    +----+----+----+----+----+----+----+")

def modifyArray(spacePicked, turn):
  board[spacePicked[0]][spacePicked[1]] = turn

def checkWin(chip):
  # 🏆 Corrected horizontal win check: check 4 across (y+3) in each row (x)
  for x in range(row):
    for y in range(col - 3):
      if board[x][y] == chip and board[x][y+1] == chip and board[x][y+2] == chip and board[x][y+3] == chip:
        print("\nGame over", chip, "wins!")
        return True

  # 🏆 Corrected vertical win check: check 4 down (x+3) in each column (y)
  for y in range(col):
    for x in range(row - 3):
      if board[x][y] == chip and board[x+1][y] == chip and board[x+2][y] == chip and board[x+3][y] == chip:
        print("\nGame over", chip, "wins!")
        return True

  # upper right to bottom left diagonal (No change needed here)
  for x in range(row - 3):
    for y in range(3, col):
      if board[x][y] == chip and board[x+1][y-1] == chip and board[x+2][y-2] == chip and board[x+3][y-3] == chip:
        print("\nGame over", chip, "wins!")
        return True

  # upper left to bottom right diagonal (No change needed here)
  for x in range(row - 3):
    for y in range(col - 3):
      if board[x][y] == chip and board[x+1][y+1] == chip and board[x+2][y+2] == chip and board[x+3][y+3] == chip:
        print("\nGame over", chip, "wins!")
        return True
  return False

def coordParser(inputString):
  coord = [None] * 2
  if len(inputString) != 2 or inputString[0] not in possibleLetters:
    # Invalid format or column
    return None 

  # Convert letter to column index (0-6)
  coord[1] = possibleLetters.index(inputString[0]) 
  
  try:
    # Convert number (row) to integer
    row_index = int(inputString[1])
    if 0 <= row_index < row: # Check if row is in the valid range (0-5)
      coord[0] = row_index
      return coord
    else:
      # Row number is out of bounds (e.g., 'A6')
      return None
  except ValueError:
    # Row is not a number (e.g., 'AB')
    return None

def isSpaceAvailable(coordinate):
  # Already checked coordinate is not None, now check the board
  return board[coordinate[0]][coordinate[1]] == ''

def gravityChecker(coordinate):
  # Check if the coordinate is the bottom row (row 5)
  if coordinate[0] == row - 1:
    return True

  # Calculate space below (one row down)
  spaceBelow = [coordinate[0] + 1, coordinate[1]]
  
  # Check for chips below it
  if not isSpaceAvailable(spaceBelow):
    return True
    
  return False

leaveLoop = False
turnCounter = 0
while(leaveLoop == False):
  if(turnCounter % 2 == 0):
    printboard()
    while True:
      spacePicked = input("\nChoose a space (e.g., A0): ").upper() # Convert to uppercase for robustness
      coord = coordParser(spacePicked)
      
      # Use specific error handling instead of a generic 'except'
      if coord is None:
        print("Invalid input format or coordinates. Use format like 'C3', where 0-5 is the row.")
        continue # Restart loop for new input

      # Check if the space is available AND gravity rules are met
      if isSpaceAvailable(coord) and gravityChecker(coord):
        modifyArray(coord, '🔵')
        break
      else:
        print("Not a valid move. Either the space is taken or there's no chip below it.")
        
    winner = checkWin('🔵')
    turnCounter += 1
  # Computer's turn
  else:
    # The CPU should only pick a column (A-G), and the chip should fall to the lowest available row
    while True:
      cpu_col_letter = random.choice(possibleLetters)
      cpu_col_index = possibleLetters.index(cpu_col_letter)
      
      # Find the lowest available row (highest row index) in the chosen column
      lowest_available_row = -1
      for r in range(row - 1, -1, -1): # Iterate from row 5 up to row 0
        if board[r][cpu_col_index] == '':
          lowest_available_row = r
          break
          
      if lowest_available_row != -1:
        cpucoord = [lowest_available_row, cpu_col_index]
        modifyArray(cpucoord, '🔴')
        print(f"\nCPU chose: {cpu_col_letter}{lowest_available_row}")
        break
        
    winner = checkWin('🔴')
    turnCounter += 1

  if(winner):
    printboard()
    break
