class Solution:
    def reverseByType(self,s:str)->str:
        """
        思路：先设置首尾指针，反转字母
            再重置首尾指针，反转特殊字符
        """
        if len(s)<=1:
            return s
        p=0
        q=len(s)-1
        ans=list(s)
        while p<q:
            while p<q and not s[p].isalpha():
                p+=1
            while p<q and not s[q].isalpha():
                q-=1
            if p >= q:
                break
            ans[p],ans[q]=s[q],s[p]
            p+=1
            q-=1
        p=0
        q=len(s)-1
        while p<q:
            while p<q and s[p].isalpha():
                p+=1
            while p<q and s[q].isalpha():
                q-=1
            if p >= q:
                break
            ans[p],ans[q]=s[q],s[p]
            p+=1
            q-=1
        return "".join(ans)

if __name__=="__main__":
    so=Solution()
    s=")ebc#da@f("
    print(so.reverseByType(s))
