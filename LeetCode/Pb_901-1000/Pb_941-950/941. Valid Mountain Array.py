class Solution:
    def validMountainArray(self, arr) -> bool:
        size = len(arr)

        switch = 0

        if size < 3:
            return False

        for i in range(size - 1):
            if arr[i + 1] > arr[i]:
                continue
            elif arr[i + 1] == arr[i]:
                return False
            elif arr[i + 1] < arr[i] and i == 0:
                return False
            else:
                switch = i
                break

        for i in range(switch, size - 1):
            if arr[i + 1] < arr[i]:
                continue
            elif arr[i + 1] < arr[i]:
                return False
            else:
                return False

        return True
