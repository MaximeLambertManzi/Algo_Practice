class Solution:
    def heightChecker(self, heights) -> int:
        heights_sorted = sorted(heights)
        size = len(heights)

        diff = 0

        for i in range(size):
            if heights[i] != heights_sorted[i]:
                diff += 1

        return diff
