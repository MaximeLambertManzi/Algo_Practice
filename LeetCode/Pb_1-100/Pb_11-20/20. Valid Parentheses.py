class Solution:
    def isValid(self, s: str) -> bool:
        list_s = list()
        dict = {"(": ")", "[": "]", "{": "}"}
        len_s = len(s)

        if len_s == 1:
            print("len = 1")
            return False

        for chr in s:
            if chr in dict:
                list_s.append(chr)
            else:
                if len(list_s) > 0 and chr == dict[list_s[-1]]:
                    list_s.pop(-1)
                else:
                    return False

        if list_s == []:
            return True
        else:
            return False
