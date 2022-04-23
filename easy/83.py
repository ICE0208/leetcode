# https://leetcode.com/problems/remove-duplicates-from-sorted-list/

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteDuplicates(self, head):
        cur = head
        node_set = list()
        while cur != None:
            if cur.val in node_set:
                last_cur.next = cur.next
            else:
                node_set.append(cur.val)
                last_cur = cur
            cur = cur.next
            
        return head

# =====
head = ListNode()
this_cur = head
this_cur.val = 1
this_cur.next = None

node1 = ListNode()
this_cur = node1
this_cur.val = 1
this_cur.next = None
head.next = node1

node2 = ListNode()
this_cur = node2
this_cur.val = 1
this_cur.next = None
node1.next = node2

s = Solution()
result = s.deleteDuplicates(head)
r_cur = result
while r_cur != None:
    print(r_cur.val)
    r_cur = r_cur.next