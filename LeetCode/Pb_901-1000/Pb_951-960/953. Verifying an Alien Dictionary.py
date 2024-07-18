class Solution:
    def isAlienSorted(self, words, order: str) -> bool:

        alien_dict = dict()

        for i, chr in enumerate(order):
            alien_dict[chr] = i

        for i in range(len(words) - 1):
            equal = True
            word1 = words[i]
            word2 = words[i + 1]

            for chr1, chr2 in zip(word1, word2):
                if alien_dict[chr1] < alien_dict[chr2]:
                    equal = False
                    break
                elif alien_dict[chr1] > alien_dict[chr2]:
                    return False

            if len(word1) > len(word2) and equal == True:
                return False
        else:
            return True
