from classes.tower import Tower
import random

class Game:

    def __init__(self, difficulty, num_layers):

        if difficulty == "wimpy":
            self.diff = .25
        if difficulty == "easy":
            self.diff = .50
        if difficulty == "medium":
            self.diff = .75
        if difficulty == "hard":
            self.diff = 1

        self.t = Tower(num_layers)

    def player_moves(self, layer, block):
        self.t.remove_block(layer, block)

    def computer_moves(self):
        # If diff == hard, then always make optimal rule
        # Otherwise, use diff % for probability of making right move
        # If odds are not in computer's favor, choose random deletion
        # Use Tower's last move for symmetry strategy


        if self.__is_optimal_used():
            if self.t.last_move == []:
                if len(self.t.get_layers()) % 2 == 0:
                    comp_layer, comp_block = self.__compute_random_move()
                    self.t.remove_block(comp_layer, comp_block)
                else:
                    comp_layer = int(len(self.t.get_layers()) / 2)
                    self.t.remove_block(comp_layer, 1)

            else:
                comp_layer, comp_block = self.__compute_optimal_move(self.t.last_move[0], self.t.last_move[1])
                self.t.remove_block(comp_layer, comp_block)

        else:
            comp_layer, comp_block = self.__compute_random_move()
            self.t.remove_block(comp_layer, comp_block)

    def __compute_random_move(self):
        while True:
            random_layer = random.randint(0, len(self.t.get_layers()) - 1)
            random_block = random.randint(0, 2)
            if self.t.is_valid(random_layer, random_block):
                break

        return random_layer, random_block

    def __compute_optimal_move(self, last_layer, last_block):
        # len(layers) - 1 :---> Sum you should get when adding two symmetrical layers
        # take previous move layer number ((len(layers) - 1) - previous_layer_number = result where comp should play in
        # block doesnt matter

        # special case!
        # player moves to middle block (odd number of layers), but chooses 0 or 2
        # must choose 0 or 2

        symmetrical_layer = ((len(self.t.get_layers()) - 1) - last_layer)
        if self.t.is_valid(symmetrical_layer, last_block):
            return symmetrical_layer, last_block
        else:
            if symmetrical_layer == int(len(self.t.get_layers()) / 2):
                if last_block == 0:
                    if self.t.is_valid(symmetrical_layer, 2):
                        return symmetrical_layer, 2
                elif last_block == 2:
                    if self.t.is_valid(symmetrical_layer, 0):
                        return symmetrical_layer, 0
                else:
                    return self.__compute_random_move()

            else:
                return self.__compute_random_move()

    def __is_optimal_used(self):
        if self.diff == 1:
            return True

        prob = random.random()

        if prob <= self.diff:
            return True

        return False

    def get_tower(self):
        return self.t