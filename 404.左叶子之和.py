#
# @lc app=leetcode.cn id=404 lang=python3
#
# [404] 左叶子之和
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        res = 0
        stack = [(root, False)]
        while stack:
            cur, is_left = stack.pop()
            if not cur:
                continue
            if not cur.left and not cur.right:
                res = res + (cur.val if is_left else 0)
            else:
                stack.append((cur.left, True))
                stack.append((cur.right, False))
        return res
        
# @lc code=end

