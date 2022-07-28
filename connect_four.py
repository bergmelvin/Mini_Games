# Ta det launa
import pygame
import numpy as np

pygame.init()
font = pygame.font.SysFont('comicsans', 30)

# rgb colors
WHITE = (255, 255, 255)
RED = (200,0,0)
BLUE1 = (0, 0, 255)
BLUE2 = (0, 100, 255)
BLACK = (0,0,0)


class Connect_four:
    def __init__(self, width = 600, heigth = 600):
        self.width = width
        self.heigth = heigth

        # Print board
        self.board = np.zeros((6,7), dtype=int)
        self.board[0][0] = 8
        print(self.board)

        # Init display
        self.surface = pygame.display.set_mode(self.width, self.heigth)
        self.surface.fill(WHITE)





# Game loop
game_running = True
while game_running:
    game = Connect_four()
    
    
    
    
    
    
    # Pygame events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_running = False
            pygame.quit()



