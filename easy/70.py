# https://leetcode.com/problems/climbing-stairs/

class Solution:
    def climbStairs(self, n):
        l = n
        r = 0
        now = 1
        sum = 1
        while l>r:
            print(f'{l-1}C{r+1} = ',end=' ')
            now = (now * ((l-r)*(l-r-1) / ((r+1)*l)))
            print((now))
            l -= 1
            r += 1
            sum += now
        print(sum)
        return round(sum)

# ======
n = int(input('n: '))
s = Solution()
print(s.climbStairs(n))
# s.climbStairs(n)