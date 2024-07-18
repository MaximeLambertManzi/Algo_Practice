class Solution:
    def sortByBits(self, arr):
        res = sorted(arr, key=lambda x: (self.hammingWeight(x), x))
        return res

    def hammingWeight(self, nb):
        weight = 0

        while nb:
            nb &= nb - 1
            weight += 1

        return weight
