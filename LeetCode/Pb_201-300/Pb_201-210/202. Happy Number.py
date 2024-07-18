class Solution:
    def isHappy(self, n: int) -> bool:

        new_value = n
        set_value = set()

        while 1:
            decoupe = list(map(int, str(new_value)))
            new_value = 0

            for x in decoupe:
                decoupe = list(map(int, str(n)))
                new_value += x**2

            if new_value == 1:
                return True

            elif new_value in set_value:
                return False

            set_value.add(new_value)
