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
        Space: O(h) - No extra data structures, but h recursive function calls on the stack
        '''
        self.k = k
        self.result = -1
        self.inOrder(root)
        return self.result

    def inOrder(self, root):
        if not root:
            return
        
        self.inOrder(root.left)
        self.k -= 1
        if self.k == 0:
            self.result = root.val
            return
        self.inOrder(root.right)
