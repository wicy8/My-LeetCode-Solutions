from itertools import product


class Solution:
    def multiply(self, num1:str, num2:str) -> str:
        """
        思路一：按照人类乘法习惯模拟，从最低位依次乘以最高位，并相加
        """
        if num1=="0" or num2=="0":
            return "0"
        ans = 0
        product=0
        n1 = len(num1)
        n2 = len(num2)
        # for i in range(n1):
        #     for j in range(n2):
        #         product += int(num1[i]) * int(num2[j])
        #         if j<n2-1:
        #             product*=10
        #     ans+=product
        #     product=0
        #     if i<n1-1:
        #         ans*=10

        """
        思路二：num1*num2的长度在n1+n2-1,n1+n2之间，定义一个长为n1+n2的数组arr，
            每次乘数放到数组中，num1[i]*num[j]的值放在arr[i+j+1]中，
            所有元素乘完将大于10的值都进位到[i+j]中。
        """
        arr=[0]*(n1+n2)
        for i in range(n1):
            for j in range(n2):
                arr[i+j+1]+=int(num1[i])*int(num2[j])
        for i in range(n1+n2-1,-1,-1):
            if arr[i]>=10:
                arr[i-1]+=arr[i]//10
                arr[i]%=10
        for i in range(n1+n2):
            ans+=arr[i]
            if i<n1+n2-1:
                ans*=10
        return str(ans)

if __name__ == '__main__':
    s = Solution()
    print(s.multiply("123","456"))