#
# @lc app=leetcode.cn id=94 lang=python3
#
# [94] 二叉树的中序遍历
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        def mid(root, res):
            if not root:
                return
            if root.left:
                mid(root.left, res)
            res.append(root.val)
            if root.right:
                mid(root.right, res)
            
        res = []
        mid(root, res)
        return res 
# @lc code=end

