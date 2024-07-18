class Solution:
    def dominantIndex(self, nums) -> int:

        maxi = nums[0]
        max_index = 0

        for i in range(1, len(nums)):
            if nums[i] > maxi:
                maxi = nums[i]
                max_index = i

        for i in range(len(nums)):
            if maxi < nums[i] * 2 and i != max_index:
                return -1

        return max_index
