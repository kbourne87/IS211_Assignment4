import random
import time

def randomListMaker(size):

    'Generates a randomized list of values within the range dictated by size'

    randomList = list(range(size))
    random.shuffle(randomList)
    return randomList


def sequential_search(a_list, item):

    'Squential search from the reading'
    'Returns a True/False for searched-for item and a time to complete'

    startTime = time.time()
    pos = 0
    found = False
    while pos < len(a_list) and not found:
        if a_list[pos] == item:
            found = True
        else:
            pos = pos+1
    endTime = time.time() - startTime
    return found, endTime

def ordered_sequential_search(a_list, item):

    'Ordered sequential search from the reading'
    'Searches for item in list, returns True/False along with time to execute'

    pos = 0
    found = False
    stop = False
    startTime = time.time()
    while pos < len(a_list) and not found and not stop:
        if a_list[pos] == item:
            found = True
        else:
            if a_list[pos] > item:
                stop = True
            else:
                pos = pos + 1

    endTime = time.time() - startTime
    return found, endTime

def binary_search_iterative(a_list, item):

    'Binary search from the reading'
    'Searches for item in list, returns True/False along with time to execute'

    first = 0
    last = len(a_list) - 1
    found = False
    startTime = time.time()
    while first <= last and not found:
        midpoint = (first + last) // 2
        if a_list[midpoint] == item:
            found = True
        else:
            if item < a_list[midpoint]:
                last = midpoint - 1
            else:
                first = midpoint + 1
    endTime = time.time() - startTime
    return found, endTime

def binary_search_recursive(a_list,item):

    'Binary recursive search from the reading'
    'Searches for item in list, returns True/False along with time to execute'

    startTime = time.time()
    found = False
    if len(a_list) == 0:
        found = False
    else:
        midpoint = len(a_list) // 2
        if a_list[midpoint] == item:
            found = True
        else:
            if item < a_list[midpoint]:
                return binary_search_recursive(a_list[:midpoint], item)
            else:
                return binary_search_recursive(a_list[midpoint + 1:], item)
    endTime = time.time() - startTime
    return found, endTime

if __name__ == "__main__":
    """Main entry point"""
    the_sizes = [500, 1000, 10000]

    total_time = 0
    for size in the_sizes:
        mylist = randomListMaker(size)
        for i in range(100):
            check = sequential_search(mylist, -1)

            'Each check returns a tuple of (T/F, time), so check[1] is to add the time only'

            total_time += check[1]

            avg_time = total_time / 100
        print(f"Sequential Search took {avg_time:10.7f} seconds to run, on average for a list of {size} elements")

    for size in the_sizes:
        mylist = sorted(randomListMaker(size))
        for i in range(100):
            check = ordered_sequential_search(mylist, -1)
            total_time += check[1]

            avg_time = total_time / 100
        print(f"Ordered Sequential Search took {avg_time:10.7f} seconds to run, on average for a list of {size} elements")

    for size in the_sizes:
        mylist = sorted(randomListMaker(size))
        for i in range(100):
            check = binary_search_iterative(mylist, -1)
            total_time += check[1]

            avg_time = total_time / 100
        print(f"Binary Iterative Search took {avg_time:10.7f} seconds to run, on average for a list of {size} elements")

    for size in the_sizes:
        mylist = sorted(randomListMaker(size))
        for i in range(100):
            check = binary_search_recursive(mylist, -1)
            total_time += check[1]

            avg_time = total_time / 100
        print(f"Binary Recursive Search took {avg_time:10.7f} seconds to run, on average for a list of {size} elements")