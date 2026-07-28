class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        non_dup = sorted(set(nums))
        longest = 1
        length = 1
        prev = None

        if len(nums) == 0:
            return 0
        
        for i in range(len(non_dup)):
            if prev == None:
                prev = non_dup[i]
            else:
                if non_dup[i] == prev+1:
                    length+=1
                else:
                    length = 1
                if length > longest:
                    longest = length
                prev = non_dup[i]
                        
        return longest