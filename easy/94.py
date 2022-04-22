# https://leetcode.com/problems/binary-tree-inorder-traversal/

class Solution:
    def inorderTraversal(self, root):
        if root==None: return []

        result = []
        
        result.extend(self.inorderTraversal(root.left))
        
        result.append(root.val)
        
        result.extend(self.inorderTraversal(root.right))

        return result

# =====
# 입력 생략