class Solution:
    def complexNumberMultiply(self,num1: str, num2: str) -> str:
        """
        思路：将复数和整数分开，倒着提取复数和整数，
            第一次遇到的数字串为复数f，并提取第一个正负号，
            第二次遇到的数字串为整数z，并提取下一个符号，若没有则不变号
            整数相乘,整数与复数交叉乘，然后相加，复数相乘，再变号，
            最后若整数为0，添加0，若复数小于0，则添加加号。
        """
        def transfer(num:str):
            z=0
            f=0
            flag=0
            k=0
            l=0
            if num[0]=='-':
                k=1
            for i in range(k,len(num)):
                if flag==0 and num[i].isdigit():
                    z=z*10+int(num[i])
                elif flag==0 and num[i]=='+':
                    flag=1
                elif flag==1 and num[i]=='-':
                    l=1
                elif flag==1 and num[i].isdigit():
                    f=f*10+int(num[i])
            z=-z if k==1 else z
            f=-f if l==1 else f
            return z,f
        a,b=transfer(num1)
        c,d=transfer(num2)
        zheng=a*c
        fu=a*d+c*b
        zheng-=b*d
        ans=""
        ans+=str(zheng)
        ans+="+"
        ans+=str(fu)+"i"
        return ans

if __name__ == '__main__':
    s = Solution()
    num1 = "78+-76i"
    num2 = "-86+72i"
    print(s.complexNumberMultiply(num1,num2))


