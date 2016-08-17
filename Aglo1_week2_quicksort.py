def quicksort1(Array, left, right, count):
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
        count += (array_len - 1)
        pivot = Array[left]#select the first element as the privot
        i = left + 1
        for j in range(left+1, right+1):
            if Array[j] < pivot:
                #swap A[i] and A[j]
                Array[i], Array[j] = Array[j], Array[i]
                i += 1
        #swap A[l] and A[i-1]
        Array[left], Array[i-1] = Array[i-1], Array[left]
        
        count = quicksort1(Array, left, i-2, count)
        count = quicksort1(Array, i, right, count)
    return count
##############################################################################

def quicksort2(Array, left, right, count):
    """This function do quicksort on array with the last element as pivot.
    
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
        count += (array_len-1)
        pivot = Array[right]
        #exchange the pviot and the first element
        Array[left], Array[right] = Array[right], Array[left]
        i = left + 1
        for j in range(left+1, right+1):
            if Array[j] < pivot:
                #swap A[j] and A[j]
                Array[i], Array[j] = Array[j], Array[i]
                i += 1
        #swap A[left] and A[i-1]
        Array[left], Array[i-1] = Array[i-1], Array[left]
        count = quicksort2(Array, left, i-2, count)
        count = quicksort2(Array, i, right, count)
    return count

#################################################################################
def middle(x, y, z):
    """Return the middle of the three give element"""
    return sorted([x, y, z])[1]
    
def quicksort3(Array, left, right, count):
    """This function do quicksort on array with the middle element as pivot.
    
    Args:
    - Array (list): The array that need to be sorted
    - left (int): The index of the leftmost element of the array
    - right (int): This index of the rightmost element of the array
    """  
    array_len = right - left + 1
    #base case
    if left > right: #base case, when array has no element
        pass
    elif array_len == 1: #base case, when array has only one element
        pass
    elif array_len == 2:
        count += 1
        if Array[left] > Array[right]:
            Array[left], Array[right] =  Array[right], Array[left]
        else:
            pass
    else:
        count += (array_len-1)
        pivot = middle(Array[left], Array[right], Array[left+array_len/2-1+array_len%2])
        this = Array.index(pivot)
        Array[left], Array[this] = Array[this], Array[left]
        i = left + 1
        for j in range(left+1, right+1):
            if Array[j] < pivot:
                #swap A[j] and A[j]
                Array[i], Array[j] = Array[j], Array[i]
                i += 1
        #swap A[left] and A[i-1]
        Array[left], Array[i-1] = Array[i-1], Array[left]
        count = quicksort3(Array, left, i-2, count)
        count = quicksort3(Array, i, right, count)
        
    return count
if __name__ == "__main__":
    file = "_32387ba40b36359a38625cbb397eee65_QuickSort.txt"
    data = []
    with open(path) as f:
        for line in f:
            data.append(int(line))

    array = data[:]
    count = quicksort1(array, 0, len(array)-1, count = 0)
    print "Number of comparion for quicksort1:", count
    
    array = data[:]
    count = quicksort2(array, 0, len(array)-1, count = 0)
    print "Number of comparion for quicksort2:", count 
     
    array = data[:]
    count = quicksort3(array, 0, len(array)-1, count = 0)
    print "Number of comparion for quicksort3:", count
     