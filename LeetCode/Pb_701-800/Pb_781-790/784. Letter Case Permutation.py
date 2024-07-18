class Solution:
    def letterCasePermutation(self, s: str):
        res = []
        size = len(s)

        def backtrack(i, temp):
            if i == size:
                res.append(temp)
            else:
                if s[i].isalpha():
                    backtrack(i + 1, temp + s[i].lower())
                    backtrack(i + 1, temp + s[i].upper())
                else:
                    backtrack(i + 1, temp + s[i])

        backtrack(0, "")
        return res
