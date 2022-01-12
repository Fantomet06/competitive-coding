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
    
    def printShortestDistance(adj, s, dest, v):
        pred=[0 for i in range(v)]
        dist=[0 for i in range(v)]
    
        
        if (BFS(adj, s, dest, v, pred, dist) == False):
            #print("Given source and destination are not connected")
            return False
        

        path = []
        crawl = dest
        path.append(crawl)
        
        while (pred[crawl] != -1):
            path.append(pred[crawl])
            crawl = pred[crawl]

        #print(dist[dest]+1)


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
        e = i
        a, b = map(int, input().split())
        add_edge(a,a,b)
        add_edge(b,b,a)
        if a not in clist:
            clist.append(a)
        
        if b not in clist:
            clist.append(b)
        #add_edge(a,e,e+1)
    """
    def del_vertex(self, k, N):
        vertices = N
        self_graph =[None]*vertices

        for i in range(vertices):
            temp = self_graph[i]
            if i == k:
                while temp:
                    self_graph[i]= temp.next
                    temp = self_graph[i]
                      
            # Delete the vertex 
            # using linked list concept        
            if temp:
                if temp[vertices] == k:
                    self_graph[i]= temp.next
                    temp = None
            while temp:
                if temp.vertex == k:
                    break
                prev = temp
                temp = temp.next
  
            if temp == None:
                continue
  
            prev.next = temp.next
            temp = None"""

    def del_vertex(adj_list2, v):
        if v not in adj_list2:
            print(f"{v} is not present in the graph!")
        else:
            adj_list2.pop(v)
            for i in adj_list2:
                if v in adj_list2[i]:
                    adj_list2[i].remove(v)
                    break

            return adj_list2
    
    #print(adj_list)
    combination = list(combinations(clist, 2))
    aconnections = []
    #rint(combination)
    print(adj_list)

    for x in range(N):
        adj_list2 = adj_list
        adj_list2  = del_vertex(adj_list2, x)
        clist2 = [y for y in clist]
        clist2.remove(x)
        print(adj_list2)
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