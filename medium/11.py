# https://leetcode.com/problems/container-with-most-water/

# ? 2022-05-21 재풀이
class Solution:
    def maxArea(self, height):
        l, r = 0, len(height) - 1
        
        max_n = 0
        cur_n = 0
        while l<r:
            cur_n = (r-l) * min(height[l], height[r])
            max_n = max(max_n, cur_n)
            
            if height[l]<height[r]:
                l+=1
            else:
                r-=1
                
        return max_n

class OldSolution:
    def maxArea(self, height):
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