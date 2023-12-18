from Roles import Roles

class Rounds:
  def __init__(self, roles):
    self.roles = roles
    self.assassinCard, self.bystanderCard, self.blueAgentCard, self.redAgentCard = self.roles.setUpIdCard()
    self.blueAgentScore = 0
    self.redAgentScore = 0
    self.firstRowSpyMaster = self.roles.setUpSpyMasterCard()[0]
    self.secondRowSpyMaster = self.roles.setUpSpyMasterCard()[1]
    self.thirdRowSpyMaster = self.roles.setUpSpyMasterCard()[2]
    self.fourthRowSpyMaster = self.roles.setUpSpyMasterCard()[3]
    self.fifthRowSpyMaster = self.roles.setUpSpyMasterCard()[4]

  def spyMasterTurn(self):
    print(self.)
    print(self.fifthRowSpyMaster)
    print(self.fourthRowSpyMaster)
  
  def blueUserTurn(self):
    self.userInput = input("What is your guess?")
    if self.userInput in self.assassinCard:
      print("Unfortunatly you picked an assassin card")
    elif self.userInput in self.bystanderCard:
      print("Unfortunatly you picked a bystander card")
      for i in range(7):
        if self.userInput == self.bystanderCard[i]:
          self.bystanderCard.pop(i)
          self.bystanderCard.insert(i, 'BYSTANDER')
    elif self.userInput in self.blueAgentCard:
      print("you picked a blue agent card")
      self.blueAgentScore += 1
      for i in range(7):
        if self.userInput == self.blueAgentCard[i]:
          self.blueAgentCard.pop(i)
          self.blueAgentCard.insert(i, 'BLUE AGENT')
      self.blueUserTurn()
      if self.userInput in self.redAgentCard:
        print("Unfortunatly you picked a red agent card")
        self.redAgentScore += 1
        for i in range(7):
          if self.userInput == self.bystanderCard[i]:
            self.redAgentCard.pop(i)
            self.redAgentCard.insert(i, 'RED AGENT')

  def redUserTurn(self):
    self.userInput = input("What is your guess?")
    if self.userInput in self.assassinCard:
      print("Unfortunatly you picked an assassin card")
    elif self.userInput in self.bystanderCard:
      print("Unfortunatly you picked a bystander card")
      for i in range(7):
        if self.userInput == self.bystanderCard[i]:
          self.bystanderCard.pop(i)
          self.bystanderCard.insert(i, 'BYSTANDER')
    elif self.userInput in self.blueAgentCard:
      print("Unfortunatly you picked a blue agent card")
      self.blueAgentScore += 1
      for i in range(7):
        if self.userInput == self.blueAgentCard[i]:
          self.blueAgentCard.pop(i)
          self.blueAgentCard.insert(i, 'BLUE AGENT')
      if self.userInput in self.redAgentCard:
        print("you picked a red agent card")
        self.redAgentScore += 1
        for i in range(7):
          if self.userInput == self.bystanderCard[i]:
            self.redAgentCard.pop(i)
            self.redAgentCard.insert(i, 'RED AGENT')
        self.redUserTurn()
  def turnLayout(self):
    self.spyMasterTurn()