from player import *  
from game import *

#definie les différants étape du jeu
def nextPlay(p):
        #affichier les dominos du joueur
        for i in range(len(p.stock)):
                print(str(i)+':'+p.stock[i].displayDomino()+',  ', end='') 
        #l'option de tier un domnio du tableau              
        print(str(len(p.stock))+': prendre un domino du table')

        #le input concernant le domino choisie         
        n = int(input('choisie le domino à jouer: '))

        #choisir où mettre le domino choisie
        if n != len(p.stock):
                side = int(input('choisie le côté où posé le domino (0: à gauche, 1: à droite): '))

        #prendre un domino du tableau
        if n == len(p.stock):
                p.takeDomino(game.table)
                for i in game.chaine:
                                print(i.displayDomino(), end='')
        # la reponse du choix d'un domino                        
        else:
                if game.play(p.stock[n],side):
                        p.stock.pop(n)
                        print('#########################################################################')
                        for i in game.chaine:
                                print(i.displayDomino(), end='')
                        print('')        
                        print('#########################################################################')                
                else:
                        print('domino mal choisie il faut choisir un autre!!')
                        nextPlay(p)

#test les input de l'utilisateur sont valable ou pas
jouer = False
while not jouer:
        nbrPlayer = int(input('Entrer le nombre des joueurs (entre 2 et 4): '))
        if nbrPlayer > 1 and nbrPlayer < 5:
                dominoNbr = int(input('Entrer le nombre des domino qui appartient à chaque joueur (entre 6 et 8): '))
                if dominoNbr > 5 and dominoNbr < 9:
                        jouer = True
                else:
                        dominoNbr = int(input('Erreur!! Entrer le nombre des domino qui appartient à chaque joueur (entre 6 et 8): '))        
        else:
                nbrPlayer = int(input('Erreur!! Entrer le nombre des joueurs (entre 2 et 4): '))

#créer un nouveau jeu 
game = game(dominoNbr,nbrPlayer)

# ajouter les différents joueurs au jeu
for i in range(nbrPlayer):
    game.addPlayer(player(dominoNbr,game.table))
    print('player '+str(i))
    for j in range(dominoNbr):
        print(game.players[i].stock[j].displayDomino())

print('le premier jeu est : '+game.theFirstPlay().displayDomino()+' par le joueur: '+str(game.indexFirstPlayer))

#la boucle while s'arrete lorsque un joueur gagne
while not game.gameEnd():
        print(' ')
        print('le tour du joueur: '+str(game.nextPlayer()))
        p = game.players[game.currentPlayer]
        nextPlay(p) 

print("le joueur "+str(game.currentPlayer)+' a gagné.')       
        




                







    
