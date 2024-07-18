class Solution:
    def checkIfExist(self, arr) -> bool:
        size = len(arr)

        set_arr = set()
        for i in range(size):
            if (arr[i] * 2) in set_arr or (arr[i] % 2 == 0 and arr[i] // 2 in set_arr):
                return True
            else:
                set_arr.add(arr[i])

        return False
