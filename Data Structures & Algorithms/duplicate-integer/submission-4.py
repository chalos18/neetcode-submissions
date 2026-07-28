class Solution:
    def hasDuplicate(self, nums: list[int]) -> bool:
        seen = set() # hash set
        for n in nums:
            if n in seen:
                return True
            seen.add(n)
        return False