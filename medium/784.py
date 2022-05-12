# https://leetcode.com/problems/letter-case-permutation/

from itertools import product

class Solution:
    def letterCasePermutation(self, s):
        ul_list = []
        for c in s:
            if c.isdigit():
                ul_list.append([c, c])
                continue
            ul_list.append([c.upper(), c.lower()])

        
        result = set()
        for tu in (product([0, 1], repeat=len(s))):
            temp_s = ""
            for i in range(len(s)):
                temp_s += ul_list[i][tu[i]]
            result.add(temp_s)
            
        return list(result)