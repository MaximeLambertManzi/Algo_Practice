class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:

        dic_mag = dict()

        for chr in magazine:
            if chr not in dic_mag:
                dic_mag[chr] = 1
            else:
                dic_mag[chr] += 1

        for chr in ransomNote:
            if chr not in dic_mag:
                return False
            else:
                if dic_mag[chr] == 0:
                    return False
                else:
                    dic_mag[chr] -= 1

        return True
