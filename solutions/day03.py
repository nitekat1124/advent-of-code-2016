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
        return len([1 for i in data if sum(sorted(map(int, i.split()))[:2]) > sorted(map(int, i.split()))[2]])

    def part2(self, data):
        count = 0
        for i in range(len(data) // 3):
            for a, b, c in zip(map(int, data[i * 3].split()), map(int, data[i * 3 + 1].split()), map(int, data[i * 3 + 2].split())):
                a, b, c = sorted([a, b, c])
                if a + b > c:
                    count += 1
        return count
