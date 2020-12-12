class BinarySearch:
    x = int()
    res = []

    def __init__(self):
        pass

    def BSBegin(self, Array, x):
        self.x = x
        self.recursionSearch(Array, 0, len(Array)-1)
        self.printResult()

    def recursionSearch(self, Array, low, high):
        if low <= high:
            mid = int((low + high)/2)
            if Array[mid] == self.x:
                self.res.append(mid)
            else:
                self.recursionSearch(Array, low, mid-1)
                self.recursionSearch(Array, mid+1, high)

    def printResult(self):
        if len(self.res) > 0:
            print(self.res)
        else:
            print("未找到元素")
        

a = [1, 2, 3, 4, 5, 6, 7, 8]
print(a)

bs = BinarySearch()
bs.BSBegin(a, 3)
