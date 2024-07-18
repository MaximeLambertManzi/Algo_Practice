class Solution:
    def twoSum(self, nums, target: int):
        set_val = set()
        for i in range(len(nums)):
            set_val.add(nums[i])
        for j in range(len(nums)):
            y = target - nums[j]
            if y in set_val:
                if nums.index(y) != j:
                    return [j, nums.index(y)]
