class Solution:
    def maxSubArray(self, nums) -> int:
        sum = 0
        max_sum = -10001

        for i in range(len(nums)):
            sum += nums[i]
            if sum > max_sum:
                max_sum = sum
            elif sum < 0:
                sum = 0
        return max_sum
