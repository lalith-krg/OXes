import pygame
def button(board):
        color = (255,0,0)
        x = 310
        y = 780
        width = 150
        height = 50
        text = "RESET"
        pygame.draw.rect(board,(0,0,0), (x-2,y-2,width+4,height+4),5)    
        pygame.draw.rect(board, color, (x,y,width,height),0)
        font = pygame.font.SysFont('comicsans',60)
        text = font.render(text,1,(0,0,0))
        board.blit(text,(x + (width/2 - text.get_width()/2), y + (height/2 - text.get_height()/2)))
        
