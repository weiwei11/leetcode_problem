#
# @lc app=leetcode.cn id=220 lang=python3
#
# [220] 存在重复元素 III
#

# @lc code=start
class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        if t < 0: return False
        n = len(nums)
        d = {}
        w = t + 1
        for i in range(n):
            m = nums[i] // w 
            if m in d.keys():
                return True
            elif m - 1 in d.keys() and abs(nums[i] - d[m-1]) < w:
                return True
            elif m + 1 in d.keys() and abs(nums[i] - d[m+1]) < w:
                return True
            else:
                d[m] = nums[i]  # if m == nums[i-k] // w then m in d.keys()
                if i >= k:
                    del d[nums[i-k] // w]
        return False
                
        
# @lc code=end

