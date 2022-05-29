# 첫번째 풀이
class Solution:
    def maxProduct(self, words):
        res = 0
        for i in range(len(words)-1):
            for j in range(i+1, len(words)):
                if set(words[i]) & set(words[j]):
                    continue
                res = max(res, len(words[i])*len(words[j]))
        return res