# https://leetcode.com/problems/max-area-of-island/

class Solution:
    def __init__(self):
        self.dx = [-1, 1, 0, 0]
        self.dy = [0, 0, -1, 1]
        self.x_len = None
        self.y_len = None
        self.grid = None
        self.cur_size = 0

    def dfs(self, cur_x, cur_y):
        if self.grid[cur_x][cur_y] == 0:
            return -1

        self.cur_size += 1
        self.grid[cur_x][cur_y] = 0 # 땅을 바다로 바꾸기
        for i, j in zip(self.dx, self.dy):
            if cur_x +i <= -1 or cur_x + i >= self.x_len:
                continue
            if cur_y + j <= -1 or cur_y + j >= self.y_len:
                continue
            self.dfs(cur_x+i, cur_y+j)

    def maxAreaOfIsland(self, grid):
        max_area = 0
        self.grid = grid[:]
        self.x_len = len(grid)
        self.y_len = len(grid[0])

        for cur_x in range(0, self.x_len):
            for cur_y in range(0, self.y_len):
                # 현재 땅이 땅이 아니라면
                if grid[cur_x][cur_y] == 0:
                    continue # 다음 땅 검사
                
                self.cur_size = 0
                self.dfs(cur_x, cur_y)
                max_area = max(max_area, self.cur_size)

        return max_area

        