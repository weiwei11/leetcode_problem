#
# @lc app=leetcode.cn id=144 lang=python3
#
# [144] 二叉树的前序遍历
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        def func(root, res):
            if not root:
                return 
            else:
                res.append(root.val)
                func(root.left, res)
                func(root.right, res)
        res = []
        func(root, res)
        return res
# @lc code=end

