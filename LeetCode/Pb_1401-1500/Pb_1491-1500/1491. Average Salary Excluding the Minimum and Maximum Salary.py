class Solution:
    def average(self, salary) -> float:
        nb_employees = len(salary)
        maxi = 1000
        mini = 1000000
        total = 0

        for i in range(nb_employees):
            if salary[i] >= maxi:
                maxi = salary[i]
            if salary[i] <= mini:
                mini = salary[i]

            total += salary[i]

        return (total - maxi - mini) / (nb_employees - 2)
