from typing import List


class Solution:
    def spiralOrder(self,matrix: List[List[int]]) -> List[int]:
        """
        思路：m行n列矩阵，先向左走，到达边界右转90度，向下走，到达边界右转90度。。。。直到ans长度为m*n。
            方法一：
            对已访问过的元素，标记为空或无穷，防止重复访问。
            用DIRS=[(0,1),(1,0),(0,−1),(−1,0)]表示上下左右四个方向，用di表示当前方向，初始值为0，表示向右。
            每次移动，把行号增加DIRS[di][0],列号增加DIRS[di][1]。
            向右旋转表示di=(di+1)%4。
        """
        # m,n=len(matrix),len(matrix[0])
        # DIRS=[(0,1),(1,0),(0,-1),(-1,0)]
        # di=0
        # ans=[]
        # row,col=0,0
        # while len(ans)<m*n:
        #     ans.append(matrix[row][col])
        #     matrix[row][col]=None
        #     x,y=row+DIRS[di][0],col+DIRS[di][1]
        #     if x<0 or x>=m or y<0 or y>=n or matrix[x][y] is None:
        #         di=(di+1)%4
        #     row+=DIRS[di][0]
        #     col+=DIRS[di][1]
        # return ans

        """
        方法二：
            第一次向右走n步，第二次向下走m-1步，第三次向左走n-1步，第四次向上走m-2步。。。。
            第一步向右走n步，走到边界另n,m=m-1,n，下一次向下走n步（m-1），第三步向左走n步（n-1）。。。。
            则无需修改其他逻辑
        """
        ans=[]
        DIRS = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        di=0
        m,n=len(matrix),len(matrix[0])
        size=m*n
        row,col=0,-1
        while len(ans)<size:
            for _ in range(n):
                row += DIRS[di][0]
                col += DIRS[di][1]
                ans.append(matrix[row][col])
            di=(di+1)%4
            n, m = m - 1, n
        return ans

if __name__ == '__main__':
    s = Solution()
    print(s.spiralOrder([[1,2,3],[4,5,6],[7,8,9]]))