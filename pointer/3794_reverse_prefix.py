class Solution:
    def reversePrefix(self,s:str,k:int)->str:
        """
        思路：首尾指针分别指向首元素和第k个元素，进行交换，
            直到首指针大于等于尾指针
        """
        p=0
        q=k-1
        s=list(s)
        while p<q:
            s[p],s[q]=s[q],s[p]
            p+=1
            q-=1
        return "".join(s)

if __name__=="__main__":
    so=Solution()
    s = "abcd"
    k = 2
    print(so.reversePrefix(s,k))