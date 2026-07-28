class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        count = {}
        for i in nums:
            if count.get(i) == 1:
                return True
            count[i] = 1
        return False
        

        