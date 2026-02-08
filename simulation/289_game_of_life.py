from typing import List


class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        思路：定义一个新数组flag记录需要修改的位置（x，y），依次遍历board，
            将需要修改的元素记录到flag中，最后再更新一次board。
        """
        # margin=[(-1, 0), (1, 0), (0, -1), (0, 1),(1,1),(-1,1),(1,-1),(-1,-1)]
        # flag=[]
        # m, n = len(board), len(board[0])
        # for i in range(m):
        #     for j in range(n):
        #         cnt=0
        #         for x,y in margin:
        #             if 0<=i+x<m and 0<=j+y<n and board[i+x][j+y]==1:
        #                 cnt+=1
        #         if cnt<2 and board[i][j]==1:
        #             flag.append((i,j))
        #         elif cnt>3 and board[i][j]==1:
        #             flag.append((i,j))
        #         elif cnt==3 and board[i][j]==0:
        #             flag.append((i,j))
        # for x,y in flag:
        #     if board[x][y]==0:
        #         board[x][y]=1
        #     else:
        #         board[x][y]=0

        """
        思路：修改需要修改为1的位置为-1，需要修改为0的地方为-2，
            当周围有1或-2时，都判定为1。
            遍历结束后将board中的-1和-2改为1和0。
        """
        margin = [(-1, 0), (1, 0), (0, -1), (0, 1), (1, 1), (-1, 1), (1, -1), (-1, -1)]
        m,n = len(board), len(board[0])
        for i in range(m):
            for j in range(n):
                cnt=0
                for x,y in margin:
                    if 0<=i+x<m and 0<=j+y<n and (board[i+x][j+y]==1 or board[i+x][j+y]==-2):
                        cnt+=1
                if (cnt<2 or cnt>3) and board[i][j]==1:
                    board[i][j]=-2
                elif cnt==3 and board[i][j]==0:
                    board[i][j]=-1
        for i in range(m):
            for j in range(n):
                if board[i][j]==-1:
                    board[i][j]=1
                elif board[i][j]==-2:
                    board[i][j]=0


if __name__ == '__main__':
    s = Solution()
    board= [[0,1,0],[0,0,1],[1,1,1],[0,0,0]]
    s.gameOfLife(board)
    print(board)