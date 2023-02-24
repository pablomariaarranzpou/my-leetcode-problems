# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def __init__(self):
        self.output = []
        
        
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]: 
        if not root:
            return []
        self.inorder(root)
        return self.output
 
        
    def inorder(self, node):
        if node.left != None:
            self.inorder(node.left)
                
        self.output.append(node.val)
                
        if node.right != None:
                
            self.inorder(node.right)
                
            
                
            
        
        
        