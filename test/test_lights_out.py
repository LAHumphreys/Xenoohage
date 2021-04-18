from unittest import TestCase
from lights_out import hit_button, matches, find_path

class TestLightsOut(TestCase):
    def get_board(self):
        return [['A', 'A', 'A'],
                ['A', 'A', '='],
                ['A', '=', 'A']]

    def test_top_left(self):
        result = hit_button(self.get_board(), [(0, 0)])
        expected =[['*', '*', '*'],
                   ['*', 'A', '='],
                   ['*', '=', 'A']]
        self.assertListEqual(result, expected)

    def test_top_middle(self):
        result = hit_button(self.get_board(), [(0, 1)])
        expected = [['*', '*', '*'],
                    ['A', '*', '='],
                    ['A', '^', 'A']]
        self.assertListEqual(result, expected)

    def test_middle(self):
        result = hit_button(self.get_board(), [(1, 1)])
        expected = [['A', '*', 'A'],
                    ['*', '*', '^'],
                    ['A', '^', 'A']]
        self.assertListEqual(result, expected)

    def test_top_left_buttom_right(self):
        result = hit_button(self.get_board(), [(0, 0), (2, 2)])
        expected =[['*', '*', '='],
                   ['*', 'A', '^'],
                   ['=', '^', '*']]
        self.assertListEqual(result, expected)

    def test_top_left_buttom_middle_right(self):
        result = hit_button(self.get_board(), [(0, 0), (2, 2), (1, 1)])
        expected =[['*', '=', '='],
                   ['=', '*', 'A'],
                   ['=', 'A', '*']]
        self.assertListEqual(result, expected)

    def test_matches(self):
        board_2 = [['*', '=', '='],
                   ['=', '*', 'A'],
                   ['=', 'A', '*']]
        board_1 = [['*', '=', '='],
                   ['=', '*', 'A'],
                   ['=', 'A', '*']]
        self.assertTrue(matches(board_1, board_2))

    def test_not_matches(self):
        board_2 = [['*', '=', '='],
                   ['=', '*', 'A'],
                   ['=', 'A', '*']]
        board_1 = [['*', '=', '='],
                   ['=', '^', 'A'],
                   ['=', 'A', '*']]
        self.assertFalse(matches(board_1, board_2))

    def test_search_one_step(self):
        input = self.get_board()
        final_board =  [['A', '*', 'A'],
                        ['*', '*', '^'],
                        ['A', '^', 'A']]
        expected = [(1,1)]
        result = find_path(input, final_board, 1)
        self.assertListEqual(expected, result)

    def test_search_two_step(self):
        input = self.get_board()
        expected = [(2, 2), (0, 0)]
        final_board =[['*', '*', '='],
                      ['*', 'A', '^'],
                      ['=', '^', '*']]
        result = find_path(input, final_board, 2)
        self.assertListEqual(expected, result)

    def test_search_three_step(self):
        input = self.get_board()
        expected = [(2, 2), (1, 1), (0, 0)]
        final_board =[['*', '=', '='],
                      ['=', '*', 'A'],
                      ['=', 'A', '*']]
        result = find_path(input, final_board, 3)
        self.assertListEqual(expected, result)
