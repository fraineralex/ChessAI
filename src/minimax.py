import chess
#import sunfish
from numpy import Infinity

class Minimax:

    def reverseArray(array): 
        return array.reverse()

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
        possibleMoves = board.legal_moves
        bestMove = Infinity * -1
        bestMoveFound = None
        
        for possible_move in possibleMoves:
            move = chess.Move.from_uci(str(possible_move))
            board.push(move)
            value = Minimax.minimax(board, depth-1, Infinity * -1, Infinity, not maximizingPlayer)
            board.pop()
            if( value >= bestMove):
                bestMove = value
                bestMoveFound = move
                print("Best move for know: ",str(bestMoveFound))

        return bestMoveFound

    def minimax(board, depth, alpha, beta, maximizingPlayer):
        if(depth == 0):
            return Minimax.evaluationBoard(board) * -1

        possibleMoves = board.legal_moves

        if(maximizingPlayer):
            bestMove = -Infinity

            for possibleMove in possibleMoves:
                move = chess.Move.from_uci(str(possibleMove))
                board.push(move)
                value = Minimax.minimax(board, depth-1, alpha, beta, False)
                bestMove = max(bestMove, value)
                alpha = max(alpha, value);
                if (alpha >= beta):
                    board.pop();
                    break;

                board.pop()

            return bestMove

        else:
            bestMove = Infinity
            for possibleMove in possibleMoves:
                move = chess.Move.from_uci(str(possibleMove))
                board.push(move)
                value = Minimax.minimax(board, depth-1, alpha, beta, True)
                bestMove = min(bestMove, value)
                if (alpha >= beta):
                    board.pop()
                    break;

                board.pop()

            return bestMove


    def evaluationBoard(board):
        totalEvaluation = 0;
        i = 0;
        while  i <= 7 :

            j = 0
            while j <= 7:
                print(board)
                totalEvaluation += (Minimax.getPieceValue(str(board.piece_at(i)), i, j))
                j += 1

            i += 1
            
        return totalEvaluation;


    def getPieceValue(piece, x, y):
        if (piece == None or piece == ''):
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

        return absoluteValue

    def main(move, next_player, board):

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
            print(" My Turn:")
            move = Minimax.minimaxRoot(board, 2, True)
            move = chess.Move.from_uci(str(move))
            board.push(move)
            print(board)

            return (move, board)
        



""" if __name__ == "__main__":
    main() """