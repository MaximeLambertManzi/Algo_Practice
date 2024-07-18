class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        sub1 = dict()
        sub2 = dict()
        len_1 = len(s1)
        len_2 = len(s2)

        for chr in s1:
            sub1[chr] = sub1.get(chr, 0) + 1

        for i in range(len_2 - len_1 + 1):
            sub2 = dict()
            temp = s2[i : i + len_1]
            for chr in temp:
                sub2[chr] = sub2.get(chr, 0) + 1

            if sub1 == sub2:
                return True

        return False
