# https://leetcode.com/problems/longest-consecutive-sequence/

class Solution:
    def longestConsecutive(self, nums):
        
        hashset = set()
        
        for n in nums:
            hashset.add(n)
        
        max_count = 0
        while hashset:
            count = 1
            n = hashset.pop()
            be = n-1
            af = n+1
            while be in hashset:
                count+=1
                hashset.remove(be)
                be -= 1
            while af in hashset:
                count+=1
                hashset.remove(af)
                af += 1
            max_count = max(max_count, count)
        return max_count