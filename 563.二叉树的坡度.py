#
# @lc app=leetcode.cn id=563 lang=python3
#
# [563] 二叉树的坡度
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTilt(self, root: TreeNode) -> int:
        return self.dfs(root)[0]
    
    def dfs(self, root):
        if not root: return (0, 0)
        l = self.dfs(root.left)
        r = self.dfs(root.right)
        return abs(l[1] - r[1]) + l[0] + r[0], root.val + l[1] + r[1]
        
# @lc code=end

