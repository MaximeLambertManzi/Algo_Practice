class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        else:
            chiffre = str(x)
            chiffre_reverse = chiffre[::-1]

            if chiffre == chiffre_reverse:
                return True
            else:
                return False
