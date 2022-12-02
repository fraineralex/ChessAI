import time
import chess
#import sunfish
import math
import random
import sys
from numpy import Infinity

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
    bestMove = -Infinity
    bestMoveFound = None
    
    for possible_move in possibleMoves:
        move = chess.Move.from_uci(str(possible_move))
        board.push(move)
        value = minimax(board, depth - 1, -Infinity, Infinity, not maximizingPlayer)
        board.pop()
        if( value >= bestMove):
            #print("Best move: ",str(bestMoveFound))
            bestMove = value
            bestMoveFound = move

    return bestMoveFound

def minimax(board, depth, alpha, beta, maximizingPlayer):
    if(depth == 0):
        return -evaluationBoard(board)

    possibleMoves = board.legal_moves

    if(maximizingPlayer):
        bestMove = -Infinity

        for possibleMove in possibleMoves:
            move = chess.Move.from_uci(str(possibleMove))
            board.push(move)
            value = minimax(board, depth-1, alpha, beta, False)
            bestMove = max(bestMove, value)
            alpha = max(alpha, value);
            if (alpha >= beta):
                board.pop();
                break;

            board.pop()

        return bestMove

    else:
        bestMove = +Infinity
        for possibleMove in possibleMoves:
            move = chess.Move.from_uci(str(possibleMove))
            board.push(move)
            value = minimax(board, depth-1, alpha, beta, True)
            bestMove = min(bestMove, value)
            if (alpha >= beta):
                board.pop()
                break;

            board.pop()

        return bestMove

""" def evaluationBoard(board):
    i = 0
    evaluation = 0
    x = True
    try:
        x = bool(board.piece_at(i).color)
    except AttributeError as e:
        x = x
    while i < 63:
        i += 1
        evaluation = evaluation + (getPieceValue(str(board.piece_at(i))) if x else -getPieceValue(str(board.piece_at(i))))
    return evaluation """

def evaluationBoard(board):
  totalEvaluation = 0;
  i = 0;
  j = 0
  while  i < 8:

    while j < 8:
        
        totalEvaluation += (getPieceValue(str(board.piece_at(i)), i, j))
        j += 1

    i += 1
    
  return totalEvaluation;

""" function evaluateBoard(board) {
  let totalEvaluation = 0;
  for (let i = 0; i < 8; i++) {
    for (let j = 0; j < 8; j++) {
      totalEvaluation += getPieceValue(board[i][j], i, j);
    }
  }
  return totalEvaluation;
} """

""" def getPieceValue(piece):
    if(piece == None):
        return 0
    value = 0
    if piece == "P" or piece == "p":
        value = 10
    if piece == "N" or piece == "n":
        value = 30
    if piece == "B" or piece == "b":
        value = 30
    if piece == "R" or piece == "r":
        value = 50
    if piece == "Q" or piece == "q":
        value = 90
    if piece == 'K' or piece == 'k':
        value = 900
    return value """

def getPieceValue(piece, x, y):
    if (piece == None or piece == ''):
        return 0;
  
    absoluteValue = 0;

    if (piece == 'P'):
        absoluteValue = 10 + pawnEvalWhite[x][y]
        return  -absoluteValue
    
    if (piece == 'p'):
        absoluteValue = 10 + pawnEvalBlack[x][y]
        return  absoluteValue
    
    if (piece == 'n'):
        absoluteValue = 10 + knightEval[x][y]
        return  absoluteValue
    
    if (piece == 'N'):
        absoluteValue = 10 + knightEval[x][y]
        return  -absoluteValue

    if (piece == 'b'):
        absoluteValue = 10 + bishopEvalBlack[x][y]
        return  absoluteValue

    if (piece == 'B'):
        absoluteValue = 10 + bishopEvalWhite[x][y]
        return  -absoluteValue

    if (piece == 'r'):
        absoluteValue = 10 + rookEvalBlack[x][y]
        return  absoluteValue

    if (piece == 'R'):
        absoluteValue = 10 + rookEvalWhite[x][y]
        return  -absoluteValue

    if (piece == 'q'):
        absoluteValue = 10 + queenEval[x][y]
        return  absoluteValue

    if (piece == 'Q'):
        absoluteValue = 10 + queenEval[x][y]
        return  -absoluteValue

    if (piece == 'k'):
        absoluteValue = 10 + kingEvalBlack[x][y]
        return  absoluteValue

    if (piece == 'K'):
        absoluteValue = 10 + kingEvalWhite[x][y]
        return  -absoluteValue

    print(f'Unknown piece type: {piece}')

def main():
    board = chess.Board()

    n = 0
    print(board)
    turn = 'person'
    while n < 100:
        if (turn == 'person'):
            print('----------------')
            move = input("😃 Your turn: ")
            move = chess.Move.from_uci(str(move))
            board.push(move)
            turn = 'bot'
        else:
            print('----------------')
            print("🤖 My Turn:")
            move = minimaxRoot(board, 2, True)
            move = chess.Move.from_uci(str(move))
            board.push(move)
            turn = 'person'
        print(board)



if __name__ == "__main__":
    main()




"""     def onDragStart(source, piece, position, orientation):
        if (board.is_game_over()): return False;

        if (piece != -1):
            return False;

    def onDrop(source, target):
        move = board.legal_moves({
        'from': source,
        'to': target,
         'promotion': 'q'
         });

        if (move == None): return 'snapback';

        time.slep(makeBestMove(), 0.25);

    def makeBestMove():
        if (board.is_game_over()):
            print('Game over');

        bestMove = minimaxRoot(board, 2, True);
        board.legal_moves(bestMove)
        board.position(board.fen())
        if (board.is_game_over()):
            print('Game over');


    def onSnapEnd():
        board.position(board.fen());

    config = {
        'draggable': True,
        'position': 'start',
        'onDragStart': onDragStart,
        'onDrop': onDrop,
        'onSnapEnd': onSnapEnd
    }

    board = chess.Board(config) """