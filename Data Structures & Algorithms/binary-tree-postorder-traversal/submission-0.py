# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        self.rpostorder(root,res)
        return res
    def rpostorder(self,root,res):
        if root:
            self.rpostorder(root.left,res)
            self.rpostorder(root.right,res)
            res.append(root.val)