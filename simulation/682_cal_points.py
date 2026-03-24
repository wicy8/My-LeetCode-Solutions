from typing import List

class Solution:
    def calPoints(self,operations:List[str])->int:
        """
        思路：遍历每个operations的元素，将前数字存放到列表中，
            遇到特殊字符则进行运算
        """
        ans=0
        l=[]
        for o in operations:
            if o.isdigit():
                l.append(int(o))
            elif o=='C':
                l=l[:-1]
            elif o=='D':
                l.append(l[-1]*2)
            elif o=='+':
                l.append(l[-1]+l[-2])
            else:
                l.append(int(o))
        for a in l:
            ans+=a
        return ans

if __name__ == "__main__":
    s=Solution()
    ops = ["1"]
    print(s.calPoints(ops))