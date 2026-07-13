# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        self.recursiveInvert(root)
        return root
    
    def recursiveInvert(self, root):
        if not root:
            return
        temp = root.left
        root.left = root.right
        root.right = temp
        self.recursiveInvert(root.left)
        self.recursiveInvert(root.right)
        return
        