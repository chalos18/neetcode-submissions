class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sublists = {}

        for i in range(len(strs)):
            word = "".join(sorted(strs[i]))
            if word in sublists:
                sublists[word].append(strs[i])
            else:
                sublists[word] = [strs[i]]

        return list(sublists.values())