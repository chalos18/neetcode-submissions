class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        return res

    def decode(self, s: str) -> List[str]:
        res, i = [], 0
    
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            s_length = int(s[i:j])
            word = s[j + 1: s_length + j + 1]
            i = j + s_length + 1
            
            res.append(word)
            
        return res
        