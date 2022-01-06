from queue import Queue

def BFS(adj_list, start_node, target_node):
    visited = set()
    queue = Queue()

    queue.put(start_node)
    visited.add(start_node)

    parent = dict()
    parent[start_node] = None

    path_found = False
    while not queue.empty():
        current_node = queue.get()
        if current_node == target_node:
            path_found = True
            break

        for next_node in adj_list[current_node]:
            if next_node not in visited:
                queue.put(next_node)
                parent[next_node] = current_node
                visited.add(next_node)

    path = []
    if path_found:
        path.append(target_node)
        while parent[target_node] is not None:
            path.append(parent[target_node]) 
            target_node = parent[target_node]
        path.reverse()
    return path

def traversal(adj_list, start_node):
    visited = set()
    queue = Queue()
    queue.put(start_node)
    visited.add(start_node)

    while not queue.empty():
        current_node = queue.get()
        print(current_node, end = " ")
        for next_node in adj_list[current_node]:
            if next_node not in visited:
                queue.put(next_node)
                visited.add(next_node)

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

print(adj_list)
path = BFS(adj_list, 1, N)
print(path)