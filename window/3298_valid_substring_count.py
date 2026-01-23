from collections import defaultdict


class Solution:
    def validSubstringCount(self, word1: str,word2: str) -> int:
        """
        题目：给你两个字符串 word1 和 word2 。
        如果一个字符串 x 重新排列后，word2 是重排字符串的前缀，那么我们称字符串 x 是 合法的 。
        请你返回 word1 中 合法子字符串的数目。
        思路：若x中的各元素个数大于等于word2的各元素个数，则x合法，统计word1中x的个数
        遍历word1，记录当前窗口中各元素个数，若满足条件，则缩小窗口，另ans+=1
        """
        ans=0
        left=0
        cnt=0
        a=defaultdict(int)
        b=defaultdict(int)
        for c in word2:
            b[c]+=1
        flag=len(b)
        for i,x in enumerate(word1):
            a[x]+=1
            if b[x]>0 and a[x]==b[x]:
                cnt+=1
            while cnt==flag:
                t=word1[left]
                a[t]-=1
                if a[t]<b[t]:
                    cnt-=1
                left+=1
            ans+=left
        return ans

if __name__=='__main__':
    word1 = "bcca"
    word2 = "abc"
    s=Solution()
    print(s.validSubstringCount(word1,word2))