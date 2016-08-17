import time

def merge(first_half, second_half):
    """ MergeSort the given two arrays.
    
    Args:
    -first_half (list): The first array
    -second_half (list): The second array 
    """
    merged = []
    i=0
    j=0
    len_first = len(first_half)
    len_second = len(second_half)
    len_total = len_first + len_second
    for k in range(0, len_total):
        if first_half[i] < second_half[j]:
            merged.append(first_half[i])
            i += 1
            if i == len_first:
                merged.extend(second_half[j:])
                return merged
        else:
            merged.append(second_half[j])
            j += 1
            if j == len_second:
                merged.extend(first_half[i:])
                return merged
    return merged

def mergesort(data):
    """Sort the give data(array) by mergesort.
    
    Args:
    -data (list): a list that need to be sorted.
    """
    n = len(data)
    #base case
    if n == 1:
        return data, 0
    else:
        #split data
        first_half = data[:n/2]
        second_half = data[n/2:]
        first_half = mergesort(first_half)
        second_half = mergesort(second_half)
        merged = merge(first_half, second_half)
        return merged

def quicksort(Array, left, right):
    """This function do quicksort on array with the first element as pivot.
    
    Args:
    - Array (list): The array that need to be sorted
    - left (int): The index of the leftmost element of the array
    - right (int): This index of the rightmost element of the array
    """  
    array_len = right - left + 1
    
    #Base case
    if left > right: #base case, when array has no element
        pass
    elif array_len == 1: #base case, when array has only one element
        pass
    else:
        pivot = Array[left]#select the first element as the privot
        i = left + 1
        for j in range(left+1, right+1):
            if Array[j] < pivot:
                #swap A[i] and A[j]
                Array[i], Array[j] = Array[j], Array[i]
                i += 1
        #swap A[l] and A[i-1]
        Array[left], Array[i-1] = Array[i-1], Array[left]
        quicksort(Array, left, i-2)
        quicksort(Array, i, right)
    return Array

if __name__ == "__main__":
    file = "_32387ba40b36359a38625cbb397eee65_QuickSort.txt"
    data = []
    with open(file) as f:
        for line in f:
            data.append(int(line))
    repeat = 100
    
    #Merge sort
    starttime = time.time()
    for i in range(repeat):
        array = data[:]
        mergesort(array)
    print "Execuation time for mergesort 100 times in second: ", time.time() - starttime
    
    #Quick sort
    starttime = time.time()
    for i in range(repeat):
        array = data[:]
        quicksort(array, 0, len(array)-1)
    print "Execuation time for quicksort 100 times in second: ", time.time() - starttime
    
    #Python sort
    starttime = time.time()
    for i in range(repeat):
        array = data[:]
        sorted(array)
    print "Execuation time for python sort (written in c) 100 times in second: ", time.time() - starttime
    