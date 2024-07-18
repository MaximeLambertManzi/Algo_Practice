class Solution:
    def pivotIndex(self, nums) -> int:

        left_sum = 0
        right_sum = 0
        len_nums = len(nums)

        for i in range(1, len_nums):
            right_sum += nums[i]

        if left_sum == right_sum:
            return 0

        for i in range(1, len_nums):
            left_sum += nums[i - 1]
            right_sum -= nums[i]
            if left_sum == right_sum:
                return i

        return -1
