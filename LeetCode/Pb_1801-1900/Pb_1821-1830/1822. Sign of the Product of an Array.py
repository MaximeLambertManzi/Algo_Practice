class Solution:
    def arraySign(self, nums) -> int:

        product = 1

        for i in range(len(nums)):
            if nums[i] < 0:
                product *= -1
            elif nums[i] == 0:
                return 0

        return product
