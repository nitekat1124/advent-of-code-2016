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
                if str(func(i)) == r[0]:
                    print(f"test {test_counter} passed")
                else:
                    print(func(i))
                    print(r[0])
                    print(f"test {test_counter} NOT passed")
            test_counter += 1
        print()

    def part1(self, data):
        code = []
        m = hashlib.md5()
        id = data[0]
        n = 0

        while len(code) < 8:
            m = hashlib.md5(f"{id}{n}".encode())
            if m.hexdigest()[:5] == "00000":
                print(n, m.hexdigest())
                code += [m.hexdigest()[5]]
            n += 1

        return "".join(code)

    def part2(self, data):
        code = list(" " * 8)
        m = hashlib.md5()
        id = data[0]
        n = 0

        while code.count(" ") > 0:
            m = hashlib.md5(f"{id}{n}".encode())
            if m.hexdigest()[:5] == "00000":
                print(n, m.hexdigest())
                a = m.hexdigest()[5]
                b = m.hexdigest()[6]
                if a.isdigit() and int(a) < 8 and code[int(a)] == " ":
                    code[int(a)] = b
            n += 1

        return "".join(code)
