class Solution:
    def permute(self, nums):
        comb_list = []
        comb = []

        def backtrack(nums, comb):
            if not nums:
                comb_list.append(comb)
            for i in range(len(nums)):
                backtrack(nums[:i] + nums[i + 1 :], comb + [nums[i]])

        backtrack(nums, comb)

        return comb_list
