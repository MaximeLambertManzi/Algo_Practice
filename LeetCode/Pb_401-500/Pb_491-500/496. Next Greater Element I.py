class Solution:
    def nextGreaterElement(self, nums1, nums2):

        res = []
        len1 = len(nums1)
        len2 = len(nums2)

        for i in range(len1):

            val = nums1[i]
            index = nums2.index(nums1[i])

            for j in range(index, len2):
                if nums2[j] > val:
                    res.append(nums2[j])
                    break
                elif j == len2 - 1:
                    res.append(-1)

        return res
