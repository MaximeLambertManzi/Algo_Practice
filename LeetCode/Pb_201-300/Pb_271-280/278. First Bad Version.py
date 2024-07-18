# The isBadVersion API is already defined for you.
# Here return true is added to delete warnings
def isBadVersion(version: int) -> bool:
    return True


class Solution:
    def firstBadVersion(self, n: int) -> int:

        low = 1
        high = n

        if isBadVersion(1):
            return 1
        else:
            while low < high:
                mid = (low + high) // 2

                if isBadVersion(mid):
                    high = mid
                else:
                    low = mid + 1

            return low
