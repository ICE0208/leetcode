# https://leetcode.com/problems/populating-next-right-pointers-in-each-node/

from collections import deque

# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root):
        if not root:
            return
        
        queue = deque()
        i = 0
        cnt = 0
        queue.append(root)
        cur = None
        
        while queue:
            new_cur = queue.popleft()
            if new_cur.left:
                queue.append(new_cur.left)
            if new_cur.right:
                queue.append(new_cur.right)
            
            cnt += 1
            if (cnt >= 2**i):
                if cur:
                    cur.next = new_cur
                cur = None
                new_cur.next = None
                i+=1
                cnt = 0
                continue
                
            if not cur:
                cur = new_cur
                continue
                
            cur.next = new_cur
            cur = new_cur
            
        return root