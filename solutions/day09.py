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
        code = data[0]
        # decompressed = ""
        # while code.count("("):
        #     idx = code.index("(")
        #     decompressed += code[:idx]
        #     code = code[idx:]
        #     idx2 = code.index(")")
        #     marker = code[: idx2 + 1]
        #     code = code[idx2 + 1 :]
        #     s, t = map(int, marker[1:-1].split("x"))
        #     c = code[:s]
        #     code = code[s:]
        #     decompressed += c * t
        # decompressed += code
        # return len(decompressed)
        decompressed = self.decomp_len(code)
        return decompressed

    def part2(self, data):
        code = data[0]
        decompressed = self.decomp_len(code, True)
        return decompressed

    def decomp_len(self, code, within=False):
        leng = 0
        while code.count("("):
            idx = code.index("(")
            leng += len(code[:idx])
            code = code[idx:]
            idx2 = code.index(")")
            marker = code[: idx2 + 1]
            code = code[idx2 + 1 :]
            s, t = map(int, marker[1:-1].split("x"))
            c = code[:s]
            code = code[s:]
            if within:
                leng += t * self.decomp_len(c, True)
            else:
                leng += t * len(c)
        else:
            leng += len(code)
        return leng
