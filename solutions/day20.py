from collections import deque
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
        ips = deque([f"0-{9 if len(data) == 3 else 2 ** 32 - 1}"])
        ips = self.apply_filter(ips, data)
        return min(int(i.split("-")[0]) for i in ips)

    def part2(self, data):
        ips = deque([f"0-{9 if len(data) == 3 else 2 ** 32 - 1}"])
        ips = self.apply_filter(ips, data)
        return sum((a := [*map(int, i.split("-"))])[1] - a[0] + 1 for i in ips)

    def apply_filter(self, ips, blacklists):
        for rule in blacklists:
            new_ips = deque([])

            while ips:
                ip = ips.popleft()
                x, y = map(int, ip.split("-"))
                a, b = map(int, rule.split("-"))

                if x > b or y < a:
                    new_ips.append(f"{x}-{y}")
                elif x < a and y > b:
                    new_ips.append(f"{x}-{a-1}")
                    new_ips.append(f"{b+1}-{y}")
                elif x == a and y > b:
                    new_ips.append(f"{b+1}-{y}")
                elif x < a and y == b:
                    new_ips.append(f"{x}-{a-1}")
                elif x < a and y < b:
                    new_ips.append(f"{x}-{a-1}")
                elif x > a and y > b:
                    new_ips.append(f"{b+1}-{y}")

            ips = new_ips
        return ips
