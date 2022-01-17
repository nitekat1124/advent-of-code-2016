from typing import Counter
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
        real_id = []
        for line in data:
            p1, p2 = line.split("[")
            p1 = p1.split("-")
            name = "".join(p1[:-1])
            id = int(p1[-1])
            checksum = p2[:-1]
            if checksum == "".join(k for k, v in sorted(Counter(name).items(), key=lambda x: (-x[1], x[0])))[:5]:
                real_id += [id]
        return sum(real_id)

    def part2(self, data):
        real_rooms = []
        for line in data:
            p1, p2 = line.split("[")
            p1 = p1.split("-")
            name = "".join(p1[:-1])
            id = int(p1[-1])
            checksum = p2[:-1]
            if checksum == "".join(k for k, v in sorted(Counter(name).items(), key=lambda x: (-x[1], x[0])))[:5]:
                real_rooms += [(id, "".join([chr((ord(i) - 97 + id) % 26 + 97) if i.isalpha() else " " for i in "-".join(p1[:-1])]))]
        if len(data) == 1:
            return real_rooms[0][0]
        else:
            return [i[0] for i in real_rooms if i[1].find("northpole object storage") != -1][0]
