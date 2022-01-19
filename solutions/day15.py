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
        discs = []
        for line in data:
            parts = line.split()
            disc = [int(parts[3]), int(parts[11][:-1])]
            discs += [disc]
        t = 0
        while 1:
            for i in range(len(discs)):
                if (1 + t + i + discs[i][1]) % discs[i][0] != 0:
                    t += 1
                    break
            else:
                return t

    def part2(self, data):
        discs = []
        for line in data:
            parts = line.split()
            disc = [int(parts[3]), int(parts[11][:-1])]
            discs += [disc]
        discs += [[11, 0]]
        t = 0
        while 1:
            for i in range(len(discs)):
                if (1 + t + i + discs[i][1]) % discs[i][0] != 0:
                    t += 1
                    break
            else:
                return t
