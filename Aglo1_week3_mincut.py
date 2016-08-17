import random
import copy
import time

def replace(ls, X, Y):
    """replace all X into Y in the give list"""
    for i,v in enumerate(ls):
        if v == X:
            ls.pop(i)
            ls.insert(i, Y)

def WeightedPick(weight, data):
    """Randomly Pick a edge in the graph 
    
    To randomly pick a edge in the graph, we need to firstly pick a vertex 
    by its weight(number of edge that connnected), then randomly pick another
    vertex that connected to it. 
    
    Args:
    - weight (dict): with key a vertex, value is its weight
    - data (dict): with key a vertex, value is the list of vertex it connected 
    """
    r = random.uniform(0, sum(weight.itervalues()))
    s = 0.0
    for k, w in weight.iteritems():
        s += w
        if r < s: 
            return k, random.choice(data[k])
def removeall(ls, element):
    """return a ls with all pointed elements removed."""
    return [i for i in ls if i != element]

def contraction(weight, data, k, v):
    """Inside the graph, contract v to k, replace all v to k.
    The contraction of v to k in 4 steps:
    1. remove all v in data[k]
    2. remove all k in data[v]
    3. extend data[k] with data[v]
    4. in all the vertex that were connected to v, replace v to k 
    
    Args:
    - weight (dict): with key a vertex, value is its weight
    - data (dict): with key a vertex, value is the list of vertex it connected
    - k (int): vertex of the edge that picked for contraction
    - v (int): vortex of the edge that will be contracted by k
    """
    data[k] = removeall(data[k], v)
    data[v] = removeall(data[v], k)
    data[k].extend(data[v])
    for i in data[v]:
        replace(data[i], v, k)

    weight[k] = len(data[k])
    data.pop(v)
    weight.pop(v)
    return weight, data

def mincut(data, weight):    
    '''return the mincut of the given graph
    
    Args:
    - weight (dict): with key a vertex, value is its weight.
    - data (dict): with key a vertex, value is the list of vertex it connected.
    '''
    while(True):
        k, v = WeightedPick(weight, data)# randomly pick a edge
        weight, data = contraction(weight, data, k, v)# contraction this edge
        #until left only two points
        if len(data) == 2:
            break
    return weight[k]

if __name__ == "__main__":
    file = "_f370cd8b4d3482c940e4a57f489a200b_kargerMinCut.txt"
    data1 = {}
    weight1 = {}
    with open(file) as f:
        for line in f:
            temp = line.split('\t')[:-1]
            data1[int(temp[0])] = [int(i) for i in temp[1:]]
            weight1[ int(temp[0]) ]= len( data1[int( temp[0] )] )
    
    start = time.time()
    mincut_nr = 1000
    for i in range(0, 200):
        if i%10 == 0:
            print "right now in loop:", i
            print "current mincut:", mincut_nr
        d = copy.deepcopy(data1)
        w = copy.deepcopy(weight1)
        temp = mincut(d, w)
        if temp < mincut_nr:
            mincut_nr = temp
            print "smaller mincut found:", mincut_nr
    
    
















# 1    2    4    
# 2    1    3    4    
# 3    2    4    
# 4    1    2    3    
# 
# 1:4
# 
# 1    2    2    3    
# 2    1    3    4    
# 3    2    1    
#     
# 2:3
# 1    2    4    
# 2    1    4    4    
# 4    1    2    2

















    