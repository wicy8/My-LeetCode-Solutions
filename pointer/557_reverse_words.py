class Solution:
    def reverseWords(self,s:str)->str:
        """
        思路：设置首尾指针为0，尾指针遇到空格时,
            p,q-1之间进行翻转，p=q+1，q=p，
            当q=len(s)-1时，翻转p，q
        思路2:使用split进行切片，翻转每个单词
        """
        # p=q=0
        # n=len(s)
        # if n==1:
        #     return s
        # s=list(s)
        # def reverse(s,p,q):
        #     while p<q:
        #         s[p],s[q]=s[q],s[p]
        #         p+=1
        #         q-=1
        # while q<n:
        #     while s[q]!=' ' and q<n-1:
        #         q+=1
        #     if q==n-1:
        #         reverse(s,p,q)
        #         break
        #     elif s[q]==' ':
        #         reverse(s,p,q-1)
        #         p=q+1
        #         q=p
        # return "".join(s)

        return " ".join(word[::-1] for word in s.split(" "))

if __name__=="__main__":
    so=Solution()
    s = "Let's take LeetCode contest"
    print(so.reverseWords(s))
