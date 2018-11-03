# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return(0)
        if root.left is None and root.right is None:
            return(1)
        if root.left is not None and root.right is None:
            return(1+self.minDepth(root.left))
        if root.left is None and root.right is not None:
            return(1+self.minDepth(root.right))
        return(1+min(self.minDepth(root.left),self.minDepth(root.right)))
        