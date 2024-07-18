class Solution:
    def hammingWeight(self, n: int) -> int:
        total = 0

        while n:
            total += n % 2
            n >>= 1

        return total


"""
res = 0
while n:
    n &= (n-1)
    res += 1
    
return res
"""
