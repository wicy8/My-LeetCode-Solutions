from collections import deque
from typing import List


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        """
        思路：遍历烂橘子的位置，添加到队列里，遍历好橘子的个数，
            记录每个好橘子相对烂橘子的最近距离，初始为-1，烂橘子为0
            使用BFS遍历好橘子并改为烂橘子，减去好橘子的个数，
            记录这个好橘子的距离为旁边烂橘子的距离+1，
            如果最后好橘子的个数大于0，则返回-1，否则返回最大的距离
        """
        m,n = len(grid), len(grid[0])
        dis=[[-1]*n for _ in range(m)]
        q=deque([])
        ans=0
        cnt=0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    q.append((i, j))
                    dis[i][j] = 0
                elif grid[i][j] == 1:
                    cnt+=1
        while q:
            i, j = q.popleft()
            for x,y in [(i-1,j), (i+1,j), (i,j-1), (i,j+1)]:
                if 0 <= x < m and 0 <= y < n and grid[x][y] == 1:
                    cnt-=1
                    dis[x][y] = dis[i][j] + 1
                    grid[x][y] = 2
                    q.append((x,y))
        for i in range(m):
            for j in range(n):
                ans=max(dis[i][j],ans) if dis[i][j]>0 else ans
        return ans if cnt==0 else -1

if __name__ == '__main__':
    s = Solution()
    print(s.orangesRotting([[2,1,1],[1,1,1],[1,1,2]]))
