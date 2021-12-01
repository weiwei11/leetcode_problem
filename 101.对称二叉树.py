#
# @lc app=leetcode.cn id=101 lang=python3
#
# [101] 对称二叉树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        def sym(l, r):
            if not l and not r:
                return True
            elif not l and r:
                return False
            elif l and not r:
                return False
            else:
                return (l.val == r.val) and \
                    sym(l.left, r.right) and sym(l.right, r.left)
        
        if not root:
            return True

        return sym(root.left, root.right)

# @lc code=end

