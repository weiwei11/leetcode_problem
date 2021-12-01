#
# @lc app=leetcode.cn id=110 lang=python3
#
# [110] 平衡二叉树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        def depth(root):
            if not root:
                return 0, True
            a, aa = depth(root.left)
            b, bb = depth(root.right)
            d = max(a, b)
            dd = (abs(a - b) <= 1) and aa and bb
            # print(d, a, b)
            return d + 1, dd
        return depth(root)[1]
        
        
# @lc code=end

