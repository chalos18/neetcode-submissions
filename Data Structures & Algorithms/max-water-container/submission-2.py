class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i, j = 0, len(heights)-1
        maxArea = 0
        while i<j:
            height = min(heights[i], heights[j])
            width = j-i
            area = height * width
            if area > maxArea:
                maxArea=area
            if heights[j] > heights[i]:
                i+=1
            else:
                j-=1
                
        return maxArea




