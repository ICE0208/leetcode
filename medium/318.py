# 첫번째 풀이
class Solution:
    def maxProduct(self, words):
        res = 0
        max_j = 0
        words.sort(key=lambda x: len(x), reverse=True)
        for i in range(len(words)-1):
            len_i= len(words[i])
            if res > len_i * len(words[i+1]):
                return res
            for j in range(i+1, len(words)):
                len_j = len(words[j])
                if len_j <= max_j:
                    break
                if set(words[i]) & set(words[j]):
                    continue
                if len_i*len_j > res:
                    res = len_i*len_j
                    max_j = len_j
        return res