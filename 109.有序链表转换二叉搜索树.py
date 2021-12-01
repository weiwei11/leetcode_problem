#
# @lc app=leetcode.cn id=109 lang=python3
#
# [109] 有序链表转换二叉搜索树
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        if not head: return None
        elif not head.next: return TreeNode(head.val)
        else:
            slow, fast = head, head.next.next
            while fast and fast.next:
                slow = slow.next
                fast = fast.next.next
            
            left = head
            tmp = slow.next
            right = tmp.next
            slow.next = None
            root = TreeNode(tmp.val)
            root.left = self.sortedListToBST(left)
            root.right = self.sortedListToBST(right)
            return root


# @lc code=end

