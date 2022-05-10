# https://leetcode.com/problems/rotting-oranges/

from collections import deque

class Solution:
    def orangesRotting(self, grid):
        
        queue = deque()
        lenx = len(grid)
        leny = len(grid[0])
        dx = [-1, 1, 0, 0]
        dy = [0, 0, -1, 1]
        
        for i in range(lenx):
            for j in range(leny):
                if grid[i][j] == 2:
                    queue.append((i, j, 0))
        
        time = 0
        while queue:
            cur = queue.popleft()
            cur_x = cur[0]
            cur_y = cur[1]
            time = cur[2]
            
            for i in range(4):
                if cur_x + dx[i] <= -1 or cur_x + dx[i] >= lenx:
                    continue
                if cur_y + dy[i] <= -1 or cur_y + dy[i] >= leny:
                    continue
                if grid[cur_x+dx[i]][cur_y+dy[i]] != 1:
                    continue
                queue.append((cur_x+dx[i], cur_y+dy[i], time+1))
                grid[cur_x+dx[i]][cur_y+dy[i]] = 2
                
        
        for i in range(lenx):
            for j in range(leny):
                if grid[i][j] == 1:
                    return -1
                
        return time

# ======

s = Solution()
grid = [[2,1,1],[1,1,0],[0,1,1]]
print(s.orangesRotting(grid))