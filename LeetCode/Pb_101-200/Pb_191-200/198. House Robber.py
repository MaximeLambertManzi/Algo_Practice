class Solution:
    def rob(self, nums) -> int:
        size = len(nums)

        if size == 1:
            return nums[0]
        elif size == 2:
            return max(nums[0], nums[1])
        else:
            rob_val = [nums[0], max(nums[0], nums[1])]

            for i in range(2, size):
                rob_val.append(max(rob_val[i - 1], rob_val[i - 2] + nums[i]))

        return rob_val[-1]
