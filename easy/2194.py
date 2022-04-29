# https://leetcode.com/problems/cells-in-a-range-on-an-excel-sheet/

class Solution:
    def cellsInRange(self, s):
        result = []

        s_list = s.split(':')
        col_start = ord(s_list[0][0])
        col_end = ord(s_list[1][0])
        row_start = int(s_list[0][1:])
        row_end = int(s_list[1][1:])
        
        for c in range(col_start, col_end+1):
            for r in range(row_start, row_end+1):
                result.append(chr(c) + str(r))

        return result

# ======

s = "A1:F1"
solution =  Solution()
print(solution.cellsInRange(s))
