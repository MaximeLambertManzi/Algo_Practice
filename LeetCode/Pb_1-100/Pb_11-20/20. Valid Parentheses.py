""" Given a string s containing just the characters
'(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

1. Open brackets must be closed by the same type of brackets.
2. Open brackets must be closed in the correct order.
3. Every close bracket has a corresponding open bracket of the same type.

Example 1:

Input: s = "()"
Output: true

Example 2:

Input: s = "()[]{}"
Output: true

Example 3:

Input: s = "(]"
Output: false

Constraints:

1 <= s.length <= 104
s consists of parentheses only '()[]{}'. """


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
