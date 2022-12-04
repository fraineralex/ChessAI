import datetime
import chess
#import sunfish
from numpy import Infinity, flip

class Minimax:

    def reverseArray(array): 
        return flip(array)

    pawnEvalWhite = [
    [ 0.0,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0],
    [ 5.0,  5.0,  5.0,  5.0,  5.0,  5.0,  5.0,  5.0],
    [ 1.0,  1.0,  2.0,  3.0,  3.0,  2.0,  1.0,  1.0],
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

    def minimaxRoot(board, depth, maximizingPlayer):
        time_before = datetime.datetime.now()
        possibleMoves = board.legal_moves
        bestMove = -9999
        bestMoveFound = None
        
        for possible_move in possibleMoves:
            time_after = datetime.datetime.now()
            move = chess.Move.from_uci(str(possible_move))
            board.push(move)
            value = Minimax.minimax(board, depth-1, -10000, 10000, not maximizingPlayer)
            board.pop()
            if( value >= bestMove):
                bestMove = value
                bestMoveFound = move
                print("Best move for now: ",str(bestMoveFound))
                answerTime = time_after - time_before
                if(answerTime.seconds >= 3):
                    return bestMoveFound
                

        return bestMoveFound

    def minimax(board, depth, alpha, beta, maximizingPlayer):
        time_before = datetime.datetime.now()
        if(depth == 0):
            return Minimax.evaluationBoard(board) * -1

        possibleMoves = board.legal_moves

        if(maximizingPlayer):
            bestMove = -9999

            for possibleMove in possibleMoves:
                time_after = datetime.datetime.now()
                move = chess.Move.from_uci(str(possibleMove))
                board.push(move)
                value = Minimax.minimax(board, depth-1, alpha, beta, False)
                bestMove = max(bestMove, value)
                board.pop()
                alpha = max(alpha, value);
                if (beta <= alpha):
                    #board.pop();
                    #break;
                    return bestMove
                
                answerTime = time_after - time_before
                if(answerTime.seconds >= 3):
                    return bestMove

                #board.pop()

            return bestMove

        else:
            bestMove = 9999
            for possibleMove in possibleMoves:
                time_after = datetime.datetime.now()
                move = chess.Move.from_uci(str(possibleMove))
                board.push(move)
                value = Minimax.minimax(board, depth-1, alpha, beta, True)
                board.pop()
                bestMove = min(bestMove, value)
                if (beta <= alpha):
                    #board.pop()
                    #break;
                    return bestMove

                answerTime = time_after - time_before
                if(answerTime.seconds >= 3):
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
            absoluteValue = 900 + Minimax.kingEvalBlack[x][y]
            return  absoluteValue * -1

        if (piece == 'K'):
            absoluteValue = 900 + Minimax.kingEvalWhite[x][y]
            return  -absoluteValue

        print(f'unknow pice: {piece} in the interval: [{x}],[{y}]')
        return absoluteValue

    def main(move, next_player, board, time_before = datetime.datetime.now()):

        #board = chess.Board()

        if (next_player == 'white'):
            print('----------------')
            #move = input("😃 Your turn: ")
            move = chess.Move.from_uci(str(move))
            board.push(move)
            print(board)

            return(board)

        elif(next_player == 'black'):
            print('----------------')
            print("Minimax Turn:")
            print('\n-----------------\nMinimax is Calculating...\n-----------------')
            move = Minimax.minimaxRoot(board, 2, True)
            time_after = datetime.datetime.now()
            answerTime = time_after - time_before
            print(f'Minimax time: {answerTime.seconds} segundos')
            move = chess.Move.from_uci(str(move))
            board.push(move)
            print(board)

            return (move, board)
        



""" if __name__ == "__main__":
    main() """