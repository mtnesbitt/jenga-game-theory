from classes.game import Game

difficulty, num_layers, first_player = input("Select your difficulty, the number of layers, and who is going first (1 for the player, 2 for the computer): ")

if first_player == 1:
    player_playing = True

else:
    player_playing = False

game = Game(difficulty, num_layers)

#print full board
print("* * * * *")
for count in range(num_layers):
    print("* 0 1 2 *")
print("* * * * *")


#play the game
while not game.get_tower().is_finished():

    if player_playing:
        layer, block = input("Make a move: ")
        game.player_moves(layer, block)
        player_playing = False

    else:
        game.computer_moves()
        player_playing = True

    #print remaining blocks
    layer_num = 0
    print("* * * * *")
    for i in game.get_tower().get_layers():

        if (len(i) == 3):
            print(str(layer_num) + " * 0 1 2 *")

        elif(len(i) == 1):
            print(str(layer_num) + " *   1   *")

        elif(i == [0, 1]):
            print(str(layer_num) + " * 0 1   *")

        elif (i == [0, 2]):
            print(str(layer_num) + " * 0   2 *")

        else:
            print(str(layer_num) + " *   1 2 *")

    print("* * * * *")

#determine who wins
if(not player_playing):
    print("Player win!")
else:
    print("Computer win!")