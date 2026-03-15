import math

class Solution:
    def fractionAddition(self,expression: str) -> str:
        """
        思路：将字符串中的数提取到栈中，前两个数的分子和分母分离，分母相乘，
            分子乘对方的分母，分子相加，最后约分，结果放回栈中，直到栈中仅剩一个数
        """
        q=[]
        j=0
        for i in range(0,len(expression)):
            if expression[i]=='-':
                if j!=i:
                    q.append(expression[j:i])
                j=i
            elif expression[i]=='+':
                if j!=i:
                    q.append(expression[j:i])
                j=i+1
        q.append(expression[j:])
        n=len(q)
        def getm(num):
            f=0# 是否为负数
            z=0# 分子的大小
            t=0# 是否遇到了‘/’
            m=0# 分母的大小
            for i in range(0,len(num)):
                if i==0 and num[i]=='-':
                    f=1
                elif t==0 and num[i].isdigit():
                    z=z*10+int(num[i])
                elif num[i]=='/':
                    t=1
                elif t==1 and num[i].isdigit():
                    m=m*10+int(num[i])
            z=-z if f==1 else z
            return z,m
        for _ in range(0,n-1):
            x=q.pop(0)
            y=q.pop(0)
            xz,xm=getm(x)
            yz,ym=getm(y)
            if xm==ym:
                z=xz+yz
            else:
                z=xz*ym+yz*xm
                xm=xm*ym
            s=str(z)+'/'+str(xm)
            q.append(s)
        z,m=getm(q.pop(0))
        if z%m==0:
            z=z//m
            m=1
        elif m%z==0:
            m=m//abs(z)
            z=z//abs(z)
        else:
            yue=1
            for i in range(2,max(abs(z),m)//2):
                if z%i==0 and m%i==0:
                    yue=i
            if yue!=1:
                z=z//yue
                m=m//yue
        s = str(z) + '/' + str(m)
        q.append(s)
        return q.pop(0)

if __name__ == '__main__':
    s = Solution()
    expression ="-1/6+2/9+3/7-5/9+3/10"
    print(s.fractionAddition(expression))
