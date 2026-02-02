class Solution:
    def addBinary(self, a: str, b: str) -> str:
        """
        思路：定义一个数组记录答案，两二进制字符串的第i位转换为整数相加，
            结果模2并转换为字符串放在第i位，将结果整除2进位到i-1位
        """
        # ans = ""
        # m, n = len(a), len(b)
        # l = max(m, n)
        # add = [0] * (l + 1)
        # up = 0
        # for i in range(1, l + 2):
        #     if m - i >= 0 and n - i >= 0:
        #         add[l - i+1] = int(a[m - i]) + int(b[n - i]) + up
        #     elif m - i >= 0:
        #         add[l - i+1] = int(a[m - i]) + up
        #     elif n - i >= 0:
        #         add[l - i+1] = int(b[n - i]) + up
        #     else:
        #         add[l - i+1] = up
        #     up = add[l - i+1] // 2
        #     add[l - i+1] = add[l - i+1] % 2
        # if add[0] == 1:
        #     ans += str(add[0])
        # for i in range(1, l + 1):
        #     ans += str(add[i])
        # return ans


        """
        思路：对a和b做反转，定义ans=[]，ans[i]=a[i]+b[i],
            对ans[i]求模，除2，得到进位。最后返回“”.join(ans)[::-1]
        """
        ans=[]
        a=a[::-1]
        b=b[::-1]
        m,n=len(a),len(b)
        l=max(m,n)
        carry=0
        for i in range(l):
            carry+=int(a[i]) if i <m else 0
            carry+=int(b[i]) if i <n else 0
            ans.append(str(carry%2))
            carry //= 2
        if carry:
            ans.append(str(carry%2))
        return ''.join(ans)[::-1]

if __name__=='__main__':
    s=Solution()
    print(s.addBinary("11","1"))