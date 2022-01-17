import re
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
        count = 0
        for ip in data:
            inside = re.findall(r"\[\w+?\]", ip)
            for i in inside:
                ip = ip.replace(i, " ")
            outside = ip.split()
            inside = [i[1:-1] for i in inside]
            if not any(self.check_abba(i) for i in inside) and any(self.check_abba(i) for i in outside):
                count += 1
        return count

    def part2(self, data):
        count = 0
        for ip in data:
            inside = re.findall(r"\[\w+?\]", ip)
            for i in inside:
                ip = ip.replace(i, " ")
            outside = ip.split()
            inside = [i[1:-1] for i in inside]
            bab = self.get_all_bab(inside)
            for i in bab:
                aba = i[1:] + i[1]
                if aba in " ".join(outside):
                    count += 1
                    break
        return count

    def check_abba(self, s):
        return any(s[i] == s[i + 3] and s[i + 1] == s[i + 2] and s[i] != s[i + 1] for i in range(len(s) - 3))

    def get_all_bab(self, ss):
        bab = []
        for s in ss:
            for i in range(len(s) - 2):
                if s[i] == s[i + 2] and s[i] != s[i + 1]:
                    bab += [s[i : i + 3]]
        return bab
