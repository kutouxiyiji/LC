# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return([])
        res = []
        stack = [root]
        while True:
            if not stack:
                return(res)
            nodes = []
            nodes.append(stack.pop())
            res.append(nodes[0].val)
            while stack:
                nodes.append(stack.pop())
            new_stack = []
            while nodes:
                N = nodes.pop()
                if N.left:
                    new_stack.append(N.left)
                if N.right:
                    new_stack.append(N.right)
            stack = new_stack
            
            
            
        
            