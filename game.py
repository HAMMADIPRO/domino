from domino import *
from player import *
from random import *

class game:

    #constructeur
    def __init__(self, maxNbr, nbrPlayer):
        #self.sequence = dominoSequence()
        self.table = []
        self.chaine = []
        for i in range(0,maxNbr):
            for j in range(i,maxNbr):
                self.table.append(Domino(i,j))
        self.players = []
        self.currentPlayer = 0
        self.indexFirstPlayer = 0
        self.winner = 0

    #ajouter un nouveau joueur au jeu    
    def addPlayer(self, player):
        self.players.append(player)

    #Determiner le joueur suivant qui doit jouer    
    def nextPlayer(self):
        self.currentPlayer = (self.currentPlayer+1)%len(self.players)
        return self.currentPlayer  

    #Definir le premier jouer qui vas jouer (qui a le plus grand domino double) et le premier domino jouer   
    def theFirstPlay(self):
        dom = Domino(-1, -1)
        for i in range(len(self.players)):
            if dom.value() < self.players[i].biggestDoubleDomino().value() :
                dom = self.players[i].biggestDoubleDomino()
                self.indexFirstPlayer = i
        self.currentPlayer = self.indexFirstPlayer  
        self.chaine.append(dom)           
        return self.players[self.indexFirstPlayer].removeDomino(dom)                   
    
    # suprimer un domino du tableau        
    def removeFromTable(self,domino):
        self.table.pop(domino)

    #tester si le joueur peut ajouter un domino à la table
    def play(self,domino,position):
        if position == 0:  
            if domino.canBePlacedLeft(self.chaine[0]):
                self.chaine = [domino] + self.chaine
                return True
            return False
        if position == 1:
            if domino.canBePlacedRight(self.chaine[len(self.chaine)-1]):
                self.chaine.append(domino)
                return True
            return False

    def gameEnd(self):
        for i in range(len(self.players)):
            if len(self.players[i].stock) == 0:
                self.winner = i
                return True
        return False        




        


                
