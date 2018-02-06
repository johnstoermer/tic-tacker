import random
import math

global GAME_HISTORY
GAME_HISTORY = []

class TicTacToe:
    def __init__(self, boardState, currentPlayer, gameOver, gameWinner):
        self.boardState = boardState
        self.currentPlayer = currentPlayer
        self.gameOver = gameOver
        self.gameWinner = gameWinner
    def updateBoardState(self, boardState):
        self.boardState = boardState
    def updateCurrentPlayer(self, currentPlayer):
        self.currentPlayer = currentPlayer
    def updateGameOver(self, gameOver):
        self.gameOver = gameOver
    def updateGameWinner(self, gameWinner):
        self.gameWinner = gameWinner
    def saveGame(self):
        GAME_HISTORY.append([self.gameWinner,self.boardState])

def printBoard(boardState):
    print(boardState[0],'\n',boardState[1],'\n',boardState[2],'\n')

def takeTurn(game):
    currentPlayer = game.currentPlayer
    boardState = game.boardState
    currentBoardState = boardState[-1]
    placeValid = False
    nextMove = findNextMove(game)
    while placeValid == False:
        automatedInput = automateInput(game, nextMove)
        placeRow = automatedInput[0]
        placeCol = automatedInput[1]
        if currentBoardState[placeRow][placeCol] == 0:
            placeValid = True
        else:
            placeValid = False
            #print('That spot is taken!')
    currentBoardState[placeRow][placeCol] = currentPlayer
    #printBoard(currentBoardState)
    boardState.append(currentBoardState)
    game.updateBoardState(boardState)

def takeTurnHuman(game):
    currentPlayer = game.currentPlayer
    boardState = game.boardState
    currentBoardState = boardState[-1]
    placeValid = False
    while placeValid == False:
        placeRow = int(input('Row: '))
        placeCol = int(input('Col: '))
        if currentBoardState[placeRow][placeCol] == 0:
            placeValid = True
        else:
            placeValid = False
            print('That spot is taken!')
    currentBoardState[placeRow][placeCol] = currentPlayer
    #printBoard(currentBoardState)
    boardState.append(currentBoardState)
    game.updateBoardState(boardState)

def checkWin(game):
    currentPlayer = game.currentPlayer
    boardState = game.boardState
    currentBoardState = boardState[-1]
    diagonal1 = [[currentBoardState[0][0],currentBoardState[1][1],currentBoardState[2][2]]]
    diagonal2 = [[currentBoardState[0][2],currentBoardState[1][1],currentBoardState[2][0]]]
    rows = []
    cols = []
    winLine = [currentPlayer,currentPlayer,currentPlayer]
    for i in range(2):
        rows.append(currentBoardState[i])
        cols.append([currentBoardState[0][i],currentBoardState[1][i],currentBoardState[2][i]])
    if winLine in diagonal1 or winLine in diagonal2 or winLine in rows or winLine in cols:
        game.updateGameWinner(currentPlayer)
        game.updateGameOver(True)

def checkCats(game):
    boardState = game.boardState
    currentBoardState = boardState[-1]
    if 0 not in currentBoardState[0] and 0 not in currentBoardState[1] and 0 not in currentBoardState[2]:
        game.updateGameOver(True)

def nextPlayer(game):
    currentPlayer = game.currentPlayer
    if currentPlayer == 1:
        game.updateCurrentPlayer(2)
    elif currentPlayer == 2:
        game.updateCurrentPlayer(1)

def findNextMove(game):
    gameArray = GAME_HISTORY
    currentBoardState = game.boardState[-1]
    nextMoves = []
    for i in range(len(gameArray)):
        if game.currentPlayer in gameArray[i]:
            if currentBoardState in gameArray[i][1]:
                nextMoves.append(gameArray[i][gameArray[i][1].index(currentBoardState)+1])
    if nextMoves != []:
        nextMove = max(nextMoves,key = nextMoves.count)
        return nextMove
    else:
        return []

def automateInput(game, nextMove):
    currentBoardState = game.boardState[-1]
    if nextMove != []:
        for i in range(len(nextMove)):
            for j in range(len(nextMove[i])):
                if nextMove[i][j] - currentBoardState[i][j] == game.currentPlayer:
                    return [i,j]
    else:
        return [random.randint(0,2), random.randint(0,2)]

def playGame():
    startState = [[[0,0,0],[0,0,0],[0,0,0]]]
    startPlayer = 2
    gameOver = False
    gameWinner = 0
    game = TicTacToe(startState, startPlayer, gameOver, gameWinner)
    while game.gameOver == False:
        nextPlayer(game)
        #print('Player ',game.currentPlayer,'\'s turn')
        takeTurn(game)
        checkWin(game)
        checkCats(game)
    #print('Player ',game.gameWinner,' wins!')
    game.saveGame()

def playGameHuman():
    startState = [[[0,0,0],[0,0,0],[0,0,0]]]
    startPlayer = 2
    gameOver = False
    gameWinner = 0
    game = TicTacToe(startState, startPlayer, gameOver, gameWinner)
    while game.gameOver == False:
        nextPlayer(game)
        print('Player ',game.currentPlayer,'\'s turn')
        if game.currentPlayer == 1:
            takeTurn(game)
        elif game.currentPlayer == 2:
            takeTurnHuman(game)
        boardState = game.boardState
        currentBoardState = boardState[-1]
        printBoard(currentBoardState)
        checkWin(game)
        checkCats(game)
    print('Player ',game.gameWinner,' wins!')
    game.saveGame()

def displayWinPercentage():
    player1Wins = 0
    player2Wins = 0
    for i in range(len(GAME_HISTORY)):
        if GAME_HISTORY[i][0] == 1:
            player1Wins = player1Wins+1
        elif GAME_HISTORY[i][0] == 2:
            player2Wins = player2Wins+1
    print('Win Percentage:\nPlayer 1: '+str(player1Wins/len(GAME_HISTORY))+' Player 2: '+str(player2Wins/len(GAME_HISTORY))+' Cats game: '+str(1-((player1Wins+player2Wins)/len(GAME_HISTORY))))

def main():
    for i in range(10):
        for j in range(1000):
            playGame()
        displayWinPercentage()
    playGameHuman()

main()
