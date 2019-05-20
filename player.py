from random import randint
from domino import *  


class player:
    #le constructure pour créer un joueur 
    def __init__(self, dominoNbr,table):
        #self.mydominos = DominoSequence()
        self.stock=[]
        for i in range(dominoNbr):
            self.takeDomino(table)
    
    
    def takeDomino(self,table):
        if len(table)!=0:
            ind = randint(0, len(table)-1)
            dom=table.pop(ind)
            self.stock.append(dom)    
        

    def biggestDoubleDomino(self):
        DominoDouble = Domino(-1, -1)
        for dom in self.stock:
            if dom.isDouble() and dom.isGratterThan(DominoDouble):
                DominoDouble = dom
        return DominoDouble

    # enlever un domino du stock    
    def removeDomino(self, domino):
        for i in range(len(self.stock)):
            if domino.isEqual(self.stock[i]):
                return self.stock.pop(i)        


    def stockVlaue(self) :
        v=0
        for dom in self.stock :
            v=v+dom.value()
        return v
        

