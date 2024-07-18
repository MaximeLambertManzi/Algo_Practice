class Solution:
    def largestPerimeter(self, nums) -> int:

        nums.sort(reverse=True)

        for a, b, c in zip(nums, nums[1:], nums[2:]):

            if b + c > a:
                return a + b + c

        return 0
