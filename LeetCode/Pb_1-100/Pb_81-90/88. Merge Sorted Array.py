class Solution:
    def merge(self, nums1, m: int, nums2, n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        for i in range(n):
            nums1.pop(-1)

        for i in range(n):
            nums1.append(nums2[i])

        nums1.sort()
