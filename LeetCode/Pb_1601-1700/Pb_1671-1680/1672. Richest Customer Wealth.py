class Solution:
    def maximumWealth(self, accounts) -> int:

        nb_customers = len(accounts)
        nb_banks = len(accounts[0])

        total_custo = 0
        max_total = 0

        for i in range(nb_customers):
            for j in range(nb_banks):
                total_custo += accounts[i][j]

            max_total = max(max_total, total_custo)
            total_custo = 0

        return max_total
