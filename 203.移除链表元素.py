#
# @lc app=leetcode.cn id=203 lang=python3
#
# [203] 移除链表元素
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        while head and head.val == val:
            head = head.next

        if not head:
            return head

        p, q = head, head.next
        while q:
            # print(q.val)
            if q.val != val:
                p.next = q
                p = p.next
            q = q.next
        if p:
            p.next = None
        return head
# @lc code=end

