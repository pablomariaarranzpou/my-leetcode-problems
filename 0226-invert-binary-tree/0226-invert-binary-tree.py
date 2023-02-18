# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        
        if not root:
            return None
        queue = [root]
        while queue:
            curr = queue.pop()
            if curr.left and curr.right:
                curr.left, curr.right = curr.right, curr.left
                queue.append(curr.left)
                queue.append(curr.right)
            elif curr.left:
                curr.right = curr.left
                curr.left = None
                queue.append(curr.right)
            elif curr.right:
                curr.left = curr.right
                curr.right = None
                queue.append(curr.left)
        return root
                
        