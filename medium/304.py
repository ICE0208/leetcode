# https://leetcode.com/problems/range-sum-query-2d-immutable/

class NumMatrix:
    def __init__(self, matrix):
        self.mat_dict = dict()
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                self.mat_dict[(i, j)] = self.mat_dict.get((i, j-1), 0) +\
                self.mat_dict.get((i-1, j), 0) - self.mat_dict.get((i-1, j-1), 0) + matrix[i][j]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return self.mat_dict.get((row2, col2), 0) - self.mat_dict.get((row2, col1-1), 0) -\
        self.mat_dict.get((row1-1, col2), 0) + self.mat_dict.get((row1-1, col1-1), 0)


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)