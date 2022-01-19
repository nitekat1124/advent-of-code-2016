from collections import deque
from copy import deepcopy
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
                if str(func(i)) == r[0]:
                    print(f"test {test_counter} passed")
                else:
                    print(func(i))
                    print(r[0])
                    print(f"test {test_counter} NOT passed")
            test_counter += 1
        print()

    def part1(self, data):
        n = int(data[0])
        w = 10 if n == 10 else 33
        h = 7 if n == 10 else 41

        p = (1, 1)
        target = (7, 4) if n == 10 else (31, 39)

        _map = self.gen_map(w, h, n)
        _map_sets = self.set_route(deepcopy(_map), p, target, 0, None)

        s = [i[target[1]][target[0]] for i in _map_sets]
        s = [i for i in s if i != "."]

        return min(s)

    def part2(self, data):
        n = int(data[0])
        w = 10 if n == 10 else 30
        h = 7 if n == 10 else 30

        p = (1, 1)

        _map = self.gen_map(w, h, n)
        _map_sets = self.set_route2(deepcopy(_map), p, 0)

        points = set()
        for m in _map_sets:
            for y in range(h):
                for x in range(w):
                    if type(m[y][x]) is int:
                        points.add((x, y))

        return len(points)

    def gen_map(self, w, h, n):
        _map = []
        for y in range(h):
            row = []
            for x in range(w):
                row += [[".", "#"][(bin(x * x + 3 * x + 2 * x * y + y + y * y + n).count("1")) % 2]]
            _map += [row]
        return _map

    def set_route(self, _map, p, target, count, _max):
        d = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        _map_sets = deque([])

        if _map[p[1]][p[0]] == ".":
            _map[p[1]][p[0]] = count

            if _max is None or _max > count:
                if p == target:
                    _max = count
                    _map_sets.append(deepcopy(_map))
                else:
                    for dp in d:
                        np = (p[0] + dp[0], p[1] + dp[1])
                        if np[0] >= 0 and np[0] < len(_map[0]) and np[1] >= 0 and np[1] < len(_map):
                            _map_sets.extend(self.set_route(deepcopy(_map), np, target, count + 1, _max))
        return _map_sets

    def set_route2(self, _map, p, count):
        d = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        _map_sets = deque([])

        if _map[p[1]][p[0]] == ".":
            _map[p[1]][p[0]] = count

            if count < 51:
                _map_sets.append(deepcopy(_map))
                for dp in d:
                    np = (p[0] + dp[0], p[1] + dp[1])
                    if np[0] >= 0 and np[0] < len(_map[0]) and np[1] >= 0 and np[1] < len(_map):
                        _map_sets.extend(self.set_route2(deepcopy(_map), np, count + 1))
        return _map_sets
