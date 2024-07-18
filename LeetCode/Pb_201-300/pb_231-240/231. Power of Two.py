class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        res = n
        if n == 0:
            return False
        else:
            while res % 2 == 0:
                res /= 2

            if res == 1:
                return True
            else:
                return False
