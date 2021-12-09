#
# @lc app=leetcode.cn id=653 lang=python3
#
# [653] 两数之和 IV - 输入 BST
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: TreeNode, k: int) -> bool:
        res = []
        self.preorder(root, res)
        l, r = 0, len(res) - 1
        print(res)
        while l < r:
            if res[l] + res[r] == k:
                return True
            elif res[l] + res[r] < k:
                l += 1
            else:
                r -= 1
        return False
               
    
    def preorder(self, root, res):
        if not root: return
        self.preorder(root.left, res)
        res.append(root.val)
        self.preorder(root.right, res)
        
# @lc code=end

