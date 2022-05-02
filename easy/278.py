# https://leetcode.com/problems/first-bad-version/

def isBadVersion(n):
    if n >= 500:
        return True
    else:
        return False

class Solution:
    def firstBadVersion(self, n):
        start_v = 1
        end_v = n
        while True:
            checking_v = start_v + (end_v - start_v) // 2
            if isBadVersion(checking_v):
                end_v = checking_v
            else:
                start_v = checking_v + 1
            
            if start_v == end_v:
                return start_v

# ====
s = Solution()
print(s.firstBadVersion(10000))