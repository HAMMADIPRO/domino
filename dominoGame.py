from domino import *
from playerdominos import *

class Game:

    #constructeur
    def __init__(self, maxNbr):
        self.sequence = playerdominos()
        self.table = []
        for i in range(0,maxNbr-1):
            for j in range(0,maxNbr-1):
                self.table.append(Domino(i,j))
        self.players = []

    def addPlayer(self, player):
        self.players.append(player)
        