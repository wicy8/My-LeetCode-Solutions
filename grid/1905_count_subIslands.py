from typing import List

class Solution:
    def countSubIslands(self,grid1:List[List[int]],grid2:List[list[int]])->int:
        """
        思路1： 找到grid1中为0，但grid2中为1的地面，
            用DFS让这个岛屿上的元素都为0，
            然后遍历grid2中的1，找到岛屿的数量。
        思路2： 使用BFS
        """
        # m=len(grid1)
        # n=len(grid1[0])
        # ans=0
        # def dfs(i,j):
        #     grid2[i][j]=0
        #     for x,y in [(i-1,j), (i+1,j), (i,j-1), (i,j+1)]:
        #         if 0<=x<m and 0<=y<n and grid2[x][y]==1:
        #             dfs(x,y)
        #     return
        # for i in range(m):
        #     for j in range(n):
        #         if grid1[i][j]==0 and grid2[i][j]==1:
        #             dfs(i,j)
        # for i in range(m):
        #     for j in range(n):
        #         if grid2[i][j]==1:
        #             dfs(i,j)
        #             ans+=1
        # return ans

        m = len(grid1)
        n = len(grid1[0])
        ans = 0
        def bfs(i, j):
            q=[(i,j)]
            while q:
                x,y=q.pop(0)
                if 0<=x<m and 0<=y<n and grid2[x][y]==1:
                    grid2[x][y]=0
                else:
                    continue
                for dx,dy in [(x-1,y), (x+1,y), (x,y-1), (x,y+1)]:
                    q+=[(dx,dy)]
        for i in range(m):
            for j in range(n):
                if grid1[i][j] == 0 and grid2[i][j] == 1:
                    bfs(i, j)
        for i in range(m):
            for j in range(n):
                if grid2[i][j] == 1:
                    bfs(i, j)
                    ans += 1
        return ans

if __name__ =="__main__":
    s=Solution()
    grid1 = [[1,0,1,0,1],[1,1,1,1,1],[0,0,0,0,0],[1,1,1,1,1],[1,0,1,0,1]]
    grid2 = [[0,0,0,0,0],[1,1,1,1,1],[0,1,0,1,0],[0,1,0,1,0],[1,0,0,0,1]]
    print(s.countSubIslands(grid1,grid2))