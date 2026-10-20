class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        i = 0
        j, k = i+1, len(nums) - 1
        out = []
        nums.sort()

        while i<len(nums):
            if nums[i] > 0:
                break
            target = -nums[i] 
            while j < k:
                op = nums[j] + nums[k]
                if op == target:
                    res = [nums[i], nums[j], nums[k]]
                    if res not in out:
                        out.append(res)
                    j+=1
                elif op > target:
                    k-=1
                else:
                    j+=1
            i+=1
            j = i+1
            k = len(nums) - 1
        return out