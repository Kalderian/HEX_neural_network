from board import Board


p = Board(9)
player = 1
noWinner = True

while(noWinner):
     invalidPlay = True
     while(invalidPlay):
         if player == 1:
             x = int(input("Xplayer1 = "))
             y = int(input("Yplayer1 = "))
         elif player == 2:
             x = int(input("Xplayer2 = "))
             y = int(input("Yplayer2 = "))
         invalidPlay = not(p.play(player, (x, y)))
     noWinner = not(p.isWon(player))
     if(noWinner):
         player = 3 - player
     p.affiche()
 
print("player n°" + str(player) + " win")