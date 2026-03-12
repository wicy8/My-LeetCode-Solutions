from typing import List
class Solution:
    def colorBorder(self, grid: List[List[int]], row: int, col: int, color: int) -> List[List[int]]:
        """
        思路：对grid[row][col]进行DFS遍历，如果grid[row][col]==color，则直接返回grid，
            否则，遍历过程中将值改为负数，如果在边界上，则修改为0，遍历后将负数改为正数,0修改为color。
        """
        # if grid[row][col]==color:
        #     return grid
        # m = len(grid)
        # n = len(grid[0])
        # def dfs(i,j):
        #     v=grid[i][j]
        #     grid[i][j]=-grid[i][j]
        #     for x,y in [(i+1,j),(i-1,j),(i,j+1),(i,j-1)]:
        #         if 0<=x<m and 0<=y<n and grid[x][y]==v:
        #             dfs(x,y)
        #         elif 0<=x<m and 0<=y<n and (grid[x][y]==0 or grid[x][y]==-v):
        #             pass
        #         else:
        #             grid[i][j]=0
        # dfs(row,col)
        # for i in range(m):
        #     for j in range(n):
        #         if grid[i][j]<0:
        #             grid[i][j]=-grid[i][j]
        #         elif grid[i][j]==0:
        #             grid[i][j]=color
        #
        # return grid

        """
        思路：使用BFS
        """
        if grid[row][col] == color:
            return grid
        m, n = len(grid), len(grid[0])
        def bfs(i,j):
            q=[(i,j)]
            v = grid[i][j]
            while q:
                x,y=q.pop(0)
                if grid[x][y]!=v:
                    continue
                grid[x][y]=-grid[x][y]
                for dx, dy in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]:
                    if 0<=dx<m and 0<=dy<n and grid[dx][dy]==v:
                        q+=[(dx, dy)]
                    elif 0<=dx<m and 0<=dy<n and (grid[dx][dy]==0 or grid[dx][dy]==-v):
                        pass
                    else:
                        grid[x][y]=0
        bfs(row,col)
        for i in range(m):
            for j in range(n):
                if grid[i][j]<0:
                    grid[i][j]=-grid[i][j]
                elif grid[i][j]==0:
                    grid[i][j]=color

        return grid

if __name__ == '__main__':
    s = Solution()
    grid=[[1,1,1],[1,1,1],[1,1,1]]
    row=1
    col=1
    color=2
    print(s.colorBorder(grid,row,col,color))