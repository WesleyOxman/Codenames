from Roles import Roles
import random
import os
from Board import Board
class Rounds:
  #initilizes the starting things for Round
  def __init__(self, roles, board):
    self.board = board
    self.roles = roles
    self.assassinCard, self.bystanderCard, self.blueAgentCard, self.redAgentCard = self.roles.setUpIdCard()
    self.blueAgentScore = 0
    self.redAgentScore = 0
    self.firstRowSpyMaster = self.roles.setUpSpyMasterCard()[0]
    self.secondRowSpyMaster = self.roles.setUpSpyMasterCard()[1]
    self.thirdRowSpyMaster = self.roles.setUpSpyMasterCard()[2]
    self.fourthRowSpyMaster = self.roles.setUpSpyMasterCard()[3]
    self.fifthRowSpyMaster = self.roles.setUpSpyMasterCard()[4]
    self.firstRow, self.secondRow, self.thirdRow, self.fourthRow, self.fifthRow = self.board.setUpWords()
    self.blueturn = 0
    self.redturn = 0
    self.bystanders = []
    self.blueAgents = []
    self.redAgents = []
    self.skipTurn = ["PASS"]

  # defines the spyMaster turn
  def spyMasterTurn(self):
    print("spy Master cards")
    print(self.firstRowSpyMaster)
    print(self.secondRowSpyMaster)
    print(self.thirdRowSpyMaster)
    print(self.fourthRowSpyMaster)
    print(self.fifthRowSpyMaster)
    self.spyMasterHint = input("Enter spy master hint: ")
    os.system('clear')
    global hint
    hint = self.spyMasterHint
    return hint

  # defines the bue team turn
  def blueUserTurn(self):
    self.redturn = 0
    print("Bystanders known: ", self.bystanders)
    print("Blue Agents known: ", self.blueAgents)
    print("Red Agents known: ", self.redAgents)
    while self.blueturn == 0:
      print("your SpyMaster hint is", self.spyMasterHint)
      self.userInput = input("Blue User What is your guess?: ")
      if self.userInput in self.skipTurn:
        self.blueturn = 1
      elif self.userInput in self.assassinCard:
        print("Unfortunatly you picked an assassin card\n")
        self.redAgentScore += 9999
        self.redturn = 1
        return self.redAgentScore
      elif self.userInput in self.bystanderCard:
        print("Unfortunatly you picked a bystander card\n")
        for i in range(7):
          if self.userInput == self.bystanderCard[i]:
            self.bystanderCard.insert(i, 'BYSTANDER')
        self.bystanders.append(self.userInput)
        self.blueturn = 1
      elif self.userInput in self.blueAgentCard:
        print("you picked a blue agent card\n")
        self.blueAgentScore += 1
        for i in range(7):
          if self.userInput == self.blueAgentCard[i]:
            self.blueAgentCard.pop(i)
            self.blueAgentCard.insert(i, 'BLUE AGENT')
        self.blueAgents.append(self.userInput)
        self.blueUserTurn()
        return self.blueAgentScore
      elif self.userInput in self.redAgentCard:
        print("Unfortunatly you picked a red agent card\n")
        self.redAgentScore += 1
        for i in range(7):
          if self.userInput == self.bystanderCard[i]:
            self.redAgentCard.pop(i)
            self.redAgentCard.insert(i, 'RED AGENT')
        self.redAgents.append(self.userInput)
        self.blueturn = 1
        return self.redAgentScore

  # defines the red teams turn
  def redUserTurn(self):
    self.blueturn = 0
    print("Bystanders known: ", self.bystanders)
    print("Blue Agents known: ", self.blueAgents)
    print("Red Agents known: ", self.redAgents)
    while self.redturn == 0:
      print("your SpyMaster hint is", self.spyMasterHint)
      self.userInput = input("Red User What is your guess?: ")
      if self.userInput in self.skipTurn:
        self.redturn = 1
      elif self.userInput in self.assassinCard:
        print("Unfortunatly you picked an assassin card\n")
        self.blueAgentScore += 9999
        self.redturn = 1
        return self.blueAgentScore
      elif self.userInput in self.bystanderCard:
        print("Unfortunatly you picked a bystander card\n")
        for i in range(7):
          if self.userInput == self.bystanderCard[i]:
            self.bystanderCard.pop(i)
            self.bystanderCard.insert(i, 'BYSTANDER')
        self.bystanders.append(self.userInput)
        self.redturn = 1
      elif self.userInput in self.blueAgentCard:
        print("Unfortunatly you picked a blue agent card\n")
        self.blueAgentScore += 1
        for i in range(7):
          if self.userInput == self.blueAgentCard[i]:
            self.blueAgentCard.pop(i)
            self.blueAgentCard.insert(i, 'BLUE AGENT')
        self.blueAgents.append(self.userInput)
        self.redturn = 1
        return self.blueAgentScore
      elif self.userInput in self.redAgentCard:
        print("you picked a red agent card\n")
        self.redAgentScore += 1
        for i in range(7):
          if self.userInput == self.bystanderCard[i]:
            self.redAgentCard.pop(i)
            self.redAgentCard.insert(i, 'RED AGENT')
            return self.redAgentScore
        self.redAgents.append(self.userInput)
        self.redUserTurn()

  # defines who goes fist and who has an extra card from previous code
  def doubleAgentSet(self):
    global blueAgenNum
    self.doubleAgent = random.randint(0,1)
    if self.doubleAgent == 0:
      self.blueAgentNum = 9
      self.redAgentNum = 8
      return self.blueAgentNum, self.redAgentNum
    if self.doubleAgent == 1:
      self.blueAgentNum = 8
      self.redAgentNum = 9
      return self.blueAgentNum, self.redAgentNum

  # defines who will go first
  def firstPick(self):
    self.doubleAgentSet()
    if self.doubleAgent == 0:
      self.turnLayoutBlueFirst()
    else:
      self.turnLayoutRedFirst()
      
  # defines how each round will go
  def turnLayoutRedFirst(self):
    for i in range(5):
      self.redUserTurn()
      self.checkWin()
      self.spyMasterTurn()
      self.checkWin()
      self.blueUserTurn()
      self.checkWin()
      self.spyMasterTurn()
      self.checkWin()
  def turnLayoutBlueFirst(self):
    for i in range(5):
      self.blueUserTurn()
      self.checkWin()
      self.spyMasterTurn()
      self.checkWin()
      self.redUserTurn()
      self.checkWin()
      self.spyMasterTurn()
      self.checkWin()
      
  # checks to see if a team won after their turn
  def checkWin(self):
    if self.doubleAgent == 0:
      if self.blueAgentScore >= 9:
        print("Blue wins!")
        exit()
      elif self.redAgentScore >= 8:
        print("Red wins!")
        exit()
    if self.doubleAgent == 1:
      if self.blueAgentScore >= 8:
        print("Blue wins!")
        exit()
      elif self.redAgentScore >= 9:
        print("Red wins!")
        exit()
