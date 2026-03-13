from typing import List

class Solution:
    def numEnclaves(self,grid: List[List[int]])->int:
        """
        思路：遍历grid，遇到1时进行DFS遍历，如果这个岛屿与边界相连，
            则返回岛屿面积，否则返回0，最终返回所有岛屿面积的总和。
        """
        # m = len(grid)
        # n = len(grid[0])
        # ans=0
        # def dfs(i,j):
        #     if i==0 or i==m-1 or j==0 or j==n-1:
        #         a=-250001
        #     else:
        #         a=1
        #     grid[i][j]=-1
        #     for x,y in [(i-1,j),(i+1,j),(i,j-1),(i,j+1)]:
        #         if 0<=x<m and 0<=y<n and grid[x][y]==1:
        #             a+=dfs(x,y)
        #     return a
        # for i in range(m):
        #     for j in range(n):
        #         if grid[i][j] == 1:
        #             area=dfs(i,j)
        #             ans+=area if area>0 else 0
        # return ans

        """
        思路：使用BFS
        """
        m = len(grid)
        n = len(grid[0])
        ans=0
        def bfs(i,j):
            q=[(i,j)]
            a=0
            while q:
                x,y=q.pop(0)
                if grid[x][y]!=1:
                    continue
                if x==0 or x==m-1 or y==0 or y==n-1:
                    a=-250001
                else:
                    a+=1
                grid[x][y]=-1
                for dx,dy in [(x-1,y), (x+1,y), (x,y-1), (x,y+1)]:
                    if 0<=dx<m and 0<=dy<n and grid[dx][dy]==1:
                        q+=[(dx,dy)]
            return a
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    area= bfs(i,j)
                    ans += area if area>0 else 0
        return ans

if __name__ == '__main__':
    s = Solution()
    grid=[[0,0,0,1,1,1,0,1,1,1,1,1,0,0,0],[1,1,1,1,0,0,0,1,1,0,0,0,1,1,1],[1,1,1,0,0,1,0,1,1,1,0,0,0,1,1],[1,1,0,1,0,1,1,0,0,0,1,1,0,1,0],[1,1,1,1,0,0,0,1,1,1,0,0,0,1,1],[1,0,1,1,0,0,1,1,1,1,1,1,0,0,0],[0,1,0,0,1,1,1,1,0,0,1,1,1,0,0],[0,0,1,0,0,0,0,1,1,0,0,1,0,0,0],[1,0,1,0,0,1,0,0,0,0,0,0,1,0,1],[1,1,1,0,1,0,1,0,1,1,1,0,0,1,0]]
    print(s.numEnclaves(grid))