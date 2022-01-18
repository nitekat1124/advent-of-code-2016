from collections import defaultdict
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
        compare = (2, 5) if len(data) == 6 else (17, 61)

        init = [i for i in data if i[:5] == "value"]
        insts = [i for i in data if i[:3] == "bot"]

        bots = defaultdict(list)
        outputs = defaultdict(list)

        for i in init:
            parts = i.split()
            bots[parts[5]] += [int(parts[1])]

        while max(len(i) for i in bots.values()) == 2:
            b = [i for i in bots if len(bots[i]) == 2][0]
            if min(bots[b]) == compare[0] and max(bots[b]) == compare[1]:
                return b
            inst = [i for i in insts if i.split()[1] == b][0]
            parts = inst.split()
            if parts[5] == "output":
                outputs[parts[6]] += [min(bots[b])]
            else:
                bots[parts[6]] += [min(bots[b])]
            bots[b].remove(min(bots[b]))

            if parts[10] == "output":
                outputs[parts[11]] += [max(bots[b])]
            else:
                bots[parts[11]] += [max(bots[b])]
            bots[b].remove(max(bots[b]))

    def part2(self, data):
        init = [i for i in data if i[:5] == "value"]
        insts = [i for i in data if i[:3] == "bot"]

        bots = defaultdict(list)
        outputs = defaultdict(list)

        for i in init:
            parts = i.split()
            bots[parts[5]] += [int(parts[1])]

        while max(len(i) for i in bots.values()) == 2:
            b = [i for i in bots if len(bots[i]) == 2][0]

            inst = [i for i in insts if i.split()[1] == b][0]
            parts = inst.split()
            if parts[5] == "output":
                outputs[parts[6]] += [min(bots[b])]
            else:
                bots[parts[6]] += [min(bots[b])]
            bots[b].remove(min(bots[b]))

            if parts[10] == "output":
                outputs[parts[11]] += [max(bots[b])]
            else:
                bots[parts[11]] += [max(bots[b])]
            bots[b].remove(max(bots[b]))

        return outputs["0"][0] * outputs["1"][0] * outputs["2"][0]
