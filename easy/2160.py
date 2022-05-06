# https://leetcode.com/problems/minimum-sum-of-four-digit-number-after-splitting-digits/

class Solution:
    def minimumSum(self, num):
        min_sum = float("inf")
        num_l = str(num)
            
        index0 = num_l[0]
        num_l = num_l[1:]
        for i in range(3):
            new1 = int("".join(sorted(index0 + num_l[i])))
            new2 = new2 = int("".join(sorted(num_l[:i] + num_l[i+1:])))
            min_sum = min(min_sum, new1+new2)
            
        return min_sum
        
        