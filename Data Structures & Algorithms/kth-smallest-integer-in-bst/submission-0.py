# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        '''
        In-order traversal visits nodes in ascending order
        Time: O(n) - Visits all nodes once
        Space: O(n) - Stores all their values in a list
        '''
        values = []
        self.inOrder(root, values)
        return values[k-1]

    def inOrder(self, root, values):
        if not root:
            return
        
        self.inOrder(root.left, values)
        values.append(root.val)
        self.inOrder(root.right, values)
