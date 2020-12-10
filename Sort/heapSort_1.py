class HeapSort:
    def __init__(self):
        pass

    def downAdjust(self, Array, root, end):
        # 向下调整
        rootChild = root * 2

        while rootChild <= end:
            
            if rootChild+1 <= end and Array[rootChild+1] > Array[rootChild]:
                rootChild += 1

            if Array[rootChild] > Array[root]:
                Array[root], Array[rootChild] = Array[rootChild], Array[root]
                root = rootChild
                rootChild = root * 2
            else:
                break

    def upAdjust(self, Array):
        # 输入数组
        end = len(Array)-1
        begin = int(len(Array)/2)-1

        for node in range(begin, -1, -1):
            self.downAdjust(Array, node, end)

    def heapSortBegin(self, Array):
        self.upAdjust(Array)

        for i in range(0, len(Array)-1):
            Array[0], Array[-i-1] = Array[-i-1], Array[0]

            self.downAdjust(Array, 0, len(Array)-(i+1)-1) 


a = [23, 45, 2, 54, 76, 4]
print(a)

hS = HeapSort()
hS.heapSortBegin(a)

print(a)
