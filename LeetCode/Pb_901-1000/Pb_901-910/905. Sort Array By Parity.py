class Solution:
    def sortArrayByParity(self, nums):
        size = len(nums)
        i = 0
        k = 0

        while i != size:

            if nums[k] % 2 == 1:
                nums.append(nums[k])
                nums.pop(k)
            else:
                k += 1

            i += 1

        return nums
