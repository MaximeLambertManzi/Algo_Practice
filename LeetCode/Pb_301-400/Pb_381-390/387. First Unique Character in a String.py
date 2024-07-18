class Solution:
    def firstUniqChar(self, s: str) -> int:

        dico = dict()

        for chr in s:
            if chr not in dico:
                dico[chr] = 1
            else:
                dico[chr] += 1

        for chr in s:
            if dico[chr] == 1:
                return s.index(chr)

        return -1
