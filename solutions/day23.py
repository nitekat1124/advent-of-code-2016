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
        register = {"a": 7, "b": 0, "c": 0, "d": 0}
        return self.exec(register, data)["a"]

    def part2(self, data):
        register = {"a": 12, "b": 0, "c": 0, "d": 0}
        return self.exec(register, data)["a"]

    def exec(self, register, instructions):
        i = 0
        while i in range(len(instructions)):
            inst = instructions[i].split()
            if inst[0] == "cpy":
                if inst[2] in register:
                    if inst[1] in register:
                        register[inst[2]] = register[inst[1]]
                    else:
                        register[inst[2]] = int(inst[1])
                i += 1
            elif inst[0] == "inc":
                if inst[1] in register:
                    # optimization:
                    if instructions[i - 1].startswith("cpy ") and instructions[i + 1].startswith("dec ") and instructions[i + 2].startswith("jnz ") and instructions[i + 3].startswith("dec ") and instructions[i + 4].startswith("jnz "):
                        inc_op = inst[1]
                        cpy_src, cpy_dest = instructions[i - 1].split()[1:]
                        dec1_op = instructions[i + 1].split()[1]
                        jnz1_cond, jnz1_off = instructions[i + 2].split()[1:]
                        dec2_op = instructions[i + 3].split()[1]
                        jnz2_cond, jnz2_off = instructions[i + 4].split()[1:]

                        if cpy_dest == dec1_op and dec1_op == jnz1_cond and dec2_op == jnz2_cond and jnz1_off == "-2" and jnz2_off == "-5":
                            register[inc_op] += (register[cpy_src] if cpy_src.isalpha() else int(cpy_src)) * (register[dec2_op] if dec2_op.isalpha() else int(dec2_op))
                            register[dec1_op] = 0
                            register[dec2_op] = 0
                            i += 5
                            continue

                    register[inst[1]] += 1
                i += 1
            elif inst[0] == "dec":
                if inst[1] in register:
                    register[inst[1]] -= 1
                i += 1
            elif inst[0] == "jnz":
                if inst[1] in register:
                    if register[inst[1]] != 0:
                        if inst[2].isalpha():
                            i += register[inst[2]]
                        else:
                            i += int(inst[2])
                    else:
                        i += 1
                else:
                    if int(inst[1]) != 0:
                        if inst[2].isalpha():
                            i += register[inst[2]]
                        else:
                            i += int(inst[2])
                    else:
                        i += 1
            elif inst[0] == "tgl":
                target = i + register[inst[1]]
                if target in range(len(instructions)):
                    target_inst = instructions[target].split()
                    if len(target_inst) == 2:
                        if target_inst[0] == "inc":
                            instructions[target] = "dec " + target_inst[1]
                        else:
                            instructions[target] = "inc " + target_inst[1]
                    elif len(target_inst) == 3:
                        if target_inst[0] == "jnz":
                            instructions[target] = "cpy " + target_inst[1] + " " + target_inst[2]
                        else:
                            instructions[target] = "jnz " + target_inst[1] + " " + target_inst[2]
                i += 1
        return register
