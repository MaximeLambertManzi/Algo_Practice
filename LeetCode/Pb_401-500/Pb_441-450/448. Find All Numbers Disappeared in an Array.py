class Solution:
    def findDisappearedNumbers(self, nums):
        size = len(nums)
        nums_all = range(1, size + 1)

        set_nums = set(nums)
        set_nums_all = set(nums_all)

        print(set_nums)
        print(set_nums_all)

        finish = set_nums_all.difference(set_nums)

        return list(finish)
