class Solution:
    def plusOne(self, digits):

        str_digits = [str(i) for i in digits]
        temp_res = int("".join(str_digits))
        temp_res += 1

        res = [int(i) for i in str(temp_res)]
        return res
