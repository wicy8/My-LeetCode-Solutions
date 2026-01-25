from collections import defaultdict


class Solution:
    def sumOfSubarrays(self, word: str, k: int) -> int:
        """
        题目：给你一个字符串 word 和一个 非负 整数 k。
            返回 word 的 子字符串中，每个元音字母（'a'、'e'、'i'、'o'、'u'）至少 出现一次，
            并且 恰好 包含 k 个辅音字母的子字符串的总数。
        思路：遍历word，统计元音字母是否都至少有一个，辅音字母包含k个以上的子字符串个数，
            减去辅音字母包含k+1个以上的子字符串个数
        """
        ans=0
        cntf1=cntf2=0#辅音字母
        yuan=['a','e','i','o','u']
        y1=defaultdict(int)
        y2=defaultdict(int)
        l1=l2=0
        for i,x in enumerate(word):
            if x in yuan:
                y1[x]+=1
                y2[x]+=1
            else:
                cntf1+=1
                cntf2+=1
            while len(y1)==5 and cntf1>=k:
                if word[l1] in y1:
                    y1[word[l1]]-=1
                    if y1[word[l1]]==0:
                        del y1[word[l1]]
                else:
                    cntf1-=1
                l1+=1
            while len(y2)==5 and cntf2>k:
                if word[l2] in y2:
                    y2[word[l2]]-=1
                    if y2[word[l2]]==0:
                        del y2[word[l2]]
                else:
                    cntf2-=1
                l2+=1
            ans+=l1-l2
        return ans

if __name__=='__main__':
    s = Solution()
    print(s.sumOfSubarrays("ieaouqqieaouqq",1))