#
# @lc app=leetcode.cn id=160 lang=python3
#
# [160] 相交链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        if not headA or not headB:
            return None
        
        h1, h2 = headA, headB
        while h1 and h2:
            h1 = h1.next
            h2 = h2.next

        while h1:
            headA = headA.next
            h1 = h1.next
        while h2:
            headB = headB.next
            h2 = h2.next

        h1, h2 = headA, headB
        while h1 and h2:
            if h1 == h2:
                return h1
            h1 = h1.next
            h2 = h2.next
        
        return None
        
# @lc code=end

