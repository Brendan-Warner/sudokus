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
  return numbers = (0,0,0,0,0,0,0,0,0,0)

def check_numbers(nums):#checks to see if any number 1-9 appears more then once, if so, we have a violation.
  for v in range (1,10):
    if(numbers[v] > 1):
      return true


def violation(board, x, y):
  numbers = number_check()
  for t in rang(0,10):#updates numbers wiith  all the numbers in a given column
    numbers[board[x+t][y].return_num()] += 1

  if check_numbers(numbers):
    return true

  numbers = number_check()
  for t in range(0,10):#updates numbers wiith  all the numbers in a given row
    numbers[board[x][y+ t].return_num()] += 1
  if check_numbers(numbers):
    return true

  #next thing is to check the current three by three section for violations

def solve_puzzle(board):#main puzzle solving algorithm, we start with a black space, putting one their, if no violation of the rules, then procead to the next number, else, we incrment the number
  increment = true
  for x in range(0,10):#goes through all nine rows
    for y in range(0,10):#goes throuugh all nine columns
      if board[x][y].is_clue():
        continue
      while increment:
        board[x][y].incrment_num()#incrment the number in the current postion, starts at 0 for all numbers
        if board[x][y].return_num == 10:#if the number we incrment to is 10, then we cannont set this postion, as a previous number needs to be changed, reset it and go back one
          board[x][y].reset_num()
          if y == 0:
            if x == 0:#if we are at the first position of the puzzel, then thier is no valid solution, ////need a more robust way to check for the first blank.//////
              print("Thier is no valid solution to this puzzel.")
              return board
            x -= 1
            y += 8
            break
          else:
            y -= 1
            break
        increment =violation(board, x, y)#check if we have a vliolation with the current number, if so,  we need to incrment it
      increment = true
  return board



board = []

board = make_board(board)

board = set_clues(board)

board = solve_puzzle(board)


for x in board:
  print(x)