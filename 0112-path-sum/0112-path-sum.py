# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        
        return self.inorder(root, targetSum, 0)

        
    def inorder(self, node, targetSum, prev):
        
        node.val += prev

        if node.val == targetSum and node.left == None and node.right == None:
            return True
        else:
            if node.left != None:
                if(self.inorder(node.left,targetSum, node.val)):
                    return True

            if node.right != None:
                if(self.inorder(node.right,targetSum, node.val)):
                    return True
                
        return False
        
