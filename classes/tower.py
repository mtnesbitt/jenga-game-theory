class Tower:

    def __init__(self, num_layers):
        self.tower = [[0,1,2] for x in range(num_layers)]
        self.last_move = []

    def is_valid(self, layer_num, block_num):
        # Checks if middle piece is left
        if len(self.tower[layer_num]) == 1:
            return False

        # checks if block number still exists in layer
        elif block_num not in self.tower[layer_num]:
            return False

        elif len(self.tower[layer_num]) == 3:
            return True

        # Checks length two cases: [1,2], [0,1]
        else:
            if block_num != 1:
                return True

        return False

    def remove_block(self, layer_num, block_num):
        self.tower[layer_num].remove(block_num)
        self.last_move = [layer_num, block_num]


    def is_finished(self):
        for layer in self.tower:
            if len(layer) == 1:
                continue
            elif len(layer) == 2:
                if 1 in layer:
                    return False
            elif len(layer) == 3:
                return False
        return True

    def get_last_move(self):
        return self.last_move

    def get_layers(self):
        return self.tower
