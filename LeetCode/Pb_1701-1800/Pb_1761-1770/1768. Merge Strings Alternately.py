class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:

        size1 = len(word1)
        size2 = len(word2)
        res = []

        if size1 > size2:
            for i in range(size2):
                res.append(word1[i])
                res.append(word2[i])

            for i in range(size2, size1):
                res.append(word1[i])

        elif size1 < size2:
            for i in range(size1):
                res.append(word1[i])
                res.append(word2[i])

            for i in range(size1, size2):
                res.append(word2[i])

        else:
            for i in range(size1):
                res.append(word1[i])
                res.append(word2[i])

        return "".join(res)
