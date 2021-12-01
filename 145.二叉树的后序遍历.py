#
# @lc app=leetcode.cn id=145 lang=python3
#
# [145] 二叉树的后序遍历
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        def func(root, res):
            if not root:
                return 
            else:
                func(root.left, res)
                func(root.right, res)
                res.append(root.val)
        res = []
        func(root, res)
        return res
# @lc code=end

