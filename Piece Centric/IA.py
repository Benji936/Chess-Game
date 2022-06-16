"""Une fonction pour chaque aspect qui détermine si le coup est bon:
 - position stratégique
 - libérer d'autre pièce
 - mettre en échec
 - manger une pièce
 - doubler les pions
 - clouer un pièce
 - attaquer une pièce
 - promotion
  """

#Un mauvais coup est défini par la capacité de l'adversaire à faire un bon coup au tour suivant 

#donc en évaluant si le coup est bon et si le coup suivant sera bon on peut déterminé un meilleur coup
# plus le ratio bon coup/ bon coup suivant est grand plus notre coup est bon

import copy
import time

def willCheck(board,move):
    if board.check():
        if board.checkmate():
            return 100
        return 1
    return 0

def willEat(board,move):
    if move.eats(board):
        return 1
    return 0

def willAttack(board,move):
    piece = board.getPiece(move.to[0],move.to[1])
    moves = piece.getPossibleMoves(board)

    res = 0
    if len(moves) > 4:
        res += 1

    for move in moves:
        if move.eats(board):
            res += 1
    return res

    
    
def ia(game,recursion,depth,value):
    #start = time.time()
    if recursion > depth:
        return [value,None]


    bestScoreOfAll = -100
    best = None
    bestOfTheBest = None
    for piece in game.pieces.values():
        if piece.color != game.turnColor():
            continue 
        #if recursion == 0:
            #print(piece,piece.color)
        bestScore = -100
        moves = piece.getPossibleMoves(game)
        #print(piece,piece.color,moves)

        for move in moves:

            boardCopy = copy.deepcopy(game)
            move.applyMove(boardCopy)
            boardCopy.turn += 1

            points = 0
            
            points += willEat(game,move)

            points += willAttack(boardCopy,move)

            points += willCheck(boardCopy,move)

            if bestScore < points:
                bestScore = points
                best = (move,boardCopy,points)

        if moves:
            points = best[2]
            if recursion%2:
                points += ia(best[1],recursion+1,depth,points)[0]
            else:
                points -= ia(best[1],recursion+1,depth,points)[0]

            if bestScoreOfAll < points:
                bestScoreOfAll = points
                bestOfTheBest = best[0]

    #print(time.time()-start)
    return [bestScoreOfAll,bestOfTheBest]




        #update(screen,cellScale,game.pieces)
        #input("oui")