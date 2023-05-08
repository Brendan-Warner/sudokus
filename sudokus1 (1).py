# -*- coding: utf-8 -*-


class peice:
  def __init__(self, num, clue):
    self.spot = num
    self.flag = flag
    

  def increment_num(self):
    self.num += 1
  
  def check_num(self):
    if self.num >9:
      return true
    return false
  def return_num(self):
    return self.num

  def set_clue(self, num):
    self.flag = true
    self.spot = num

  def reset_num(self):
    self.num = -1
  def fill_blank(self):
    self.num = 1
  def is_clue(self):
    return flag

  
def make_board(board):
  for x in range(0,10):
    sub_board = []
    for i in range (0,10):
      p = peice(0, false)
      sub_board.append(p)
    board.append(sub_board)
  return board

def number_check():#used to check how many times a given number appears in the area we are checking.
  return numbers = [0,0,0,0,0,0,0,0,0,0]

def check_numbers(nums):#checks to see if any number 1-9 appears more then once, if so, we have a violation.
  for v in range (1,10):
    if(numbers[v] > 1):
      return true

def return_section(num):
  if num < 3:
    return(0,2)
  elif num > 5:
    return(6,8)
  else:
    return(3,5)

def find_quadrent(x,y):
  section= []
  section.append(return_section(x))
  section.append(return_section(y))
  return section
  

  


def violation(board, x, y):
  numbers = number_check()
  for t in rang(0,9):#updates numbers wiith  all the numbers in a given column
    numbers[board[x+t][y].return_num()] += 1

  if check_numbers(numbers):
    return true

  numbers = number_check()
  for t in range(0,9):#updates numbers wiith  all the numbers in a given row
    numbers[board[x][y+ t].return_num()] += 1
  if check_numbers(numbers):
    return true

  numbers = number_check()
  section = find(quadrent(x,y))

  for z in range(section[0][0], section[0][1]):
    for r in range(section[1][0], section[1][1]):
      numbers[board[z][r].return_num()] += 1
  if(check_numbers):
    return true
  return false


  #next thing is to check the current three by three section for violations

def solve_puzzle(board):#main puzzle solving algorithm, we start with a black space, putting one their, if no violation of the rules, then procead to the next number, else, we incrment the number
  increment = true
  pos = 0#used to keep track of which non clue square we are on.
  for x in range(0,9):#goes through all nine rows
    for y in range(0,9):#goes throuugh all nine columns
      if board[x][y].is_clue():
        continue
      while increment:
        
        board[x][y].incrment_num()#incrment the number in the current postion, starts at 0 for all numbers
        if board[x][y].return_num == 10:#if the number we incrment to is 10, then we cannont set this postion, as a previous number needs to be changed, reset it and go back one
          pos--
          board[x][y].reset_num()
          if pos == -1:
            print("Thier is no valid solution to this puzzel.")
            return board
          if y == 0:
            x -= 1
            y += 8
            pos--
            break
          else:
            y -= 1
            pos--
            break
      increment =violation(board, x, y)#check if we have a vliolation with the current number, if so,  we need to incrment it
    pos++#incrment pos only when we are working with a non clue square and after we have finished with the current number
    increment = true
  return board


def set_clues(board):
  set_clue = true
  while set_clue:
    x_cord = input("Please set the row you would like to set a clue on.")
    y_cord = input("Please set the column you would like to set a clue on")
    num = input("Please input a number to include in the puzzle")
    board[x_cord][y_cord].set_clue(num)

    cont= input("Would you like to enter another clue? enter y for yes and anything else for no")

    if cont != "y":
      set_clue = false



board = []

board = make_board(board)

board = set_clues(board)

board = solve_puzzle(board)


for x in board:
  print(x)