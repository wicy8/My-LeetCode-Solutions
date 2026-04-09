from typing import List

class Solution:
    def nearestExit(self,maze:List[List[str]],entrance:List[int])->int:
        """
        思路：使用BFS遍历maze，找到第一个exit，返回步数
        """
        m,n=len(maze),len(maze[0])
        i,j=entrance
        def bfs(i,j):
            q=[(i,j)]
            dis=[[-1]*n for _ in range(m)]
            dis[i][j]=0
            while q:
                x,y=q.pop(0)
                if maze[x][y]=="+":
                    continue
                if x==0 or x==m-1 or y==0 or y==n-1:
                    if x==i and y==j:
                        pass
                    else:
                        return dis[x][y]
                maze[x][y]="+"
                for dx,dy in [(x-1,y),(x+1,y),(x,y-1),(x,y+1)]:
                    if 0 <= dx < m and 0 <= dy < n and maze[dx][dy]==".":
                        dis[dx][dy]=dis[x][y]+1
                        q.append((dx,dy))
            return -1
        return bfs(i,j)

if __name__=="__main__":
    s=Solution()
    maze = [["+", "+", ".", "+"], [".", ".", ".", "+"], ["+", "+", "+", "."]]
    entrance = [1, 2]
    print(s.nearestExit(maze,entrance))