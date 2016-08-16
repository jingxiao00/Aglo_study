def countsort(first_half, second_half):
    """ MergeSort the given two arrays and return the number of inversions 
    before sorting.
    
    Args:
    -first_half (list): The first array
    -second_half (list): The second array 
    """
    nrb_invers = 0
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
                return merged, nrb_invers
        else:
            merged.append(second_half[j])
            j += 1
            nrb_invers += (len(first_half) - i)
            if j == len_second:
                merged.extend(first_half[i:])
                return merged, nrb_invers
    return merged, nrb_invers

def count_inverse(data):
    """Sort the give data(array) and count the number of inversions in the array
    
    Args:
    -data (list): a list that need to be sorted and count the inversions. 
    """
    n = len(data)
    #base case
    if n == 1:
        return data, 0
    else:
        #split data
        first_half = data[:n/2]
        second_half = data[n/2:]
        first_half, nrb_inverse_1st = count_inverse(first_half)
        second_half, nrb_inverse_2nd = count_inverse(second_half)
        merged, nrb_inverse_merged = countsort(first_half, second_half)
        return merged, nrb_inverse_1st + nrb_inverse_2nd + nrb_inverse_merged

if __name__ == "__main__":
    file = "D:\Gdrivewangbo\CAglo\_bcb5c6658381416d19b01bfc1d3993b5_IntegerArray.txt"
    data = []
    with open(file) as f:
        for line in f:
            data.append(int(line))
    print 'Number of inversions is:',count_inverse(data)[1]
