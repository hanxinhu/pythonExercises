#已知有一个由数字字符串构成的列表，统计列表中数字字符'0'-'9'各自出现的次数并返回统计结果
#-*- coding:utf-8 -*-

class Solution():
    def solve(self, A):
        B = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0
             , 5: 0, 6: 0, 7: 0, 8: 0, 9: 0}
        for i in A:
            for c in i:
                B[int(c)] += 1
        return B
        pass



B = "1211213"
S = Solution()
B = S.solve(B)
print(B)