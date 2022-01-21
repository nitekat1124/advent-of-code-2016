from collections import deque
from itertools import combinations, permutations
from utils.solution_base import SolutionBase


class Solution(SolutionBase):
    def solve(self, part_num: int):
        self.test_runner(part_num)

        func = getattr(self, f"part{part_num}")
        result = func(self.data)
        return result

    def test_runner(self, part_num):
        test_inputs = self.get_test_input()
        test_results = self.get_test_result(part_num)
        test_counter = 1

        func = getattr(self, f"part{part_num}")
        for i, r in zip(test_inputs, test_results):
            if len(r):
                if (tr := str(func(i))) == r[0]:
                    print(f"test {test_counter} passed")
                else:
                    print(f"your result: {tr}")
                    print(f"test answer: {r[0]}")
                    print(f"test {test_counter} NOT passed")
            test_counter += 1
        print()

    def part1(self, data):
        points = {}
        points_distances = {}
        routes_distances = []

        self.map = []
        for line in data:
            row = []
            for x, v in enumerate(line):
                if v in ".#":
                    row += [v]
                else:
                    points[int(v)] = (x, len(self.map))
                    row += ["."]
            self.map += [row]

        routes = [r for r in permutations(points.keys(), len(points)) if r[0] == 0]
        pairs = [*combinations(points.keys(), 2)]

        for p in pairs:
            d = self.find_distances(points[p[0]], points[p[1]])
            points_distances[p] = d
            p1 = (p[1], p[0])
            points_distances[p1] = d

        routes_distances = [sum(points_distances[(r[i], r[i + 1])] for i in range(len(r) - 1)) for r in routes]
        return min(routes_distances)

    def part2(self, data):
        points = {}
        points_distances = {}
        routes_distances = []

        self.map = []
        for line in data:
            row = []
            for x, v in enumerate(line):
                if v in ".#":
                    row += [v]
                else:
                    points[int(v)] = (x, len(self.map))
                    row += ["."]
            self.map += [row]

        routes = [list(r) + [0] for r in permutations(points.keys(), len(points)) if r[0] == 0]
        pairs = [*combinations(points.keys(), 2)]

        for p in pairs:
            d = self.find_distances(points[p[0]], points[p[1]])
            points_distances[p] = d
            p1 = (p[1], p[0])
            points_distances[p1] = d

        routes_distances = [sum(points_distances[(r[i], r[i + 1])] for i in range(len(r) - 1)) for r in routes]
        return min(routes_distances)

    def find_distances(self, p1, p2):
        routes = deque([(0, p1)])
        seen = set([p1])
        while routes:
            dst, curr = routes.pop()
            if curr == p2:
                return dst  # first match must be the shortest
            x, y = curr
            for nx, ny in [(x, y - 1), (x + 1, y), (x, y + 1), (x - 1, y)]:
                if self.map[ny][nx] == "." and (nx, ny) not in seen:
                    routes.appendleft((dst + 1, (nx, ny)))
                    seen.add((nx, ny))
        return -1
