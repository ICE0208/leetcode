# https://leetcode.com/problems/group-anagrams/

class Solution:
    def groupAnagrams(self, strs):
        hashmap = dict()
        result = []
        
        for s in strs:
            std_s = "".join(sorted(s))
            if std_s not in hashmap:
                hashmap[std_s] = len(result)
                result.append([s])
                continue
            result[hashmap[std_s]].append(s)
        return result