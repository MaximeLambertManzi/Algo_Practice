class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        str_n = str(n)

        product_n = 1
        sum_n = 0

        for i in range(len(str_n)):
            sum_n += int(str_n[i])

        for i in range(len(str_n)):
            product_n *= int(str_n[i])

        return product_n - sum_n
