class Solution:
    def moveZeroes(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        size = len(nums)
        i = 0
        k = 0

        while i != size:
            if nums[k] == 0:
                nums.pop(k)
                nums.append(0)
            else:
                k += 1
            i += 1

        return nums
