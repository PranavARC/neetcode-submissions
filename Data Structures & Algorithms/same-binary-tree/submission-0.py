# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        return self.recursiveSameTree(p,q)

    def recursiveSameTree(self, p, q):
        if not (p or q):
            return True
        elif not p or not q:
            return False
        
        if p.val != q.val:
            return False
        
        return self.recursiveSameTree(p.left, q.left) and self.recursiveSameTree(p.right, q.right)
