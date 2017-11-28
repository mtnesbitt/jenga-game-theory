from unittest import TestCase
from classes.tower import Tower

class TestTower(TestCase):

    def test_is_valid_true_full_game(self):
        t = Tower(3)
        self.assertTrue(t.is_valid(0,0))

    def test_is_valid_non_existent_block(self):
        t = Tower(3)
        self.assertFalse(t.is_valid(0,4))

    def test_is_valid_non_existent_layer(self):
        t = Tower(3)
        self.assertFalse(t.is_valid(4,0))

    def test_remove_block_exception(self):
        t = Tower(3)
        t.remove_block(0, 1)
        self.assertRaises(Exception, t.remove_block(0,2))

    def test_is_finished_true(self):
        t = Tower(1)
        t.remove_block(0, 1)
        self.assertTrue(t.is_finished())

    def test_is_finished_false(self):
        t = Tower(1)
        self.assertFalse(t.is_finished())

    def test_get_last_move(self):
        t = Tower(1)
        t.remove_block(0, 1)
        self.assertEquals([0,1], t.get_last_move())

    def test_get_layers(self):
        t = Tower(1)
        t.remove_block(0, 1)
        self.assertEquals([[0, 2]], t.get_layers())

