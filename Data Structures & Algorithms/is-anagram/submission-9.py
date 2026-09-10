class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count_s = defaultdict(int)
        count_t = defaultdict(int)
        for letter in s:
            count_s[letter] += 1
        for letter in t:
            count_t[letter] += 1
        return count_s == count_t
            