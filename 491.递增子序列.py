#
# @lc app=leetcode.cn id=491 lang=python3
#
# [491] 递增子序列
#

# @lc code=start
class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        # def doit(nums):
        #     if len(nums) == 0:
        #         return [[]]
        #     elif len(nums) == 1:
        #         return [[nums[0]]]
        #     else:
        #         anchor = nums[0]
        #         res = []
        #         for i in range(1, len(nums)):
        #             if nums[i] >= anchor:
        #                 res.extend(doit(nums[i:]))
        #                 # print(nums[i], res)
        #         a = deepcopy(res)
        #         # print(res)
        #         [x.append(anchor) for x in a]
        #         res.extend(a)
        #         res.append([anchor])
        #         return res
        
        # res = doit(nums)
        # res = set([tuple(x[::-1]) for x in res if len(x) > 1])
        
        # return list(res)

        def backtrack(curr, nums):
            if( len(curr) >= 2 and curr[-1] < curr[-2] ): return
            if( len(curr) >= 2 and curr[:] not in result):
                result.add(curr[:])
            for i in range(len(nums)):
                backtrack( curr + (nums[i],), nums[i+1:] )  # using tuples for curr instead of list
        result = set()
        backtrack( (), nums)
        return list(result)

        
# @lc code=end

