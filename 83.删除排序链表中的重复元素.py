#
# @lc app=leetcode.cn id=83 lang=python3
#
# [83] 删除排序链表中的重复元素
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        
        p, n = head, head.next
        while n:
            if p.val == n.val:
                pass
            else:
                p.next = n
                p = p.next
            n = n.next
        p.next = n
        return head
            
        
# @lc code=end

