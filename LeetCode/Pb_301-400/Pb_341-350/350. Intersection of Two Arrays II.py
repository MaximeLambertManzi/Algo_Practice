class Solution:
    def intersect(self, nums1, nums2):

        nums_final = []

        len1 = len(nums1)
        len2 = len(nums2)

        nums1.sort()
        nums2.sort()

        i = 0
        j = 0

        while i < len1 and j < len2:
            if nums1[i] == nums2[j]:
                nums_final.append(nums1[i])
                i += 1
                j += 1

            elif nums1[i] > nums2[j]:
                j += 1
            else:
                i += 1

        return nums_final
