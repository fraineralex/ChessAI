import datetime
import time
import chess
import pygame
import sys

from const import *
from game import Game
from minimax import Minimax
from square import Square
from move import Move
from bot_player import BotPlayer
from traslate_move import TraslateMove

class Main:

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode( (WIDTH, HEIGHT) )
        pygame.display.set_caption('Chess')
        self.game = Game()

    def mainloop(self):
        
        screen = self.screen
        game = self.game
        board = self.game.board
        dragger = self.game.dragger
        minimax_board = chess.Board()
        time_before = datetime.datetime.now()
        limit_minimax_time = 10

        while True:
            #First player
            #############################

            # show methods
            game.show_bg(screen)
            game.show_last_move(screen)
            game.show_moves(screen)
            game.show_pieces(screen)
            game.show_hover(screen)

            if dragger.dragging:
                dragger.update_blit(screen)

            
            for event in pygame.event.get():

                # click
                if event.type == pygame.MOUSEBUTTONDOWN:
                    dragger.update_mouse(event.pos)

                    clicked_row = dragger.mouseY // SQSIZE
                    clicked_col = dragger.mouseX // SQSIZE

                    # if clicked square has a piece ?
                    if board.squares[clicked_row][clicked_col].has_piece():
                        piece = board.squares[clicked_row][clicked_col].piece
                        # valid piece (color) ?
                        if piece.color == game.next_player:
                            board.calc_moves(piece, clicked_row, clicked_col, bool=True)
                            dragger.save_initial(event.pos)
                            dragger.drag_piece(piece)
                            # show methods 
                            game.show_bg(screen)
                            game.show_last_move(screen)
                            game.show_moves(screen)
                            game.show_pieces(screen)
                
                # mouse motion
                elif event.type == pygame.MOUSEMOTION:
                    motion_row = event.pos[1] // SQSIZE
                    motion_col = event.pos[0] // SQSIZE

                    game.set_hover(motion_row, motion_col)

                    if dragger.dragging:
                        dragger.update_mouse(event.pos)
                        # show methods
                        game.show_bg(screen)
                        game.show_last_move(screen)
                        game.show_moves(screen)
                        game.show_pieces(screen)
                        game.show_hover(screen)
                        dragger.update_blit(screen)
                
                # click release
                elif event.type == pygame.MOUSEBUTTONUP:
                    
                    if dragger.dragging:
                        dragger.update_mouse(event.pos)

                        released_row = dragger.mouseY // SQSIZE
                        released_col = dragger.mouseX // SQSIZE

                        # create possible move
                        initial = Square(dragger.initial_row, dragger.initial_col)
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

                            time_after = datetime.datetime.now()
                            answerTime = time_after - time_before
                            
                            # Minimax call
                            human_origin_location = TraslateMove.traslate_to_minimax(dragger.initial_col, dragger.initial_row)
                            human_destine_location = TraslateMove.traslate_to_minimax(released_col, released_row)
                            human_move = f'{human_origin_location}{human_destine_location}'
                            minimax_board = Minimax.main(human_move, game.next_player, minimax_board)
                            if(minimax_board == None):
                                pygame.quit()
                                sys.exit()
                            print(f'Person time: {answerTime.seconds} segundos')

                            # next turn
                            game.next_turn()

                            
                    
                    dragger.undrag_piece()
                
                elif(game.next_player == 'black'):

                    ##########################################
                    #-------------Second player------------#
                    ##########################################
                    botPlayer = BotPlayer()
                    minimax_board = botPlayer.main(screen, game, board, dragger, minimax_board, limit_minimax_time )
                    time_before = datetime.datetime.now()
                    if(minimax_board == 'Game over'):
                        pygame.quit()
                        sys.exit()

                # key press
                elif event.type == pygame.KEYDOWN:

                    # changing themes
                    if event.key == pygame.K_t:
                        game.change_theme()

                     # reset game
                    if event.key == pygame.K_r:
                        game.reset()
                        game = self.game
                        board = self.game.board
                        dragger = self.game.dragger

                # quit application
                elif event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            
            pygame.display.update()


main = Main()
main.mainloop()