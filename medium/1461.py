# https://leetcode.com/problems/check-if-a-string-contains-all-binary-codes-of-size-k/

# 2차 풀이
class Solution:
    def hasAllCodes(self, s: str, k: int):
        hashset = set(range(0, 2**k))
            
        for i in range(0, len(s)-k+1):
            target = int(s[i:i+k], 2)
            if target in hashset:
                hashset.remove(target)
        
        if hashset:
            return False
        return True

# 1차 풀이
class OldSolution:
    def hasAllCodes(self, s: str, k: int):
        hashset = set()
        for n in range(0, 2**k):
            hashset.add(f"{n:b}".zfill(k))
            
        for i in range(0, len(s)-k+1):
            target = s[i:i+k]
            if target in hashset:
                hashset.remove(target)
        
        if hashset:
            return False
        return True