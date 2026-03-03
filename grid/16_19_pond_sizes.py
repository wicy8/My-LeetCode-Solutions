from typing import List


class Solution:
    def pondSizes(self, land: List[List[int]]) -> List[int]:
        """
        思路1：遍历land，遇到0则使用DFS遍历此元素，判断八个方向是否为0，
            为0则面积加1，结束返回面积，添加到数组中
        """
        # n = len(land)
        # m = len(land[0])
        # ans=[]
        # def dfs(i, j, land):
        #     size=0
        #     land[i][j] = -1
        #     for x, y in ((i-1,j-1),(i-1,j),(i-1,j+1),(i,j-1),(i,j),(i,j+1),(i+1,j-1),(i+1,j),(i+1,j+1)):
        #         if 0<=x<n and 0<=y<m and land[x][y]==0:
        #             size+=dfs(x,y,land)
        #     return size + 1
        #
        # for i in range(n):
        #     for j in range(m):
        #         if land[i][j] == 0:
        #             ans.append(dfs(i,j,land))
        #
        # return sorted(ans)

        """
        思路2：遍历land，遇到0则使用BFS遍历此元素，判断八个方向是否为0，
            为0则面积加1，结束返回面积，添加到数组中
        """
        n = len(land)
        m = len(land[0])
        ans=[]
        def bfs(i,j,land):
            size=0
            q=[(i,j)]
            while q:
                x,y=q.pop(0)
                if 0 <= x < n and 0 <= y < m and land[x][y] == 0:
                    size+=1
                    land[x][y]=-1
                    q+=[(x-1,y-1),(x-1,y),(x-1,y+1),(x,y-1),(x,y),(x,y+1),(x+1,y-1),(x+1,y),(x+1,y+1)]
            return size

        for i in range(n):
            for j in range(m):
                if land[i][j] == 0:
                    ans.append(bfs(i,j,land))

        return sorted(ans)

if __name__ == '__main__':
    s = Solution()
    land=[
      [0,2,1,0],
      [0,1,0,1],
      [1,1,0,1],
      [0,1,0,1]
    ]
    print(s.pondSizes(land))