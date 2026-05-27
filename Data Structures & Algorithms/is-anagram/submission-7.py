class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        count = [0] * 26

        for c in s:
            index = ord(c) - ord("a")
            count[index] += 1

        for c in t:
            index = ord(c) - ord("a")
            count[index] -= 1

        if all(value == 0 for value in count):
            return True
        else:
            return False