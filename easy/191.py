# https://leetcode.com/problems/number-of-1-bits/

class Solution:
    def hammingWeight(self, n):
        sum = 0
        while True:
            sum += n & 1
            n = n >> 1
            if n==0:
                return sum