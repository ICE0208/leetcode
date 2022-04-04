# https://leetcode.com/problems/palindrome-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        list = []
        list.append(head.val)
        n = head.next
        while n is not None:
            list.append(n.val)
            n = n.next
            
        list_len = len(list)
        target_len = list_len // 2
        
        for i in range(0, target_len):
            if list[i] != list[list_len-1-i]:
                return False
        return True