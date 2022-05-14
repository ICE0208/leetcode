# https://leetcode.com/problems/power-of-two/

class Solution:
    def isPowerOfTwo(self, n):
        if n<1:
            return False
        
        n = str(bin(n))
        if n.count('1') == 1:
            return True
        
        return False

# Better Answer
# class Solution(object):
#     def isPowerOfTwo(self, n):
#         return n and not (n & n - 1)