# Tic Tac Toe Game
 
# -----------------------------------------------------------------------------------------------------------------------------------------------------------
import random
 
# tic tac toe board 
board = [0,0,0,0,0,0,0,0,0]
 
 
def initialize():
  """
  This function initialize board to play new game
  """
  for i in range(0,9):
    board[i] = 0
 
 
# -----------------------------------------------------------------------------------------------------------------------------------------------------------
 
 
# function to print board
def print_board():
  """
  This function is used to print the tic tac toe board
  """
 
  i = 8
  while i>=0:
    print(f' {board[i-2]} | {board[i-1]} | {board[i]} ')
    print('----------')
    i -= 3
 
 
# -----------------------------------------------------------------------------------------------------------------------------------------------------------
 
# function to check whether board is full or not?
def isFull():
  """
  This function is to check whether tic tac toe board has empty spaces or not
  returns false if has empty spaces else returns true
  """
 
  flag = 0
  for i in board:
    if i=='X' or i=='O':
      flag += 1
 
  if flag == 9:
    return True
  else:
    return False
 
 
# -----------------------------------------------------------------------------------------------------------------------------------------------------------
 
# function to check is there any winner
 
def anyWon():
  if (board[0] == 'X' and board[1] == 'X' and board[2] == 'X') or (board[0] == 'O' and board[1] == 'O' and board[2] == 'O'):  #rows
    if board[0] == 'X':
      return (True,'X')
    else:
      return (True,'O')
  elif (board[3] == 'X' and board[4] == 'X' and board[5] == 'X') or (board[3] == 'O' and board[4] == 'O' and board[5] == 'O'):
    if board[3] == 'X':
      return (True,'X')
    else:
      return (True,'O')
  elif (board[6] == 'X' and board[7] == 'X' and board[8] == 'X') or (board[6] == 'O' and board[7] == 'O' and board[8] == 'O'):
    if board[6] == 'X':
      return (True,'X')
    else:
      return (True,'O')
  elif (board[0] == 'X' and board[3] == 'X' and board[6] == 'X') or (board[0] == 'O' and board[3] == 'O' and board[6] == 'O'):  #columns
    if board[0] == 'X':
      return (True,'X')
    else:
      return (True,'O')
  elif (board[1] == 'X' and board[4] == 'X' and board[7] == 'X') or (board[1] == 'O' and board[4] == 'O' and board[7] == 'O'):
    if board[1] == 'X':
      return (True,'X')
    else:
      return (True,'O')
  elif (board[2] == 'X' and board[5] == 'X' and board[8] == 'X') or (board[2] == 'O' and board[5] == 'O' and board[8] == 'O'):
     if board[2] == 'X':
      return (True,'X')
     else:
      return (True,'O')
  elif (board[0] == 'X' and board[4] == 'X' and board[8] == 'X') or (board[0] == 'O' and board[4] == 'O' and board[8] == 'O'):  #diagonals
    if board[0] == 'X':
      return (True,'X')
    else:
      return (True,'O')
  elif (board[2] == 'X' and board[4] == 'X' and board[6] == 'X') or (board[2] == 'O' and board[4] == 'O' and board[6] == 'O'):
    if board[2] == 'X':
      return (True,'X')
    else:
      return (True,'O')
  else:
    return (False,'-') 
 
 
# -----------------------------------------------------------------------------------------------------------------------------------------------------------
 
 
# accept user choices
def user_choice():
  """
  This function is used to accept sign, User 1 will enter sign which he wants to use to play game
  """
  while True:
    print('User 1')
    choice = input('Enter your choice: 1) X    2) O : ')
    if choice.upper() == 'X':
      return ('X','O')
    elif choice.upper() == 'O':
      return ('O','X')
    else:
      print('Wrong choice!!!')
 
 
# -----------------------------------------------------------------------------------------------------------------------------------------------------------
 
 
# accept user choices to play a game
def accept_input(toss,user1,user2):
  """
  This function is used to accept input from user to play a game
  """
  if toss == 0:
    command = 'X'
  else:
    command = 'O'
 
  if command == 'X':
    if user1 == 'X':
      position = int(input('user 1 : enter position (1-9) -   '))
    else:
      position = int(input('User 2: enter position (1-9)  -   '))
  else:
    if user1 == 'O':
      position = int(input('User 1: enter position (1-9)  -   '))
    else:
      position = int(input('User 2: enter position (1-9)  -   '))
 
  board[position-1] = command.upper()
 
# -----------------------------------------------------------------------------------------------------------------------------------------------------------
 
while True:
 
  initialize()
 
  user1,user2 = user_choice()
 
  print('----------------------------------')
  print(f"User 1 is using '{user1}' to play")
  print(f"User 2 is using '{user2}' to play")
  print('----------------------------------')
 
  toss = random.randint(0,1)
  #print(toss)
 
  while not isFull():
    flag,winner = anyWon()
 
    if not flag: 
      accept_input(toss,user1,user2)
    else:
      if winner == 'X' and user1 == 'X':
        winner_name = 'User 1'
      else:
        winner_name = 'User 2'
 
      print('--------------------------------')
      print(f'| {winner_name} has won the game |')
      print('--------------------------------')
      break
 
    if toss ==0:
      toss = 1
    else:
      toss = 0
 
    print_board()
 
  flag1,winner = anyWon()
 
  if isFull() and not flag1:
    print('--------------------------------')
    print(f'|     No one won the game     |')
    print('--------------------------------')
 
  ch = int(input('Do you want to play again? (press 1 to continue else press 0) :  '))
 
  # to exit from game
  if ch == 0:
    break
