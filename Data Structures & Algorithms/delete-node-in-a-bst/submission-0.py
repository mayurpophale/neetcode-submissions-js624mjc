# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def min_value(self,temp):
        current = temp
        while current.left is not None:
            current = current.left
        return current.val
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        return self.rdelete(root,key)
    
    def rdelete(self,root,key):
        if root is None: #empty list
            return root 
        if key < root.val: #
            root.left = self.rdelete(root.left,key)
        elif key > root.val:
            root.right = self.rdelete(root.right,key)
        else:
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left
            root.val = self.min_value(root.right)
            root.right = self.rdelete(root.right,root.val)
        return root