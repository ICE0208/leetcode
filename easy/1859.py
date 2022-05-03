# https://leetcode.com/problems/sorting-the-sentence/

class Solution:
    def sortSentence(self, s: str):
        dic = dict()
        l = s.split()
        for v in l:
            dic[v[-1]] = v[:-1]
        dic = sorted(dic.items())
        result = ""
        for v in dic:
            result += (v[1]+" ")
        return result.strip()
        