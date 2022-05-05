# https://leetcode.com/problems/reverse-words-in-a-string-iii/

class Solution:
    def reverseWords(self, s):
        l = s.split()
        for i in range(len(l)):
            l[i] = "".join(reversed(list(l[i])))
        return " ".join(l)
        


# list_of_word = s.split()
# temp = []
# for each in list_of_word:
# temp.append(each[::-1])
# return ' '.join(temp)