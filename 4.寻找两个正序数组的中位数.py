#
# @lc app=leetcode.cn id=4 lang=python3
#
# [4] 寻找两个正序数组的中位数
#

# @lc code=start
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        l = len(nums1) + len(nums2)
        if l % 2:
            return self.kth(nums1, nums2, l // 2)
        else:
            return (self.kth(nums1, nums2, l // 2) \
                + self.kth(nums1, nums2, l // 2 - 1)) / 2
        
    def kth(self, a, b, k):
        if not a:
            return b[k]
        if not b:
            return a[k]
        
        ai, bi = len(a) // 2, len(b) // 2
        if ai + bi < k:
            if a[ai] > b[bi]:
                return self.kth(a, b[bi + 1:], k - bi - 1)
            else:
                return self.kth(a[ai + 1:], b, k - ai - 1)
        else:
            if a[ai] > b[bi]:
                return self.kth(a[:ai], b, k)
            else:
                return self.kth(a, b[:bi], k)
            
        
# @lc code=end

