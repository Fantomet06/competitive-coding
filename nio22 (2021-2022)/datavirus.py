def del_vertex(k, v):
        if v not in k:
            print(f"{v} is not present in the graph!")
        else:
            k.pop(v)
            for i in k:
                if v in k[i]:
                    k[i].remove(v)

            return k

def main():
    def BFS(adj, src, dest, v, pred, dist):
        queue = []
    
        visited = [False for i in range(v)]
    
        for i in range(v):
            dist[i] = 1000000
            pred[i] = -1

        visited[src] = True
        dist[src] = 0
        queue.append(src)
        while (len(queue) != 0):
            u = queue[0]
            queue.pop(0)
            try:
                for i in range(len(adj[u])):
                    if (visited[adj[u][i]] == False):
                        visited[adj[u][i]] = True
                        dist[adj[u][i]] = dist[u] + 1
                        pred[adj[u][i]] = u
                        queue.append(adj[u][i])
                        if (adj[u][i] == dest):
                            return True
            except:
                pass
        return False

    adj_list = {}
    mylist = []
    
    def add_edge(node, node1, node2):
        if node not in mylist:
            mylist.append(node)
            
        temp = []
        if node1 not in adj_list:
            temp.append(node2)
            adj_list[node1] = temp

        elif node1 in adj_list:
            temp.extend(adj_list[node1])
            temp.append(node2)
            adj_list[node1] = temp


    N, M = map(int, input().split())

    from itertools import combinations
    clist = []
    connections = 0

    for i in range(M):
        a, b = map(int, input().split())
        add_edge(a,a,b)
        add_edge(b,b,a)
        if a not in clist:
            clist.append(a)
        
        if b not in clist:
            clist.append(b)
    aconnections = []

    for x in range(N):
        print(adj_list)
        #adj_list2 = [y for y in adj_list]
        adj_list2  = del_vertex(adj_list2, x)
        print(adj_list2)
        clist2 = [y for y in clist]
        clist2.remove(x)
        combination2 = list(combinations(clist2, 2))

        connections = 0

        for i in range(len(combination2)):
            pred=[0 for i in range(N)]
            dist=[0 for i in range(N)]
            bfs = BFS(adj_list2, combination2[i][0], combination2[i][1], N, pred, dist)
            if bfs != False:
                connections += 1
        
        aconnections.append(connections)

    aconnections.sort(reverse=True)
    print(aconnections[0])
main()