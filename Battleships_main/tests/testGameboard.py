import unittest
from ..Battleships_main.Gameboard import GameBoard

class TestGameBoard(unittest.TestCase):
    def setUp(self) -> None:
        return super().setUp()
    def tearDown(self) -> None:
        return super().tearDown()
        
    def test___newBoard(self):
        self.assertEqual(__newBoard(2), [[' ',' '],[' ',' ']])

    def test_sumUp(self):
        result = sumUp(1,1)
        self.assertEqual(result, 2)

if __name__ == '__main__':
    unittest.main()