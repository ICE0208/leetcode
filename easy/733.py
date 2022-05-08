# https://leetcode.com/problems/flood-fill/

from collections import deque

class Solution:
    def floodFill(self, image, sr, sc, newColor):
        queue = deque() # bfs를 위한 queue
        already = [] # 한번 체크한 곳 튜플로 append
        
        # 위, 아래, 왼쪽, 오른쪽 방향
        dx = [-1, 1, 0, 0]
        dy = [0, 0, -1, 1]

        # 세로 길이, 가로 길이
        x_len = len(image)
        y_len = len(image[0])
        
        # 바꿀 색깔
        targetColor = image[sr][sc]
        
        queue.append((sr, sc))
        while queue:
            cur_pos = queue.popleft() # 현재 위치
            
            # 이미 체크한 곳인지 확인
            if cur_pos in already:
                continue
            already.append(cur_pos)
            
            # 현재 위치를 x와 y, 2개의 변수 분리
            cur_x = cur_pos[0]
            cur_y = cur_pos[1]

            # 현재 체크하는 곳이 바꿀 대상의 색깔인지 확인
            if image[cur_x][cur_y] != targetColor:
                continue
            image[cur_x][cur_y] = newColor
            
            # 위, 아래, 왼쪽, 아래 방향이 존재하는지 확인하고 queue에 추가
            for i,j in zip(dx, dy):
                if cur_x + i <= -1 or cur_x + i >= x_len:
                    continue
                if cur_y + j <= -1 or cur_y + j >= y_len:
                    continue
                queue.append((cur_x+i, cur_y+j))
                
        return image
        
# =======
# input 생략