# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        '''
        Intuition states to check if the left (if it exists) is smaller, check if the right (if it exists) is larger
        If either of those are False, return False, if both are true, then return the AND of the method ran on the left/right

        Time: O(n) since the method is ran on every node
        Space: O(logh) since we only check one side at a time
        '''
        return self.recursiveValid(root, -float('inf'), float('inf'))

    def recursiveValid(self, root, l_bound, r_bound):
        if root.left:
            if not l_bound < root.left.val < root.val or not self.recursiveValid(root.left, l_bound, root.val):
                return False
        
        if root.right:
            if not root.val < root.right.val < r_bound or not self.recursiveValid(root.right, root.val, r_bound):
                return False

        return True
