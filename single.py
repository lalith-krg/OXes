from pygame import *
from Grid import *
from over import *
from os import *
from Exit1 import *
from button import *
import random

def play_alone():
  environ['SDL_VIDEO_WINDOW_POS'] = '400,40'
  grid1 = grid()
  board = display.set_mode((770,900))
  display.set_caption("Tic Tac Toe")
  game_on = True
  winner = None
  init()
  count = 0
  player = 'X'
  
  while game_on:
    once = 0 #for the computer to print X only once
    winner = win(player, grid1.grid)
    
    if winner!= None:
        break;

    player = 'O'
    
    for items in event.get():
        
        if items.type == QUIT:
            game_on = False
        
        if winner!= None:
            game_on = False
        
        if(count >= 9):
            game_on = False
        
        if items.type == MOUSEBUTTONDOWN:
            if mouse.get_pressed()[0]:
              position = mouse.get_pos()
              
              if position[0] > 310 and position[0] < 310 + 150 and(position[1] > 780 and position[1] < 768 + 50): # reset
                    grid1.grid =[[0,0,0],[0,0,0],[0,0,0]]
                    count = 0
              
              elif (position[1] > 770 and position[1] < 900):
                    game_on = True
              
              else:
                l = [0,1,2]
                x = position[0]//256
                y = position[1]//256
                
                if player == 'O' and grid1.grid[y][x] == 0:
                    count += 1
                    grid1.get_mouse(x, y, player)
                    player = 'X'
                
                while(once==0 and count!= 9):#when count is 9 loop shouldnot be executed 
                       i = random.choice(l)
                       j = random.choice(l)
                       
                       if player == 'X' and grid1.grid[j][i] == 0 and once == 0:
                          grid1.get_mouse(i,j, player)#this is printing
                          count += 1
                          once += 1

    board.fill((255,255,0))
    grid1.sketch(board)
    button(board)
    display.flip()
  
  if count == 9:
    
    winner = win(player, grid1.grid)
    
    if winner == 'X':
        gameover("   X Wins")
    
    elif winner == 'O':
        gameover("   O Wins")
    
    else:
        gameover("     TIE!")
  
  if winner == "X":
    gameover("   X Wins")

  if winner == "O":
    gameover("   O Wins")

