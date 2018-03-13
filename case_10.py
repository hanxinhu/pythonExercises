#已知列表fruits中顺序保存了某商店每日出售的水果品名，例如fruits=['apple','banana','cherry','pineapple','banana','peach','pear','peach','cherry']，完成函数solve()计算每一种水果的出售次数，存入字典result中并将结果返回
class Solution():
    def solve(self, A):
        B = {}
        for i in A:
            print(i)
            if i in B.keys():
                B[i] += 1
            else:
                B[i] = 1
        return B
        pass
S = Solution()
fruits=['apple','banana','cherry','pineapple','banana','peach','pear','peach','cherry']
B = S.solve(fruits)
print(B)