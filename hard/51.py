# https://leetcode.com/problems/n-queens/

import copy
class Solution:
    
    rst = []
    
    def appendRst(self, pan):
        panList = list()
        for s in pan:
            cur_s = ""
            for c in s:
                if c==0 or c==1:
                    cur_s += "."
                else:
                    cur_s += "Q"
            panList.append(cur_s)
        self.rst.append(panList)
        
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
                    newpan = copy.deepcopy(pan)
                    newpan[i][j] = 2
                    self.appendRst(newpan)
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
                    
    
    def solveNQueens(self, n: int):
        self.rst = []
        pan = [[0] * n for _ in range(n)]
        self.fillOne(0, pan)
        return self.rst