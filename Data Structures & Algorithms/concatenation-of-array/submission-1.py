class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        
        ans = []
        
        counter = 2
        while counter != 0:
            for i in nums:
                ans.append(i)
            counter -= 1

        print(ans)

        return ans