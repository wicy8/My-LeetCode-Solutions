from typing import List


class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        """
        思路：从初始点位，使用DFS遍历image，遇到与初始点位颜色相同的元素，
            进行修改，并与初始点位做相同的处理
        """
        # if image[sr][sc]==color:
        #     return image
        # m=len(image)
        # n=len(image[0])
        # fir=image[sr][sc]
        # def dfs(i,j):
        #     image[i][j]=color
        #     for x,y in [(i+1,j),(i-1,j),(i,j+1),(i,j-1)]:
        #         if 0<=x<m and 0<=y<n and image[x][y]==fir:
        #             dfs(x,y)
        # dfs(sr,sc)
        # return image

        """
        思路：使用BFS
        """
        if image[sr][sc]==color:
            return image
        m=len(image)
        n=len(image[0])
        fir=image[sr][sc]
        def bfs(i,j):
            q=[(i,j)]
            while q:
                x,y=q.pop(0)
                if 0<=x<m and 0<=y<n and image[x][y]==fir:
                    image[x][y]=color
                    q+=[(x+1,y),(x-1,y),(x,y+1),(x,y-1)]
        bfs(sr,sc)
        return image

if __name__ == '__main__':
    s = Solution()
    print(s.floodFill([[1,1,1],[1,1,0],[1,0,1]],1,1,2))