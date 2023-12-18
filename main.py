# Wesley Oxman
# 11.29.2023
# code for the Final Froject, Final Project is board game Codenames

import pygame
from Board import Board
from Roles import Roles
from Rounds import Rounds

Board1 = Board()
Board1.make_board()
Board1.setUpWords()
board_str = Board1.print_board()
firstRow, secondRow, thirdRow, fourthRow, fifthRow = Board1.setUpWords()
#print(board_str)
Roles1 = Roles(Board1)
Roles1.setRoles()
firstRowSpyMaster, secondRowSpyMaster, thirdRowSpyMaster, fourthRowSpyMaster, fifthRowSpyMaster = Roles1.setUpSpyMasterCard()
assassinCard, bystanderCard, blueAgentCard, redAgentCard = Roles1.setUpIdCard()
firstTeam = Roles1.firstSet()
Rounds1 = Rounds(Roles1)
if firstTeam == 0:
  Rounds1.turnLayoutBlueFirst()
else:
  Rounds1.turnLayoutRedFirst()

black = (0, 0, 0)

pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
font = pygame.font.Font('freesansbold.ttf', 18)
pygame.display.set_caption("Codenames")
text1 = font.render(firstRow, True, black)
text2 = font.render(secondRow, True, black)
text3 = font.render(thirdRow, True, black)
text4 = font.render(fourthRow, True, black)
text5 = font.render(fifthRow, True, black)
screen.fill("tan")
screen.blit(text1, (250, 100))
screen.blit(text2, (250, 125))
screen.blit(text3, (250, 150))
screen.blit(text4, (250, 175))
screen.blit(text5, (250, 200))
text6 = font.render(firstRowSpyMaster, True, black)
text7 = font.render(secondRowSpyMaster, True, black)
text8 = font.render(thirdRowSpyMaster, True, black)
text9 = font.render(fourthRowSpyMaster, True, black)
text10 = font.render(fifthRowSpyMaster, True, black)

pygame.display.flip()
clock.tick(60)


def main():
  while True:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        pygame.quit()
        return

  
main()