import math

class Solution:
    def maxArea(self, height: List[int]) -> int:
        max = float("-inf")
        k=0
        for i in height:
            for j in range(k+1, len(height)):
                this_height = min(i, height[j])
                this_width = j - k
                area = this_height * this_width
                if (area > max):
                    max = area
            k+=1
                    
        return max  