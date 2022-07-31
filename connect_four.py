# Ta det launa
from tracemalloc import start
import pygame
import random
import numpy as np

ROW_COUNT = 6
COLUMN_COUNT = 7

# rgb colors
WHITE = (255, 255, 255)
RED = (200,0,0)
BLUE1 = (0, 0, 255)
BLUE2 = (0, 100, 255)
BLACK = (0,0,0)

class Player:
    def __init__(self, name, symbol):
        self.name = name
        self.symbol = symbol

PLAYER_1 = Player('Player_1', 'X')
PLAYER_2 = Player('Player_2', 'O')        




class Connect_four:
    def __init__(self, width = 600, heigth = 600):
        self.width = width
        self.heigth = heigth
        
        # Print board
        self.board = np.zeros((ROW_COUNT, COLUMN_COUNT) ,dtype=object)
        print(self.board, end='\n\n')

        # Init turn and symbol
        if random.randint(1,2) == 1:
            self.turn = PLAYER_1
        else:
            self.turn = PLAYER_2
        


    def play_step(self):
        # Return move if valid
        row, column = self._user_input()

        # Drop piece
        self._drop_piece(row, column)

        # Swith Player
        self.turn = self._switch_player()
    
        
        
        
        return True # Returns true if game continues
    

    def _user_input(self):
        sel_col = int(input('\033[1m' + self.turn.name + '\033[0m' + f', Please select a column by typing a number between 1-{COLUMN_COUNT}: ')) - 1

        if self.board[0][sel_col] == 0:
        # If Column is not full
            for i in range(ROW_COUNT):
                if self.board[i][sel_col] == 'X' or self.board[i][sel_col] == 'O':
                    return i-1, sel_col
            if self.board[ROW_COUNT - 1][sel_col] == 0:
                return ROW_COUNT - 1, sel_col
        
        # If column is full
        else:
            print(f'Column 2 {sel_col} is full.')
            self._user_input()

    def _drop_piece(self, row, column):
        self.board[row][column] = self.turn.symbol
        print(self.board)

    def _switch_player(self):
        if self.turn == PLAYER_1: 
            return PLAYER_2
        else:
            return PLAYER_1
        






game = Connect_four() 

# Game loop
game_running = True
while game_running:
    game_running = game.play_step()
    
   
    if game_running == False:
        break



pygame.quit()