from typing import List


class Solution:
    def numIslands(self,grid: List[List[str]]) -> int:
        """
        思路一：依次遍历grid，找到第一个1，然后进行深度搜索DFS，把搜索到的1变为-1
            直到搜索完此区域，另ans+=1，然后继续遍历grid找到其他1，再进行DFS。。。
            直到遍历完grid，返回ans
        """
        # ans = 0
        # m, n = len(grid), len(grid[0])
        #
        # def dfs(i: int, j: int) -> int:
        #     if grid[i][j] != '1':
        #         return
        #     grid[i][j] = "-1"
        #     for x, y in (i, j - 1), (i, j + 1), (i - 1, j), (i + 1, j):
        #         if 0 <= x < m and 0 <= y < n and grid[x][y] == "1":
        #             dfs(x, y)
        #
        # for i, row in enumerate(grid):
        #     for j, num in enumerate(row):
        #         if num == '1':
        #             dfs(i, j)
        #             ans += 1
        # return ans

        """
        思路二：与思路一类似，但使用BFS进行搜索
        """
        ans=0
        m, n = len(grid), len(grid[0])
        def bfs(grid,i,j):
            queue = [(i,j)]
            while queue:
                i,j = queue.pop(0)
                if 0<=i<m and 0<=j<n and grid[i][j]=="1":
                    grid[i][j] = "-1"
                    queue+=[(i,j-1),(i,j+1),(i-1,j),(i+1,j)]

        for i, row in enumerate(grid):
            for j, num in enumerate(row):
                if num == '1':
                    bfs(grid,i, j)
                    ans += 1
        return ans

if __name__=='__main__':
    grid=[
        ['1', '1', '0', '0', '0'],
        ['1', '1', '0', '0', '0'],
        ['0', '0', '1', '0', '0'],
        ['0', '0', '0', '1', '1']
    ]
    s=Solution()
    print(s.numIslands(grid))

