# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pathSum(self, root, s):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        if not root:
            return([])
        result = []
        def helper(root,res,s):
            if root.val == s and not root.left and not root.right:
                result.append(res+[root.val])
            elif not root.left and not root.right:
                return()
            if root.left is not None:
                helper(root.left,res+[root.val],s-root.val)
            if root.right is not None:
                helper(root.right, res+[root.val],s-root.val)
        helper(root,[],s)
        return(result)