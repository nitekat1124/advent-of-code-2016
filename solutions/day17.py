import hashlib
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
        passcode = data[0]
        path = ""
        loc = (0, 0)
        self.dirs = {(0, -1): "U", (0, 1): "D", (-1, 0): "L", (1, 0): "R"}

        paths = self.all_paths(loc, passcode, path)
        return sorted(paths, key=lambda x: len(x))[0]

    def part2(self, data):
        passcode = data[0]
        path = ""
        loc = (0, 0)
        self.dirs = {(0, -1): "U", (0, 1): "D", (-1, 0): "L", (1, 0): "R"}

        paths = self.all_paths(loc, passcode, path)
        return len(sorted(paths, key=lambda x: len(x))[-1])

    def all_paths(self, loc, passcode, path):
        paths = []

        if loc == (3, 3):
            return [path]

        hash = hashlib.md5((passcode + path).encode("utf-8")).hexdigest()[:4]

        idx = [i for i, v in enumerate([1 if i in "bcdef" else 0 for i in hash]) if v == 1]
        possible_moves = [i for i in [list(self.dirs.keys())[i] for i in idx] if loc[0] + i[0] in range(4) and loc[1] + i[1] in range(4)]

        for move in possible_moves:
            next_loc = (loc[0] + move[0], loc[1] + move[1])
            next_path = path + self.dirs[move]
            paths.extend(self.all_paths(next_loc, passcode, next_path))

        return paths
