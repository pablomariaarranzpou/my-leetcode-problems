# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def __init__(self):
        self.nodes = []
        
        
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        
        visited = set()
        _min = float('inf')
        self.dfs_dist(root, visited)
        
        self.nodes.sort()
        for i in range(len(self.nodes) - 1):
            
            _min = min(_min, abs(self.nodes[i] - self.nodes[i + 1]))
            
        return _min
        
        
        
    def dfs_dist(self, node, visited):
        
        if node not in visited:
            
            visited.add(node)
            self.nodes.append(node.val)
            
            if node.left:
                self.dfs_dist(node.left, visited)

            if node.right:
                self.dfs_dist(node.right, visited) 
                

        