class QuickSort:
    def __init__(self):
        pass

    def smallR(self, Array, low, high):
        # index = low
        privx = Array[low]

        while low < high:
            while low < high and Array[high] >= privx:
                high -= 1
            # miss
            if low < high:
                # Array[low], Array[high] = Array[high], Array[low]
                Array[low] = Array[high]
                low += 1

            while low < high and Array[low] <= privx:
                low += 1
            if low < high:
                Array[high] = Array[low]
                high -= 1

                
        print("low is", low, "high is", high)
        Array[low] = privx

        return low

    def bigR(self, Array, low, high):
        # low = 0
        # high = len(Array) - 1
        print(Array)

        if low < high:
            index = self.smallR(Array, low, high)
            if index > low+1:
                self.bigR(Array, low, index-1)
            if index < high-1:
                self.bigR(Array, index+1, high)


a = [12,65,23,76,4,98]
print(a)

qSort = QuickSort()
qSort.bigR(a, 0, len(a)-1)

print(a)
