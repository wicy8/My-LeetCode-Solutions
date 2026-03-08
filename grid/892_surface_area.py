from typing import List


class Solution:
    def surfaceArea(self,grid: List[List[int]]) -> int:
        """
        思路：遍历grid，找到不为0的元素，进行DFS遍历，
            设表面积a=0，每个元素的表面积为4*v+2，
            相邻元素的表面积4*k+2,减去重叠表面积min(v,k)*2
        """
        # m=len(grid)
        # n=len(grid[0])
        # area=0
        # def dfs(i,j):
        #     a=0
        #     a+=grid[i][j]*4+2
        #     v=grid[i][j]
        #     grid[i][j]=-grid[i][j]
        #     for x,y in [(i-1,j), (i+1,j), (i,j-1), (i,j+1)]:
        #         if 0<=x<n and 0<=y<m and grid[x][y]!=0:
        #             a-=min(abs(grid[x][y]),v)
        #             if grid[x][y]>0:
        #                 a+=dfs(x,y)
        #     return a
        # for i in range(m):
        #     for j in range(n):
        #         if grid[i][j]>0:
        #             area+=dfs(i,j)
        # return area

        """
        思路：使用BFS
        """
        m, n = len(grid), len(grid[0])
        area = 0
        def bfs(i, j):
            q=[(i,j)]
            a=0
            while q:
                x,y = q.pop(0)
                if grid[x][y]>0:
                    a+=grid[x][y]*4+2
                    v=grid[x][y]
                    grid[x][y]=-1
                    for dx,dy in [(x-1,y),(x+1,y),(x,y-1),(x,y+1)]:
                        if 0<=dx<m and 0<=dy<n and grid[dx][dy]>0:
                            a-=min(v,grid[dx][dy])*2
                            q.append((dx,dy))
            return a

        for i in range(m):
            for j in range(n):
                if grid[i][j]>0:
                    area+=bfs(i,j)
        return area


if __name__ == '__main__':
    s = Solution()
    grid = [[1,2],[3,4]]
    print(s.surfaceArea(grid))