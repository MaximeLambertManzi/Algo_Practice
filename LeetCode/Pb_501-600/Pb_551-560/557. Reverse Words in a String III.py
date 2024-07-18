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
