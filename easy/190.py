# https://leetcode.com/problems/reverse-bits/

class Solution:
    def reverseBits(self, n):
        s = ""
        for _ in range(32):
            if n%2 == 1:
                s += "1"
            else:
                s += "0"
            n = n >> 1
        return int(s, 2)