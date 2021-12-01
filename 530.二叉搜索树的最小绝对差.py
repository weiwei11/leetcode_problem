#
# @lc app=leetcode.cn id=530 lang=python3
#
# [530] 二叉搜索树的最小绝对差
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    min_abs = int(1e6)
    prev = None

    def getMinimumDifference(self, root: TreeNode) -> int:
        self.dfs(root)
        return self.min_abs

    def dfs(self, root):
        if not root: return

        self.dfs(root.left)
        self.min_abs = min(self.min_abs, abs(root.val - self.prev.val)) if self.prev else self.min_abs
        self.prev = root
        self.dfs(root.right)
        
        
# @lc code=end

