# https://leetcode.com/problems/top-k-frequent-elements/

from collections import defaultdict

class Solution:
    def topKFrequent(self, nums , k):
        hashmap = defaultdict(int)
        
        for num in nums:
            hashmap[num] += 1
            
        hashlist = sorted(hashmap.items(), key=lambda x:x[1], reverse=True)
        rst = []
        
        for i in range(k):
            rst.append(hashlist[i][0])
            
        return rst