import math


class AndroidLock:
    def __init__(self, w, h):
        self.width = w
        self.height = h
        self.pad = [(x, y) for x in range(1, w + 1) for y in range(1, h + 1)]

    def distance(self, a, b):
        return abs(a - b)

    def is_knights_move(self, a, b):
        (x1, y1), (x2, y2) = a, b
        return (self.distance(y1, y2) is 2 and self.distance(x1, x2) is 1) or (
            self.distance(x1, x2) is 2 and self.distance(y1, y2) is 1)

    def nothing_blocking(self, a, b, visited):
        (x1, y1), (x2, y2) = a, b

        if (x1 == x2): dx = 0
        elif x1 < x2: dx = 1
        else: dx = -1

        if (y1 == y2): dy = 0
        elif y1 < y2: dy = 1
        else: dy = -1

        (i, j) = a

        while (i, j) != b:
            i += dx
            j += dy
            if (i, j) != a and (i, j) != b and (i, j) not in visited:
                return False

        return True

    def is_diagonal(self, a, b):
        (x1, y1), (x2, y2) = a, b
        return abs(x1 - x2) is abs(y1 - y2)

    def straight_line(self, a, b, visited):
        (x1, y1), (x2, y2) = a, b

        if (x1 is not x2) and (y1 is not y2) and not self.is_diagonal(a, b):
            return False

        return self.nothing_blocking(a, b, visited)

    def can_visit(self, a, b, visited):
        if self.is_knights_move(a, b):
            return True

        return self.straight_line(a, b, visited)

    def solve(self, min_len, max_len):
        total_paths = []

        for length in range(min_len, max_len + 1):
            paths = []

            for coord in self.pad:
                unvisited = set(self.pad)
                unvisited.remove(coord)

                self.visit(unvisited, [coord], paths, length,
                           self.printPad(self.width, self.height))

            print(f"there are {len(paths)} paths with length {length}")
            total_paths += paths

        print(f"there are {len(total_paths)} total paths")
        return len(total_paths)

    def visit(self, unvisited, visited, res, length, p):
        if len(visited) == length:
            res.append(visited)
            return

        for coord in unvisited:
            if self.can_visit(visited[-1], coord, visited):
                visited_copy = list(visited)
                visited_copy.append(coord)

                unvisited_copy = set(unvisited)
                unvisited_copy.remove(coord)

                self.visit(unvisited_copy, visited_copy, res, length, p)

    def printPad(self, w, h):
        pad = [['' for x in range(w)] for y in range(h)]

        def print1(visited, unvisited):
            for (x, y) in visited:
                pad[x - 1][y - 1] = 'x'
            for (x, y) in unvisited:
                pad[x - 1][y - 1] = '-'

            for i in range(len(pad)):
                for j in range(len(pad[i])):
                    print(pad[i][j], end=' ')
                print()

        return print1
