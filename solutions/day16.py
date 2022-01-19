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
        a = data[0]
        leng = 20 if a == "10000" else 272
        return self.get_checksum(a, leng)

    def part2(self, data):
        a = data[0]
        leng = 20 if a == "10000" else 35651584
        return self.get_checksum(a, leng)

    def get_checksum(self, a, leng):
        while len(a) < leng:
            b = a[::-1]
            b = bin((2 ** len(b) - 1) ^ int(b, 2))[2:].rjust(len(a), "0")
            a = a + "0" + b
        a = a[:leng]
        c = a
        while len(c) % 2 == 0:
            c = "".join(["0", "1"][c[i] == c[i + 1]] for i in range(0, len(c), 2))
        return c
