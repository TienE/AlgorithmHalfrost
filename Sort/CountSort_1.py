class CountSort:
    countdict = {}

    def __init__(self):
        pass

    def sortBegain(self, Array, n):
        # 0~n 左闭右开 n 不包含
        # 内容必须 > -1
        for i in Array:
            self.countdict[i] = self.countdict.get(i, 0) + 1
        
        # 输出结果
        index = 0
        for i in range(0, n):
            i_nums = self.countdict.get(i, 0)
            if i_nums > 0:
                for x in range(0, i_nums):
                    Array[index] = i
                    index += 1

a = [6,3,8,2,6,2]
print(a)

cs = CountSort()
cs.sortBegain(a, 9)

print(a)
