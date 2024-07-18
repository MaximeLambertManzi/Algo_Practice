class Solution:
    def removeElement(self, nums, val: int) -> int:
        size = len(nums)
        k = size
        i = 0

        while i < size:
            if nums[i] == val:
                nums.remove(val)
                nums.append("_")
                k -= 1
                i -= 1
            else:
                i += 1
        return k
