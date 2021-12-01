#
# @lc app=leetcode.cn id=2 lang=python3
#
# [2] 两数相加
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1 or not l2:
            return l1 if l1 else l2
        
        f = 0
        h = ListNode(0)
        p = h
        while l1 and l2:
            s = l1.val + l2.val + f
            f = s // 10
            p.next = ListNode(s % 10)
            
            l1 = l1.next
            l2 = l2.next
            p = p.next

        l1 = l1 if l1 else l2
        while l1:
            s = l1.val + f
            f = s // 10
            p.next = ListNode(s % 10)
            
            l1 = l1.next
            p = p.next
        if f:
            p.next = ListNode(f)
        return h.next
        
# @lc code=end

