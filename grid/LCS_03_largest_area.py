from typing import List


class Solution:
    def largestArea(self, grid: List[str]) -> int:
        """
        思路：遍历grid，遇到非0元素时进行DFS遍历，并记录相同元素面积，初始化flag=0，
            如果DFS过程中有元素处于边界或与0相邻，则记录flag+=1。
            如果flag=0，返回面积，否则返回0.
        """
        # n = len(grid)
        # m = len(grid[0])
        # t=[[0] * m for _ in range(n)]
        # ans=0
        # for i in range(n):
        #     for j in range(m):
        #         t[i][j]=int(grid[i][j])
        # def dfs(i, j):
        #     area=1
        #     flag=0
        #     if i==0 or i==n-1 or j==0 or j==m-1:
        #         flag=1
        #     p=t[i][j]
        #     t[i][j]=-1
        #     for x,y in [(i-1,j), (i+1,j), (i,j-1), (i,j+1)]:
        #         if 0<=x<n and 0<=y<m and t[x][y]==p:
        #             if x==0 or x==n-1 or y==0 or y==m-1:
        #                 flag+=1
        #             a,f=dfs(x,y)
        #             area += a
        #             flag += f
        #         if 0<=x<n and 0<=y<m and t[x][y]==0:
        #             flag+=1
        #     return area, flag
        #
        # for i in range(n):
        #     for j in range(m):
        #         if t[i][j]>0:
        #             area, flag = dfs(i, j)
        #             area=0 if flag!=0 else area
        #             ans=max(ans, area)
        # return ans

        """
        思路：使用BFS搜索，思路与DFS一样
        """
        n = len(grid)
        m = len(grid[0])
        g=[list(i) for i in grid]
        ans=0
        def bfs(i,j,g):
            q=[(i,j)]
            area=1
            p=g[i][j]
            g[i][j]='7'
            if i==0 or i==n-1 or j==0 or j==m-1:
                flag=1
            else:
                flag=0
            while q:
                x,y=q.pop(0)
                for dx,dy in [[x-1,y],[x+1,y],[x,y-1],[x,y+1]]:
                    if 0<=dx<n and 0<=dy<m and g[dx][dy]==p:
                        if dx==0 or dx==n-1 or dy==0 or dy==m-1:
                            flag=1
                        area+=1
                        g[dx][dy]='7'
                        q+=[(dx,dy)]
                    if 0<=dx<n and 0<=dy<m and g[dx][dy]=='0':
                        flag=1
            return area if flag==0 else 0

        for i in range(n):
            for j in range(m):
                if g[i][j]!='0' and g[i][j]!='7':
                    area= bfs(i, j,g)
                    ans=max(ans, area)
        return ans



if __name__ == '__main__':
    s = Solution()
    grid=["02520253","51551213","03512513","34312132","21051025","52005131","34235150","22154013"]
    print(s.largestArea(grid))
