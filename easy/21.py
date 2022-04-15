# https://leetcode.com/problems/merge-two-sorted-lists/

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1, list2):
        l_list1 = []
        l_list2 = []
        
        head1 = ListNode()
        head1.next = list1
        this_next = head1.next
        while this_next != None:
            l_list1.append(this_next.val)
            this_next = this_next.next
            
        head2 = ListNode()
        head2.next = list2
        this_next = head2.next
        while this_next != None:
            l_list2.append(this_next.val)
            this_next = this_next.next
        
        l_result = sorted(l_list1 + l_list2)
        n_result_head = ListNode()
        this = n_result_head
        for value in l_result:
            this.next = ListNode()
            this.next.val = value
            this = this.next
            
        return n_result_head.next

# =======
# LeetCode 에디터에서 직접 풀어서 입력 부분 구현 없음


