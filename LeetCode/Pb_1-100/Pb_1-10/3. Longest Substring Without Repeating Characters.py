""" Given a string s, find the length of the longest
substring without repeating characters.

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring,
"pwke" is a subsequence and not a substring.

Constraints:

0 <= s.length <= 5 * 104
s consists of English letters, digits, symbols and spaces. """


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        max_sub = 0
        counter = 0
        for i in range(len(s)):

            sub = set()

            for j in range(i, len(s)):
                if s[j] not in sub:
                    sub.add(s[j])
                    counter += 1
                else:
                    max_sub = max(max_sub, counter)
                    counter = 0
                    break

            max_sub = max(max_sub, counter)
            counter = 0

        return max_sub
