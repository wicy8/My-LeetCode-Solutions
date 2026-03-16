from typing import List

class Solution:
    def maxMoves(self,grid: List[List[int]]) -> int:
        """
        思路：遍历grid的第一列，对其使用DFS向右遍历，并记录DFS次数，
            如果没有严格小于右侧的元素则退出。
        """
        # ans=0
        # m=len(grid)
        # n=len(grid[0])
        # def dfs(i,j):
        #     times=0
        #     v=grid[i][j]
        #     grid[i][j]=0
        #     for x in range(max(i-1,0),min(i+2,m)):
        #         if j+1<n and v<grid[x][j+1]:
        #             times=max(times,dfs(x,j+1))
        #     return times+1
        # for i in range(m):
        #     ans=max(ans,dfs(i,0)-1)
        #     if ans == n - 1:
        #         break
        # return ans

        """
        思路：使用BFS
        """
        ans=0
        m=len(grid)
        n=len(grid[0])
        def bfs(i,j):
            times=0
            q=[(i,j)]
            while q:
                x,y=q.pop(0)
                v=grid[x][y]
                if v==0:
                    continue
                times=max(times,y+1)
                grid[x][y]=0
                for dx,dy in [(x-1,y+1),(x,y+1),(x+1,y+1)]:
                    if 0<=dx<m and 0<=dy<n and grid[dx][dy]>v:
                        q+=[(dx,dy)]
                if times==n:
                    break
            return times
        for i in range(m):
            ans=max(ans,bfs(i,0)-1)
            if ans==n-1:
                break
        return ans

if __name__ == '__main__':
    s = Solution()
    grid = [[187,167,209,251,152,236,263,128,135],[267,249,251,285,73,204,70,207,74],[189,159,235,66,84,89,153,111,189],[120,81,210,7,2,231,92,128,218],[193,131,244,293,284,175,226,205,245]]
    print(s.maxMoves(grid))

