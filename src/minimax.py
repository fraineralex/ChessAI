import datetime
import chess
#import sunfish
from numpy import Infinity, flip

from game import Game

class Minimax:

    def reverseArray(array): 
        return flip(array)

    pawnEvalWhite = [
    [ 0.0,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0],
    [ 5.0,  5.0,  5.0,  5.0,  5.0,  5.0,  5.0,  5.0],
    [ 1.0,  1.0,  2.0,  3.0,  6.0,  2.0,  1.0,  1.0],
    [ 0.5,  0.5,  1.0,  2.5,  2.5,  1.0,  0.5,  0.5],
    [ 0.0,  0.0,  0.0,  2.0,  2.0,  0.0,  0.0,  0.0],
    [ 0.5, -0.5, -1.0,  0.0,  0.0, -1.0, -0.5,  0.5],
    [ 0.5,  1.0,  1.0, -2.0, -2.0,  1.0,  1.0,  0.5],
    [ 0.0,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0]
    ];

    pawnEvalBlack = reverseArray(pawnEvalWhite);

    knightEval = [
        [-5.0, -4.0, -3.0, -3.0, -3.0, -3.0, -4.0, -5.0],
        [-4.0, -2.0,  0.0,  0.0,  0.0,  0.0, -2.0, -4.0],
        [-3.0,  0.0,  1.0,  1.5,  1.5,  1.0,  0.0, -3.0],
        [-3.0,  0.5,  1.5,  2.0,  2.0,  1.5,  0.5, -3.0],
        [-3.0,  0.0,  1.5,  2.0,  2.0,  1.5,  0.0, -3.0],
        [-3.0,  0.5,  1.0,  1.5,  1.5,  1.0,  0.5, -3.0],
        [-4.0, -2.0,  0.0,  0.5,  0.5,  0.0, -2.0, -4.0],
        [-5.0, -4.0, -3.0, -3.0, -3.0, -3.0, -4.0, -5.0]
    ];

    bishopEvalWhite = [
        [-2.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -2.0],
        [-1.0,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0, -1.0],
        [-1.0,  0.0,  0.5,  1.0,  1.0,  0.5,  0.0, -1.0],
        [-1.0,  0.5,  0.5,  1.0,  1.0,  0.5,  0.5, -1.0],
        [-1.0,  0.0,  1.0,  1.0,  1.0,  1.0,  0.0, -1.0],
        [-1.0,  1.0,  1.0,  1.0,  1.0,  1.0,  1.0, -1.0],
        [-1.0,  0.5,  0.0,  0.0,  0.0,  0.0,  0.5, -1.0],
        [-2.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -2.0]
    ];

    bishopEvalBlack = reverseArray(bishopEvalWhite);

    rookEvalWhite = [
        [ 0.0,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0],
        [ 0.5,  1.0,  1.0,  1.0,  1.0,  1.0,  1.0,  0.5],
        [-0.5,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0, -0.5],
        [-0.5,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0, -0.5],
        [-0.5,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0, -0.5],
        [-0.5,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0, -0.5],
        [-0.5,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0, -0.5],
        [ 0.0,  0.0,  0.0,  0.5,  0.5,  0.0,  0.0,  0.0]
    ];

    rookEvalBlack = reverseArray(rookEvalWhite);

    queenEval = [
        [-2.0, -1.0, -1.0, -0.5, -0.5, -1.0, -1.0, -2.0],
        [-1.0,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0, -1.0],
        [-1.0,  0.0,  0.5,  0.5,  0.5,  0.5,  0.0, -1.0],
        [-0.5,  0.0,  0.5,  0.5,  0.5,  0.5,  0.0, -0.5],
        [ 0.0,  0.0,  0.5,  0.5,  0.5,  0.5,  0.0, -0.5],
        [-1.0,  0.5,  0.5,  0.5,  0.5,  0.5,  0.0, -1.0],
        [-1.0,  0.0,  0.5,  0.0,  0.0,  0.0,  0.0, -1.0],
        [-2.0, -1.0, -1.0, -0.5, -0.5, -1.0, -1.0, -2.0]
    ];

    kingEvalWhite = [
        [-3.0, -4.0, -4.0, -5.0, -5.0, -4.0, -4.0, -3.0],
        [-3.0, -4.0, -4.0, -5.0, -5.0, -4.0, -4.0, -3.0],
        [-3.0, -4.0, -4.0, -5.0, -5.0, -4.0, -4.0, -3.0],
        [-3.0, -4.0, -4.0, -5.0, -5.0, -4.0, -4.0, -3.0],
        [-2.0, -3.0, -3.0, -4.0, -4.0, -3.0, -3.0, -2.0],
        [-1.0, -2.0, -2.0, -2.0, -2.0, -2.0, -2.0, -1.0],
        [ 2.0,  2.0,  0.0,  0.0,  0.0,  0.0,  2.0,  2.0],
        [ 2.0,  3.0,  1.0,  0.0,  0.0,  1.0,  3.0,  2.0]
    ];

    kingEvalBlack = reverseArray(kingEvalWhite);

    def minimaxRoot(board: chess.Board, depth, maximizingPlayer, time_before: datetime.datetime, limit_time):
        possibleMoves = board.legal_moves
        bestMove = float("-inf")
        bestMoveFound = None
        
        for possible_move in possibleMoves:
            time_after = datetime.datetime.now()
            move = chess.Move.from_uci(str(possible_move))
            board.push(move)
            value = Minimax.minimax(board, depth-1, float("-inf"), float("inf"), not maximizingPlayer, time_before, limit_time, 'black')
            board.pop()
            if( value >= bestMove):
                bestMove = value
                bestMoveFound = move
                print("Best move for now: ",str(bestMoveFound))
                answerTime = time_after - time_before
                if(answerTime.seconds >= limit_time):
                    return bestMoveFound
                

        return bestMoveFound

    def minimax(board: chess.Board, depth, alpha, beta, maximizingPlayer, time_before: datetime.datetime, limit_time, turn):
        time_after = datetime.datetime.now()
        answerTime = time_after - time_before
        if(depth == 0 or answerTime.seconds >= limit_time):
            # Heuristic evaluation
            node_evaluation = 0
            node_evaluation += Minimax.check_status(board, node_evaluation, turn)
            node_evaluation += Minimax.evaluationBoard(board)
            node_evaluation += Minimax.checkmate_status(board, turn)
            node_evaluation += Minimax.good_square_moves(board, turn)
            #print('Node puntuation: ',node_evaluation)
            return -node_evaluation

        possibleMoves = board.legal_moves

        if(maximizingPlayer):
            bestMove = float("-inf")

            for possibleMove in possibleMoves:
                time_after = datetime.datetime.now()
                move = chess.Move.from_uci(str(possibleMove))
                board.push(move)
                value = Minimax.minimax(board, depth-1, alpha, beta, False, time_before, limit_time, 'black')
                bestMove = max(bestMove, value)
                board.pop()
                alpha = max(alpha, value);
                if (beta <= alpha):
                    #board.pop();
                    #break;
                    return bestMove
                
                answerTime = time_after - time_before
                if(answerTime.seconds >= limit_time):
                    return bestMove

                #board.pop()

            return bestMove

        else:
            bestMove = float("inf")
            for possibleMove in possibleMoves:
                time_after = datetime.datetime.now()
                move = chess.Move.from_uci(str(possibleMove))
                board.push(move)
                value = Minimax.minimax(board, depth-1, alpha, beta, True, time_before, limit_time, 'white')
                board.pop()
                bestMove = min(bestMove, value)
                if (beta <= alpha):
                    #board.pop()
                    #break;
                    return bestMove

                answerTime = time_after - time_before
                if(answerTime.seconds >= limit_time):
                    return bestMove
                #board.pop()

            return bestMove


    def evaluationBoard(board):
        totalEvaluation = 0;
        i = 0;
        s = -1
        #while s >= 63:
        while  i <= 7 :
            j = 0
            while j <= 7:
                s += 1
                totalEvaluation += (Minimax.getPieceValue(str(board.piece_at(s)), i, j))
                j += 1

            i += 1
        
        #print('The number is: ',s)
        return totalEvaluation;


    def getPieceValue(piece, x, y):
        if (piece == None or piece == 'None'):
            return 0;
    
        absoluteValue = 0;

        if (piece == 'P'):
            absoluteValue = 10 + Minimax.pawnEvalWhite[x][y]
            return  absoluteValue
        
        if (piece == 'p'):
            absoluteValue = 10 + Minimax.pawnEvalBlack[x][y]
            return  absoluteValue * -1
        
        if (piece == 'n'):
            absoluteValue = 30 + Minimax.knightEval[x][y]
            return  absoluteValue * -1
        
        if (piece == 'N'):
            absoluteValue = 30 + Minimax.knightEval[x][y]
            return  absoluteValue

        if (piece == 'b'):
            absoluteValue = 30 + Minimax.bishopEvalBlack[x][y]
            return  absoluteValue * -1

        if (piece == 'B'):
            absoluteValue = 30 + Minimax.bishopEvalWhite[x][y]
            return  absoluteValue

        if (piece == 'r'):
            absoluteValue = 50 + Minimax.rookEvalBlack[x][y]
            return  absoluteValue * -1

        if (piece == 'R'):
            absoluteValue = 50 + Minimax.rookEvalWhite[x][y]
            return  absoluteValue

        if (piece == 'q'):
            absoluteValue = 90 + Minimax.queenEval[x][y]
            return  absoluteValue * -1

        if (piece == 'Q'):
            absoluteValue = 90 + Minimax.queenEval[x][y]
            return  absoluteValue

        if (piece == 'k'):
            absoluteValue = 9000 + Minimax.kingEvalBlack[x][y]
            return  absoluteValue * -1

        if (piece == 'K'):
            absoluteValue = 9000 + Minimax.kingEvalWhite[x][y]
            return  absoluteValue

        print(f'unknow pice: {piece} in the interval: [{x}],[{y}]')
        return absoluteValue

    def checkmate_status(board: chess.Board, turn):
        node_evaluation = 0
        is_checkmate = board.is_checkmate()
        #turn = "black" if currently_player == False else "white"

        if turn == "white":
            if (is_checkmate):
                node_evaluation += float("inf")
        else:
            if (is_checkmate):
                node_evaluation += float("-inf")

        return node_evaluation

    def check_status(board: chess.Board, node_evaluation, turn):
        black_evaluation = 0
        is_check = board.is_check()
        #turn = "black" if currently_player == False else "white"

        if turn == "white":
            if (is_check):
                #print('check status white: True')
                black_evaluation += 10 #* node_evaluation
        else:
            if (is_check):
                #print('check status black: True')
                black_evaluation -= 10 #* node_evaluation

        return black_evaluation
    
    def good_square_moves(board: chess.Board, turn):
        node_evaluation = 0
        #turn = "black" if currently_player == False else "white"
        square_values = {"e4": 1, "e5": 1, "d4": 1, "d5": 1, "c6": 0.5, "d6": 0.5, "e6": 0.5, "f6": 0.5,
                        "c3": 0.5, "d3": 0.5, "e3": 0.5, "f3": 0.5, "c4": 0.5, "c5": 0.5, "f4": 0.5, "f5": 0.5}

        possible_moves = board.legal_moves
        for possible_move in possible_moves:
            move = str(possible_move)
            if turn == "white":
                if move[2:4] in square_values:
                    node_evaluation += square_values[move[2:4]]
            else:
                if move[2:4] in square_values:
                    node_evaluation -= square_values[move[2:4]]
                    
        return node_evaluation

    def main(move, next_player, board: chess.Board, limit_time = 3,):

        #board = chess.Board()

        if (next_player == 'white'):
            is_game_over = board.outcome()
            if(is_game_over):
                print('Game over')

                return 'Game over'
            else:
                move = chess.Move.from_uci(str(move))
                board.push(move)
                print(board)
                print('----------------')
                print('Person move: ',str(move))

                return(board)

        elif(next_player == 'black'):
            #is_game_over = board.outcome()
            if(board == None or board == 'Game over'):
                return print('Game over')
            else:
                print('----------------')
                print("Minimax Turn:")
                print('\n-----------------\nMinimax is Calculating...\n-----------------')
                time_before = datetime.datetime.now()
                move = Minimax.minimaxRoot(board, 3, True, time_before, limit_time)

                if(move == None):
                    return print('Game over')

                time_after = datetime.datetime.now()
                answerTime = time_after - time_before
                print(f'Minimax time: {answerTime.seconds} segundos')
                move = chess.Move.from_uci(str(move))
                board.push(move)
                print(board)

                return (move, board)
        



""" if __name__ == "__main__":
    main() """