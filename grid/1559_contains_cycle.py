from typing import List
import copy

from numpy.matlib import zeros


class Solution:
    def containsCycle(self,grid:List[List[str]])->bool:
        """
        思路：遍历grid，使用DFS搜索长度大于等于4且能回到起点的环
        """
        m,n=len(grid),len(grid[0])
        vis=[[0]*n for _ in range(m)]
        def dfs(i,j,k,l):
            if vis[i][j]==1:
                return True
            vis[i][j]=1
            for x,y in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
                if x==k and y==l:
                    continue
                if 0<=x<m and 0<=y<n and grid[x][y]==grid[i][j]:
                    if dfs(x,y,i,j):
                        return True
            return False
        for i in range(m):
            for j in range(n):
                if vis[i][j]==0 and dfs(i,j,-1,-1):
                    return True
        return False

if __name__=="__main__":
    s=Solution()
    grid = [["c","a","d"],["a","a","a"],["a","a","d"],["a","c","d"],["a","b","c"]]
    print(s.containsCycle(grid))
