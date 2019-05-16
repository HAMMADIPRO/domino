from playerdominos import *
from random import randint
from domino import *  


class player:
    #le constructure pour créer un joueur 
    def __init__(self, playerNbr,table):
        self.mydominos = playerdominos()
        self.stock=[]
        for i in range(playerNbr):
            self.takeDomino(table)
           
    
    def takeDomino(self,table):
        ind = randint(0, len(table)-1)
        dom=table.pop(ind)        
        self.stock.append(dom)

    def biggestDoubleDomino(self):
        DominoDouble = Domino(-1, -1)
        for dom in self.stock:
            if dom.isDouble() and dom.isGratterThen(DominoDouble):
                DominoDouble=dom
        return DominoDouble

    def bigestDominoTable(self, firstDomino):
        if self.mydominos.length()!=0:
            lastdomino=self.mydominos.top()
        else:
            lastdomino=firstDomino
        for dom in self.stock:
            if dom.A == lastdomino.B:
                return dom
            elif dom.B == lastdomino.B:
                return dom.permute()
        return Domino(-1, -1)



    # Retourne le nombre de dominos dans la reserve du joueur.
    def nomberOfDominosStock(self):
        return len(self.stock)

    def stockVlaue(self) :
        v=0
        for dom in self.stock :
            v=v+dom.valeur()
        return v
        