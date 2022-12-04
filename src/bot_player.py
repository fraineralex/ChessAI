import ast
import datetime
import pygame

from const import *
from game import Game
from square import Square
from move import Move
from dragger import Dragger
from board import Board
from traslate_move import TraslateMove
from minimax import Minimax

class BotPlayer:

    def __init__(self):
        self.test = 'd'


    def Minimax(self, screen, game: Game, board: Board, dragger: Dragger, minimax_board):

        if(game.next_player == 'black'):
            
            time_before = datetime.datetime.now()

            game.show_bg(screen)
            game.show_last_move(screen)
            game.show_moves(screen)
            game.show_pieces(screen)
            game.show_hover(screen)

            if dragger.dragging:
                dragger.update_blit(screen)

            minimaxResult = Minimax.main('', game.next_player, minimax_board, time_before)
            move = str(minimaxResult[0])
            minimax_board = minimaxResult[1]
            print(f'Move Bot: {move}')
            origin_location = TraslateMove.traslate_to_interface(move[0], move[1])
            destine_location = TraslateMove.traslate_to_interface(move[2], move[3])
            #origin_location = ast.literal_eval(input('😃 Enter your origin location (col, row): '))
            #destine_location = ast.literal_eval(input("😃 Enter yout destine location (col, row): "))
            print(f'Origin: {origin_location} Destine: {destine_location}')

            event_pos = (origin_location[0]*100, origin_location[1]*100)

            dragger.update_mouse(event_pos)

            clicked_col = origin_location[0]
            clicked_row = origin_location[1]

            # if clicked square has a piece ?
            if board.squares[clicked_row][clicked_col].has_piece():
                piece = board.squares[clicked_row][clicked_col].piece
                # valid piece (color) ?
                if piece.color == game.next_player:
                    board.calc_moves(piece, clicked_row, clicked_col, bool=True)
                    dragger.save_initial(event_pos)
                    dragger.drag_piece(piece)
                    # show methods 
                    game.show_bg(screen)
                    game.show_last_move(screen)
                    game.show_moves(screen)
                    game.show_pieces(screen)

                
                if dragger.dragging:
                    dragger.update_mouse(event_pos)

                    released_col = destine_location[0]
                    released_row = destine_location[1]

                    # create possible move
                    initial = Square(origin_location[1], origin_location[0])
                    final = Square(released_row, released_col)
                    move = Move(initial, final)

                    # valid move ?
                    if board.valid_move(dragger.piece, move):
                        # normal capture
                        captured = board.squares[released_row][released_col].has_piece()
                        board.move(dragger.piece, move)

                        board.set_true_en_passant(dragger.piece)                            

                        # sounds
                        game.play_sound(captured)
                        # show methods
                        game.show_bg(screen)
                        game.show_last_move(screen)
                        game.show_pieces(screen)
                        # next turn
                        game.next_turn()
                    
                    dragger.undrag_piece()

            return minimax_board