# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        order = []
        
        if not root:
            return []
        
        def postorder(node):
            
            
            if node.left:
                
                postorder(node.left)
                
            if node.right:
                
                postorder(node.right)
                
                
            order.append(node.val)
            
            
        postorder(root)
        
        return order
                
            
                
            