# https://leetcode.com/problems/middle-of-the-linked-list/

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def middleNode(self, head):
        list = []
        n = head
        while n is not None:
            list.append(n.val)
            n = n.next

        start_position = len(list) // 2 + 1
        result_list = list[start_position-1:]
        print(result_list)

        result_node = ListNode(result_list[0])
        now_node = result_node
        for i in result_list[1:]:
            now_node.next = ListNode(i)
            now_node = now_node.next
        return result_node

# --------------------------------------------------------
# Input List -> Linked List
s = Solution()
temp_list = list(map(int, input().split(" ")))
ln = ListNode(temp_list[0])
now_node = ln
for i in temp_list[1:]:
    now_node.next = ListNode(i)
    now_node = now_node.next

# Print Linked List
# n = ln
# while n is not None:
#     print(n.val)
#     n = n.next

s.middleNode(ln)