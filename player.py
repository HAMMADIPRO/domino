from playerdominos import *

class player:
    def __init__(self,name, playerNbr):
        self.mydominos=palyerdominos()
        self.stock=[]
        for i in range(playerNbr):
            self.takedomino(listofdominos)
           


