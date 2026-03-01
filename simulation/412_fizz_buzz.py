from typing import List


class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        """
        思路：判断i+1是否是15的倍数，如果是则answer[i]=“fizzBuzz”；
            判断是否是3的倍数，如果是answer[i]=“fizz”；
            判断是否是5的倍数，如果是answer[i]=“Buzz”；
            最后如果不是3或5的倍数，则answer[i]=str(i+1)。
        """
        answer = []
        for i in range(1, n+1):
            if i % 15 == 0:
                answer.append('FizzBuzz')
                continue
            if i % 3 == 0:
                answer.append('Fizz')
                continue
            if i % 5 == 0:
                answer.append('Buzz')
                continue
            answer.append(str(i))
        return answer