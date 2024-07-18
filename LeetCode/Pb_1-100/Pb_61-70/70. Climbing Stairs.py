class Solution:
    def climbStairs(self, n: int) -> int:
        dict = {1: 1, 2: 2}

        def fib(n):
            if n in dict:
                return dict[n]
            else:
                dict[n] = fib(n - 1) + fib(n - 2)
                return dict[n]

        return fib(n)
