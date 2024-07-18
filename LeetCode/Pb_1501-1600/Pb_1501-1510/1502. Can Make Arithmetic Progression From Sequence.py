class Solution:
    def canMakeArithmeticProgression(self, arr) -> bool:

        arr.sort()
        r = arr[1] - arr[0]

        for i in range(1, len(arr) - 1):
            if arr[i + 1] - arr[i] != r:
                return False

        return True
