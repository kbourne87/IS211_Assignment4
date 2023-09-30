import time
import random

def randomListMaker(size):

    'Generates a randomized list of values within the range dictated by size'

    randomList = list(range(size))
    random.shuffle(randomList)
    return randomList


def insertion_sort(a_list):
    'Insertion sort from the reading'
    startTime = time.time()

    for index in range(1, len(a_list)):
        current_value = a_list[index]
        position = index

        while position > 0 and a_list[position - 1] > current_value:
            a_list[position] = a_list[position - 1]
            position = position - 1

        a_list[position] = current_value
    endTime = time.time() - startTime
    return endTime

def shell_sort(alist):

    'Shell sort from the reading'
    startTime = time.time()
    sublistcount = len(alist)//2
    while sublistcount > 0:
        for startposition in range(sublistcount):
            gapInsertionSort(alist,startposition,sublistcount)

        sublistcount = sublistcount // 2
    endTime = time.time() - startTime
    return endTime


def gapInsertionSort(alist, start, gap):
    for i in range(start+gap, len(alist), gap):
        currentvalue = alist[i]
        position = i

        while position >= gap and alist[position-gap] > currentvalue:
            alist[position] = alist[position-gap]
            position = position - gap

        alist[position] = currentvalue

def python_sort(a_list):

    'Simply the built-in python sort'
    startTime = time.time()
    endTime = time.time() - startTime
    return sorted(a_list), endTime

if __name__ == "__main__":
    """Main entry point"""
    the_sizes = [500, 1000, 10000]

    total_time = 0
    for size in the_sizes:
        mylist = randomListMaker(size)
        for i in range(100):
            check = insertion_sort(mylist)

            total_time += check

            avg_time = total_time / 100
        print(f"Insertion Sort took {avg_time:10.7f} seconds to run, on average for a list of {size} elements")


    for size in the_sizes:
        mylist = randomListMaker(size)
        for i in range(100):
            check = shell_sort(mylist)
            total_time += check

            avg_time = total_time / 100
        print(f"Shell Sort took {avg_time:10.7f} seconds to run, on average for a list of {size} elements")

    for size in the_sizes:
        mylist = randomListMaker(size)
        for i in range(100):
            check = python_sort(mylist)

            'This one returns a tuple, so check[1] is just the time'

            total_time += check[1]

            avg_time = total_time / 100
        print(f"Python's built-in sort took {avg_time:10.7f} seconds to run, on average for a list of {size} elements")