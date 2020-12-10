class QuickSort:
    def __init__(self):
        pass

    def smallLoap(self, Array, low, high):
        privix = Array[low]

        while low < high:
            while low < high and Array[high] >= privix:
                high -= 1
            if low < high:
                Array[low] = Array[high]
                # low += 1

            while low < high and Array[low] <= privix:
                low += 1
            if low < high:
                Array[high] = Array[low]
                # high -= 1

        Array[low] = privix
        
        return low
    
    def smallLoap2(self, Array, low, high):
        if low < high:
            privix = Array[high]
            index = low - 1

            for i in range(low, high):
                if Array[i] < privix:
                    index += 1
                    Array[index], Array[i] = Array[i], Array[index]

            Array[high], Array[index+1] = Array[index+1], Array[high]
            low = index + 1

        return low

    def bigLoap2(self, Array, low, high):
        if low < high:
            index = self.smallLoap2(Array, low, high)
            if index > low:
                self.bigLoap(Array, low, index-1)
            if index < high:
                self.bigLoap(Array, index+1, high)

    def bigLoap(self, Array, low, high):
        if low < high:
            index = self.smallLoap(Array, low, high)

            if index > low:
                self.bigLoap(Array, low, index-1)
            if index < high:
                self.bigLoap(Array, index+1, high)

    def begain(self, Array, method='dent'):
        # method = 'dent' or 'pick'
        high = len(Array) - 1

        if method == 'dent':
            self.bigLoap(Array, 0, high)
        if method == 'pick':
            self.bigLoap2(Array, 0, high)


a = [34, 45, 213, 78, 35, 12, 5]
print(a)

qs = QuickSort()
qs.begain(a,'pick')

print(a)


