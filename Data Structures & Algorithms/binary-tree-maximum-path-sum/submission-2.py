# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        '''
        At each root, there are the following possibilities for the maxPath that can be returned
        root + maxPath from left subtree, root + maxPath from right subtree, root + maxPaths of both subtrees,
        root, maxPath from left subtree, and maxPath from right subtree.
        Find the maxPath values for left/right subtrees, and return the max of the previously mentioned root maxPaths

        Time - O(n) - Each node's value is considered once, and the max will always be done between 6 values for each node
        Space - O(h) - Only h number of functions will be active at a time on the recursive stack
        '''
        
        maxPaths = self.recursiveMaxPath(root)
        print(maxPaths)

        return max(list(maxPaths.values()))
    
    def recursiveMaxPath(self, root):
        if not root:
            return {"root": -float('inf'), "nonroot": -float('inf')}


        maxPathLeft = self.recursiveMaxPath(root.left)
        maxPathRight = self.recursiveMaxPath(root.right)

        rootMaxPaths = [root.val, maxPathLeft["root"]+root.val, maxPathRight["root"]+root.val]
        nonRootMaxPaths = [maxPathLeft["root"], maxPathRight["root"], maxPathLeft["nonroot"], maxPathRight["nonroot"], maxPathLeft["root"]+root.val+maxPathRight["root"]]

        maxRoot = max(rootMaxPaths)
        maxNonRoot = max(nonRootMaxPaths)

        return {"root": maxRoot, "nonroot": maxNonRoot}
