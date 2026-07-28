class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hash_count_s = {} 
        hash_count_t = {}

        for char in s:
            if char not in hash_count_s:
                hash_count_s[char] = 1
            else:
                hash_count_s[char] += 1

        for char in t:
            if char not in hash_count_t:
                hash_count_t[char] = 1
            else:
                hash_count_t[char] += 1

        return hash_count_s == hash_count_t
        