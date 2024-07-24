""" Given a string s, you can transform every letter individually
to be lowercase or uppercase to create another string.

Return a list of all possible strings we could create.
Return the output in any order.

Example 1:

Input: s = "a1b2"
Output: ["a1b2","a1B2","A1b2","A1B2"]

Example 2:

Input: s = "3z4"
Output: ["3z4","3Z4"]

Constraints:

1 <= s.length <= 12
s consists of lowercase English letters, uppercase English letters, and digits. """


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
