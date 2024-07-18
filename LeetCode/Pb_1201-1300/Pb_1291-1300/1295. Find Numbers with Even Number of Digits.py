class Solution:
    def findNumbers(self, nums) -> int:
        total = 0
        taille = len(nums)
        for i in range(taille):
            if len(str(nums[i])) % 2 == 0:
                total += 1
        return total
