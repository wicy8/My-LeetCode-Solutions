from typing import List


class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        """
        思路：定义一个数组DIRS=[(0,1),(1,0),(0,−1),(−1,0)]表示上下左右四个方向，用di表示当前方向，初始值为0，表示向右。
            初始位置为(0,-1),先移动一次，然后存入元素。第一次向右移动k次，第二次向下移动m(m=k-1)次，第三次向左移动k-1次，
            第四次向上移动m-1次，第五次向右移动k-2次......直到n*n次。
            每走完一次，另k,m=m-1,k，其他不变。
        """
        # DIRS = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        # di = 0
        # ans = [[0 for _ in range(n)] for _ in range(n)]
        # m = k = n
        # row = 0
        # col = -1
        # num = 1
        # while k > 0:
        #     for i in range(k):
        #         row += DIRS[di][0]
        #         col += DIRS[di][1]
        #         ans[row][col] = num
        #         num += 1
        #     di = (di + 1) % 4
        #     k, m = m - 1, k
        # return ans

        """
            思路二：当遇到边界或遇到ans[i][j]!=0时，转向
        """
        DIRS=[(0,1),(1,0),(0,-1),(-1,0)]
        di=0
        ans=[[0]*n for _ in range(n)]
        row=0
        col=0
        for v in range(1,n*n+1):
            ans[row][col]=v
            x,y=row+DIRS[di][0],col+DIRS[di][1]
            if x<0 or x>=n or y<0 or y>=n or ans[x][y]!=0:
                di=(di+1)%4
            row+=DIRS[di][0]
            col+=DIRS[di][1]
        return ans

if __name__ == '__main__':
    s = Solution()
    print(s.generateMatrix(3))