import time
import sys
sys.setrecursionlimit(20000)

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
            tail, head = int(temp[0]) - 1, int(temp[1]) - 1 
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

############           DFS            ################################
def DFS(graph, nodes_to_visit, reverse, verbose):
    '''Recusive DFS_search implementation.
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
    
    '''
    visited = set()
    leader_with_scc = {}
    dfs_finish_order = []
    
    def dfs(graph, leader_with_scc, leader, i, visited, verbose):
        if verbose:
            print "On node: ",i
        visited.add(i)
        leader_with_scc[leader].append(i)
        for j in graph[i]:
            if j in visited:
                if verbose:
                    print "Already visited ", j
            else:
                dfs(graph, leader_with_scc, leader, j, visited, verbose)
        if verbose:
            print "complete ", i
        dfs_finish_order.append(i)
    
    for n in nodes_to_visit:
        if verbose:
            print "Start exploring ", n 
        if n in visited:
            if verbose:
                print "Already explored ",n
        else:
            leader_with_scc[n] = []
            dfs(graph, leader_with_scc, n, n, visited, verbose)
    if reverse:
        return dfs_finish_order
    else:
        return leader_with_scc

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

    print "...........................................1st DFS search ... "
    magic_list = DFS(reversed_graph, nodes_to_visit=range(8), 
                     reverse=True, verbose=True)
    
    magic_list.reverse()
    print "reversed magic list:", magic_list

    print ".............................2nd DFS search and generage SCC.."
    scc = DFS(origin_graph, nodes_to_visit=magic_list, 
              reverse=False, verbose=True)
    print "leader_with_scc:", scc
    
    scc_size(scc)

