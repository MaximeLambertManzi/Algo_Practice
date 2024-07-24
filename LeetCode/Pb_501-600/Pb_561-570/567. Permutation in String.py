""" Given two strings s1 and s2, return true
if s2 contains a permutation of s1, or false otherwise.

In other words, return true if one of s1's permutations is the substring of s2.

Example 1:

Input: s1 = "ab", s2 = "eidbaooo"
Output: true

Explanation: s2 contains one permutation of s1 ("ba").

Example 2:

Input: s1 = "ab", s2 = "eidboaoo"
Output: false

Constraints:

1 <= s1.length, s2.length <= 104
s1 and s2 consist of lowercase English letters. """


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
            temp = s2[i : i + len_1]  # noqa: E203
            for chr in temp:
                sub2[chr] = sub2.get(chr, 0) + 1

            if sub1 == sub2:
                return True

        return False
