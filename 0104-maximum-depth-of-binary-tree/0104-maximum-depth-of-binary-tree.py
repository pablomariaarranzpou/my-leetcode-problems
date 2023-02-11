# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        if root == None:
            return 0
        
        visited = set()
        max_depth = 1
        queue = [(root, 1)]
        depth = 0
        
        while queue:
            next_queue = []
            node, depth = queue.pop(0)
            
            if depth > max_depth:
                max_depth = depth
                
            if node not in visited:
                visited.add(node)
                if node.left != None:
                    queue.append((node.left, depth + 1))
                if node.right != None:
                    queue.append((node.right, depth + 1))
        return depth
    

            
            
        
        
        