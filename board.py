
# -*- coding: utf-8 -*-
''' Un board de jeu est representé par une matrix, dont les dimensions sont fixées par la "width" du board. 
Voici les fonctions dont la classe est constituée:
    -play actualise le board en rentrant le numéro du player aux coordonnées demandées
    -affiche permet de visualiser le board plus facilement avec sa forme de losange
    -path explore les 6 cases adjacentes pour vérifier s'il existe un path d'un bord à l'autre du board
    -isWon renvoie le player gagnant de la partie'''

class Board:
    # une case est vide (= 0) player 1 (= 1) ou player 2 (= 2)

    def __init__(self, width, matrix = []):
        self.size = width
        if matrix == []:
            self.mat = [[0]*self.size for _ in range(self.size)]
        else:
            self.mat = matrix
        
    def play(self, player, move):
        i = move[0]
        j = move[1]
        if(self.mat[i][j] == 0):
            self.mat[i][j] = player
            return True
        else:
            return False
    
    def read(self, coord):
        return self.mat[coord[0]][coord[1]]

    def affiche(self):
        s = ""
        for i in range(0, self.size):
            s += str(i) + "  "
        print("  " * self.size + "x\y", s)
        for i in range(0, self.size):
            print("  " * (self.size - i - 1), i, self.mat[i])

  
    def deepcopy(self):
        newMat = [line[:] for line in self.mat]
        p = Board(self.size, newMat)
        return p
    
    def path(self, player, xStart, yStart, dejaVu):
        dejaVu.append((xStart, yStart))
        #Cas de base, on est arrivé de l'autre coté du board
        if((yStart == self.size-1 and player == 1) or (xStart == self.size-1 and player == 2)):
            return True
        else:
            #On créé la liste des cases adjacentes non visitées
            ptsAdja = []
            if(xStart < self.size-1):
                if not((xStart+1, yStart) in dejaVu):
                    ptsAdja.append((xStart+1, yStart))
                if (yStart < self.size-1) and not((xStart+1, yStart+1) in dejaVu):
                    ptsAdja.append((xStart+1, yStart+1))
            if(xStart > 0):
                if not((xStart-1, yStart) in dejaVu):
                    ptsAdja.append((xStart-1, yStart))
                if(yStart > 0) and not((xStart-1, yStart-1) in dejaVu):
                    ptsAdja.append((xStart-1, yStart-1))
            if(yStart < self.size-1) and not((xStart, yStart+1) in dejaVu):
                ptsAdja.append((xStart, yStart+1))
            if(yStart > 0) and not((xStart, yStart-1) in dejaVu):
                ptsAdja.append((xStart, yStart-1))
            #On applique récursivement path Ă  chaque case de la liste contenant un pion de player
            for i in range(0, len(ptsAdja)):
                if((self.mat[ptsAdja[i][0]][ptsAdja[i][1]] == player) and (self.path(player, ptsAdja[i][0], ptsAdja[i][1], dejaVu))):
                    return True
            return False
        
    def isWon(self, player):
        sortie = False
        if(player == 1):
            for i in range(0, self.size):
                if(self.mat[i][0] == player) and not(sortie):
                    sortie = self.path(player, i, 0, [])
        if(player == 2):
            for i in range(0, self.size):
                if(self.mat[0][i] == player) and not(sortie):
                    sortie = self.path(player, 0, i, [])
        return sortie
    
    