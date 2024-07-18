class Solution:
    def reverseBits(self, n: int) -> int:

        res = 0

        while n:
            res <<= 1
            res = res + (n & 1)
            n >>= 1

        return res
