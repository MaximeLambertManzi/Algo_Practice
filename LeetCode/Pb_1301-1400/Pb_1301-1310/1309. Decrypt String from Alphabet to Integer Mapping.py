class Solution:
    def freqAlphabets(self, s: str) -> str:

        res = []
        len_s = len(s)
        i = 0

        while i < len_s:

            if i < len_s - 2 and s[i + 2] == "#":
                res.append(int("".join([s[i], s[i + 1]])))
                i += 3
            else:
                res.append(int(s[i]))
                i += 1

        for i in range(len(res)):
            res[i] = chr(res[i] + (ord("a") - 1))

        return "".join(res)
