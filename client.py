import socket
import threading
from pygame import *
from Grid import *
from os import *
from over import *
from Exit2 import *
from button import *
import sys

# creating socket for server-client connection
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('127.0.0.1', int(sys.argv[1])))

# changing the default screen position.(origin - TOP LEFT)
environ['SDL_VIDEO_WINDOW_POS'] = '900,200'
grid = grid()

# initialising all global variables
turn = False
player = 'O'
winner = None
count = 0
game_on = True

# to be run if game is over
def finish():
    global winner, count
    if count == 9:

        if winner == 'X':
            gameover("-You Lost!-")

        if winner == 'O':
            gameover("-You Won!-")

        if winner == None:
            gameover("    -TIE!-")

    if winner == "X":
        gameover("-You Lost!-")
    
    if winner == "O":
        gameover("-You Won!-")

# funciton to play the game
def play_game():

    Tie = None

    init()
    board = display.set_mode((770, 850))  # SIZE OF WINDOW
    display.set_caption("Tic Tac Toe: Client")
    global turn, player, winner, count, game_on
    
    # runs as long as game is finished or closed
    while(game_on):
        for items in event.get():
    
            if(count == 9):
                # ALL OCCUPIED BLOCKS
                print("ITS A TIE")
                game_on = False
            
            # checking if the opponent won
            winner = win('X', grid.grid)
            if winner != None:
                game_on = False
                break
            
            # if the window is closed
            if items.type == QUIT:
                game_on = False
                sdata = '0 0 quit'
                s.send(sdata)
                pygame.quit()
                sys.exit()
            
            # if the mouse button is clicked
            if items.type == MOUSEBUTTONDOWN:
                if mouse.get_pressed()[0] and turn:
                    
                    click_position = mouse.get_pos()
                    xcell = click_position[0]//256
                    ycell = click_position[1]//256

                    # if reset button is clicked
                    if mouse.get_pressed()[0] and click_position[0] > 310 and click_position[0] < 310 + 150 and(click_position[1] > 780 and click_position[1] < 780 + 50): # reset
                        grid.grid =[[0,0,0],[0,0,0],[0,0,0]]
                        count = 0
                        turn = False
                        sdata = '0 0 reset'
                        print sdata
                        s.send(sdata)
                    
                    # if anywhere in the grid is clicked
                    elif(xcell<=2 and ycell<=2):
                        print str(xcell) + ' ' + str(ycell)
                        grid.get_mouse(xcell, ycell, player)
                        
                        # checking if the player won
                        winner = win(player, grid.grid)
                        print winner

                        if winner != None:
                            sdata = '{} {} over'.format(xcell, ycell)
                            s.send(sdata)
                            game_on = False
                            break

                        else:
                            sdata = '{} {} play'.format(xcell, ycell)
                            print type(sdata)
                            print sdata
                            s.send(sdata)
                    
                        print winner
                        turn = False
                        count += 1
                        print count
        
        # updating the entire grid
        board.fill((255, 255, 0))  # color
        grid.sketch(board)  # draw grid
        button(board)
        display.flip() # updates the entire screen (color not showing without it)
    
    # when game ends
    finish()

# function to create thread and to be run in the background while game is being played
def make_thread(target):
    thread = threading.Thread(target = target)
    thread.daemon = True
    thread.start()

# to recieve data
def recv_data():
    global turn, count, game_on
    make_thread(play_game)
    while True:
        data = s.recv(128).split(' ')
        print data
        x, y = int(data[0]), int(data[1])
        print str(x) + ' ' + str(y)
        
        # placing the opponet's sign in the grid
        if grid.get_cell_value(x, y) == 0:
            grid.set_cell_value(x, y, 'X')
            count += 1
            turn = True

        # if reset button was pressed
        if data[2] == 'reset':
            grid.grid =[[0,0,0],[0,0,0],[0,0,0]]
            count = 0
            turn = True

        # if the game was quit
        elif data[2] == 'quit':
            pygame.quit()
            sys.exit()
            break

# running the recieve data function once game is connected
recv_data()


