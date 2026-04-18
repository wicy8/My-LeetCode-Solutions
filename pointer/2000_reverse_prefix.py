class Solution:
    def reversePrefix(self,word:str,ch:str)->str:
        """
        思路：依次遍历word，找到ch的位置，设置首尾指针，
            p=0，q=ch的位置，依次交换pq的位置
        思路2：直接反转
        """
        # p=0
        # q=0
        # for i,w in enumerate(word):
        #     if w==ch:
        #         q=i
        #         break
        # word=list(word)
        # while p<q:
        #     word[p],word[q]=word[q],word[p]
        #     p+=1
        #     q-=1
        # return "".join(word)

        i=word.find(ch)+1
        return word[:i][::-1]+word[i:]

if __name__=="__main__":
    s=Solution()
    word = "abcdefd"
    ch = 'd'
    print(s.reversePrefix(word,ch))