class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMap = {}

        for i, num in enumerate(nums):
            diff = target - num
            if diff in prevMap:
                j = prevMap[diff]
                return [min(i, j), max(i, j)]
            prevMap[num] = i
        
        return []
            
