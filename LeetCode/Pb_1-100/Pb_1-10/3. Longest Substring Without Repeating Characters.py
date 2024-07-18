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
