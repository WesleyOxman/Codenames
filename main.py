# Wesley Oxman
# 11.29.2023
# code for the Final Froject, Final Project is board game Codenames

import pygame
from Board import Board
from Roles import Roles
from Rounds import Rounds

#iniitialize pygame and put in things from the other files to be used
Board1 = Board()
Board1.make_board()
Board1.setUpWords()
board_str = Board1.print_board()
firstRow, secondRow, thirdRow, fourthRow, fifthRow = Board1.setUpWords()
Roles1 = Roles(Board1)
Roles1.setRoles()
assassinCard, bystanderCard, blueAgentCard, redAgentCard = Roles1.setUpIdCard()
Rounds1 = Rounds(Roles1, Board1)
black = (0, 0, 0)
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
font = pygame.font.Font('freesansbold.ttf', 18)
pygame.display.set_caption("Codenames")

# readies the rows of the board to be shown
text1 = font.render(firstRow, True, black)
text2 = font.render(secondRow, True, black)
text3 = font.render(thirdRow, True, black)
text4 = font.render(fourthRow, True, black)
text5 = font.render(fifthRow, True, black)

# defines the backround color
screen.fill("tan")

# shows the board on pygame
screen.blit(text1, (250, 100))
screen.blit(text2, (250, 125))
screen.blit(text3, (250, 150))
screen.blit(text4, (250, 175))
screen.blit(text5, (250, 200))
pygame.display.flip()
hint = Rounds1.spyMasterTurn()
Rounds1.firstPick()
clock.tick(60)
