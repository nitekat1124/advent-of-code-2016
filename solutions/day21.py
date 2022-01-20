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
        password = "abcde" if len(data) == 8 else "abcdefgh"
        password = deque(password)

        for ope in data:
            ope = ope.split()
            if ope[0] == "swap":
                if ope[1] == "position":
                    password[int(ope[2])], password[int(ope[5])] = password[int(ope[5])], password[int(ope[2])]
                elif ope[1] == "letter":
                    pos1 = password.index(ope[2])
                    pos2 = password.index(ope[5])
                    password[pos1], password[pos2] = password[pos2], password[pos1]
            elif ope[0] == "reverse":
                password = list(password)
                password[int(ope[2]) : int(ope[4]) + 1] = password[int(ope[2]) : int(ope[4]) + 1][::-1]
                password = deque(password)
            elif ope[0] == "rotate":
                if ope[1] == "left":
                    password.rotate(-int(ope[2]))
                elif ope[1] == "right":
                    password.rotate(int(ope[2]))
                elif ope[1] == "based":
                    pos = password.index(ope[6])
                    if pos >= 4:
                        pos += 1
                    password.rotate(pos + 1)
            elif ope[0] == "move":
                pos1 = int(ope[2])
                pos2 = int(ope[5])
                v = password[pos1]
                del password[pos1]
                password.insert(pos2, v)
        return "".join(password)

    def part2(self, data):
        password = "decab" if len(data) == 8 else "fbgdceah"
        password = deque(password)

        rotate_reverse = [4, -1, 1, -2, 0] if len(data) == 8 else [7, -1, 2, -2, 1, -3, 0, -4]

        for ope in data[::-1]:
            ope = ope.split()
            if ope[0] == "swap":
                if ope[1] == "position":
                    password[int(ope[2])], password[int(ope[5])] = password[int(ope[5])], password[int(ope[2])]
                elif ope[1] == "letter":
                    pos1 = password.index(ope[2])
                    pos2 = password.index(ope[5])
                    password[pos1], password[pos2] = password[pos2], password[pos1]
            elif ope[0] == "reverse":
                password = list(password)
                password[int(ope[2]) : int(ope[4]) + 1] = password[int(ope[2]) : int(ope[4]) + 1][::-1]
                password = deque(password)
            elif ope[0] == "rotate":
                if ope[1] == "left":
                    password.rotate(int(ope[2]))
                elif ope[1] == "right":
                    password.rotate(-int(ope[2]))
                elif ope[1] == "based":
                    pos = password.index(ope[6])
                    password.rotate(rotate_reverse[pos])
            elif ope[0] == "move":
                pos1 = int(ope[5])
                pos2 = int(ope[2])
                v = password[pos1]
                del password[pos1]
                password.insert(pos2, v)
        return "".join(password)


"""
rotate_based in reverse:

origin 0 1 2 3  4
move   1 2 3 4  6
add up 1 3 5 7 10
final  1 3 0 2  0

origin 0 1 2 3  4  5  6  7
move   1 2 3 4  6  7  8  9
add up 1 3 5 7 10 12 14 16
final  1 3 5 7  2  4  6  0
"""
