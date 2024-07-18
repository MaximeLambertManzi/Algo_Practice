class Solution:
    def toLowerCase(self, s: str) -> str:

        list_s = list(s)

        for i in range(len(list_s)):

            if list_s[i] >= "A" and list_s[i] <= "Z":

                list_s[i] = chr(ord(list_s[i]) - (ord("A") - ord("a")))

        return "".join(list_s)
