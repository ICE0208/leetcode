# https://leetcode.com/problems/pascals-triangle/

class Solution:
    def generate(self, numRows):
        result = []
        temp = []
        last_temp = []
        for i in range(numRows):
            for j in range(0, i+1):
                if j!=0 and j!=i:
                    temp.append(last_temp[j-1] + last_temp[j])
                    pass
                else:
                    temp.append(1)
            result.append(temp)
            last_temp = temp
            temp = []
        return result

# ======
row = int(input('numRows : '))
s = Solution()
print(s.generate(row))
        