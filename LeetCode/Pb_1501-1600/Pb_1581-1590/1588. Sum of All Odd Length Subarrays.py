class Solution:
    def sumOddLengthSubarrays(self, arr) -> int:

        len_arr = len(arr)
        sum_arr = sum(arr)

        for i in range(len_arr):
            for j in range(i + 1, len_arr + 1):
                if (j - i) % 2 == 1 and (j - i) != 1:
                    sum_arr += sum(arr[i:j])

        return sum_arr
