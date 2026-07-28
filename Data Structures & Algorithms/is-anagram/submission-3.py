class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_split = list(s)
        s_split.sort()
        t_split = list(t)
        t_split.sort()

        return s_split == t_split
