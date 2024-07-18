class Solution:
    def findTheDifference(self, s: str, t: str) -> str:

        list_s = list(s)
        list_s.sort()
        list_t = list(t)
        list_t.sort()

        if s == "":
            return t
        else:
            for chr1, chr2 in zip(list_s, list_t):
                if chr1 != chr2:
                    return chr2

            return list_t[-1]
