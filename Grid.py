from pygame import *
from os import *
X=image.load(path.join('img','x.png'))
O=image.load(path.join('img','o.png'))
class grid :
    def __init__(self):
        self.lines =[((0,256),(768,256)), # 1st horizontal line
                     ((0,512),(768,512)),  # 2nd horizontal line
                     ((256,0),(256,768)),  # 1st vertical line
                     ((512,0),(512,768)),  # 2nd vertical line
                     ((0,0),(768,0)),
                     ((0,0),(0,768)),
                     ((768,0),(768,768)) 
                      #end1coo,end2coo
                    ] 
        self.grid =[[0,0,0],[0,0,0],[0,0,0]]      
    
    def sketch(self,board):
        for line in self.lines:
            draw.line( board,(0,0,0),line[0],line[1],5)
            #          screen,(color),end1,end2,thickness
        for y in range(3):
            for x in range(3):
                if self.grid[y][x]=='X':
                    board.blit(X,(x*256 ,y*256)) # DISPLAY X ON SCREEN
                elif self.grid[y][x]=='O':
                    board.blit(O,(x*256 ,y*256)) # DISPLAY O ON SCREEN
     
    def get_mouse(self,x,y,player):
        if self.grid[y][x]==0:
          if player=='X':
              self.grid[y][x]='X'
          elif player=='O':
              self.grid[y][x]='O'        
    
    def print_grid(self) :
       for row in self.grid :
        print(row)         
    
    def get_cell_value(self, x, y):
        return self.grid[y][x]

    def set_cell_value(self, x, y, value):
        self.grid[y][x] = value
