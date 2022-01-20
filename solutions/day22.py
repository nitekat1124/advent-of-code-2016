from itertools import combinations
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
        nodes = []
        for line in data[2:]:
            parts = line.split()
            p = parts[0].split("-")
            node = (int(p[1][1:]), int(p[2][1:]), int(parts[2][:-1]), int(parts[3][:-1]))
            nodes += [node]
        pairs = list(combinations(nodes, 2))
        viable = 0
        for a, b in pairs:
            if (a[0], a[1]) == (b[0], b[1]):
                continue
            if a[2] <= b[3] and a[2] > 0:
                viable += 1
            if b[2] <= a[3] and b[2] > 0:
                viable += 1
        return viable

    def part2(self, data):
        large = 15 if len(data) == 11 else 100

        nodes = {}
        for line in data[2:]:
            parts = line.split()
            p = parts[0].split("-")
            nodes[(int(p[1][1:]), int(p[2][1:]))] = (int(parts[1][:-1]), int(parts[2][:-1]), int(parts[3][:-1]))

        w = max(i[0] for i in nodes.keys())
        h = max(i[1] for i in nodes.keys())

        grid = []
        for y in range(h + 1):
            row = []
            for x in range(w + 1):
                sign = " G " if (x, y) == (w, 0) else "(.)" if (x, y) == (0, 0) else " # " if nodes[(x, y)][0] > large else " _ " if nodes[(x, y)][1] == 0 else " . "
                row += [sign]
            grid += [row]

        # for i in grid:
        #     print(*i, sep="")

        steps = 0
        while 1:
            empty = [(i, j) for i in range(w + 1) for j in range(h + 1) if grid[j][i] == " _ "][0]
            g_pos = [(i, j) for i in range(w + 1) for j in range(h + 1) if grid[j][i] == " G "][0]

            if g_pos == (0, 0):
                return steps

            # print(g_pos)
            # print(empty)

            if g_pos == (w, 0):
                if empty[1] > 0:
                    up = [grid[i][empty[0]] for i in range(empty[1])]
                    if " # " in up:
                        grid[empty[1]][empty[0]], grid[empty[1]][empty[0] - 1] = grid[empty[1]][empty[0] - 1], grid[empty[1]][empty[0]]
                    else:
                        grid[empty[1]][empty[0]], grid[empty[1] - 1][empty[0]] = grid[empty[1] - 1][empty[0]], grid[empty[1]][empty[0]]
                    steps += 1
                elif empty[0] < g_pos[0]:
                    grid[empty[1]][empty[0]], grid[empty[1]][empty[0] + 1] = grid[empty[1]][empty[0] + 1], grid[empty[1]][empty[0]]
                    steps += 1
            else:
                if empty[0] == g_pos[0] - 1:
                    grid[empty[1]][empty[0]], grid[g_pos[1]][g_pos[0]] = grid[g_pos[1]][g_pos[0]], grid[empty[1]][empty[0]]
                    steps += 1
                elif empty[0] == g_pos[0] + 1:
                    grid[empty[1]][empty[0]], grid[g_pos[1]][g_pos[0] - 1] = grid[g_pos[1]][g_pos[0] - 1], grid[empty[1]][empty[0]]
                    steps += 4

            empty = [(i, j) for i in range(w + 1) for j in range(h + 1) if grid[j][i] == " _ "][0]
            g_pos = [(i, j) for i in range(w + 1) for j in range(h + 1) if grid[j][i] == " G "][0]

            # print(steps)
            # print(g_pos)
            # print(empty)
            # print()
            # time.sleep(0.03)
