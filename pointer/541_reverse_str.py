class Solution:
    def reverseStr(self,s:str,k:int)->str:
        """
        思路：设置首尾指针和记录指针，当到达p+k时，q=p+k，
            当len(s)<p+k时，q=len(s)-1
        思路2:分块，for循环每次走2*k步，每次反转前k个字符
        """
        # def reverse(s,p,q):
        #     while p<q:
        #         s[p],s[q]=s[q],s[p]
        #         p+=1
        #         q-=1
        # p=0
        # q=0
        # i=0
        # a=len(s)
        # ans=list(s)
        # while i<=a:
        #     if i==p+k and i<a:
        #         q=p+k-1
        #         reverse(ans,p,q)
        #         p=p+2*k
        #         if p>=a-1:
        #             break
        #     elif i==a and p<i:
        #         q=a-1
        #         reverse(ans,p,q)
        #         break
        #     i+=1
        # return "".join(ans)
        s=list(s)
        for i in range(0,len(s),2*k):
            s[i:i+k]=s[i:i+k][::-1]
        return "".join(s)

if __name__=="__main__":
    so=Solution()
    s = "abcdefg"
    k = 2
    print(so.reverseStr(s,k))