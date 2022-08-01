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
        # Make a move if valid
        piece_row, piece_col = self._user_input()

        # Drop piece
        self._drop_piece(piece_row, piece_col)

        # Check if game over
        if self._check_gameover(piece_row, piece_col):
            return True

        # Swith Player
        self.turn = self._switch_player()
            

        return False # Return false if game not over
    

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
            print(f'Column {sel_col + 1} is full.')
            self._user_input()

    def _drop_piece(self, row, column):
        self.board[row][column] = self.turn.symbol
        print(self.board)

    def _check_gameover(self, piece_row, piece_col):

        for i in range(COLUMN_COUNT - 3):
            
            # Check horizontal
            tile = self.board[piece_row][i:i+4]
            if np.count_nonzero(tile == self.turn.symbol) == len(tile):
                return True
        
            # Check vertical
            tile = self.board.transpose()[piece_col][i:i+4]
            if np.count_nonzero(tile == self.turn.symbol) == len(tile):
                return True
            
        # Check / diagonal
        for r in range(5,2,-1):
            for c in range(COLUMN_COUNT - 3):
                if self.board[r][c] == self.board[r-1][c+1] == self.board[r-2][c+2] == self.board[r-3][c+3] == self.turn.symbol:
                    return True
        
        # Check \ diagonal
            

        return False
    
        
    
    
    def _switch_player(self):
        if self.turn == PLAYER_1: 
            return PLAYER_2
        else:
            return PLAYER_1
        






game = Connect_four() 

# Game loop
game_over = False
while game_over == False:
    game_over = game.play_step()
    
   
    if game_over == True:
        break

print('game over')
pygame.quit()