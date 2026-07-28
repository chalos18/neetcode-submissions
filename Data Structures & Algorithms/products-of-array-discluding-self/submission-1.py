class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        A = {index: num for index, num in enumerate(nums)}
        i, prev = 0, 1
        res = []
        while i < len(nums):
            product = 0
            for key, value in A.items():
                if key != i:
                    product = prev * value
                    prev = product
            res.append(product)
            prev, product = 1, 0
            i+=1
        return res
            