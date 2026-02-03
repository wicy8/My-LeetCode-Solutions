from typing import List


class Solution:
    def countIslands(self, grid: List[List[int]],k: int) -> int:
        """
        思路：使用DFS，依次遍历grid，为陆地时，进行DFS，
            递归调用DFS，每次返回此陆地加上其探索到的陆地的价值
            对第一次调用DFS的陆地返回的价值模k，若为0则ans+=1
        """
        # ans = 0
        # m,n = len(grid), len(grid[0])
        # def dfs(i, j):
        #     v=grid[i][j]
        #     grid[i][j]=0
        #     for x,y in (i-1,j), (i+1,j), (i,j-1), (i,j+1):
        #         if 0<=x<m and 0<=y<n and grid[x][y]!=0:
        #             v+=dfs(x,y)
        #     return v
        #
        # for i in range(m):
        #     for j in range(n):
        #         if grid[i][j]!=0:
        #             f=dfs(i,j)
        #             if f%k==0:
        #                 ans+=1
        # return ans

        """
        思路：使用BFS，依次遍历grid，为陆地时，进行BFS，
            累加此次调用的价值，返回总价值，若模k得0，ans+=1
        """
        ans = 0
        m, n = len(grid), len(grid[0])
        def bfs(i, j):
            v=0
            q=[(i, j)]
            while q:
                x, y = q.pop(0)
                if 0<=x<m and 0<=y<n and grid[x][y]!=0:
                    v += grid[x][y]
                    grid[x][y] = 0
                    q+=[(x+1,y),(x-1,y),(x,y+1),(x,y-1)]
            return v

        for i in range(m):
            for j in range(n):
                if grid[i][j] != 0:
                    f=bfs(i, j)
                    if f%k==0:
                        ans+=1
        return ans

if __name__=='__main__':
    s = Solution()
    grid=[[0,0,0],[0,0,1],[11,0,6],[0,10,2],[0,0,0],[8,0,0]]
    k = 19
    print(s.countIslands(grid,k))