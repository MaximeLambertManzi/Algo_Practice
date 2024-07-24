""" Given a string s, reverse the order of characters in each word
within a sentence while still preserving whitespace and initial word order.

Example 1:

Input: s = "Let's take LeetCode contest"
Output: "s'teL ekat edoCteeL tsetnoc"

Example 2:

Input: s = "Mr Ding"
Output: "rM gniD"

Constraints:

1 <= s.length <= 5 * 104
s contains printable ASCII characters.
s does not contain any leading or trailing spaces.
There is at least one word in s.
All the words in s are separated by a single space. """


class Solution:
    def reverseWords(self, s: str) -> str:

        list_words = s.split()

        for i in range(len(list_words)):
            list_words[i] = list(list_words[i])

        for s_list in list_words:
            i = 0
            j = len(s_list) - 1

            while i < j:

                s_list[i], s_list[j] = s_list[j], s_list[i]
                i += 1
                j -= 1

        for i in range(len(list_words)):
            list_words[i] = "".join(list_words[i])

        return " ".join(list_words)
