def BFS_SP(graph, start, goal):
    explored = []
     
    # Queue for traversing the
    # graph in the BFS
    queue = [[start]]
     
    # If the desired node is
    # reached
    if start == goal:
        print("Same Node")
        return
     
    # Loop to traverse the graph
    # with the help of the queue
    while queue:
        path = queue.pop(0)
        node = path[-1]
         
        # Condition to check if the
        # current node is not visited
        if node not in explored:
            neighbours = graph[node]
             
            # Loop to iterate over the
            # neighbours of the node
            for neighbour in neighbours:
                new_path = list(path)
                new_path.append(neighbour)
                queue.append(new_path)
                 
                # Condition to check if the
                # neighbour node is the goal
                if neighbour == goal:
                    return new_path
            explored.append(node)
 
    # Condition when the nodes
    # are not connected
    print("So sorry, but a connecting"\
                "path doesn't exist :(")
    return

adj_list = {}
mylist = []

def add_node(node):
  if node not in mylist:
    mylist.append(node)
  else:
    print("Node ",node," already exists!")
 
def add_edge(node1, node2):
  temp = []
  if node1 in mylist and node2 in mylist:
    if node1 not in adj_list:
      temp.append(node2)
      adj_list[node1] = temp
   
    elif node1 in adj_list:
      temp.extend(adj_list[node1])
      temp.append(node2)
      adj_list[node1] = temp
       
  else:
    print("Nodes don't exist!")

N = int(input())

for i in range(N):
    add_node(i+1)

for i in range(N-1):
    a, b, c = map(int, input().split())
    add_edge(i+1,a)
    add_edge(i+1,b)
    add_edge(i+1,c)
    add_edge(i+1,i+2)

#print(adj_list)
r = BFS_SP(adj_list, 1, N)
print(len(r))