class Solution:
    def removeDuplicates(self, nums) -> int:
        size = len(nums)
        k = size
        i = 0

        while i < size - 1:
            if nums[i + 1] == nums[i] and nums[i + 1] != "_":
                nums.pop(i + 1)
                nums.append("_")
                k -= 1
                i -= 1
            else:
                i += 1
        return k
