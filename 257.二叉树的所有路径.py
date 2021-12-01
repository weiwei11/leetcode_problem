#
# @lc app=leetcode.cn id=257 lang=python3
#
# [257] 二叉树的所有路径
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        if not root:
            return []
        elif not root.left and not root.right:
            return [str(root.val)]
        else:
            res = []
            if root.left:
                a = self.binaryTreePaths(root.left)
                res.extend(a)
            if root.right:
                a = self.binaryTreePaths(root.right)
                res.extend(a)
            res = [str(root.val) + '->' + s for s in res]
            return res
        
# @lc code=end

