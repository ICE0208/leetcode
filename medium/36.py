# https://leetcode.com/problems/valid-sudoku/

from collections import defaultdict

class Solution:
    def isValidSudoku(self, board):
        column = defaultdict(set)
        nine_box = defaultdict(set)
        
        for k, r in  enumerate(board):
            temp = set()
            for i, n in enumerate(r):
                if n == ".":
                    continue
                nine_po = (k//3) * 3 + (i//3)
                if n in nine_box[nine_po]:
                    return False
                nine_box[nine_po].add(n)
                if n in temp:
                    return False
                temp.add(n)
                if n in column[i]:
                    return False
                column[i].add(n)
                
        return True
                
            
        