class Domino:
        def __init__(self, f1, f2):
            #constructeur de la class domino
            self.f1 = f1
            self.f2 = f2

        #Afficher les deux faces du domino
        def displayDomino(self):
            return '['+str(self.f1)+'|'+str(self.f2)+']'

        #La somme des deux faces du domino
        def value(self):
            return (self.f1 + self.f2)

        #Definir si le domino est un double(a deux faces identiques)
        def isDouble(self):
            return (self.f1 == self.f2)

        #Tester si le domino est vide
        def isEmpty(self):
            return (self.isDouble() and self.f1 == 0)

        #Comparer si ce dominon est identique un autre domino donnant
        def isEqual(self, domino):
            if (self.f1 == domino.f1 and self.f2 == domino.f2) or (self.f1 == domino.f2 and self.f2 == domino.f1):
                return True
            return False

        #Tester si le domino courant peut être placer devant un autre domino donnant
        def canBePlacedRight(self, domino):
            if self.f1 == domino.f2 :
                return True
            elif self.f2 == domino.f2:
                self.permute()
                return True
            return False 
        def canBePlacedLeft(self, domino):
            if self.f2 == domino.f1:
                return True
            elif self.f1 == domino.f1:
                self.permute()
                return True
            return False

        # permuter les deux faces du domino    
        def permute(self):
            self.f1, self.f2 = self.f2, self.f1

        # Tester si la valeur de ce domino est supérieur à un autre domino    
        def isGratterThan(self, domino):
            if self.value() > domino.value():
                return True
            return False        

d1 = Domino(10, 10)
d2 = Domino(0, 0)

print(d1.isDouble())
print(d1.isEqual(d2))
print(d2.isEmpty())