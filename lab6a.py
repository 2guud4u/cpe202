import time
import random
class sorts:
    def selectionSort(self, alist):
        compara_num = 0
        for fillslot in range(len(alist)-1,0,-1):
            positionOfMax=0
            for location in range(1,fillslot+1):
                if alist[location]>alist[positionOfMax]:
                    positionOfMax = location
                    compara_num += 1
            temp = alist[fillslot]
            alist[fillslot] = alist[positionOfMax]
            alist[positionOfMax] = temp
        return compara_num
    def insertionSort(self, alist):
        compara_num = 0
        for index in range(1,len(alist)):

            currentvalue = alist[index]
            position = index

            while position>0 and alist[position-1]>currentvalue:
                alist[position]=alist[position-1]
                position = position-1
                compara_num += 1
            alist[position]=currentvalue
        return compara_num
    def test(self, test_num):
        num = None
        alist = random.sample(range(0, test_num*10), test_num)
        alist1 = alist
        alist2 = alist

        start_time = time.time()
        num = self.insertionSort(alist1)
        print('insertion:', "--- %s seconds ---" % (time.time() - start_time))
        print('and did', num, 'comparisons')

        start_time = time.time()
        num = self.selectionSort(alist2)
        print('selection:', "--- %s seconds ---" % (time.time() - start_time))
        print('and did', num, 'comparisons')
