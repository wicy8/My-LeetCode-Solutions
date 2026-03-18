from typing import List

class Solution:
    def closedIsland(self,grid:List[List[int]]) -> int:
        """
        思路：遍历grid，遇到0进行DFS搜索，如果遇不到边界，则为封闭岛
        """
        # ans=0
        # m=len(grid)
        # n=len(grid[0])
        # def dfs(i,j):
        #     if i == 0 or i == m - 1 or j == 0 or j == n - 1:
        #         a = 1
        #     else:
        #         a=0
        #     grid[i][j]=-1
        #     for x,y in [(i-1,j), (i+1,j), (i,j-1), (i,j+1)]:
        #         if 0<=x<m and 0<=y<n and grid[x][y]==0:
        #             a+=dfs(x,y)
        #     return a
        # for i in range(m):
        #     for j in range(n):
        #         if grid[i][j]==0:
        #             a=dfs(i,j)
        #             ans+=1 if a==0 else 0
        # return ans

        """
        思路：使用BFS
        """
        ans=0
        m=len(grid)
        n=len(grid[0])
        def bfs(i,j):
            q=[(i,j)]
            a=0
            while q:
                x,y=q.pop(0)
                grid[x][y]=-1
                if x == 0 or x == m - 1 or y == 0 or y == n - 1:
                    a+=1
                for dx,dy in [(x-1,y), (x+1,y), (x,y-1), (x,y+1)]:
                    if 0<=dx<m and 0<=dy<n and grid[dx][dy]==0:
                        q+=[(dx,dy)]
            return a
        for i in range(m):
            for j in range(n):
                if grid[i][j]==0:
                    a=bfs(i,j)
                    ans+=1 if a==0 else 0
        return ans

if __name__=="__main__":
    s=Solution()
    grid=[[1,1,1,1,1,1,1],
             [1,0,0,0,0,0,1],
             [1,0,1,1,1,0,1],
             [1,0,1,0,1,0,1],
             [1,0,1,1,1,0,1],
             [1,0,0,0,0,0,1],
             [1,1,1,1,1,1,1]]
    print(s.closedIsland(grid))