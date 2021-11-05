import time
import random
class quicksorty_first:
    def __init__(self):
        self.count = 0

    def quickSort(self, alist):
        self.quickSortHelper(alist, 0, len(alist) - 1)
        return self.count

    def quickSortHelper(self, alist, first, last):
        if first < last:
            splitpoint = self.partition(alist, first, last)

            self.quickSortHelper(alist, first, splitpoint - 1)
            self.quickSortHelper(alist, splitpoint + 1, last)

    def partition(self, alist, first, last):
        pivotvalue = alist[first]

        leftmark = first + 1
        rightmark = last

        done = False
        while not done:

            while leftmark <= rightmark and alist[leftmark] <= pivotvalue:
                leftmark = leftmark + 1
                self.count += 1

            while alist[rightmark] >= pivotvalue and rightmark >= leftmark:
                rightmark = rightmark - 1
                self.count += 1

            if rightmark < leftmark:
                done = True
            else:
                temp = alist[leftmark]
                alist[leftmark] = alist[rightmark]
                alist[rightmark] = temp

        temp = alist[first]
        alist[first] = alist[rightmark]
        alist[rightmark] = temp

        return rightmark
    def test(self, test_num):
        num = None
        alist = random.sample(range(0, test_num*10), test_num)
        alist1 = alist
        start_time = time.time()
        num = self.quickSort(alist1)
        print('quick:', "--- %s seconds ---" % (time.time() - start_time))
        print('and did', num, 'comparisons')
        print(alist)


class quickysort_median(quicksorty_first):# class for median sort
    def quickSort(self, alist):
        median_list = []
        median_list.append(alist[0])
        median_list.append(alist[len(alist) - 1])
        median_list.append(alist[int(len(alist)/2)])
        self.quickSortHelper(median_list, 0, len(median_list) - 1)

        median = alist.index(median_list[1])
        temp = alist[0]
        alist[0] = alist[median]
        alist[median] = temp
        self.quickSortHelper(alist, 0, len(alist) - 1)
        return self.count

class quickysort_first_ordered(quicksorty_first):# class for pivot first ordered sort
    def test(self, test_num):
        num = None
        alist = random.sample(range(0, test_num * 10), test_num)
        alist1 = sorted(alist)
        print(alist1)
        start_time = time.time()
        num = self.quickSort(alist1)
        print('quick:', "--- %s seconds ---" % (time.time() - start_time))
        print('and did', num, 'comparisons')
class quickysort_median_ordered(quickysort_median):# class for median pivot ordered sort
    def test(self, test_num):
        num = None
        alist = random.sample(range(0, test_num * 10), test_num)
        alist1 = sorted(alist)
        print(alist1)
        start_time = time.time()
        num = self.quickSort(alist1)
        print('quick:', "--- %s seconds ---" % (time.time() - start_time))
        print('and did', num, 'comparisons')

class quickysort_median_random(quickysort_median):# class for median pivot random sort
    def test(self, test_num):
        n = 0
        sum = 0
        while(n < 10):
            num = None
            alist = random.sample(range(0, test_num * 10), test_num)
            alist1 = alist
            num = self.quickSort(alist1)
            sum = sum + num
            n += 1
        print(sum / 10)
class quickysort_first_random(quicksorty_first):# class for pivot first random sort
    def test(self, test_num):
        n = 0
        sum = 0
        while (n < 10):
            num = None
            alist = random.sample(range(0, test_num * 10), test_num)
            alist1 = alist
            num = self.quickSort(alist1)
            sum = sum + num
            n += 1
        print(sum / 10)







