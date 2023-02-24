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
        
        self.inorder(root, set())
        
        return self.output
        
        
        
        
    def inorder(self, node, visited):
        
        if node not in visited:
            
            visited.add(node)
            
            if node.left != None:
                self.inorder(node.left, visited)
                
            self.output.append(node.val)
                
            if node.right != None:
                
                self.inorder(node.right, visited)
                
            
                
            
        
        
        