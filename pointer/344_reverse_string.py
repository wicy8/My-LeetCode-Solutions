from typing import List

class Solution:
    def reverseString(self,s:List[str])->None:
        """
        思路：使用首尾双指针交换元素
        """
        if len(s)<=1:
            return
        p=0
        q=len(s)-1
        while p<q:
            s[p],s[q]=s[q],s[p]
            p+=1
            q-=1
        return


if __name__ == "__main__":
    so=Solution()
    s = ["h", "e", "l", "l", "o"]
    so.reverseString(s)
    print(s)