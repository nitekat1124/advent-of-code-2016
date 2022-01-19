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
        register = {"a": 0, "b": 0, "c": 0, "d": 0}
        return self.exec(register, data)["a"]

    def part2(self, data):
        register = {"a": 0, "b": 0, "c": 1, "d": 0}
        return self.exec(register, data)["a"]

    def exec(self, register, instructions):
        i = 0
        while i in range(len(instructions)):
            inst = instructions[i].split()
            if inst[0] == "cpy":
                if inst[1] in register:
                    register[inst[2]] = register[inst[1]]
                else:
                    register[inst[2]] = int(inst[1])
                i += 1
            elif inst[0] == "inc":
                register[inst[1]] += 1
                i += 1
            elif inst[0] == "dec":
                register[inst[1]] -= 1
                i += 1
            elif inst[0] == "jnz":
                if inst[1] in register:
                    if register[inst[1]] != 0:
                        i += int(inst[2])
                    else:
                        i += 1
                else:
                    if int(inst[1]) != 0:
                        i += int(inst[2])
                    else:
                        i += 1
        return register
