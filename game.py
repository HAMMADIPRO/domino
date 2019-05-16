from domino import *
from dominoSequence import *
from player import *
from random import *

class Game:

    #constructeur
    def __init__(self, maxNbr):
        self.sequence = DominoSequence()
        self.table = []
        for i in range(0,maxNbr):
            for j in range(i,maxNbr):
                self.table.append(Domino(i,j))
        self.players = []
        self.actuelPlayer = 0
        self.firstPlayer = player()

    #ajouter un nouveau joueur au jeu    
    def addPlayer(self, player):
        self.players.append(player)

    #Determiner le joueur suivant qui doit jouer    
    def nextPlayer(self):
        id = 0
        while self.actuelPlayer != self.players[id]:
            id= id+1
        self.actuelPlayer = self.players[(id+1)%len(self.players)]  

    #Definir le premier jouer qui vas jouer (qui a le plus grand domino double)    
    def theFirstPlayer(self):
        maxValue = self.players[0].biggestDoubleDomino().value()
        self.firstPlayer = self.players[0]
        for i in range(len(self.players)):
            if maxValue < self.players[i].biggestDoubleDomino().value() :
                maxValue =  self.players[i].biggestDoubleDomino().value()
                self.firstPlayer = self.players[i] 
        return self.firstPlayer    

    #la première partie du jeu    
    def startPlay(self):
        self.theFirstPlayer()
        dominoSequence = DominoSequence() 
        #Si aucun joueur a au moin un double domino choisir le premier joueur au hasard
        if not self.firstPlayer.biggestDoubleDomino.isEmpty():
            dominoSequence.add_element(self.firstPlayer.biggestDoubleDomino)
        else:
            self.firstPlayer = self.players[randint(0,len(self.players))]







              



