class Solution:
    def judgeCircle(self, moves: str) -> bool:
        """
        思路：设置两个计数器，分别记录纵轴和横轴，遇到左上加，遇到右下减，
            如果最后都等于0，则回到了原点
        """
        zong=0
        heng=0
        for m in moves:
            if m=='R':
                heng-=1
            elif m=='L':
                heng+=1
            elif m=='D':
                zong-=1
            elif m=='U':
                zong+=1
        return True if zong==0 and heng==0 else False

if __name__=="__main__":
    s=Solution()
    moves="LL"
    print(s.judgeCircle(moves))