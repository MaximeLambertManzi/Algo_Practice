class Solution:
    def replaceElements(self, arr):
        size = len(arr)

        maxi = 0
        indice_max = 0

        for i in range(size):
            if i == size - 1:
                arr[i] = -1
            else:
                if i < indice_max:
                    arr[i] = maxi
                else:
                    maxi = 0
                    indice_max = 0
                    for j in range(i + 1, size):
                        if arr[j] > maxi:
                            maxi = arr[j]
                            indice_max = j

                    arr[i] = maxi

        return arr
