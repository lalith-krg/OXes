import socket
import threading
from pygame import *
from Grid import *
from os import *
from over import *
from Exit1 import *
from button import *
from single import *
import sys

thread = None

# creating thread function for running the background communication while game is being played
def make_thread(tar):
    global thread
    thread = threading.Thread(target = tar)
    thread.daemon = True
    thread.start()

# creating a socket for server-client connection
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
port = 0
port = int(sys.argv[1]) # input port number

s.bind( ('127.0.0.1', port) )

# to play single player against computer, port is 0
if port == 0:
    play_alone()
    sys.exit()

s.listen(1)

conn, add = None, None
conn_active = False

# changing the default screen position.(origin - TOP LEFT)
environ['SDL_VIDEO_WINDOW_POS'] = '100,200'
grid = grid()

# initialising all required global variables
turn = True
player = 'X'
winner = None
count = 0
game_on = True

# the function run if the game is over
def finish():
    global winner, count
    if count == 9:
        if winner == 'X':
            gameover("-You Won!-")
    
        if winner == 'O':
            gameover("-You Lost!-")
    
        if winner == None:
            gameover("    -TIE!-")

    if winner == "X":
        gameover("-You Won!-")

    if winner == "O":
        gameover("-You Lost!-")


# the game to play the function
def play_game():

    Tie = None

    init()
    board = display.set_mode((770, 850))  # SIZE OF WINDOW
    display.set_caption("Tic Tac Toe: Server")
    
    global turn, player, count, game_on, winner
    
    # game runs till the end
    while(game_on):
        
        for items in event.get():
            
            # if the game has ended
            if(count == 9):
                # ALL OCCUPIED BLOCKS
                print("ITS A TIE")
                game_on = False
                break
            
            # checking if the opponent has won
            winner = win('O', grid.grid)
            if winner != None:
                game_on = False
                break
            
            # if close button is clicked
            if items.type == QUIT:
                game_on = False
                sdata = '0 0 quit'
                conn.send(sdata)
                pygame.quit()
                sys.exit()
            
            # if any other space in the grid or reset is clicked
            if items.type == MOUSEBUTTONDOWN and conn_active:
                
                if mouse.get_pressed()[0] and turn:
		    
                    # getting the click locations
                    click_position = mouse.get_pos()
                    xcell = click_position[0]//256
                    ycell = click_position[1]//256
                    
                    # condition for reset button
                    if mouse.get_pressed()[0] and click_position[0] > 310 and click_position[0] < 310 + 150 and(click_position[1] > 780 and click_position[1] < 780 + 50): # reset
                        grid.grid =[[0,0,0],[0,0,0],[0,0,0]]
                        count = 0
                        turn = False
                        sdata = '0 0 reset'
                        print sdata
                        conn.send(sdata)

                    # if clicked in the grid
                    elif xcell<=2 and ycell <=2:
                        print str(xcell) + ' ' + str(ycell)
                        grid.get_mouse(xcell, ycell, player)
                        
                        # checking if the player won
                        winner = win(player, grid.grid)
                        print winner
                        if winner != None:
                            sdata = '{} {} over'.format(xcell, ycell)
                            print sdata
                            conn.send(sdata)
                            game_on = False
                            break
    
                        else:
                            sdata = '{} {} play'.format(xcell, ycell)
                            print type(sdata)
                            print sdata
                            conn.send(sdata)
                        
                        # to not let the current user play till the other player plays
                        turn = False
                        count += 1
                        print count
                    
        # updating the entire grid 
        board.fill((255, 255, 0))  # color
        grid.sketch(board)  # draw grid
        button(board)
        display.flip()  # updates the entire screen (color not showing without it)

    # once game is over call finish
    finish()

# function to recieve data
def recv_data():
    make_thread(play_game)  # creating a thread
    global turn, count, game_on, winner

    while True:
        if conn != None:
            data = conn.recv(128).split(' ')
            print data
            x, y = int(data[0]), int(data[1])
            print str(x) + ' ' + str(y)
            
            # checking various conditions and placing the respective sign in the grid
            if grid.get_cell_value(x, y) == 0:
                grid.set_cell_value(x, y, 'O')
                count += 1
                turn = True
            
            # checkng for reset
            if data[2] == 'reset':
                grid.grid =[[0,0,0],[0,0,0],[0,0,0]]
                count = 0
                turn = True

            # checking for quit
            elif data[2] == 'quit':
                pygame.quit()
                sys.exit()
                break

# run for establishing connection
def wait_conn():
    global conn, add, conn_active
    conn, add = s.accept()
    print 'Conn established'
    print str(conn) + ' ' + str(add)
    conn_active = True
    print conn_active
    recv_data()

# calling the connection function
wait_conn()

