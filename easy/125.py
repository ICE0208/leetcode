# https://leetcode.com/problems/valid-palindrome/

class Solution:
    def isPalindrome(self, s):
        s = s.lower()
        print(s)
        
        l = 0
        r = len(s)-1
        
        while True: 
            while not (s[l].isalpha() or s[l].isdigit()):
                l += 1
                if l>=r or l >= len(s):
                    return True

            while not (s[r].isalpha() or s[r].isdigit()):
                r -= 1
                if r<=l or r < 0:
                    return True
            
            if s[l] != s[r]:
                return False
            
            l+=1
            r-=1
            if l>=r:
                return True