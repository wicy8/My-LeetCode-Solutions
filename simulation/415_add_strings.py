class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        """
        思路：将字符串求逆逐个相加到数组中，再翻转回来
        """
        s=min(len(num1), len(num2))
        l=max(len(num1), len(num2))
        ans = []
        num1="".join(reversed(num1))
        num2="".join(reversed(num2))
        p=0
        for i in range(s):
            t=(int(num1[i])+int(num2[i]))+p
            if t>9:
                t=t%10
                p=1
            else:
                p=0
            ans.append(str(t))
        for i in range(s,l):
            if len(num1)>len(num2):
                t=int(num1[i])+p
            else:
                t=int(num2[i])+p
            if t>9:
                t=t%10
                p=1
            else:
                p=0
            ans.append(str(t))
        if p==1:
            ans.append("1")
        res="".join(reversed(ans))
        return res

if __name__ == '__main__':
    s = Solution()
    print(s.addStrings("11","123"))
