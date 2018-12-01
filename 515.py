# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def largestValues(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return([])
        stack = [root]
        res =[]
        while True:
            temp =[]
            largest = float('-inf')
            while stack:
                node = stack.pop()
                largest = max(largest, node.val)
#                print(largest)
                if node.left:
                    temp.append(node.left)
                if node.right:
                    temp.append(node.right)
            res.append(largest)
            if not temp:
                break
            stack = temp
        return(res)
                