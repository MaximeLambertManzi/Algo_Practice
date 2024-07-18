class Solution:
    def rotate(self, nums, k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        len_num = len(nums)
        k = k % len_num

        result = [] * len_num

        result[0:] = nums[(len_num - k) :]
        result[k:] = nums[: (len_num - k)]

        for i in range(len_num):
            nums[i] = result[i]
