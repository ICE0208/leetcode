# https://leetcode.com/problems/transpose-matrix/

class Solution:
    def transpose(self, matrix):
        rst = []
        for i in range(0, len(matrix[0])):
            rst.append([])
            for j in range(0, len(matrix)):
                rst[i].append(matrix[j][i])
        return rst