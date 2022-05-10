# https://leetcode.com/problems/01-matrix/

from collections import deque

class Solution:


    def updateMatrix(self, mat):
        lenx = len(mat)
        leny = len(mat[0])
        result = [[-1 for i in range(leny)] for j in range(lenx)]
        queue = deque()

        dx = [-1, 1, 0, 0]
        dy = [0, 0, -1, 1]

        for i in range(lenx):
            for j in range(leny):
                if mat[i][j] == 0:
                    queue.append((i, j, 0))
                    result[i][j] = 0

        while queue:
            cur = queue.popleft()
            curx = cur[0]
            cury = cur[1]
            curd = cur[2]

            for i in range(4):
                if curx+dx[i] <=-1 or curx+dx[i] >= lenx:
                    continue
                if cury+dy[i] <=-1 or cury+dy[i] >= leny:
                    continue
                if result[curx+dx[i]][cury+dy[i]] != -1:
                    continue
                queue.append((curx+dx[i], cury+dy[i], curd+1))
                result[curx+dx[i]][cury+dy[i]] = curd+1

        return result

# ====
s = Solution()
mat = [[0,0,0],[0,1,0],[1,1,1]]
print(s.updateMatrix(mat))