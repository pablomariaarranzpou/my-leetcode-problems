# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def __init__(self):
        self.mini = float('inf')
    
    
    def minDepth(self, root: Optional[TreeNode]) -> int:
        
        
        def aux(node, depth):
            
            if not node.left and not node.right:
                
                self.mini = min(self.mini, depth)
                
            if node.right:
                aux(node.right, depth + 1)
                
            if node.left:
                aux(node.left, depth + 1)
        
        if not root:
            return 0
        
        aux(root, 1)
        
        return self.mini
        
        
        
                
                
        