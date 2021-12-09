#
# @lc app=leetcode.cn id=671 lang=python3
#
# [671] 二叉树中第二小的节点
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findSecondMinimumValue(self, root: TreeNode) -> int:
        if not root: return -1
        return self._find(root, root.val)
    
    def _find(self, root, min_val):
        if not root: return -1
        
        if root.val != min_val:
            return root.val
        else:
            l = self._find(root.left, min_val)
            r = self._find(root.right, min_val)
            if l != -1 and r != -1:
                return min(l, r)
            else:
                return l if l != -1 else r
            
        
# @lc code=end

