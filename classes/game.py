from classes.tower import Tower

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

        self.diff = difficulty
        self.t = Tower(num_layers)

    def player_moves(self, layer, block):
        if not self.t.remove_block(layer, block):
            return True
        return False

    def computer_moves(self):
        # If diff == hard, then always make optimal rule
        # Otherwise, use diff % for probability of making right move
        # If odds are not in computer's favor, choose random deletion
        # Use Tower's last move for symmetry strategy
        previous_play = self.t.last_move


        return

    def __get_tower(self):
        return self.t

