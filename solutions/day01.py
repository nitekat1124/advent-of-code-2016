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
                if func(i) == int(r[0]):
                    print(f"test {test_counter} passed")
                else:
                    print(func(i))
                    print(r[0])
                    print(f"test {test_counter} NOT passed")
            test_counter += 1
        print()

    def part1(self, data):
        insts = data[0].split(", ")
        direction = 0
        loc = (0, 0)
        move = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        for inst in insts:
            d, n = inst[0], int(inst[1:])
            if d == "R":
                direction = (direction + 1) % 4
            else:
                direction = (direction + 3) % 4
            loc = (loc[0] + move[direction][0] * n, loc[1] + move[direction][1] * n)
        return abs(loc[0]) + abs(loc[1])

    def part2(self, data):
        insts = data[0].split(", ")
        direction = 0
        loc = (0, 0)
        last = loc
        move = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        visited = [loc]

        for inst in insts:
            d, n = inst[0], int(inst[1:])
            if d == "R":
                direction = (direction + 1) % 4
            else:
                direction = (direction + 3) % 4
            for i in range(1, n + 1):
                loc = (last[0] + move[direction][0] * i, last[1] + move[direction][1] * i)
                if loc in visited:
                    return abs(loc[0]) + abs(loc[1])
                visited += [loc]
            last = loc
