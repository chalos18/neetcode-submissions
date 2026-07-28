class Solution:
    def findMin(self, nums: List[int]) -> int:
        min_n = math.inf
        for i in range(len(nums)):
            if nums[i] < min_n:
                min_n = nums[i]
        return min_n