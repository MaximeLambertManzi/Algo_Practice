class Solution:
    def twoSum(self, numbers, target: int):

        values = set()
        index1 = 0
        index2 = 0

        for i in range(len(numbers)):
            target2 = target - numbers[i]

            if target2 in values:
                index2 = i
                index1 = numbers.index(target2)
                break
            else:
                values.add(numbers[i])

        res = [index1 + 1, index2 + 1]
        return res
