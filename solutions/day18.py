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
        rows = data
        rounds = 10 if len(rows[0]) == 10 else 40
        rows = self.exec(rows, rounds)
        return sum(r.count(".") for r in rows)

    def part2(self, data):
        rows = data
        rounds = 10 if len(rows[0]) == 10 else 400000
        rows = self.exec(rows, rounds)
        return sum(r.count(".") for r in rows)

    def exec(self, rows, rounds):
        for _ in range(rounds - 1):
            prev = "." + rows[-1] + "."
            cur = []
            for i in range(len(rows[-1])):
                c = prev[i : i + 3]
                cur += [["^", "."][c[0] == c[2]]]
            rows += ["".join(cur)]
        return rows
