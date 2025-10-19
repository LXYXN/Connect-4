import random

print("Welcome to Connect Four")
print("-----------------------")

possibleLetters = ["A","B","C","D","E","F","G"]
board = [["","","","","","",""], ["","","","","","",""], ["","","","","","",""], ["","","","","","",""], ["","","","","","",""], ["","","","","","",""]]

row = 6
col = 7

def printboard():
  print("\n     A    B    C    D    E    F    G  ", end="")
  for x in range(row):
    print("\n   +----+----+----+----+----+----+----+")
    print(x, " |", end="")
    for y in range(col):
      if(board[x][y] == "🔵"):
        print("",board[x][y], end=" |")
      elif(board[x][y] == "🔴"):
        print("", board[x][y], end=" |")
      else:
        print(" ", board[x][y], end="  |")
  print("\n   +----+----+----+----+----+----+----+")

def modifyArray(spacePicked, turn):
  board[spacePicked[0]][spacePicked[1]] = turn

def checkWin(chip):
  # horizontal
  for y in range(row):
    for x in range(col - 3):
      if board[x][y] == chip and board[x+1][y] == chip and board[x+2][y] == chip and board[x+3][y] == chip:
        print("\nGame over", chip, "wins!")
        return True

  # vertical
  for x in range(row):
    for y in range(col - 3):
      if board[x][y] == chip and board[x][y+1] == chip and board[x][y+2] == chip and board[x][y+3] == chip:
        print("\nGame over", chip, "wins!")
        return True

  # upper right to bottom left diagonal
  for x in range(row - 3):
    for y in range(3, col):
      if board[x][y] == chip and board[x+1][y-1] == chip and board[x+2][y-2] == chip and board[x+3][y-3] == chip:
        print("\nGame over", chip, "wins!")
        return True

  # upper left to bottom right diagonal
  for x in range(row - 3):
    for y in range(col - 3):
      if board[x][y] == chip and board[x+1][y+1] == chip and board[x+2][y+2] == chip and board[x+3][y+3] == chip:
        print("\nGame over", chip, "wins!")
        return True
  return False

def coordParser(inputString):
  coord = [None] * 2
  if(inputString[0] == "A"):
    coord[1] = 0
  elif(inputString[0] == "B"):
    coord[1] = 1
  elif(inputString[0] == "C"):
    coord[1] = 2
  elif(inputString[0] == "D"):
    coord[1] = 3
  elif(inputString[0] == "E"):
    coord[1] = 4
  elif(inputString[0] == "F"):
    coord[1] = 5
  elif(inputString[0] == "G"):
    coord[1] = 6
  else:
    print("Invalid")
  coord[0] = int(inputString[1])
  return coord

def isSpaceAvailable(coordinate):
  if(board[coordinate[0]][coordinate[1]] == '🔴'):
    return False
  elif(board[coordinate[0]][coordinate[1]] == '🔵'):
    return False
  else:
    return True

def gravityChecker(coordinate):
  # Calculate space below
  spaceBelow = [None] * 2
  spaceBelow[0] = coordinate[0] + 1
  spaceBelow[1] = coordinate[1]
  # Check if the coord is at ground level
  if(spaceBelow[0] == 6):
    return True
  # Check for chips below it
  if(isSpaceAvailable(spaceBelow) == False):
    return True
  return False

leaveLoop = False
turnCounter = 0
while(leaveLoop == False):
  if(turnCounter % 2 == 0):
    printboard()
    while True:
      spacePicked = input("\nChoose a space: ")
      coord = coordParser(spacePicked)
      try:
        # Check if the space is available
        if((isSpaceAvailable(coord)) and gravityChecker(coord)):
          modifyArray(coord, '🔵')
          break
        else:
          print("Not a valid coord")
      except:
        print("Error occured. Please try again.")
    winner = checkWin('🔵')
    turnCounter += 1
  # Computer's turn
  else:
    while True:
      cpuChoice = [random.choice(possibleLetters), random.randint(0,5)]
      cpucoord = coordParser(cpuChoice)
      if(isSpaceAvailable(cpucoord) and gravityChecker(cpucoord)):
        modifyArray(cpucoord, '🔴')
        break
    turnCounter += 1
    winner = checkWin('🔴')

  if(winner):
    printboard()
    break
