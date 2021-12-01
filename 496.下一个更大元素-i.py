#
# @lc app=leetcode.cn id=496 lang=python3
#
# [496] 下一个更大元素 I
#

# @lc code=start
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if not nums2: return None

        d2i = {}
        j = length = len(nums2)
        for i in reversed(range(len(nums2))):

            j = i + 1
            while j != -1 and j < length and nums2[j] <= nums2[i]:
                j = d2i[nums2[j]]
            d2i[nums2[i]] = j if j < length else -1
            # print(d2i)
        
        return [nums2[d2i[x]] if d2i[x] >= 0 else -1 for x in nums1]
                
# @lc code=end

