# https://leetcode.com/problems/number-of-steps-to-reduce-a-number-to-zero/submissions/

class Solution:
    def numberOfSteps(self, num: int):
        cnt = 0
        while num:
            if num%2:
                num -= 1
                cnt += 1
            else:
                num/=2
                cnt += 1
        return cnt


#  ==================================================
s = Solution()
num = int(input('num : '))
print(s.numberOfSteps(num))
