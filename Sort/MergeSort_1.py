class MergeSort:
    def __init__(self):
        pass

    def merge(self, Array, leftbegin, rightbegin, rightend):
        # 接受下标，不接受数字
        # 必须是  两个有序表
        A = Array[leftbegin:rightbegin].copy()
        B = Array[rightbegin:rightend+1].copy()

        index = leftbegin
        i_a = 0
        i_b = 0

        while i_a < len(A) and i_b < len(B):
            if A[i_a] < B[i_b]:
                Array[index] = A[i_a]
                index += 1
                i_a += 1
            else:
                Array[index] = B[i_b]
                index += 1
                i_b += 1

        while i_a < len(A):
            Array[index] = A[i_a]
            index += 1
            i_a += 1
        while i_b < len(B):
            Array[index] = B[i_b]
            index += 1
            i_b += 1
    
    def bigLoap(self, Array, begin, end):
        if begin < end:
            mid = int((begin+end)/2)

            if begin < mid:
                self.bigLoap(Array, begin, mid)
            if mid < end:
                self.bigLoap(Array, mid+1, end)

            self.merge(Array, begin, mid+1, end)

    def beginSort(self, Array):
        end = len(Array) - 1
        self.bigLoap(Array, 0, end)

a = [32,37,78,13,27]
print(a)

mQ = MergeSort()
mQ.beginSort(a)

print(a)
