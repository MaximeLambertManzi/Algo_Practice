class Solution:
    def findMaxConsecutiveOnes(self, nums) -> int:
        maxi = 0
        temp = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                temp += 1
            else:
                temp = 0

            if temp > maxi:
                maxi = temp

        return maxi
