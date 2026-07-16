# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    '''
    Serialize via preorder DFS, and deserialize via the same (use N to mark None)

    Time: O(n) - During serialization, we visit each node once.
    During deserialization, we visit each index of the node list once
    Space: O(n) - The node list is size n, the stack space for recursion is h
    '''

    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        self.dfsList = []
        self.dfs(root)
        return ",".join(self.dfsList)
    
    def dfs(self, root):
        if not root:
            self.dfsList.append("N")
            return
        
        self.dfsList.append(str(root.val))
        self.dfs(root.left)
        self.dfs(root.right)

    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        self.dfsList = data.split(",")
        self.index = 0
        root = self.dfsM()
        return root
    
    def dfsM(self):
        if self.dfsList[self.index] == "N":
            self.index += 1
            return None
        
        root = TreeNode(int(self.dfsList[self.index]))
        self.index += 1

        root.left = self.dfsM()
        root.right = self.dfsM()

        return root