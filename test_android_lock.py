import unittest
from android_lock import AndroidLock


class AndroidLockTest(unittest.TestCase):
    def setUp(self):
        self.solver = AndroidLock(3, 3)

    def test_num_1(self):
        self.assertEqual(9, self.solver.solve(1, 1))

    def test_num_2(self):
        small_solver = AndroidLock(2, 2)
        self.assertEqual(12, small_solver.solve(2, 2))

    def test_num_3(self):
        small_solver = AndroidLock(2, 2)
        self.assertEqual(24, small_solver.solve(3, 3))

    def test_num_4(self):
        self.assertEqual(9, self.solver.solve(1, 1))

    def test_num_5(self):
        self.assertEqual(1624, self.solver.solve(4, 4))

    #  corners = 5
    #  mids = 7
    #  center = 8
    #  5 * 4 + 7 * 4 + 8 = 56
    def test_num_6(self):
        self.assertEqual(56, self.solver.solve(2, 2))

    def test_num_7(self):
        self.assertEqual(389112, self.solver.solve(4, 9))

    def test_num_8(self):
        self.assertEqual(7152, self.solver.solve(5, 5))

    def test_num_9(self):
        self.assertEqual(26016, self.solver.solve(6, 6))

    def test_num_10(self):
        self.assertEqual(72912, self.solver.solve(7, 7))

    def test_num_10(self):
        self.assertEqual(140704, self.solver.solve(8, 8))

    def test_straight_line_1(self):
        a = (1, 2)
        b = (3, 2)
        visited = [(2, 2)]

        self.assertEqual(True, self.solver.straight_line(a, b, visited))

        a = (1, 1)
        b = (3, 3)
        visited = [(2, 2)]

        self.assertEqual(True, self.solver.straight_line(a, b, visited))

        a = (1, 1)
        b = (3, 3)
        visited = []

        self.assertEqual(False, self.solver.straight_line(a, b, visited))

        a = (1, 1)
        b = (3, 1)
        visited = self.all_nums()
        visited.remove((2, 1))

        self.assertEqual(False, self.solver.straight_line(a, b, visited))

    def test_knights_move(self):
        a = (1, 1)
        b = (2, 3)

        self.assertEqual(True, self.solver.is_knights_move(a, b))

        a = (1, 1)
        b = (2, 2)

        self.assertEqual(False, self.solver.is_knights_move(a, b))

    def all_nums(self):
        return [(x, y) for x in range(1, self.solver.width + 1)
                for y in range(1, self.solver.height + 1)]


if __name__ == '__main__':
    unittest.main()
