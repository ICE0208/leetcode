# https://leetcode.com/problems/maximum-number-of-words-found-in-sentences/

class Solution:
    def mostWordsFound(self, sentences):
        max_num_of_words = -1
        for sentence in sentences:
            max_num_of_words = max(max_num_of_words, sentence.count(' ')+1)
        return max_num_of_words

# ======
sentences = ["alice and bob love leetcode", "i think so too", "this is great thanks very much"]
s = Solution()
print(s.mostWordsFound(sentences))