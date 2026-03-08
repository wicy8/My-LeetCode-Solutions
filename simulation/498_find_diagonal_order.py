from typing import List


class Solution:
    def findDiagonalOrder(self,mat: List[List[int]]) -> List[int]:
        """
        思路：从左下到右上，再到左下，再到右上，直至遍历完mat
            由（0,0）-（0,1）-（1,0）-（2,0）-（1,1,）-（0,2）
            每层对角线上的横坐标+纵坐标的和相等，x+y=i,i为层数
            y的范围为max(k-m+1,0),min(k,n-1)
        """
        m = len(mat)
        n = len(mat[0])
        ans=[]
        for k in range(m+n-1):
            min_j=max(k-m+1,0)
            max_j=min(k,n-1)
            if k%2==0:
                for j in range(min_j,max_j+1):
                    ans.append(mat[k-j][j])
            else:
                for j in range(max_j,min_j-1,-1):
                    ans.append(mat[k-j][j])
        return ans

if __name__ == '__main__':
    s = Solution()
    print(s.findDiagonalOrder([[1,2],[3,4]]))


