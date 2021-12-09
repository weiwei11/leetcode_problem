#
# @lc app=leetcode.cn id=606 lang=python3
#
# [606] 根据二叉树创建字符串
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        if not root: return ''
        s = str(root.val)
        l = self.tree2str(root.left)
        r = self.tree2str(root.right)
        if root.right:
            l = '(' + l + ')'
            r = '(' + r + ')'
        elif not root.right and root.left:
            l = '(' + l + ')'
        return s + l + r

# @lc code=end

