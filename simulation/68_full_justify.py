from typing import List


class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        """
        思路：累加words[i]+1的长度l,l再-1，若l>maxWidth，则累加到第i-1个字符，此时l<=maxWidth，
            在此行加入maxWidth-l=k个空格，依次在第i个单词后加入k//(i-j-1)+k%(i-j-1)个空格，j为此行第一个单词。
            对于最后一行，if i == len(words)-1 即最后一个单词,则退出循环，跳出添加空格的判断，
            单独对最后一行做填充。
        """
        ans=[]
        n = len(words)
        cnt = 0  # 此行总长度
        num = 0  # 此行单词个数
        for i,w in enumerate(words):
            cnt+=len(w)+1
            num+=1
            if cnt>maxWidth+1:#非最后一行
                cnt-=len(w)+2
                num-=1
                k = maxWidth - cnt
                temp = ""
                if num>1:
                    m=k%(num-1)
                    k//=num-1
                    for j in range(i-num,i):
                        if m>0:
                            temp+=words[j]
                            temp+=" " * (k+2)
                            m-=1
                        else:
                            temp+=words[j]
                            if j!=i-1:
                                temp+=" " * (k+1)
                else:
                    temp+=words[i-num]
                    temp+=" " * (maxWidth-len(temp))
                ans.append(temp)
                cnt=len(w)+1
                num=1
        if cnt>0 and num>0:
            temp=""
            for j in range(n-num,n):
                temp+=words[j]
                if j!=n-1:
                    temp+=" "
            temp+=" "*(maxWidth-len(temp))
            ans.append(temp)
        return ans




if __name__ == '__main__':
    s = Solution()
    words = ["Science","is","what","we","understand","well","enough","to","explain","to","a","computer.","Art","is","everything","else","we","do"]
    maxWidth = 20
    print(s.fullJustify(words, maxWidth))