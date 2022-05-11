# https://leetcode.com/problems/reverse-linked-list/

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head):
        node_list = []
        cur = head
        while cur:
            node_list.append(cur.val)
            cur = cur.next
        
        if not node_list:
            return None
        
        result_head = ListNode()
        cur = result_head
        cur.val = node_list[-1]
        for v in node_list[-2::-1]:
            cur.next = ListNode()
            cur = cur.next
            cur.val = v
            
        return result_head

# ======
# 입력 생략
        