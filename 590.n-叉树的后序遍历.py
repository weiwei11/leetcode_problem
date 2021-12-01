#
# @lc app=leetcode.cn id=590 lang=python3
#
# [590] N 叉树的后序遍历
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        if not root: return []
        stack = [root]
        visited = [0]
        res = []
        while stack:
            # print(stack, vis)
            if visited[-1]:
                res.append(stack.pop().val)
                visited.pop()
            else:
                visited[-1] = 1
                visited.extend([0 for _ in stack[-1].children])
                stack.extend(reversed(stack[-1].children))
        return res
        
# @lc code=end

