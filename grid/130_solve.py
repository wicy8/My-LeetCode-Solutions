from typing import List

class Solution:
    def solve(self,board:List[List[str]])-> None:
        """
        思路：遍历board找出O，对O进行DFS遍历，将board[i][j]=‘-’，如果遇到靠边缘的O，
            返回1，再从此点DFS遍历‘-’和‘O’，将其改为X
        思路2：使用BFS
        """
        # m=len(board)
        # n=len(board[0])
        # def dfs(i,j):
        #     if 0<=i<m and 0<=j<n and board[i][j]=='O':
        #         board[i][j]='A'
        #         dfs(i+1,j)
        #         dfs(i-1,j)
        #         dfs(i,j+1)
        #         dfs(i,j-1)
        # for i in range(m):
        #     dfs(i,0)
        #     dfs(i,n-1)
        # for i in range(n):
        #     dfs(0,i)
        #     dfs(m-1,i)
        # for i in range(m):
        #     for j in range(n):
        #         if board[i][j]=='O':
        #             board[i][j]='X'
        #         elif board[i][j]=='A':
        #             board[i][j]='O'

        m=len(board)
        n=len(board[0])
        def bfs(i,j):
            q=[(i,j)]
            while q:
                x,y=q.pop(0)
                if 0<=x<m and 0<=y<n and board[x][y]=='O':
                    board[x][y]='A'
                    q+=[(x+1,y),(x-1,y),(x,y+1),(x,y-1)]
        for i in range(m):
            bfs(i,0)
            bfs(i,n-1)
        for i in range(n):
            bfs(0,i)
            bfs(m-1,i)
        for i in range(m):
            for j in range(n):
                if board[i][j]=='O':
                    board[i][j]='X'
                elif board[i][j]=='A':
                    board[i][j]='O'

if __name__=="__main__":
    s=Solution()
    board = [["O","O","O"],["O","O","O"],["O","O","O"]]
    s.solve(board)
    print(board)
