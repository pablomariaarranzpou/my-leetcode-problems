"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        
        res = []
        
        if not root:
            return []
        
        def _aux(node):
            
            
            for child in node.children:
                
                _aux(child)
                
            res.append(node.val)
            
            
        _aux(root)
        
        return res
                
                
        
        