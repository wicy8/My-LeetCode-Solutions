from typing import List

class Solution:
    def matrixReshape(self,mat:List[List[int]],r:int,c:int) -> List[List[int]]:
        """
        思路：如果m*n!=r*c,则返回mat数组。遍历mat，每存入c次，r+1
        """
        m = len(mat)
        n = len(mat[0])
        if r*c != m *n:
            return mat
        ans=[[0]*c for _ in range(r)]
        a,b=0,0
        for i in range(m):
            for j in range(n):
                if b==c:
                    b=0
                    a+=1
                ans[a][b]=mat[i][j]
                b+=1
        return ans

if __name__ == '__main__':
    s = Solution()
    mat = [[1, 2], [3, 4]]
    r = 2
    c = 4
    print(s.matrixReshape(mat,r,c))