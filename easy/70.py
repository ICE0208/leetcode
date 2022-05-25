# https://leetcode.com/problems/climbing-stairs/

# 3차 풀이
class Solution:
    def climbStairs(self, n: int) -> int:

        d = {}
        d[1] = 1
        d[2] = 2
        for i in range(3, n+1):
            d[i] = d[i-1] + d[i-2]
        return d[n]

# 2차 풀이
class OldSolution:
    def climbStairs(self, n: int) -> int:
    
        fn_n = 1
        fn_1 = 1
        fn_2 = 1
        
        for i in range(n-2, -1, -1):
            fn_n = fn_1 + fn_2
            fn_2 = fn_1
            fn_1 = fn_n

        return fn_n

# 1차 풀이
# class Solution:
#     def climbStairs(self, n):
#         l = n
#         r = 0
#         now = 1
#         sum = 1
#         while l>r:
#             print(f'{l-1}C{r+1} = ',end=' ')
#             now = (now * ((l-r)*(l-r-1) / ((r+1)*l)))
#             print((now))
#             l -= 1
#             r += 1
#             sum += now
#         print(sum)
#         return round(sum)

# ======
n = int(input('n: '))
s = Solution()
print(s.climbStairs(n))
# s.climbStairs(n)