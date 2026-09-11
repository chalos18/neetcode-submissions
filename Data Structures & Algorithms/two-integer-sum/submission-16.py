class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = defaultdict()
        output = []
        for i, num in enumerate(nums):
            diff = target - num
            if diff in seen:
                output.append(seen[diff])
                output.append(i)
            seen[num]=i
        return output
                