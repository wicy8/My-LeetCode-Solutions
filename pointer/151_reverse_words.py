class Solution:
    def reverseWords(self,s:str)->str:
        """
        思路1：直接从s末尾查找不是空格的字符，
            保存单词末尾指针，查找空格，
            将空格到单词末尾的字符串添加到新数组中去，
            循环到s开头。
        思路2：先处理掉多余空格
            整体进行翻转，然后根据空格翻转单词
        思路3：使用切片方法进行翻转
        """
        # s=list(s)
        # i=0
        # if s[0]==' ':
        #     while i<len(s) and s[i]==' ':
        #         i+=1
        # s=s[i:]
        # i=len(s)-1
        # if s[-1]==' ':
        #     while i>0 and s[i]==' ':
        #         i-=1
        # s=s[:i+1]
        # cnt=0
        # i=0
        # while i<len(s):
        #     if s[i]==' ':
        #         cnt+=1
        #     else:
        #         if cnt > 1:
        #             s = s[:i-cnt+1] + s[i:]
        #             i-=cnt-1
        #         cnt=0
        #     i+=1
        # s="".join(s)
        # return " ".join(word[::-1] for word in s[::-1].split(' '))
        # return " ".join(word[::-1] for word in s[::-1].split())
        return " ".join(reversed(s.split()))

if __name__=="__main__":
    so=Solution()
    s="F R  I   E    N     D      S      "
    print(so.reverseWords(s))