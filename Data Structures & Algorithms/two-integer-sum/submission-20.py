class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        A = []
        for i, num in enumerate(nums):
            A.append([num, i])

        A.sort()
        i, j = 0, len(nums) - 1

        while i != j:
            two_sum = A[i][0] + A[j][0]
            if two_sum > target:
                j-=1
            if two_sum < target:
                i+=1
            if two_sum == target:
                return [min(A[i][1], A[j][1]), max(A[i][1], A[j][1])]

        return []

            