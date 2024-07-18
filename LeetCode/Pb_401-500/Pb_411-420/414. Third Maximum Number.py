class Solution:
    def thirdMax(self, nums) -> int:
        nums_sorted = sorted(nums, reverse=True)
        size = len(nums)

        maxi_third = nums_sorted[0]
        counter = 1

        print(nums_sorted)

        for i in range(size - 1):
            if nums_sorted[i + 1] < nums_sorted[i]:
                maxi_third = nums_sorted[i + 1]
                counter += 1
            if counter == 3:
                return maxi_third

        return nums_sorted[0]
