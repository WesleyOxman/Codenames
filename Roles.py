from Board import Board
import random

class Roles:
  #initilizes the starting things for Roles
  def __init__(self, board):
    self.board = board
    self.blueAgentNum = 0
    self.redAgentNum = 0
    self.spyMasterList = self.board.board
    self.words = self.board.words
    self.tempList = []
    self.assassinKeyWord = []
    self.bystanderKeyWord = []
    self.blueAgentKeyWord = []
    self.redAgentKeyWord = []

# defines the assassin and what card it is
  def assassinSet(self):
    self.assassinLocation = random.choice(self.spyMasterList)
    self.assassinIndex = self.spyMasterList.index(self.assassinLocation)
    self.assassinWord = random.choice(self.assassinLocation)
    if self.assassinWord in self.words:
      self.assassinKeyWord.append(self.assassinWord)
    while self.assassinWord not in self.words:
      self.assassinLocation = random.choice(self.spyMasterList)
      self.assassinIndex = self.spyMasterList.index(self.assassinLocation)
      self.assassinWord = random.choice(self.assassinLocation)
      if self.assassinWord in self.words:
        self.assassinKeyWord.append(self.assassinWord)
    self.spyMasterList[self.assassinIndex] = ['ASSASSIN' if word == self.assassinWord else word for word in self.assassinLocation]

# defines the bystanders and what cards they are
  def bystanderSet(self):
    for i in range(7):
      self.bystanderLocation = random.choice(self.spyMasterList)
      self.bystanderIndex = self.spyMasterList.index(self.bystanderLocation)
      self.bystanderWord = random.choice(self.bystanderLocation)
      if self.bystanderWord in self.words:
        self.bystanderKeyWord.append(self.bystanderWord)
      while self.bystanderWord not in self.words:
        self.bystanderLocation = random.choice(self.spyMasterList)
        self.bystanderIndex = self.spyMasterList.index(self.bystanderLocation)
        self.bystanderWord = random.choice(self.bystanderLocation)
        if self.bystanderWord in self.words:
          self.bystanderKeyWord.append(self.bystanderWord)
      self.spyMasterList[self.bystanderIndex] = ['BYSTANDER' if word == self.bystanderWord else word for word in self.bystanderLocation]

  # defines the blueagents and what cards they are
  def blueAgentSet(self):
    for i in range(self.blueAgentNum):
      self.blueAgentLocation = random.choice(self.spyMasterList)
      self.blueAgentIndex = self.spyMasterList.index(self.blueAgentLocation)
      self.blueAgentWord = random.choice(self.blueAgentLocation)
      if self.blueAgentWord in self.words:
        self.blueAgentKeyWord.append(self.blueAgentWord)
      while self.blueAgentWord not in self.words:
        self.blueAgentLocation = random.choice(self.spyMasterList)
        self.blueAgentIndex = self.spyMasterList.index(self.blueAgentLocation)
        self.blueAgentWord = random.choice(self.blueAgentLocation)
        if self.blueAgentWord in self.words:
          self.blueAgentKeyWord.append(self.blueAgentWord)
      self.spyMasterList[self.blueAgentIndex] = ['BLUE AGENT' if word == self.blueAgentWord else word for word in self.blueAgentLocation]

  # defines the Redagents and what cards they are
  def redAgentSet(self):
    for i in range(self.redAgentNum):
      self.redAgentLocation = random.choice(self.spyMasterList)
      self.redAgentIndex = self.spyMasterList.index(self.redAgentLocation)
      self.redAgentWord = random.choice(self.redAgentLocation)
      if self.redAgentWord in self.words:
        self.redAgentKeyWord.append(self.redAgentWord)
      while self.redAgentWord not in self.words:
        self.redAgentLocation = random.choice(self.spyMasterList)
        self.redAgentIndex = self.spyMasterList.index(self.redAgentLocation)
        self.redAgentWord = random.choice(self.redAgentLocation)
        if self.redAgentWord in self.words:
          self.redAgentKeyWord.append(self.redAgentWord)
      self.spyMasterList[self.redAgentIndex] = ['RED AGENT' if word == self.redAgentWord else word for word in self.redAgentLocation]

  # defines who goes first and who needs to get an extra card
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

  # sets up the spyMaster card that the spyMaster can use
  def setUpSpyMasterCard(self):
    global firstRowSpyMaster, secondRowSpyMaster, thirdRowSpyMaster, fourthRowSpyMaster, fifthRowSpyMaster
    firstRowSpyMaster = " ".join(self.spyMasterList[0])
    secondRowSpyMaster = " ".join(self.spyMasterList[1])
    thirdRowSpyMaster = " ".join(self.spyMasterList[2])
    fourthRowSpyMaster = " ".join(self.spyMasterList[3])
    fifthRowSpyMaster = " ".join(self.spyMasterList[4])
    return firstRowSpyMaster, secondRowSpyMaster, thirdRowSpyMaster, fourthRowSpyMaster, fifthRowSpyMaster

  # allows for other files to use this data
  def setUpIdCard(self):
    global assassinCard, bystanderCard, blueAgentCard, redAgentCard
    assassinCard = self.assassinKeyWord
    bystanderCard = self.bystanderKeyWord
    blueAgentCard = self.blueAgentKeyWord
    redAgentCard = self.redAgentKeyWord
    return assassinCard, bystanderCard, blueAgentCard, redAgentCard

  # puts in what order the code will run
  def setRoles(self):
    self.assassinSet()
    self.bystanderSet()
    self.doubleAgentSet()
    self.blueAgentSet()
    self.redAgentSet()
    self.setUpSpyMasterCard()
