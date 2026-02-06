from typing import List


class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        """
        思路：使用DFS搜索，遍历grid，如果有鱼，则进行搜索，累加鱼数
        """
        # ans=0
        # m,n=len(grid),len(grid[0])
        # def dfs(i,j):
        #     v=grid[i][j]
        #     grid[i][j]=0
        #     for x,y in [(i+1,j),(i-1,j),(i,j-1),(i,j+1)]:
        #         if 0<=x<m and 0<=y<n and grid[x][y]!=0:
        #             v+=dfs(x,y)
        #     return v
        #
        # for i in range(m):
        #     for j in range(n):
        #         if grid[i][j]!=0:
        #             ans=max(ans, dfs(i,j))
        #
        # return ans

        """
        思路：使用BFS搜索，遍历grid，如果有鱼，则进行搜索，累加鱼数
        """
        ans=0
        m,n=len(grid),len(grid[0])
        def bfs(i,j):
            v=0
            q=[(i,j)]
            while q:
                x,y=q.pop(0)
                if 0<=x<m and 0<=y<n and grid[x][y]:
                    v += grid[x][y]
                    grid[x][y] = 0
                    q+=[(x+1,y),(x-1,y),(x,y+1),(x,y-1)]
            return v

        for i in range(m):
            for j in range(n):
                if grid[i][j]:
                    ans = max(ans, bfs(i,j))

        return ans

if __name__=='__main__':
    s=Solution()
    grid=[[0,2,1,0],[4,0,0,3],[1,0,0,4],[0,3,2,0]]
    print(s.findMaxFish(grid))