from typing import List

class Solution:
    def flipAndInvertImage(self,image:List[List[int]])->List[List[int]]:
        """
        思路：使用List[i]=List[i][-1:]进行翻转，
            然后使用List[i]=[1 for i in List[i] if i==0 else 1]
        """
        # m,n=len(image),len(image[0])
        # t=n//2
        # for i in range(m):
        #     for j in range(t):
        #         image[i][j],image[i][-j-1]=image[i][-j-1],image[i][j]
        #         image[i][j]=0 if image[i][j]==1 else 1
        #         image[i][-j-1] = 0 if image[i][-j-1] == 1 else 1
        #     if n%2==1:
        #         image[i][n//2]=0 if image[i][n//2]==1 else 1
        # return image

        for row in image:
            for j in range((len(row) + 1) // 2):
                if row[j] == row[-1 - j]:  # 采用Python化的符号索引
                    row[j] = row[-1 - j] = 1 - row[j]
        return image
if __name__=="__main__":
    s=Solution()
    image = [[1]]
    print(s.flipAndInvertImage(image))
