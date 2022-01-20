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
        elves = [*range(1, int(data[0]) + 1)]
        while len(elves) > 1:
            ll = len(elves) % 2
            elves = [v for i, v in enumerate(elves) if i % 2 == 0]
            if ll:
                elves = elves[-1:] + elves[:-1]
        return elves[0]

    def part2(self, data):
        # return self.part2_attempt_1(data)
        # return self.part2_attempt_2(data)
        return self.part2_attempt_3(data)

    """
    # very straight forward, and very slow
    # but we can use it to observe the pattern of the elves skipping
    """

    def part2_attempt_1(self, data):
        elves = deque([*range(1, int(data[0]) + 1)])

        cur = 1
        while len(elves) > 1:
            idx = elves.index(cur)
            skipped_idx = ((len(elves) - 2) // 2 + idx + 1) % len(elves)
            print(elves)
            print(f"current: {cur}")
            print(f"skipped: {elves[skipped_idx]}")
            elves.remove(elves[skipped_idx])
            cur = elves[(elves.index(cur) + 1) % len(elves)]
        exit()
        return elves[0]

    """
    # the whole concept is in the notes at the very end, based on what we observed via part2_attempt_1
    # there's a pattern: showing what elves will be skipped, we can list them quickly without actually calculating them
    # but removing them is slow, finished in about 30 minutes
    """

    def part2_attempt_2(self, data):
        elves = deque([*range(1, int(data[0]) + 1)])

        while len(elves) > 2:
            skip_idx = deque([])

            skip_count = ((len(elves) - 2) // 3 + 1) * 2
            if len(elves) % 3 == 2:
                skip_count -= 1

            start = elves[(len(elves) - 1) // 2] if len(elves) % 2 else elves[(len(elves) - 1) // 2 + 1]
            start_idx = elves.index(start)

            while len(skip_idx) < skip_count:
                if (skip_count - len(skip_idx) == 1) or (len(skip_idx) == 0 and len(elves) % 2):
                    skip_idx += [start_idx]
                    start_idx = (start_idx + 2) % len(elves)
                else:
                    skip_idx += [start_idx]
                    skip_idx += [(start_idx + 1) % len(elves)]
                    start_idx = (start_idx + 3) % len(elves)

            skip_idx = sorted(skip_idx)
            while skip_idx:
                idx = skip_idx.pop()
                del elves[idx]

        return elves[0]

    """
    # the concept is totally the same with part2_attempt_2, but removing the elves in a more efficient way
    # instead of keeping the elves index and removing them one by one later
    # using deque.rotate() and deque.popleft() is much faster, finished in about 2 seconds, wow
    """

    def part2_attempt_3(self, data):
        elves = deque([*range(1, int(data[0]) + 1)])

        while len(elves) > 2:
            skip_count = ((len(elves) - 2) // 3 + 1) * 2 - [0, 1][len(elves) % 3 == 2]
            skipped_count = 0

            start_idx = (len(elves) - 1) // 2 + 1 - len(elves) % 2
            elves.rotate(-start_idx)

            while skipped_count < skip_count:
                if (skip_count - skipped_count == 1) or (skipped_count == 0 and len(elves) % 2):
                    elves.popleft()
                    skipped_count += 1
                else:
                    elves.popleft()
                    elves.popleft()
                    skipped_count += 2
                elves.rotate(-1)

            elves = deque(sorted(elves))
        return elves[0]


"""
notes:

how many elves should skip out per round(from #1 to last)?

total - skip:

 2 - 1
 3 - 2
 4 - 2

 5 - 3
 6 - 4
 7 - 4

 8 - 5
 9 - 6
10 - 6

11 - 7
12 - 8
13 - 8

14 - 9
15 - 10
16 - 10

17 - 11
18 - 12
19 - 12

20 - 13
21 - 14
22 - 14

let's say x is the length of the elves

the count of skipped elves per round is:
max = ((x-2)//3 + 1) * 2
min = max - 1

if x % 3 == 2:
    skip min elves
else:
    skip max elves

if x is even, find middle of the rest,
skip 2 => jump over 1 => skip 2 => jump over 1 => skip 2 => jump over 1...
until reached the skipped elves count, and start all over again

if x is odd, find middle-left of the rest,
skip 1 => jump over 1 => skip 2 => jump over 1 => skip 2 => jump over 1...
until reached the skipped elves count, and start all over again
"""
