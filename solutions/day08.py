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
        screen = [[False] * 50 for i in range(6)]
        for line in data:
            if line.startswith("rect"):
                x, y = line.split(" ")[1].split("x")
                for i in range(int(x)):
                    for j in range(int(y)):
                        if i in range(50) and j in range(6):
                            screen[j][i] = True
            elif line.startswith("rotate row"):
                parts = line.split(" ")
                y = int(parts[2].split("=")[1])
                n = int(parts[-1])
                if y in range(6):
                    row = screen[y]
                    screen[y] = row[-n:] + row[:-n]
            elif line.startswith("rotate column"):
                parts = line.split(" ")
                x = int(parts[2].split("=")[1])
                n = int(parts[-1])
                if x in range(50):
                    col = [screen[i][x] for i in range(6)]
                    for i in range(6):
                        screen[i][x] = col[(i - n) % 6]
        return sum([sum(row) for row in screen])

    def part2(self, data):
        screen = [[False] * 50 for i in range(6)]
        for line in data:
            if line.startswith("rect"):
                x, y = line.split(" ")[1].split("x")
                for i in range(int(x)):
                    for j in range(int(y)):
                        if i in range(50) and j in range(6):
                            screen[j][i] = True
            elif line.startswith("rotate row"):
                parts = line.split(" ")
                y = int(parts[2].split("=")[1])
                n = int(parts[-1])
                if y in range(6):
                    row = screen[y]
                    screen[y] = row[-n:] + row[:-n]
            elif line.startswith("rotate column"):
                parts = line.split(" ")
                x = int(parts[2].split("=")[1])
                n = int(parts[-1])
                if x in range(50):
                    col = [screen[i][x] for i in range(6)]
                    for i in range(6):
                        screen[i][x] = col[(i - n) % 6]
        for row in screen:
            print("".join(["#" if i else " " for i in row]))
        return None
