import pygame  
from os import *
import sys
G=pygame.image.load(path.join('img','G2.png'))
def gameover(msg):
    environ['SDL_VIDEO_WINDOW_POS'] = '900,40'
    pygame.init()
    board = pygame.display.set_mode((768, 768))  # SIZE OF WINDOW
    pygame.display.set_caption("GAME OVER !!")
    board = pygame.display.set_mode((768,768))
    font =pygame.font.SysFont('sitkasmallsitkatextsitkasubheadingsitkaheadingsitkadisplaysitkabanner',150)
    font.set_bold(True)
    text=font.render(msg,True,(0,0,0))
    notexit = True
    while(notexit):
        for items in pygame.event.get():
            if items.type == pygame.QUIT:  # for x button in window
                notexit = False
                pygame.quit()
		sys.exit()
                return
        board.fill((255, 255, 0))  # color
        board.blit(G,(120,0))
        board.blit(text,[60,550])
        pygame.display.flip()
#gameover()
#print(pygame.font.get_fonts())        
#'sitkasmallsitkatextbolditalicsitkasubheadingbolditalicsitkaheadingbolditalicsitkadisplaybolditalicsitkabannerbolditalic'
#'sitkasmallsitkatextboldsitkasubheadingboldsitkaheadingboldsitkadisplayboldsitkabannerbold'
