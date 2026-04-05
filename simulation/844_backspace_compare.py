class Solution:
    def backspaceCompare(self,s:str,t:str)->bool:
        """
        思路：创建两个栈，分别记录s和t的字符，
            相等返回true
        思路2：使用双指针，从后往前一一对照，
            如果遇到#，记录跳过的字符数
        """
        # ss=[]
        # ts=[]
        # for v in s:
        #     if v=="#":
        #         if len(ss)>0:
        #             ss.pop()
        #     else:
        #         ss.append(v)
        # for c in t:
        #     if c=="#":
        #         if len(ts)>0:
        #             ts.pop()
        #     else:
        #         ts.append(c)
        # if ss==ts:
        #     return True
        # return False

        sp=len(s)-1
        tp=len(t)-1
        cnts=0
        cntt=0
        while sp>=0 or tp>=0:
            while sp>=0:
                if s[sp]=="#":
                    cnts+=1
                    sp-=1
                elif cnts>0:
                    sp-=1
                    cnts-=1
                else:
                    break
            while tp>=0:
                if t[tp]=="#":
                    cntt+=1
                    tp-=1
                elif cntt>0:
                    cntt-=1
                    tp-=1
                else:
                    break
            if tp>=0 and sp>=0:
                if s[sp]!=t[tp]:
                    return False
            elif tp>=0 or sp>=0:
                return False
            tp-=1
            sp-=1
        return True

if __name__=="__main__":
    s = "l#d##cm#z##nfto"
    t = "i#l#d##cmx##z##nfto"
    so=Solution()
    print(so.backspaceCompare(s,t))
