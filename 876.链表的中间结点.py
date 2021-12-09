#
# @lc app=leetcode.cn id=876 lang=python3
#
# [876] 链表的中间结点
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        if not head or not head.next: return head

        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        # if not fast:
        #     slow = slow.next

        return slow
        
# @lc code=end

