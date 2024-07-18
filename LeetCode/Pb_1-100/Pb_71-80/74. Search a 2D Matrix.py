class Solution:
    def searchMatrix(self, matrix, target: int) -> bool:

        index = -1
        for i in range(len(matrix)):
            if target >= matrix[i][0] and target <= matrix[i][-1]:
                index = i

        if index == -1:
            return False
        else:
            low = 0
            high = len(matrix[index]) - 1

            while low <= high:
                mid = (high + low) // 2
                if target > matrix[index][mid]:
                    low = mid + 1
                elif target < matrix[index][mid]:
                    high = mid - 1
                else:
                    return True

            return False
