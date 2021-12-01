#
# @lc app=leetcode.cn id=547 lang=python3
#
# [547] 省份数量
#

# @lc code=start
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        if len(isConnected) <= 0:
            return 0
        
        visited = set()
        n = len(isConnected)
        stack = []
        num = 0
        for i in range(n):
            if i not in visited:
                num += 1
                stack.append(i)
                visited.add(i)

                while len(stack) > 0:
                    a = stack.pop()
                    for j in range(0, n):
                        if j not in visited and isConnected[a][j] == 1:
                            stack.append(j)
                            visited.add(j)
        return num 


        
# @lc code=end

