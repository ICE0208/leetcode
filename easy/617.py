# https://leetcode.com/problems/merge-two-binary-trees/

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def mergeTrees(self, root1, root2):
        if not root1:
            return root2
        if not root2:
            return root1
        
        result = TreeNode()
        result.val = root1.val + root2.val
        result.left = self.mergeTrees(root1.left, root2.left)
        result.right = self.mergeTrees(root1.right, root2.right)
        
        return result
                    


        