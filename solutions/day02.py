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
        loc = (1, 1)
        move = {"U": (0, -1), "R": (1, 0), "D": (0, 1), "L": (-1, 0)}
        code = []
        for i in data:
            for c in i:
                m = move[c]
                loc = (min(2, max(0, loc[0] + m[0])), min(2, max(0, loc[1] + m[1])))
            code += [str(loc[0] + loc[1] * 3 + 1)]
        return "".join(code)

    def part2(self, data):
        loc = (0, 2)
        move = {"U": (0, -1), "R": (1, 0), "D": (0, 1), "L": (-1, 0)}
        keypads = {
            (2, 0): "1",
            (1, 1): "2",
            (2, 1): "3",
            (3, 1): "4",
            (0, 2): "5",
            (1, 2): "6",
            (2, 2): "7",
            (3, 2): "8",
            (4, 2): "9",
            (1, 3): "A",
            (2, 3): "B",
            (3, 3): "C",
            (2, 4): "D",
        }
        code = []
        for i in data:
            for c in i:
                m = move[c]
                new_loc = (loc[0] + m[0], loc[1] + m[1])
                if new_loc in keypads:
                    loc = new_loc

            code += [keypads[loc]]
        return "".join(code)
