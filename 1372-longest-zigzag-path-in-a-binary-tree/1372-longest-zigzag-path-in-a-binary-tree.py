# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def __init__(self):
        self.max_val = 0
        
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        
        if not root:
            return 0
        
        if(root.left):
            self.inorder(root.left, "Left", 1)
        if(root.right):
            self.inorder(root.right, "Right", 1)
            
        return self.max_val

        
    def inorder(self, node, prev, val):
        
        if not node:
            return
            
        if val > self.max_val:
            self.max_val = val
        
        if prev == "Left":
            self.inorder(node.right,"Right", val + 1)
            self.inorder(node.left, "Left", 1)
            
        if prev == "Right":
            self.inorder(node.left,"Left", val + 1)
            self.inorder(node.right, "Right", 1)

        