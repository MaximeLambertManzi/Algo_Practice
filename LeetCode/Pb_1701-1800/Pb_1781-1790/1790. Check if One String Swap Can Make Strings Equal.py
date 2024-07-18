class Solution:
    def areAlmostEqual(
        self,
        s1: str,
        s2: str,
    ) -> bool:

        diff_count = 0
        len_x = len(s1)
        indices = []

        if s1 == s2:
            return True

        for i in range(len_x):
            if s1[i] != s2[i]:
                diff_count += 1
                indices.append(i)

        if diff_count != 2:
            return False
        else:
            if s1[indices[0]] == s2[indices[1]] and s1[indices[1]] == s2[indices[0]]:
                return True
            else:
                return False
