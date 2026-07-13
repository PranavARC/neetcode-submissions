# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return self.recursiveDepth(root, 0)

    def recursiveDepth(self, root, currDepth):
        if not root:
            return currDepth
        newDepth = currDepth + 1
        return max(self.recursiveDepth(root.left, newDepth), self.recursiveDepth(root.right, newDepth))
