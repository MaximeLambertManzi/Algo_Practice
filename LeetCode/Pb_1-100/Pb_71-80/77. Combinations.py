class Solution:
    def combine(self, n: int, k: int):
        comb_list = []
        comb = []

        def backtrack(k, comb, next_num):
            if k == 0:
                comb_list.append(comb.copy())
            else:
                for i in range(next_num, n + 1):
                    comb.append(i)
                    backtrack(k - 1, comb, i + 1)
                    comb.pop()

        backtrack(k, comb, 1)
        print(comb_list)
