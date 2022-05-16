# https://leetcode.com/problems/valid-anagram/

# 두 번째 풀이
class Solution:
    def isAnagram(self, s, t):
        hashdic = dict()
        
        for n in s:
            if n in hashdic:
                hashdic[n] += 1
                continue
            hashdic[n] = 1
        
        for m in t:
            if m in hashdic:
                hashdic[m] -= 1
                if hashdic[m] == 0:
                    del hashdic[m]
                    continue
                continue
            return False
        
        return not(hashdic)

# 첫 번째 풀이
class OldSolution:
    def isAnagram(self, s, t):
        return sorted(s) == sorted(t)