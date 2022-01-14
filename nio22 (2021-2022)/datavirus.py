def del_vertex(k, v):
        if v not in k:
            print(f"{v} is not present in the graph!")
        else:
            k.pop(v)
            for i in k:
                if v in k[i]:
                    k[i].remove(v)

            return k

N = 100000
gr1 = {}
gr2 = {}
vis1 = [0] * N
vis2 = [0] * N



def dfs1(x) :
    vis1[x] = True
    if x not in gr1:
        gr1[x] = {}
            
    for i in gr1[x]:
        if (not vis1[i]):
            dfs1(i)

# DFS function
def dfs2(x) :
    vis2[x] = True

    if x not in gr2:
        gr2[x] = {}
            
    for i in gr2[x]:
        if (not vis2[i]):
            dfs2(i)

def Is_Connected(n):
    global vis1
    global vis2
        
    vis1 = [False] * len(vis1)
    dfs1(1)
        
    vis2 = [False] * len(vis2)
    dfs2(1)
        
    for i in range(1, n + 1):
        if (not vis1[i] and not vis2[i]) :
            return False
    return True

def Add_edge(u, v) :
 
    if u not in gr1 :
        gr1[u] = []
         
    if v not in gr2 :
        gr2[v] = []
         
    gr1[u].append(v)
    gr2[v].append(u)

def DFSUtil(graph, v, visited):
        # Mark the current node as visited and print it
        visited.add(v)

        # recur for all the vertices adjacent to this vertex
        for neighbour in graph[v]:
            if neighbour not in visited:
                DFSUtil(graph, neighbour, visited)
        # The function to do DFS traversal. It uses recursive DFSUtil

def DFS(graph):
    # create a set to store all visited vertices
    visited = set()
    # call the recursive helper function to print DFS traversal starting from all
    # vertices one by one
    for vertex in graph:
        if vertex not in visited:
            DFSUtil(graph, vertex, visited)

def main():
    adj_list = {}
    mylist = []
    
    """def add_edge(node, node1, node2):
        if node not in mylist:
            mylist.append(node)
            
        temp = []
        if node1 not in adj_list:
            temp.append(node2)
            adj_list[node1] = temp

        elif node1 in adj_list:
            temp.extend(adj_list[node1])
            temp.append(node2)
            adj_list[node1] = temp"""


    V, M = map(int, input().split())

    from itertools import combinations
    import copy
    clist = []
    connections = 0

    for i in range(M):
        a, b = map(int, input().split())
        Add_edge(a,b)
        #Add_edge(b,a)
        if a not in clist:
            clist.append(a)
        
        if b not in clist:
            clist.append(b)
    aconnections = []

    for x in range(V):
        #print(adj_list)
        adj_list2 = copy.deepcopy(adj_list)
        adj_list2  = del_vertex(adj_list2, x)
        #print(adj_list2)
        clist2 = [y for y in clist]
        clist2.remove(x)
        combination2 = list(combinations(clist2, 2))
        #print(combination2)

        connections = 0

        for i in range(len(combination2)):
            #pred=[0 for i in range(N)]
            #dist=[0 for i in range(N)]
            if (Is_Connected(V)):
                connections += 1
            else:
                pass
        
        aconnections.append(connections)

    aconnections.sort(reverse=False)
    print(aconnections[0])
main()