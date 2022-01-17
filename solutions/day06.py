from typing import Counter
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
        length = len(data[0])
        chars = [[c[i] for c in data] for i in range(length)]
        s = [Counter(c).most_common(1)[0][0] for c in chars]
        return "".join(s)

    def part2(self, data):
        length = len(data[0])
        chars = [[c[i] for c in data] for i in range(length)]
        s = [Counter(c).most_common()[-1][0] for c in chars]
        return "".join(s)
