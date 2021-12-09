#
# @lc app=leetcode.cn id=700 lang=python3
#
# [700] 二叉搜索树中的搜索
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        if not root: return None
        stack = [root]
        while stack:
            r = stack.pop()
            if val == r.val:
                return r
            elif val < r.val and r.left:
                stack.append(r.left)
            elif val > r.val and r.right:
                stack.append(r.right)
        return None
            
                
        
# @lc code=end

