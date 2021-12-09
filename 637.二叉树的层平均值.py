#
# @lc app=leetcode.cn id=637 lang=python3
#
# [637] 二叉树的层平均值
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        res = []
        self.dfs(root, res, 0)
        return [x[0]/x[1] for x in res]
    
    def dfs(self, root, res, depth):
        if not root: return
        if depth < len(res):
            res[depth] = (res[depth][0] + root.val, res[depth][1] + 1)
        else:
            res.append((root.val, 1))
        self.dfs(root.left, res, depth+1)
        self.dfs(root.right, res, depth+1)
        

# @lc code=end

