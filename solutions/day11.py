from copy import deepcopy
from itertools import combinations
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
                if str(func(i)) == r[0]:
                    print(f"test {test_counter} passed")
                else:
                    print(func(i))
                    print(r[0])
                    print(f"test {test_counter} NOT passed")
            test_counter += 1
        print()

    def part1(self, data):
        floors = self.parse_states(data)
        return self.run_steps(floors)

    def part2(self, data):
        floors = self.parse_states(data)
        floors[0] = floors[0].union({("ele", "g"), ("ele", "m"), ("dil", "g"), ("dil", "m")})
        return self.run_steps(floors)

    def parse_states(self, data):
        floors = []
        for line in data:
            floor = set()
            parts = line.split(" a ")
            for x in parts[1:]:
                n, t = x.split()[:2]
                floor.add((n[:3], t[0]))
            floors += [floor]
        return floors

    def run_steps(self, floors):
        conds = set()

        # count, elevator position, floors
        steps = deque([(0, 0, floors)])

        while steps:
            step = steps.popleft()

            if self.is_done(step[2]):
                return step[0]

            for next_step in self.get_possible_steps(step):
                status = self.get_floors_status(next_step)

                if status not in conds:
                    conds |= {status}
                    steps += [next_step]

    def get_possible_steps(self, state):
        count, elevator_pos, floors = state

        possible_moves = list(combinations(floors[elevator_pos], 2)) + list(combinations(floors[elevator_pos], 1))

        steps = []
        for move in possible_moves:
            for direction in [-1, 1]:
                next_elevator_pos = elevator_pos + direction
                if next_elevator_pos not in range(4):
                    continue

                next_floors = deepcopy(floors)
                next_floors[elevator_pos] = next_floors[elevator_pos].difference(move)
                next_floors[next_elevator_pos] = next_floors[next_elevator_pos].union(move)

                if self.is_floor_safe(next_floors[elevator_pos]) and self.is_floor_safe(next_floors[next_elevator_pos]):
                    steps += [(count + 1, next_elevator_pos, next_floors)]
        return steps

    def is_done(self, floors):
        return sum(len(f) for f in floors[:3]) == 0

    def is_floor_safe(self, floor):
        all_m = [i[0] for i in floor if i[1] == "m"]
        all_g = [i[0] for i in floor if i[1] == "g"]
        return len(all_g) == 0 or len([m for m in all_m if m not in all_g]) == 0

    def get_floors_status(self, step):
        _, elevator, floors = step
        key = "|".join([str(sum(1 for i in floor if i[1] == "g")) + "g" + str(sum(1 for i in floor if i[1] == "m")) + "m" for floor in floors])
        return elevator, key
