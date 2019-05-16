
class playerdominos:

    #ici le consctructeur de la classe table qui est une pile des dominos 
    def __init__(self):
        self.nbr=0
        self.dominos=[]

    #pour ajouter un élément 
    def add_element(self,domino):
        self.dominos.append(domino)
        self.nbr +=1

    #la suppression de l'élément     
    def del_element(self):
        assert not self.is_empty()
        do=self.dominos[self.nbr-1]
        del self.dominos[self.nbr-1]
        self.nbr-=1
        return do

    #pour tester la liste est vide ou non 
    def is_empty(self):
        return self.nbr==0
    #
    def top(self):
        assert not self.is_empty()
        return self.dominos[self.nbr-1]
    #la taille de la liste des dominos    
    def length(self):
                return self.nbr







