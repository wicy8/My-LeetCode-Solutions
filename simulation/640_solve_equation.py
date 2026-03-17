class Solution:
    def solveEquation(self, equation: str) -> str:
        """
        思路：遍历equation，分别对左右两边进行计算，遇到x记录它的系数，
            遇到数字进行计算，最后左边的x系数减去右边的x系数，右边的数字减去左边的数字，
            将数字除去x的系数，得到x的值
        """
        ans="x="
        x=0
        n=0
        a=0
        f=1
        z=1
        l=1
        for e in equation:
            if e=='x':
                a=f*a
                x+=z*a if a!=0 else z*f*l
                a=0
            elif e=='-':
                a=f*a
                n+=-z*a
                a=0
                f=-1
            elif e=='+':
                a=f*a
                n+=-z*a
                a=0
                f=1
            elif e=='=':
                a = f * a
                n += -z * a
                a=0
                z=-1
                f=1
            else:
                l=0 if a==0 and e=='0' else 1
                a=a*10+int(e)
        if equation[-1]=="x":
            x-=f*a
        else:
            n+=f*a
        if x==0 and n==0:
            return "Infinite solutions"
        elif x==0 or n%x!=0:
            return "No solution"
        else:
            return ans+str(n//x)

if __name__ == '__main__':
    s=Solution()
    equation="0x=0"
    print(s.solveEquation(equation))

