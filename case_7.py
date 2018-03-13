#完成函数solve，判断传入的整数列表A中的数字是否是素数，并将所有的素数保存到另一个列表中并返回
# -*- coding:utf-8 -*-

class Solution():
    def solve(self, A):
        # call function prime
        B = []
        for i in A:
            if (self.prime(i)):
                B.append(i)
        return B
        pass

    # judge whether x is prime or not
    def prime(self, x):
        if (x <= 1):
            return False
        if (x == 2):
            return True
        for i in range(2, x):
            if (x % i == 0):
                return False
        return True
        pass
