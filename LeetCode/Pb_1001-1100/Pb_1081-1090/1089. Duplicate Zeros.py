class Solution:
    def duplicateZeros(self, arr) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """

        taille = len(arr)
        i = 0

        while i < taille:

            if arr[i] == 0:
                arr.insert(i, 0)
                arr.pop(-1)
                i += 2
            else:
                i += 1
