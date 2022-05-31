# https://leetcode.com/problems/check-if-a-string-contains-all-binary-codes-of-size-k/

# 1차 풀이
class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
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