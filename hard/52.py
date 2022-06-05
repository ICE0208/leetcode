# https://leetcode.com/problems/n-queens-ii/

import copy
class Solution:
    
    rst = 0
        
    def extendOne(self, i, j, pan):
        cur_i, cur_j = i, j
        while (cur_i + 1 < len(pan)):
            cur_i += 1
            pan[cur_i][cur_j] = 1
        cur_i = i
        while (cur_i + 1 < len(pan) and cur_j - 1 >= 0):
            cur_i += 1
            cur_j -= 1
            pan[cur_i][cur_j] = 1
        cur_i, cur_j = i, j
        while (cur_i + 1 < len(pan) and cur_j + 1 < len(pan)):
            cur_i += 1
            cur_j += 1
            pan[cur_i][cur_j] = 1
        
    def fillOne(self, i, pan):
        if i == len(pan)-1:
            for j in range(len(pan)):
                if not(pan[i][j] == 0):
                    continue
                else:
                    self.rst += 1
        else:
            for j in range(len(pan)):
                if not(pan[i][j] == 0):
                    continue
                else:
                    newpan = copy.deepcopy(pan)
                    # newpan = pan[:]
                    newpan[i][j] = 2
                    self.extendOne(i, j, newpan)
                    self.fillOne(i+1, newpan)
                    
    
    def totalNQueens(self, n: int):
        self.rst = 0
        pan = [[0] * n for _ in range(n)]
        self.fillOne(0, pan)
        return self.rst