from typing import List


class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        """
        思路：遍历grid，遇到1则DFS搜索更多的陆地，每次遇到0或边界则周长加一。
        """
        # perimeter = 0
        # n = len(grid)
        # m = len(grid[0])
        # def dfs(i, j):
        #     p=0
        #     grid[i][j]=-1
        #     for x,y in [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]:
        #         if 0<=x<n and 0<=y<m:
        #             if grid[x][y] == 1:
        #                 p+=dfs(x,y)
        #             if grid[x][y]==0:
        #                 p+=1
        #         if x<0 or x>=n or y<0 or y>=m:
        #             p+=1
        #     return p
        #
        # for i in range(n):
        #     for j in range(m):
        #         if grid[i][j] == 1:
        #             perimeter+=dfs(i,j)
        # return perimeter


        """
        思路:方法同上，使用BFS
        """
        n = len(grid)
        m = len(grid[0])
        perimeter = 0
        def bfs(i, j):
            p=0
            q=[(i,j)]
            grid[i][j]=-1
            while q:
                x,y=q.pop(0)
                for dx,dy in [(x-1,y),(x+1,y),(x,y-1),(x,y+1)]:
                    if 0<=dx<n and 0<=dy<m:
                        if grid[dx][dy] == 1:
                            grid[dx][dy]=-1
                            q+=[(dx,dy)]
                        if grid[dx][dy]==0:
                            p+=1
                    if dx<0 or dx>=n or dy<0 or dy>=m:
                        p+=1
            return p
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    perimeter += bfs(i,j)
        return perimeter

if __name__ == '__main__':
    s = Solution()
    grid = [[1,1],[1,1]]
    print(s.islandPerimeter(grid))