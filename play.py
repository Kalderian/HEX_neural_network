from board import Board


p = Board(9)
player = 1
noWinner = True

while(noWinner):
    invalidMove = True
    while(invalidMove):
        if player == 1:
            x = int(input("Xplayer o = "))
            y = int(input("Yplayer o = "))
        elif player == -1:
            x = int(input("Xplayer x = "))
            y = int(input("Yplayer x = "))
        coord = x * p.size + y
        invalidMove = not(p.play(player, coord))
    noWinner = not(p.isWon(player))
    if(noWinner):
        player = - player
    p.affiche()
if player == 1:
    print("player o win")
else:
    print("player x win")    