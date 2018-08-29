from board import Board
class Node:

    def __init__(self, board, player, parent):
        self.board = board
        self.neuralNotation = 0
        self.nWin = 0
        self.nEndsReached = 0
        self.state = 0
        self.player = player
        self.parent = parent
        self.children = []
        
    def updateNotation(self):
        if self.state == 0:
            if self.board.isWon(1):
                self.state = 1
                self.nEndsReached = 1
                self.nWin = 1
            elif self.board.isWon(-1):
                self.state = -1
                self.nEndsReached = 1
                self.nWin = 0
#            self.neuralNotation = XXX
        elif self.state == 1:
            self.nEndsReached += 1
            self.nWin += 1
        else:
            self.nEndsReached += 1
            

                
        

class Tree:
    
    def __init__(self):
        node = Node(Board(9), 1, 0)
        self.nodes = [node]
        
    def selectNode(self):
        
        
    def expandNode(self, idNode):
        node = self.nodes[idNode]
        if node.state == 0
            moves = node.board.allowedMoves()
            for move in moves:
                board = node.board.deepCopy()
                board.play(node.player, move)
                childNode = Node(board, -node.player, idNode)
                childNode.updateNotation()
                node.children.append(len(self.nodes))
                self.nodes.append(childNode)
    
    def backpropNotation(self, idNode):
        node = self.nodes[idNode]
        p = node.player
        nWin = 0
        nEndsReached = 0
        neuralNotation = -p
        for i in node.children:
            childNode = self.nodes[i]
            nWin += childNode.nWin
            nEndsReached += childNode.nEndsReached
            neuralNotation = p*max(p*neuralNotation, p*childNode.neuralNotation)
        node.nWin = nWin
        node.nEndsReached = nEndsReached
        node.neuralNotation = neuralNotation
        if idNode != 0:
            self.backpropNotation(node.parent)
            
            
    
            

        
        