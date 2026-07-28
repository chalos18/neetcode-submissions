class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        

        ans= {i:0 for i in nums}

        for i in nums:
            if ans[i] == 1:
                return True
            ans[i] = 1
        return False