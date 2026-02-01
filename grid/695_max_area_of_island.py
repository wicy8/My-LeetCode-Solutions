from typing import List


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        """
        思路一：使用DFS策略，依次遍历每个岛屿，记录最大值
        """
        # maxArea = 0
        # m, n = len(grid), len(grid[0])
        # def dfs(i,j,grid):
        #     area=1
        #     grid[i][j] = 0
        #     for x,y in (i, j - 1), (i, j + 1), (i - 1, j), (i + 1, j):
        #         if 0<=x<m and 0<=y<n and grid[x][y]==1:
        #             area+=dfs(x,y,grid)
        #     return area
        #
        # for i in range(m):
        #     for j in range(n):
        #         if grid[i][j]==1:
        #             maxArea=max(dfs(i,j,grid), maxArea)
        # return maxArea

        """
        思路二：使用BFS策略，遍历每个岛屿，记录最大值
        """
        maxArea = 0
        m, n = len(grid), len(grid[0])
        def bfs(i, j,grid):
            area=0
            q=[(i,j)]
            while q:
                i,j = q.pop(0)
                if 0<=i<m and 0<=j<n and grid[i][j]==1:
                    grid[i][j]=-1
                    area += 1
                    q+=[(i+1,j),(i-1,j),(i,j+1),(i,j-1)]
            return area

        for i in range(m):
            for j in range(n):
                if grid[i][j]==1:
                    maxArea=max(bfs(i,j,grid), maxArea)
        return maxArea


if __name__ == '__main__':
    grid = [[0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
            [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
            [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0]]
    s = Solution()
    print(s.maxAreaOfIsland(grid))

