import unittest

from chess_dfs import *


class TestChessDFS(unittest.TestCase):
    def test_is_win(self):
        knight1 = ChessFigure('a', 8)
        pawn1 = ChessFigure('a', 8)
        pawn2 = ChessFigure('b', 7)
        self.assertTrue(is_win(knight1, pawn1))
        self.assertFalse(is_win(knight1, pawn2))

    def test_is_right_index(self):
        knight1 = ChessFigure('a', 8)
        self.assertFalse(is_right_index(knight1, deltas_sequence[0]))
        self.assertFalse(is_right_index(knight1, deltas_sequence[1]))
        self.assertFalse(is_right_index(knight1, deltas_sequence[2]))
        self.assertFalse(is_right_index(knight1, deltas_sequence[3]))
        self.assertFalse(is_right_index(knight1, deltas_sequence[4]))
        self.assertTrue(is_right_index(knight1, deltas_sequence[5]))
        self.assertTrue(is_right_index(knight1, deltas_sequence[6]))
        self.assertFalse(is_right_index(knight1, deltas_sequence[7]))

        knight2 = ChessFigure('d', 4)
        for delta in deltas_sequence:
            self.assertTrue(is_right_index(knight2, delta))

    def test_is_dead_move(self):
        pawn = ChessFigure('e', 7)
        self.assertTrue(is_dead_move(5, 5, pawn))
        self.assertTrue(is_dead_move(3, 5, pawn))
        self.assertFalse(is_dead_move(3, 3, pawn))

    def test_get_next_pos_indexes(self):
        knight = ChessFigure('d', 4)
        self.assertEqual(get_next_pos_indexes(knight, deltas_sequence[0]), (4, 5))
        self.assertEqual(get_next_pos_indexes(knight, deltas_sequence[1]), (2, 5))

    def test_get_neighbours(self):
        knight1 = ChessFigure('h', 7)
        pawn1 = ChessFigure('e', 7)
        self.assertEqual(get_neighbours(knight1, pawn1), [('f', 8), ('g', 5)])
        knight2 = ChessFigure('d', 4)
        pawn2 = ChessFigure('d', 3)
        self.assertEqual(get_neighbours(knight2, pawn2), [('e', 6), ('c', 6), ('b', 5), ('b', 3), ('f', 3), ('f', 5)])

    def test_get_route_with_dfs(self):
        knight1, pawn1 = ChessFigure('b', 5), ChessFigure('e', 7)
        visited1 = [(knight1.letter, knight1.number)]
        stack1 = [(knight1.letter, knight1.number)]
        route1 = [(knight1.letter, knight1.number)]
        self.assertEqual(get_route_with_dfs(pawn1, visited1, stack1, route1),
                         [('b', 5), ('c', 7), ('a', 8), ('b', 6),
                          ('c', 8), ('a', 7), ('c', 6), ('d', 8),
                          ('b', 7), ('a', 5), ('b', 3), ('c', 5),
                          ('d', 7), ('b', 8), ('a', 6), ('b', 4),
                          ('a', 2), ('c', 1), ('d', 3), ('e', 5),
                          ('f', 7), ('g', 5), ('h', 7), ('f', 8),
                          ('e', 6), ('d', 4), ('c', 2), ('a', 3),
                          ('b', 1), ('c', 3), ('d', 5), ('e', 7)])
        knight2, pawn2 = ChessFigure('b', 5), ChessFigure('b', 5)
        visited2 = [(knight2.letter, knight2.number)]
        stack2 = [(knight2.letter, knight2.number)]
        route2 = [(knight2.letter, knight2.number)]
        self.assertEqual(get_route_with_dfs(pawn2, visited2, stack2, route2),
                         [('b', 5)])


if __name__ == '__main__':
    unittest.main()
