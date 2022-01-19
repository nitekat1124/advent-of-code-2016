import hashlib
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
        salt = data[0]
        n = 0
        self.possible_keys = []
        self.valid_keys = []

        while len(self.valid_keys) < 64:
            key = hashlib.md5((salt + str(n)).encode()).hexdigest()
            is_key, c = self.is_key(key)
            if is_key:
                self.possible_keys += [(key, n, c)]
                self.validation(n)
            n += 1

        max_n = max([k[1] for k in self.possible_keys])
        re_check_length = sum([1 for i in self.possible_keys if i[1] < max_n])

        while re_check_length > 0:
            key = hashlib.md5((salt + str(n)).encode()).hexdigest()
            is_key, c = self.is_key(key)
            if is_key:
                self.possible_keys += [(key, n, c)]
                self.validation(n)
            n += 1
            re_check_length = sum([1 for i in self.possible_keys if i[1] < max_n])

        r = sorted(self.valid_keys, key=lambda x: x[1])[63][1]
        return r

    def part2(self, data):
        salt = data[0]
        n = 0
        self.possible_keys = []
        self.valid_keys = []

        while len(self.valid_keys) < 64:
            key = hashlib.md5((salt + str(n)).encode()).hexdigest()
            for _ in range(2016):
                key = hashlib.md5(key.encode()).hexdigest()
            is_key, c = self.is_key(key)
            if is_key:
                self.possible_keys += [(key, n, c)]
                self.validation(n)
            n += 1

        max_n = max([k[1] for k in self.possible_keys])
        re_check_length = sum([1 for i in self.possible_keys if i[1] < max_n])

        while re_check_length > 0:
            key = hashlib.md5((salt + str(n)).encode()).hexdigest()
            for _ in range(2016):
                key = hashlib.md5(key.encode()).hexdigest()
            is_key, c = self.is_key(key)
            if is_key:
                self.possible_keys += [(key, n, c)]
                self.validation(n)
            n += 1
            re_check_length = sum([1 for i in self.possible_keys if i[1] < max_n])

        r = sorted(self.valid_keys, key=lambda x: x[1])[63][1]
        return r

    def is_key(self, key):
        c = None
        for i in range(len(key) - 2):
            if key[i] * 3 == key[i : i + 3]:
                c = key[i] * 5
                break
        if c is None:
            return False, None
        else:
            return True, c

    def validation(self, n):
        for key, n, c in self.possible_keys:
            next_keys = [k for k, m, h in self.possible_keys if n + 1000 >= m > n]
            for i in next_keys:
                if c in i:
                    self.valid_keys += [(key, n, c)]
                    break
        for i in self.valid_keys:
            if i in self.possible_keys:
                self.possible_keys.remove(i)

        self.cleanup_possible_keys()

    def cleanup_possible_keys(self):
        max_n = max([k[1] for k in self.possible_keys])
        need_delete = []
        for i in self.possible_keys:
            if i[1] < max_n - 1000:
                need_delete += [i]
        for i in need_delete:
            self.possible_keys.remove(i)
