class Solution:
    def countOdds(self, low: int, high: int) -> int:

        count = 0
        delta = high - low

        if (delta + 1) % 2 == 0:
            count = (delta + 1) // 2
        else:
            if high % 2 == 0:
                count = delta // 2
            else:
                count = (delta // 2) + 1

        return count
