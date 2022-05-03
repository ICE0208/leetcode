# https://leetcode.com/problems/split-a-string-in-balanced-strings/

class Solution:
    def balancedStringSplit(self, s: str):
        l = 0
        r = 0
        cnt = 0
        for c in s:
            if c == 'R':
                r += 1
            else:
                l += 1
            if l==r:
                cnt+=1
                l = 0
                r = 0
        return cnt