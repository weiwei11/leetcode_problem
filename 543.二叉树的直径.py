#
# @lc app=leetcode.cn id=543 lang=python3
#
# [543] 二叉树的直径
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        return self.dfs(root)[0]
    
    def dfs(self, root):
        if not root: return (0, 0)
        l = self.dfs(root.left)
        r = self.dfs(root.right)
        return max(l[0], r[0], l[1]+r[1]), max(l[1], r[1]) + 1

# @lc code=end

