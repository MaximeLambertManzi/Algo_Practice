class Solution:
    def containsDuplicate(self, nums) -> bool:
        if (len(nums) - len(set(nums))) == 0:
            return False
        else:
            return True
