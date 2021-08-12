from pygame import *
from Grid import *
from os import *
from over import *
from Exit import *

# changing the default screen position.(origin - TOP LEFT)
environ['SDL_VIDEO_WINDOW_POS'] = '400,40'
grid = grid()

Tie = None
winner = None

player = 'O'  # DIFFERENT FROM THE PLAYER THAT WILL START

init()
board = display.set_mode((768, 868))  # SIZE OF WINDOW
display.set_caption("Tic Tac Toe")
game_on = True
count = 0

while(game_on):
    for items in event.get():
        
        if items.type == QUIT:  # for x button in window
            game_on = False
        
        winner = win(player, grid.grid)
        
        if(count == 9):
            # ALL OCCUPIED BLOCKS
            print("ITS A TIE")
            game_on = False
        
        if(winner != None):
            # print(winner+"wins!!")
            game_on = False    
        
        if items.type == MOUSEBUTTONDOWN:
            # print(mouse.get_pressed())
            if mouse.get_pressed()[0]:
                click_position = mouse.get_pos()
                xcell = click_position[0]//256
                ycell = click_position[1]//256
                # to make sure that on clicking on the already occupied block does not change the player .and on clicking next on the valid(empty)
                #print str(xcell) + "  " + str(ycell)
                if player == 'X' and grid.grid[ycell][xcell] == 0:
                    # prints the alternate (if previous x then next 0 )
                    player = "O"
                    count += 1  # number of filled blocks
                
                elif player == "O" and grid.grid[ycell][xcell] == 0:
                    player = "X"
                    count += 1  # number of filled blocks
                
                grid.get_mouse(xcell, ycell, player)
                # grid.print_grid()

    board.fill((255, 255, 0))  # color
    grid.sketch(board)  # draw grid
    display.flip()  # updates the entire screen (color not showing without it)

if count == 9:
    
    if winner == 'X':
        gameover("X Wins")
    
    if winner == 'O':
        gameover("O Wins")
    
    if winner == None:
        gameover("  TIE!")

if winner == "X":
    gameover("X Wins")

if winner == "O":
    gameover("O Wins")
