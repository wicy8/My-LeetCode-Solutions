class Solution:
    def reverseWords(self,s:str)->str:
        """
        思路：先统计第一个单词中的元音字符个数，
            往后遇到相同个数的单词就进行翻转。
        """
        yuan=['a','e','i','o','u']
        cnt=0
        i=0
        while i<len(s) and s[i]!=' ':
            if s[i] in yuan:
                cnt+=1
            i+=1
        def reverse(s,p,q):
            while p<q:
                s[p],s[q]=s[q],s[p]
                p+=1
                q-=1
        c=0
        i+=1
        p=i
        q=p
        s=list(s)
        while i<len(s):
            if s[i] in yuan:
                c+=1
            elif s[i]==' ':
                q=i-1
                if c==cnt:
                    reverse(s,p,q)
                p=i+1
                c=0
            i+=1
        if c==cnt:
            reverse(s,p,len(s)-1)
        return "".join(s)

if __name__=="__main__":
    so=Solution()
    s="book is nice"
    print(so.reverseWords(s))
