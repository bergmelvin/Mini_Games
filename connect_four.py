from random import random
import numpy as np
import pygame
import math
import random

class Player:
    def __init__(self, name, symbol, color):
        self.name = name
        self.symbol = symbol
        self.color = color





# ----- GLOBAL VARIABLES -----
ROW_COUNT = 6
COLUMN_COUNT = 7
BLOCK_SIZE = 100
RADIUS = (BLOCK_SIZE/2) - 10 
DISPLAY_W = BLOCK_SIZE * COLUMN_COUNT
DISPLAY_H = BLOCK_SIZE * (ROW_COUNT + 1)

# Rgb colors
WHITE = (255, 255, 255)
RED = (200,0,0)
YELLOW = (255,255,0)
BLUE1 = (0, 0, 255)
BLUE2 = (0, 100, 255)
BLACK = (0,0,0)

# Players
PLAYER_1 = Player('Player_1', 1, RED)
PLAYER_2 = Player('Player_2', 2, YELLOW)


# ----- FUNCTIONS -----
def create_board(symbol = 0):
    board = [[symbol for col in range(7)] for col in range(6)]

    return board

def valid_location(board, sel_col):
    if board[0][sel_col] == 0:
        return True

def _drop_piece(board, sel_col, turn):
    print(turn)
    # If column is empty
    if board[ROW_COUNT-1][sel_col] == 0:
        board[ROW_COUNT-1][sel_col] = turn.symbol

        return board

    # If column is NOT empty
    for row in range(ROW_COUNT):
        if board[row][sel_col] != 0:
            board[row-1][sel_col] = turn.symbol

            break
            
    return board

def _update_ui(surface, board, sel_col, turn):
    # Find current move
    for row in range(ROW_COUNT):
        if board[row][sel_col] != 0:
            pygame.draw.circle(surface, turn.color, (((BLOCK_SIZE * sel_col) + BLOCK_SIZE/2), ((BLOCK_SIZE * row) + BLOCK_SIZE * 1.5)), RADIUS)

            break
    
    pygame.display.flip()

def _check_gameover(board, turn):
    # Check horizontal
    for r in range(ROW_COUNT):
        for c in range(COLUMN_COUNT - 3):
            if board[r][c] == board[r][c+1] == board[r][c+2] == board[r][c+3] == turn.symbol:
                return True
    
    # Check vertical
    for r in range(ROW_COUNT - 3):
        for c in range(COLUMN_COUNT):
            if board[r][c] == board[r+1][c] == board[r+2][c] == board[r+3][c] == turn.symbol:
                return True
    # Check / diagonal
    for r in range(5,2,-1):
        for c in range(COLUMN_COUNT - 3):
            if board[r][c] == board[r-1][c+1] == board[r-2][c+2] == board[r-3][c+3] == turn.symbol:
                return True
    
    # Check \ diagonal
    for r in range(3):
        for c in range(4):
            if board[r][c] == board[r+1][c+1] == board[r+2][c+2] == board[r+3][c+3] == turn.symbol:
                return True
        
    return False

def _switch_player(turn):
    if turn == PLAYER_1:
        turn = PLAYER_2
    else:
        turn = PLAYER_1
    
    return turn


def main():


    # ----- INIT GAME STATE -----
    board = create_board()

    # Do some drawing
    surface = pygame.display.set_mode((DISPLAY_W, DISPLAY_H))
    pygame.display.set_caption('Connect Four')
    surface.fill(WHITE)
    pygame.draw.rect(surface, BLUE1, pygame.Rect(0, BLOCK_SIZE, DISPLAY_W, DISPLAY_H - BLOCK_SIZE))

    for row in range(ROW_COUNT):
        for col in range (COLUMN_COUNT):
            pygame.draw.circle(surface, WHITE, ((BLOCK_SIZE * col) + BLOCK_SIZE/2, (BLOCK_SIZE * row) + (BLOCK_SIZE * 1.5)), RADIUS)

    pygame.display.flip()

    # Init turn
    if (f'PLAYER_{random.randint(1,2)}') == 'PLAYER_1':
        turn = PLAYER_1
    else:
        turn = PLAYER_2


    

    # ----- GAME LOOP -----
    game_over = False
    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    game_over = True
        
        

        # ----- USER INPUT -----
            # Select column with a mouseclick event
            if event.type == pygame.MOUSEBUTTONDOWN:
                sel_col = math.floor(event.pos[0] // BLOCK_SIZE)

                if valid_location(board, sel_col):

                    # 1. Drop piece
                    board = _drop_piece(board, sel_col, turn)
                    
                    # 2. Update UI
                    _update_ui(surface, board, sel_col, turn)
                    
                    # 3. Check if game over
                    game_over = _check_gameover(board, turn)

                    # 4. Switch player
                    turn = _switch_player(turn)
                    

       
    pygame.quit()



if __name__ == '__main__':
    main()


