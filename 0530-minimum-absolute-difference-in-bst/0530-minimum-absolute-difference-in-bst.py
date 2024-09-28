# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        vals = []

        def inorder(node):
            if node is None:
                return
            inorder(node.left)
            vals.append(node.val)
            inorder(node.right)
        
        inorder(root)
        minDifference = float('inf')
        for i in range(1, len(vals)):
            minDifference = min(minDifference, vals[i] - vals[i-1])

        return minDifference
                
        