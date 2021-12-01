#
# @lc app=leetcode.cn id=210 lang=python3
#
# [210] 课程表 II
#

# @lc code=start
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = [[] for i in range(numCourses)]
        visited =  [0 for i in range(numCourses)]
        for x, y in prerequisites:
            graph[x].append(y)
        
        res = []
        for i in range(numCourses):
            if self.dfs(graph, visited, i, res):
                return []
        return res
    
    def dfs(self, graph, visited, i, res):
        if visited[i] == -1:
            return True
        elif visited[i] == 1:
            return False
        else:
            visited[i] = -1
            for j in graph[i]:
                if self.dfs(graph, visited, j, res):
                    return True
            visited[i] = 1
            res.append(i)
            return False
# @lc code=end

