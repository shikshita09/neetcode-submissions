class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        counts = {}
        for char in s:
            counts[char] = counts.get(char, 0) + 1
        sorted_s = sorted(s)
        sorted_t = sorted(t)
        return sorted_s == sorted_t