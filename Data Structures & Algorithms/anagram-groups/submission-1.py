class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        A = defaultdict(list)

        for word in strs:
            sorted_word = "".join(sorted(word))
            A[sorted_word].append(word)

        return list(A.values())

        