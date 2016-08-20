import time
def readin_graph(path):
    """ Read the original file.
    Args:
    - path(string): The file path.
    
    returns:
    - graph (nested list): with element index as the tail node, the list element
        the head nodes that connected to the tail
    
    - node_list (list): A none repe 
    """
    graph = [[]]
    node_list = []
    seen = set()
    idx=0
    with open(path) as f:
        for line in f:
            temp = line.split(' ')[:-1]
            tail, head = int(temp[0]) - 1, int(temp[1]) -1 
            if tail==idx:
                graph[tail].append(head)
            else:
                while(tail!=idx):
                    graph.append([])
                    idx+=1
                graph[tail].append(head)
    return graph
#############    reverse graph         ################################
def reverse(graph):
    """Return a reversed graph.
    Args:
    - graph(list): list that represent the graph 
    
    """
    rev_graph = []
    for i in range(len(graph)):
        rev_graph.append([])
    for idx, i in enumerate(graph):
        for j in i:
            rev_graph[j].append(idx)
    return rev_graph

############           DFS_search            ################################
def DFS_search(graph, nodes_to_visit, reverse, verbose):
    """DFS_search implementation.
    The recusive DFS aglo was transfered here into a while loop to avoid 
    stack overflow. 
    To make the non recursive DFS algorithm, see reference:
    http://stackoverflow.com/questions/5278580/non-recursive-depth-first-search-algorithm 
    
    Args:
    - graph (list): The graph for DFS
    - nodes_to_visit (list): The DFS will be executed based on the given ordered 
        nodes list.
    - reverse (bool): The graph is reversed or not. Depends on the value, 
        different object will be returned. If the graph is reversed 
        (1st DFS search), thenthe magic nodes list for the 2nd DFS search will 
        be returned. If the graph is not reversed (2nd DFS search on the 
        original graph), then the SCC dict with leader nodes will be returned. 
    - verbose (bool): Type some debug message if True.
    
    """
    visited = set() #Store the visited node here
    if reverse:
        dfs_finish_order = [] #Store the finished DFS node here in order. 
    else:
        leader_with_scc = {} #Store the scc with its leader node as key, scc as 
                             #value (list)
    N=1.0
    N_total = len(nodes_to_visit)
    for i in nodes_to_visit:
        N+=1
        print "Finished %", N/N_total*100 #Show progress
        if verbose:
            print "start explore ", i
        if i in visited:
            if verbose:
                print "Already explored ", i
            continue
        else:
            if not reverse:
                leader_with_scc[i] = []
            visited.add(i)
            track = [i]     
            while len(track) != 0:
                current_node = track[-1]
                if verbose:
                    print 'currently_on_node', current_node
                visited.add(current_node)
                
                toextend = list(set(graph[current_node]) - visited)
                if len(toextend) == 0:
                    finished_node = track.pop()
                    if reverse:
                        dfs_finish_order.append(finished_node)
                        if verbose:
                            print "List of node finished search:", dfs_finish_order
                    else:
                        leader_with_scc[i].append(finished_node)
                else: 
                    track.extend(toextend)
    if reverse:
        if verbose:
            print "dfs_finish_time_list:", dfs_finish_order 
        return dfs_finish_order
    else:
        if verbose:
            print "leader_with_scc:", leader_with_scc 
        return leader_with_scc

def reversed_magic_lise(magic_list):
    """return a reversed magic_list
    firstly remove the duplicated element in order, then reverse the list.
    eg: magic_list: [0,1,3,5,1,5,2]
        cleaned magic_list: [0,1,3,5,2]
        reversed magic_list: [2,5,3,1,0]
    
    Args:
    - magic_list (list): a magic list
    """
    seen = set()
    temp = []
    for i in magic_list:
        if i in seen:
            continue
        else:
            temp.append(i)
            seen.add(i)
    return list( reversed(temp) )
    
def scc_size(scc_dict):
    """Print the first 5 largest scc size 
    Args:
    - scc_dict (dict): key: leader node, value: scc nodes under the leader node.
    """
    
    len_dict = {}
    for k in scc_dict.keys():
        len_dict[k] = len( set(scc_dict[k]) )
    scc_len_list = list(sorted(len_dict.values(), reverse=True))
    print "The first 5 largest SCC length : ", scc_len_list[:5]

if __name__ == "__main__":
    start_time = time.time()
    file = "_410e934e6553ac56409b2cb7096a44aa_SCC.txt"
    print "..........................................read in graph... "
    origin_graph = readin_graph(file)

    print "...........................................Reverse graph... "
    reversed_graph = reverse(origin_graph)

    print "..................1st DFS search and generate magic list... "
    magic_list = DFS_search(graph=reversed_graph, 
                            nodes_to_visit=range(875714), 
                            reverse = True, verbose=False)

    print ".......................................reverse magic_list... "
    reversed_magic_list = reversed_magic_lise(magic_list) 
    
    print ".............................2nd DFS search and generage SCC.."
    scc = DFS_search(graph=origin_graph, 
                            nodes_to_visit=reversed_magic_list, 
                            reverse = False, verbose=False)
    scc_size(scc)
    print "..................Time used in sec: ", time.time() - start_time
    
    
    if False:
        print 'graph:',origin_graph
        print "regraph:", reversed_graph
        print "magic_list", magic_list     
        print "reversed_magic_list: ", magic_list
        print "SCC:", scc
         