class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        split_s = list(s)
        split_t = list(t)

        dic_s = {i:0 for i in split_s}
        dic_t = {i:0 for i in split_t}
        
        print(dic_s)
        for i in split_s:
            dic_s[i]  += 1

        for i in split_t:
            dic_t[i] += 1

        return dic_s == dic_t
