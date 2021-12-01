#
# @lc app=leetcode.cn id=207 lang=python3
#
# [207] 课程表
#

# @lc code=start
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = [[] for i in range(numCourses)]
        visited =  [0 for i in range(numCourses)]
        for x, y in prerequisites:
            graph[x].append(y)
        
        for i in range(numCourses):
            if self.dfs(graph, visited, i):
                return False
        return True
    
    def dfs(self, graph, visited, i):
        if visited[i] == -1:
            return True
        elif visited[i] == 1:
            return False
        else:
            visited[i] = -1
            for j in graph[i]:
                if self.dfs(graph, visited, j):
                    return True
            visited[i] = 1
            return False
        
# @lc code=end

