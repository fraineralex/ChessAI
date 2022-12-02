from const import *
from game import Game
from square import Square
from move import Move
import pygame
from piece import Piece

class BotPlayer:

    def __init__(self):
        self.game = Game()
        self.screen = pygame.display.set_mode( (WIDTH, HEIGHT) )

    def bot_player():

        print("🤖 It's my turn")

        game = Game()
        board = game.board
        dragger = game.dragger
        screen = pygame.display.set_mode( (WIDTH, HEIGHT) )
        piece = Piece('pawn', 'black', -1.0, 'assets/images/imgs-128px/black_pawn.png')
        
        if True:
            dragger.update_mouse((430, 317))

            released_row = 3
            released_col = 4

            # create possible move
            initial = Square(1, 4)
            final = Square(3, 4)
            move = Move(initial, final)

            # valid move ?
            if board.valid_move(piece, move):
                # normal capture
                captured = board.squares[released_row][released_col].has_piece()
                board.move(piece, move)

                board.set_true_en_passant(piece)                            

                # sounds
                game.play_sound(captured)
                # show methods
                game.show_bg(screen)
                game.show_last_move(screen)
                game.show_pieces(screen)
                # next turn
                game.next_turn()
                print('All right! :D')