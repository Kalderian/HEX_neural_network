import numpy as np
import random as rd
import queue
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
            self.mat = np.zeros(self.size*self.size)            
        else:
            self.mat = matrix
        
        
    def play(self, player, move):
        if(self.mat[move] == 0):
            self.mat[move] = player
            return True
        else:
            return False
    

    
    def read(self, i, j):
        coord = self.size * i + j
        return self.mat[coord]


    def affiche(self):
        s = ""
        for i in range(self.size):
            s += str(i) + "  "
        print("  " * self.size + "x\y", s)
        for i in range(self.size):
            s = ""
            for j in range(self.size):
                coord = self.size * i + j
                if self.mat[coord] == 1:
                    s += "o  "
                elif self.mat[coord] == -1:
                    s += "x  "
                else:
                    s += "¤  "
            print("  " * (self.size - i - 1), i," ", s)

                    
    def deepCopy(self):
        newMat = np.copy(self.mat)
        p = Board(self.size, newMat)
        return p
    
        
    def path(self, player, coord, visited, queueCells):
        x = coord // self.size
        y = coord % self.size
        visited[coord] = True
        #Cas de base, on est arrivé de l'autre coté du board
        if((y == self.size-1 and player == 1) or (x == self.size-1 and player == -1)):
            return True
        up_left = coord-self.size-1
        up = coord-self.size
        left = coord-1
        right = coord+1
        down = coord+self.size
        down_right = coord+self.size+1
        if (x > 0):
            if (self.mat[up] == player) and not(visited[up]): 
                visited[up] = True
                queueCells.put(up)
            if (y > 0):       
                if (self.mat[up_left] == player) and not(visited[up_left]): 
                    visited[up_left] = True
                    queueCells.put(up_left)
        if (x < self.size-1):
            if (self.mat[down] == player) and not(visited[down]): 
                visited[down] = True
                queueCells.put(down)
            if (y < self.size-1):
                if (self.mat[down_right] == player) and not(visited[down_right]): 
                    visited[down_right] = True
                    queueCells.put(down_right)
        if (y > 0):
            if (self.mat[left] == player) and not(visited[left]): 
                visited[left] = True
                queueCells.put(left)
        if (y < self.size-1):
            if (self.mat[right] == player) and not(visited[right]): 
                visited[right] = True
                queueCells.put(right)
        if queueCells.empty():
            return False
        coord = queueCells.get()
        return self.path(player, coord, visited, queueCells)
        

    def isWon(self, player):
        sortie = False
        queueCells = queue.Queue()
        if(player == 1):
            for i in range(0, self.size*self.size, self.size):
                if(self.mat[i] == player) and not(sortie):
                    sortie = self.path(player, i, [False]*(self.size*self.size), queueCells)
        if(player == -1):
            for j in range(self.size):
                if(self.mat[j] == player) and not(sortie):
                    sortie = self.path(player, j, [False]*(self.size*self.size), queueCells)
        return sortie

  
    def allowedMoves(self):
        moves = []
        for i in range (self.size*self.size):
            if (self.mat[i] == 0):
                moves.append(i)
        return moves


def randomGame(board, player):
    moves = board.allowedMoves()
    rd.shuffle(moves)
    j = player
    for elt in moves:
        board.play(j, elt)
        j = - j

for _ in range(10):
    p = Board(9)
    randomGame(p, 1)
    p.affiche()
    if p.isWon(1):
        print("joueur o")
    if p.isWon(-1):
        print("joueur x")
    









