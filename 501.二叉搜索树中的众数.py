#
# @lc app=leetcode.cn id=501 lang=python3
#
# [501] 二叉搜索树中的众数
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    prev = None
    max_count = 0
    cur_count = 0
    result = []

    def findMode(self, root: TreeNode) -> List[int]:
        self.dfs(root)
        return self.result
    
    def dfs(self, node):
        if not node: return
        self.dfs(node.left)
        self.cur_count = 1 if node.val != self.prev else self.cur_count + 1
        if self.cur_count == self.max_count:
            self.result.append(node.val)
        elif self.cur_count > self.max_count:
            self.result = [node.val]
            self.max_count = self.cur_count
        self.prev = node.val
        self.dfs(node.right)
        
# @lc code=end

