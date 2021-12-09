#
# @lc app=leetcode.cn id=733 lang=python3
#
# [733] 图像渲染
#

# @lc code=start
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        if image[sr][sc] == newColor: return image
        old = image[sr][sc]
        stack = [[sr, sc]]
        m, n = len(image), len(image[0])
        while stack:
            r, c = stack.pop()
            image[r][c] = newColor
            if 0 <= r - 1 < m and 0 <= c < n and image[r - 1][c] == old:
                stack.append([r-1, c])
            if 0 <= r + 1 < m and 0 <= c < n and image[r + 1][c] == old:
                stack.append([r+1, c])
            if 0 <= r < m and 0 <= c - 1 < n and image[r][c - 1] == old:
                stack.append([r, c-1])
            if 0 <= r < m and 0 <= c + 1 < n and image[r][c + 1] == old:
                stack.append([r, c+1])
        return image
# @lc code=end

