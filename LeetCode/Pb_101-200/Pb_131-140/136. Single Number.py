class Solution:
    def singleNumber(self, nums) -> int:
        res = 0

        for nb in nums:
            res ^= nb

        return res
